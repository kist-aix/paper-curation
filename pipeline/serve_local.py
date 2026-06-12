#!/usr/bin/env python3
"""로컬 미리보기 서버 — docs/ 정적 서빙 + /api/embed Gemini 프록시.

`python -m http.server` 는 정적 파일만 돌려주므로, Deep Research UI 가
같은 출처(`/api/embed`) 로 쿼리 임베딩을 요청하면 응답하지 못한다. 이
스크립트는 docs/ 를 그대로 서빙하면서 `/api/embed` POST 를 운영자의
Gemini 키로 프록시해 로컬 미리보기에서도 검색이 동작하게 한다.

- GET                 → docs/ 정적 파일 (mime 자동, 디렉토리는 index.html)
- POST /api/embed     → {"text": ...} → gemini-embedding-001 (768d,
                        taskType RETRIEVAL_QUERY) → L2 정규화 후
                        {"embedding": [...], "model": ..., "dim": 768}
- POST /api/audio-email → 501 (로컬은 이메일 발송 미지원 → 다운로드 안내)

추가 의존성 없음 — 표준 라이브러리(http.server + urllib)만 사용.

키 우선순위: GOOGLE_API_KEY/GEMINI_API_KEY env → config.json
(gemini_api_key/google_api_key) → docs/_local_keys.json (google_key/gemini_key).
"""

import argparse
import functools
import json
import math
import os
import ssl
import sys
import urllib.error
import urllib.request
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

# config_loader 를 그대로 재사용 (sys.path 트릭 — config_loader 는 건드리지 않는다).
PIPELINE_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = PIPELINE_DIR.parent
DOCS_DIR = PROJECT_ROOT / "docs"
sys.path.insert(0, str(PIPELINE_DIR))
try:
    from config_loader import load_config
except Exception:  # config.json 없거나 import 실패해도 env/_local_keys 로 동작
    load_config = None

# Gemini 임베딩 설정 (인덱스 빌드와 동일 — RETRIEVAL_QUERY 만 다르다).
GEMINI_MODEL = "gemini-embedding-001"
GEMINI_ENDPOINT = (
    "https://generativelanguage.googleapis.com/v1beta/models/"
    f"{GEMINI_MODEL}:embedContent"
)
EMBED_DIM = 768

# 사내 프록시가 HTTPS 를 self-signed 인증서로 가로채는 환경 대응 (config_loader 와 동일).
_ssl_ctx = ssl.create_default_context()
_ssl_ctx.check_hostname = False
_ssl_ctx.verify_mode = ssl.CERT_NONE

_GOOGLE_KEY_CACHE = None


def resolve_google_key():
    """Gemini 키 조회. env → config.json → docs/_local_keys.json 순. 캐싱(비어있으면 재시도)."""
    global _GOOGLE_KEY_CACHE
    if _GOOGLE_KEY_CACHE:
        return _GOOGLE_KEY_CACHE

    key = os.environ.get("GOOGLE_API_KEY") or os.environ.get("GEMINI_API_KEY") or ""

    if not key and load_config is not None:
        try:
            cfg = load_config() or {}
            key = cfg.get("gemini_api_key") or cfg.get("google_api_key") or ""
        except Exception:
            key = ""

    if not key:
        local_keys = DOCS_DIR / "_local_keys.json"
        if local_keys.exists():
            try:
                data = json.loads(local_keys.read_text(encoding="utf-8"))
                key = data.get("google_key") or data.get("gemini_key") or ""
            except Exception:
                key = ""

    if key:
        _GOOGLE_KEY_CACHE = key
    return key


def gemini_embed(text, api_key):
    """gemini-embedding-001 으로 쿼리 임베딩 → L2 정규화한 768d 리스트 반환.

    중요: output_dimensionality != 3072 이면 Gemini 가 비정규화 벡터를 돌려준다.
    int8 양자화/코사인 비교 전에 반드시 L2 정규화해야 인덱스와 스케일이 맞는다.
    """
    payload = {
        "model": f"models/{GEMINI_MODEL}",
        "content": {"parts": [{"text": text}]},
        "taskType": "RETRIEVAL_QUERY",
        "outputDimensionality": EMBED_DIM,
    }
    req = urllib.request.Request(
        GEMINI_ENDPOINT,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "x-goog-api-key": api_key,
        },
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=30, context=_ssl_ctx) as resp:
        out = json.load(resp)

    values = (out.get("embedding") or {}).get("values") or []
    if not values:
        raise ValueError("Gemini 응답에 embedding.values 가 없습니다: " + json.dumps(out)[:200])

    norm = math.sqrt(sum(v * v for v in values)) or 1.0
    return [v / norm for v in values]


class LocalHandler(SimpleHTTPRequestHandler):
    """docs/ 정적 서빙 + /api/* POST 핸들러."""

    def _send_json(self, code, obj):
        body = json.dumps(obj, ensure_ascii=False).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _read_body(self):
        length = int(self.headers.get("Content-Length", 0) or 0)
        return self.rfile.read(length) if length > 0 else b""

    def do_POST(self):  # noqa: N802 (stdlib 규약)
        route = self.path.split("?", 1)[0]
        if route == "/api/embed":
            self._handle_embed()
        elif route == "/api/audio-email":
            # 로컬에는 이메일 발송 백엔드가 없다 → 501. UI(sendAudioEmail)는
            # r.ok 가 아니면 조용히 다운로드로 폴백하므로 graceful 하게 실패한다.
            self._send_json(501, {"error": "로컬에서는 이메일 발송 미지원 — 다운로드를 이용"})
        else:
            self._send_json(404, {"error": "not found"})

    def _handle_embed(self):
        try:
            req = json.loads(self._read_body() or b"{}")
        except Exception as e:
            self._send_json(400, {"error": f"invalid JSON body: {e}"})
            return

        text = (req.get("text") or "").strip()
        if not text:
            self._send_json(400, {"error": "missing 'text'"})
            return

        api_key = resolve_google_key()
        if not api_key:
            self._send_json(503, {
                "error": "Gemini 키 없음 — GOOGLE_API_KEY env 또는 "
                         "config.json(gemini_api_key) 를 설정하세요.",
            })
            return

        try:
            vec = gemini_embed(text, api_key)
        except urllib.error.HTTPError as e:
            try:
                detail = e.read().decode("utf-8", "replace")[:300]
            except Exception:
                detail = str(e)
            self._send_json(502, {"error": f"Gemini embed {e.code}: {detail}"})
            return
        except Exception as e:
            self._send_json(502, {"error": f"Gemini embed 실패: {e}"})
            return

        self._send_json(200, {"embedding": vec, "model": GEMINI_MODEL, "dim": len(vec)})


def main():
    parser = argparse.ArgumentParser(
        description="docs/ 정적 서빙 + /api/embed Gemini 프록시 (로컬 미리보기용)"
    )
    parser.add_argument("--port", type=int, default=8000, help="리슨 포트 (기본 8000)")
    parser.add_argument("--topic", default="", help="열어볼 토픽 (URL 안내용, 예: ai4s)")
    args = parser.parse_args()

    if not DOCS_DIR.exists():
        print(f"ERROR: docs 디렉토리를 찾을 수 없습니다: {DOCS_DIR}", file=sys.stderr)
        sys.exit(1)

    sub = (args.topic.strip("/") + "/") if args.topic else ""
    url = f"http://localhost:{args.port}/{sub}"

    handler = functools.partial(LocalHandler, directory=str(DOCS_DIR))
    httpd = ThreadingHTTPServer(("", args.port), handler)

    has_key = bool(resolve_google_key())
    print(f"docs/ 서빙 + /api/embed → Gemini ({GEMINI_MODEL}, {EMBED_DIM}d) 프록시")
    print(f"Gemini 키: {'감지됨' if has_key else '없음 (검색 임베딩 비활성 — 키 설정 필요)'}")
    print(f"열기: {url}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n종료합니다.")
    finally:
        httpd.shutdown()
        httpd.server_close()


if __name__ == "__main__":
    main()
