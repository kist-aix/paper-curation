"""
Canonical review.md → index.html converter.
Enforces consistent layout across all review pages.

Usage:
  PYTHONUTF8=1 python review_to_html.py [--topic ai4s|scisci] [--slugs 251-258] [--all]
  PYTHONUTF8=1 python review_to_html.py --all              # regenerate all
  PYTHONUTF8=1 python review_to_html.py --slugs 251-394    # specific range
"""
import os, re, sys, json, argparse
from html import escape as esc

from config_loader import PAPERS_DIR as _PAPERS_DIR
PAPERS = str(_PAPERS_DIR)

# Zotero PDF attachment keys (slug → key). Written by build_topic_index;
# absent on the very first build, harmless when missing — button just doesn't
# render for papers without a known key.
_ZOTERO_KEYS_PATH = os.path.join(os.path.dirname(_PAPERS_DIR), "_zotero_keys.json")
try:
    with open(_ZOTERO_KEYS_PATH, "r", encoding="utf-8") as _f:
        _ZOTERO_KEYS = json.load(_f)
except Exception:
    _ZOTERO_KEYS = {}

# Gemini key for the browser-direct Audio Overview feature. Baked into the
# review page at build time (like the Deep Research keys in build_topic_index),
# then stripped from every deployed page by prepare_deploy.py. On Cloudflare the
# value is "" so the generate button stays disabled (localhost-only feature).
_GEMINI_KEY = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY") or ""
if not _GEMINI_KEY:
    _cfg_path = os.path.join(os.path.dirname(os.path.dirname(_PAPERS_DIR)), "config.json")
    try:
        with open(_cfg_path, "r", encoding="utf-8") as _f:
            _cfg = json.load(_f)
        _GEMINI_KEY = _cfg.get("gemini_api_key") or _cfg.get("google_api_key", "")
    except Exception:
        pass

THEMES = {
    "ai4s": {"accent": "#D63423", "accent_dark": "#A62018", "accent_bg": "#FEF0EF",
             "essence_border": "#8B1A1A", "essence_bg": "#FDF8F8",
             "link_color": "#A62018", "back_href": "../../ai4s/index.html"},
    "scisci": {"accent": "#2374D6", "accent_dark": "#1856A0", "accent_bg": "#EBF3FF",
               "essence_border": "#1856A0", "essence_bg": "#F8FAFD",
               "link_color": "#1856A0", "back_href": "../../scisci/index.html"},
}

# Paper connections cache (loaded once per run)
_connections_cache = {}

def _load_connections():
    """Load all _paper_connections.json files."""
    global _connections_cache
    if _connections_cache:
        return _connections_cache
    from config_loader import get_topic_dir
    for topic in THEMES:
        conn_path = os.path.join(str(get_topic_dir(topic)), "_paper_connections.json")
        if os.path.exists(conn_path):
            with open(conn_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            _connections_cache.update(data)
    return _connections_cache

def get_css(t):
    return f"""* {{ margin: 0; padding: 0; box-sizing: border-box; }}
body {{ font-family: 'KoPub Dotum', 'KoPubDotumMedium', -apple-system, 'Noto Sans KR', sans-serif; max-width: 820px; margin: 0 auto; padding: 2rem 1.5rem; line-height: 1.7; color: #333; background: #f0f2f5; }}
h1 {{ font-size: 1.4rem; color: #1a1a2e; border-bottom: 3px solid {t['accent']}; padding-bottom: 0.5rem; margin-bottom: 1rem; }}
h2 {{ font-size: 1.1rem; color: {t['accent']}; margin: 0 0 0.6rem; padding: 0; border: none; }}
h3 {{ font-size: 1rem; color: #333; margin: 0.8rem 0 0.4rem; }}
p {{ margin: 0.4rem 0; font-size: 0.93rem; }}
blockquote {{ border-left: 4px solid {t['accent']}; margin: 0.8rem 0; padding: 0.6rem 1rem; background: #f0f4f8; border-radius: 0 8px 8px 0; font-size: 0.88rem; color: #555; }}
ul, ol {{ margin: 0.4rem 0 0.4rem 1.5rem; }}
li {{ margin: 0.2rem 0; font-size: 0.93rem; }}
.section-box {{ background: white; border-radius: 12px; padding: 1.2rem 1.5rem; margin-bottom: 1rem; box-shadow: 0 1px 4px rgba(0,0,0,0.06); }}
table {{ border-collapse: collapse; margin: 0.5rem 0; font-size: 0.85rem; width: 100%; }}
th, td {{ border: 1px solid #e0e0e0; padding: 6px 12px; text-align: left; }}
th {{ background: {t['accent']}; color: white; font-weight: 600; font-size: 0.82rem; }}
tr:nth-child(even) {{ background: #f8f9fa; }}
td:last-child {{ text-align: center; font-weight: 600; color: {t['accent']}; }}
.eval-badges {{ display: flex; flex-wrap: wrap; gap: 0.4rem; margin: 0.6rem 0; }}
.eval-badge {{ background: {t['accent_bg']}; color: {t['accent_dark']}; padding: 0.2rem 0.7rem; border-radius: 14px; font-size: 0.8rem; font-weight: 600; }}
.essence-box {{ border: 2px solid {t['essence_border']}; border-radius: 10px; padding: 1rem 1.2rem; margin: 0.8rem 0; background: {t['essence_bg']}; }}
.essence-box h2 {{ color: {t['essence_border']}; margin: 0 0 0.5rem; border: none; padding: 0; }}
code {{ background: #e8edf3; padding: 0.15rem 0.4rem; border-radius: 4px; font-size: 0.85rem; }}
img {{ max-width: min(100%, 700px); border: 1px solid #e8e8e8; border-radius: 8px; margin: 0.8rem auto; display: block; box-shadow: 0 2px 8px rgba(0,0,0,0.08); }}
hr {{ border: none; border-top: 1px solid #e0e0e0; margin: 0.5rem 0; }}
strong {{ color: #1a1a2e; }}
a {{ color: {t['link_color']}; }}
.back {{ margin-top: 1.5rem; padding: 0.8rem 0; border-top: 2px solid #e0e0e0; }}
.back a {{ font-weight: 600; text-decoration: none; }}
.back a:hover {{ text-decoration: underline; }}
.connections-box {{ background: white; border-radius: 12px; padding: 1.2rem 1.5rem; margin: 1.2rem 0; box-shadow: 0 1px 4px rgba(0,0,0,0.06); }}
.connections-box h2 {{ color: {t['accent']}; margin: 0 0 0.8rem; border: none; padding: 0; font-size: 1.05rem; }}
.conn-item {{ border-left: 3px solid #ddd; padding: 0.6rem 0 0.6rem 1rem; margin-bottom: 0.6rem; }}
.conn-item.alternative {{ border-left-color: #3B82F6; }}
.conn-item.extension {{ border-left-color: #10B981; }}
.conn-item.foundation {{ border-left-color: #8B5CF6; }}
.conn-item.counterpoint {{ border-left-color: #F59E0B; }}
.conn-item.application {{ border-left-color: #EF4444; }}
.conn-type {{ font-size: 0.72rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.04em; color: #888; margin-bottom: 0.15rem; }}
.conn-item.alternative .conn-type {{ color: #3B82F6; }}
.conn-item.extension .conn-type {{ color: #10B981; }}
.conn-item.foundation .conn-type {{ color: #8B5CF6; }}
.conn-item.counterpoint .conn-type {{ color: #F59E0B; }}
.conn-item.application .conn-type {{ color: #EF4444; }}
.conn-title {{ font-size: 0.9rem; font-weight: 600; }}
.conn-title a {{ color: #1a1a2e; text-decoration: none; }}
.conn-title a:hover {{ color: {t['accent']}; text-decoration: underline; }}
.conn-reason {{ font-size: 0.85rem; color: #555; margin-top: 0.15rem; }}
.review-fig {{ text-align: center; margin: 1.5rem 0; padding: 1rem; background: #f8f9fa; border-radius: 12px; }}
.review-fig img {{ max-width: min(100%, 700px); border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); cursor: zoom-in; }}
.lightbox {{ display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.85); z-index: 9999; cursor: zoom-out; align-items: center; justify-content: center; }}
.lightbox.active {{ display: flex; }}
.lightbox img {{ max-width: 95%; max-height: 95%; object-fit: contain; border-radius: 8px; }}
.fig-caption {{ font-size: 0.85rem; color: #888; margin-top: 0.5rem; font-style: italic; }}"""


# ---------------------------------------------------------------------------
# Audio Overview (browser-direct podcast generation via Gemini). localhost-only.
# ---------------------------------------------------------------------------

def get_audio_css(t):
    return f""".audio-bar {{ margin: 0.6rem 0 0.2rem; }}
.audio-btn {{ display: inline-flex; align-items: center; gap: 0.4rem; background: {t['accent']}; color: #fff; border: none; border-radius: 20px; padding: 0.45rem 1rem; font-size: 0.85rem; font-weight: 600; cursor: pointer; font-family: inherit; box-shadow: 0 1px 4px rgba(0,0,0,0.12); }}
.audio-btn:hover {{ background: {t['accent_dark']}; }}
.audio-btn:disabled {{ background: #bbb; cursor: not-allowed; box-shadow: none; }}
.audio-modal-bg {{ display: none; position: fixed; inset: 0; background: rgba(0,0,0,0.5); z-index: 10000; align-items: center; justify-content: center; padding: 1rem; }}
.audio-modal-bg.active {{ display: flex; }}
.audio-modal {{ background: #fff; border-radius: 14px; max-width: 540px; width: 100%; max-height: 92vh; overflow-y: auto; padding: 1.4rem 1.6rem; box-shadow: 0 8px 40px rgba(0,0,0,0.25); }}
.audio-modal h3 {{ margin: 0 0 0.2rem; color: {t['accent']}; font-size: 1.15rem; }}
.audio-modal .sub {{ font-size: 0.8rem; color: #888; margin-bottom: 1rem; }}
.audio-row {{ margin-bottom: 0.9rem; }}
.audio-row > label {{ display: block; font-size: 0.82rem; font-weight: 700; color: #444; margin-bottom: 0.3rem; }}
.audio-seg {{ display: inline-flex; border: 1px solid #ddd; border-radius: 8px; overflow: hidden; }}
.audio-seg button {{ background: #fff; border: none; padding: 0.4rem 0.9rem; font-size: 0.85rem; cursor: pointer; font-family: inherit; color: #555; border-right: 1px solid #eee; }}
.audio-seg button:last-child {{ border-right: none; }}
.audio-seg button.on {{ background: {t['accent_bg']}; color: {t['accent_dark']}; font-weight: 700; }}
.audio-modal select, .audio-modal input[type=text], .audio-modal textarea {{ width: 100%; padding: 0.45rem 0.6rem; border: 1px solid #ddd; border-radius: 8px; font-size: 0.85rem; font-family: inherit; color: #333; background: #fff; }}
.audio-modal textarea {{ min-height: 80px; resize: vertical; line-height: 1.55; }}
.audio-adv-toggle {{ font-size: 0.82rem; color: {t['accent_dark']}; cursor: pointer; user-select: none; font-weight: 600; }}
.audio-adv {{ display: none; margin-top: 0.6rem; }}
.audio-adv.open {{ display: block; }}
.audio-actions {{ display: flex; gap: 0.6rem; justify-content: flex-end; margin-top: 1.1rem; }}
.audio-actions .cancel {{ background: #eee; color: #555; }}
.audio-actions button {{ border: none; border-radius: 20px; padding: 0.5rem 1.2rem; font-size: 0.88rem; font-weight: 600; cursor: pointer; font-family: inherit; }}
.audio-actions .go {{ background: {t['accent']}; color: #fff; }}
.audio-actions .go:disabled {{ background: #bbb; cursor: not-allowed; }}
.audio-status {{ font-size: 0.82rem; color: #666; margin-top: 0.8rem; min-height: 1.1em; }}
.audio-player {{ display: none; margin-top: 1rem; padding-top: 1rem; border-top: 1px solid #eee; }}
.audio-player.show {{ display: block; }}
.audio-player audio {{ width: 100%; margin-bottom: 0.6rem; }}
.audio-speed {{ display: flex; align-items: center; gap: 0.6rem; font-size: 0.82rem; color: #555; }}
.audio-speed input[type=range] {{ flex: 1; }}
.audio-dl {{ display: inline-block; margin-top: 0.6rem; font-size: 0.82rem; color: {t['accent_dark']}; text-decoration: none; font-weight: 600; }}"""


def audio_bar_html():
    """Button shown under the title; disabled & relabeled when no key (deployed)."""
    if _GEMINI_KEY:
        return ('<div class="audio-bar">'
                '<button class="audio-btn" id="audio-open" onclick="openAudioModal()">'
                '\U0001F3A7 Audio Overview 생성</button></div>')
    return ('<div class="audio-bar">'
            '<button class="audio-btn" disabled '
            'title="로컬(localhost)에서만 생성할 수 있습니다">'
            '\U0001F3A7 Audio Overview (로컬 전용)</button></div>')


def audio_modal_html():
    if not _GEMINI_KEY:
        return ""
    return """
<div class="audio-modal-bg" id="audio-modal-bg">
  <div class="audio-modal">
    <h3>\U0001F3A7 Audio Overview</h3>
    <div class="sub">이 논문 리뷰를 팟캐스트형 오디오로 생성합니다. (Gemini · 로컬 전용)</div>
    <div class="audio-row">
      <label>화자 수</label>
      <div class="audio-seg" id="seg-speakers">
        <button data-v="1">1인</button><button data-v="2">2인</button><button data-v="3">3인</button>
      </div>
    </div>
    <div class="audio-row">
      <label>언어</label>
      <div class="audio-seg" id="seg-lang">
        <button data-v="ko">한국어</button><button data-v="en">English</button>
      </div>
    </div>
    <div class="audio-row">
      <label>대상 청중</label>
      <select id="audio-audience">
        <option value="general">일반인</option>
        <option value="student">대학생·대학원생</option>
        <option value="expert">전문가</option>
      </select>
    </div>
    <div class="audio-row">
      <label>길이</label>
      <div class="audio-seg" id="seg-length">
        <button data-v="10">10분</button><button data-v="20">20분</button><button data-v="30">30분</button>
      </div>
    </div>
    <div class="audio-row">
      <label>톤</label>
      <select id="audio-tone">
        <option value="friendly">친근한</option>
        <option value="academic">학술적</option>
        <option value="lively">활기찬</option>
      </select>
    </div>
    <div class="audio-row">
      <label>주안점 (선택)</label>
      <input type="text" id="audio-focus" placeholder="예: 방법론의 한계, 산업 응용 가능성">
    </div>
    <div class="audio-row">
      <span class="audio-adv-toggle" onclick="toggleAudioAdv()">▸ 고급: 구성 방향(대본 작성 지침) 직접 수정</span>
      <div class="audio-adv" id="audio-adv">
        <textarea id="audio-direction"></textarea>
      </div>
    </div>
    <div class="audio-status" id="audio-status"></div>
    <div class="audio-actions">
      <button class="cancel" onclick="closeAudioModal()">닫기</button>
      <button class="go" id="audio-go" onclick="runAudioGen()">생성</button>
    </div>
    <div class="audio-player" id="audio-player">
      <audio id="audio-el" controls></audio>
      <div class="audio-speed">
        <span>속도</span>
        <input type="range" id="audio-speed" min="0.75" max="1.75" step="0.05" value="1">
        <span id="audio-speed-val">1.0x</span>
      </div>
      <a class="audio-dl" id="audio-dl" download="audio_overview.mp3">⬇ MP3 다운로드</a>
    </div>
  </div>
</div>"""


# Browser-side generation logic. Plain string (no f-substitution) — the key
# and per-paper context are injected by audio_script_block() as a prefix.
AUDIO_JS = r"""
const GKEY = window._GEMINI_KEY || "";
const CTX = window._AUDIO || {title:"", review:"", connections:[]};
const SCRIPT_MODEL = "gemini-2.5-pro";
const TTS_MODEL = "gemini-2.5-flash-preview-tts";
const GBASE = "https://generativelanguage.googleapis.com/v1beta/models/";
const SAMPLE_RATE = 24000;
const MAX_CHUNK_CHARS = 2200;   // per TTS call, keeps long scripts within limits
const POOL = 3;                 // concurrent TTS calls

const DEFAULT_DIRECTION = {
  ko: "논문의 originality(독창성)를 중심으로, '같이 보면 좋은 논문'들과의 연관성(예: 장단점 비교, 대조, 후속, 보완 등)을 엮어서 전체 맥락을 파악할 수 있도록 구성한다.",
  en: "Center the narrative on the paper's originality, weaving in how it relates to the recommended related papers (e.g., pros/cons comparison, contrast, follow-up, complement) so the listener grasps the overall context."
};

const ROLES = {
  ko: {
    1: [{label:"내레이터", voice:"Kore", desc:"차분하고 명료한 1인 내레이터"}],
    2: [{label:"전문가", voice:"Kore", desc:"과학기술 전문가(여성). 논문의 originality와 기술적 핵심을 정확하고 깊이 있게 설명한다."},
        {label:"리포터", voice:"Puck", desc:"논문의 파급효과와 의의에 관심이 많은 진행자(남성). 청취자 눈높이에서 질문하고, 같이 보면 좋은 논문들과의 관계를 짚으며 맥락을 넓힌다."}],
    3: [{label:"사회자", voice:"Leda", desc:"토론을 이끌고 핵심을 정리하는 진행자"},
        {label:"전문가", voice:"Kore", desc:"과학기술 전문가(여성). originality와 기술 핵심을 설명한다."},
        {label:"리포터", voice:"Algieba", desc:"파급효과와 연관 논문에 관심 많은 패널(남성)."}]
  },
  en: {
    1: [{label:"Narrator", voice:"Kore", desc:"a calm, clear solo narrator"}],
    2: [{label:"Expert", voice:"Kore", desc:"a science-and-technology expert (female) who explains the paper's originality and technical core precisely and in depth"},
        {label:"Reporter", voice:"Puck", desc:"a host (male) keen on the paper's impact and significance, asking listener-level questions and connecting it to the recommended related papers"}],
    3: [{label:"Host", voice:"Leda", desc:"a host who drives the discussion and sums up the key points"},
        {label:"Expert", voice:"Kore", desc:"a science-and-technology expert (female) explaining originality and the technical core"},
        {label:"Reporter", voice:"Algieba", desc:"a panelist (male) keen on impact and related papers"}]
  }
};

// Gemini multi-speaker TTS needs a leading style instruction or it tries to
// "answer" the transcript as text instead of voicing it.
const TTS_PREFIX = {ko: "다음 대화를 자연스럽고 생동감 있게 읽어줘:\n", en: "Read the following conversation naturally and with energy:\n"};

const AUDIENCE = {
  ko: {general:"일반 대중", student:"대학생·대학원생", expert:"해당 분야 전문가"},
  en: {general:"a general audience", student:"undergraduate and graduate students", expert:"domain experts"}
};
const TONE = {
  ko: {friendly:"친근하지만 전문적이고, 청취자에게 말 걸 듯이", academic:"차분하고 학술적이며 정확하게", lively:"활기차고 박진감 있게"},
  en: {friendly:"warm yet professional, speaking directly to the listener", academic:"calm, academic and precise", lively:"lively and energetic"}
};

const SETTINGS_KEY = "paperAudioSettings";
function defaultSettings() {
  return {speakers:"2", lang:"ko", audience:"student", length:"10", tone:"friendly",
          focus:"", direction:DEFAULT_DIRECTION.ko, directionDirty:false};
}
function loadSettings() {
  try { return Object.assign(defaultSettings(), JSON.parse(localStorage.getItem(SETTINGS_KEY) || "{}")); }
  catch (e) { return defaultSettings(); }
}
function saveSettings(s) { try { localStorage.setItem(SETTINGS_KEY, JSON.stringify(s)); } catch (e) {} }

function setSeg(groupId, val) {
  document.querySelectorAll("#" + groupId + " button").forEach(function(b) {
    b.classList.toggle("on", b.getAttribute("data-v") === String(val));
  });
}
function getSeg(groupId) {
  const on = document.querySelector("#" + groupId + " button.on");
  return on ? on.getAttribute("data-v") : null;
}

function openAudioModal() {
  const s = loadSettings();
  setSeg("seg-speakers", s.speakers);
  setSeg("seg-lang", s.lang);
  setSeg("seg-length", s.length);
  document.getElementById("audio-audience").value = s.audience;
  document.getElementById("audio-tone").value = s.tone;
  document.getElementById("audio-focus").value = s.focus || "";
  const dir = document.getElementById("audio-direction");
  dir.value = s.directionDirty ? s.direction : DEFAULT_DIRECTION[s.lang];
  dir.dataset.dirty = s.directionDirty ? "1" : "";
  document.getElementById("audio-status").textContent = "";
  document.getElementById("audio-modal-bg").classList.add("active");
}
function closeAudioModal() { document.getElementById("audio-modal-bg").classList.remove("active"); }
function toggleAudioAdv() {
  const a = document.getElementById("audio-adv");
  a.classList.toggle("open");
  document.querySelector(".audio-adv-toggle").textContent =
    (a.classList.contains("open") ? "▾" : "▸") + " 고급: 구성 방향(대본 작성 지침) 직접 수정";
}

function wireAudioModal() {
  ["seg-speakers", "seg-lang", "seg-length"].forEach(function(gid) {
    document.querySelectorAll("#" + gid + " button").forEach(function(b) {
      b.addEventListener("click", function() {
        setSeg(gid, b.getAttribute("data-v"));
        if (gid === "seg-lang") {
          const dir = document.getElementById("audio-direction");
          if (!dir.dataset.dirty) dir.value = DEFAULT_DIRECTION[b.getAttribute("data-v")];
        }
      });
    });
  });
  const dir = document.getElementById("audio-direction");
  if (dir) dir.addEventListener("input", function() { dir.dataset.dirty = "1"; });
  document.getElementById("audio-modal-bg").addEventListener("click", function(e) {
    if (e.target.id === "audio-modal-bg") closeAudioModal();
  });
}

function collectSettings() {
  const dir = document.getElementById("audio-direction");
  return {
    speakers: getSeg("seg-speakers") || "2",
    lang: getSeg("seg-lang") || "ko",
    audience: document.getElementById("audio-audience").value,
    length: getSeg("seg-length") || "10",
    tone: document.getElementById("audio-tone").value,
    focus: document.getElementById("audio-focus").value.trim(),
    direction: dir.value.trim(),
    directionDirty: dir.dataset.dirty === "1"
  };
}

function lengthGuide(min, lang) {
  // Calibrated from measured Gemini TTS rate (~560 ko chars/min) and over-asked
  // ~1.3x because the model under-fills long length targets. ko≈730 chars/min.
  const m = parseInt(min, 10);
  if (lang === "en") return "about " + m + " minutes — write at least " + (m * 200) +
    " words; fill the entire length with substantive discussion and do not wrap up early";
  return "약 " + m + "분 분량 — 한국어로 최소 " + (m * 730) +
    "자 이상 작성하고, 내용을 충분히 깊게 다뤄 분량을 끝까지 채울 것(중간에 서둘러 마무리하지 말 것)";
}

function connectionsText(lang) {
  const cs = CTX.connections || [];
  if (!cs.length) return "";
  const head = lang === "en" ? "Recommended related papers (weave these into the context):"
                             : "같이 보면 좋은 논문 (맥락에 엮을 것):";
  const lines = cs.map(function(c) {
    return "- [" + (c.relation || "") + "] " + (c.title || "") + (c.reason ? " — " + c.reason : "");
  });
  return head + "\n" + lines.join("\n");
}

function buildScriptPrompt(s) {
  const lang = s.lang;
  const roles = ROLES[lang][s.speakers];
  const tone = TONE[lang][s.tone];
  const aud = AUDIENCE[lang][s.audience];
  const len = lengthGuide(s.length, lang);
  const conns = connectionsText(lang);
  let fmt;
  if (s.speakers === "1") {
    fmt = lang === "en"
      ? "- Format: a single narrator from start to finish; output narration text only, no speaker labels."
      : "- 형식: 한 명의 내레이터가 처음부터 끝까지 진행. 화자 라벨 없이 순수 내레이션 텍스트만 출력.";
  } else {
    const roleLines = roles.map(function(r) {
      return (lang === "en" ? "- " + r.label + ": " + r.desc
                            : "- " + r.label + ": " + r.desc);
    }).join("\n");
    const labels = roles.map(function(r) { return r.label; });
    fmt = (lang === "en"
        ? "- Format: a " + s.speakers + "-person conversational podcast.\n" + roleLines +
          "\n- Begin every utterance with exactly one of these labels followed by ': ' — " +
          labels.join(", ") + "\n- Natural turn-taking; no one speaks more than ~5 sentences in a row."
        : "- 형식: " + s.speakers + "인 대화형 팟캐스트.\n" + roleLines +
          "\n- 각 발화는 반드시 다음 라벨 중 하나로 시작하고 콜론+공백을 붙일 것 — " +
          labels.join(", ") + "\n- 자연스러운 turn-taking, 한 명이 5문장 이상 연속 독점 금지.");
  }
  const focusLine = s.focus ? (lang === "en" ? "- Special emphasis: " + s.focus + "\n"
                                             : "- 주안점: " + s.focus + "\n") : "";
  if (lang === "en") {
    return "You are a science-podcast scriptwriter. Using the paper review below, write a script a listener can play in one sitting.\n\n" +
      "Requirements:\n- Length: " + len + "\n- Tone: " + tone + "\n- Target audience: " + aud +
      " — use vocabulary and analogies at this level.\n" + focusLine +
      "- Editorial direction: " + s.direction + "\n" + fmt +
      "\n- Spell out acronyms on first use, then abbreviate.\n- No markdown, no headers, no bullet symbols, no sound-effect or SSML tags.\n\n" +
      (conns ? conns + "\n\n" : "") +
      "Paper review:\n---\n" + CTX.review + "\n---\n\nOutput only the script body, starting immediately (no 'Script:' preamble).";
  }
  return "당신은 과학 팟캐스트 작가입니다. 아래 논문 리뷰를 바탕으로 청취자가 한 번에 들을 수 있는 대본을 작성하세요.\n\n" +
    "요구사항:\n- 길이: " + len + "\n- 톤: " + tone + "\n- 대상 청취자: " + aud +
    " — 이 수준의 어휘와 비유로 설명할 것.\n" + focusLine +
    "- 구성 방향: " + s.direction + "\n" + fmt +
    "\n- 영어 약어는 첫 등장 시 한국어 풀이를 곁들이고 이후 약어 사용.\n- 마크다운 헤더·불릿·강조 기호 금지. 효과음·SSML 태그·괄호 안 메타 표기 없음.\n\n" +
    (conns ? conns + "\n\n" : "") +
    "논문 리뷰 자료:\n---\n" + CTX.review + "\n---\n\n위 요구사항에 따라 대본 본문만 출력하세요. '대본:' 같은 머리말 없이 바로 시작.";
}

async function geminiPost(model, body) {
  const r = await fetch(GBASE + model + ":generateContent?key=" + encodeURIComponent(GKEY), {
    method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify(body)
  });
  if (!r.ok) {
    let msg = r.status + " " + r.statusText;
    try { const j = await r.json(); if (j.error && j.error.message) msg = j.error.message; } catch (e) {}
    throw new Error(msg);
  }
  return r.json();
}

async function callScript(prompt) {
  const j = await geminiPost(SCRIPT_MODEL, {
    contents: [{parts: [{text: prompt}]}],
    generationConfig: {temperature: 0.85, maxOutputTokens: 65536}
  });
  const parts = (((j.candidates || [])[0] || {}).content || {}).parts || [];
  return parts.map(function(p) { return p.text || ""; }).join("").trim();
}

function speechSingle(voice) {
  return {voiceConfig: {prebuiltVoiceConfig: {voiceName: voice}}};
}
function speechMulti(roles) {
  return {multiSpeakerVoiceConfig: {speakerVoiceConfigs: roles.map(function(r) {
    return {speaker: r.label, voiceConfig: {prebuiltVoiceConfig: {voiceName: r.voice}}};
  })}};
}

function b64ToBytes(b64) {
  const bin = atob(b64);
  const out = new Uint8Array(bin.length);
  for (let i = 0; i < bin.length; i++) out[i] = bin.charCodeAt(i);
  return out;
}

async function ttsCall(text, speechConfig) {
  const j = await geminiPost(TTS_MODEL, {
    contents: [{parts: [{text: text}]}],
    generationConfig: {responseModalities: ["AUDIO"], speechConfig: speechConfig}
  });
  const part = ((((j.candidates || [])[0] || {}).content || {}).parts || [])[0] || {};
  const data = (part.inlineData || part.inline_data || {}).data;
  if (!data) throw new Error("TTS 응답에 오디오가 없습니다");
  return b64ToBytes(data);
}

function parseTurns(script, labels) {
  const esc = labels.map(function(l) { return l.replace(/[.*+?^${}()|[\]\\]/g, "\\$&"); });
  const re = new RegExp("^(" + esc.join("|") + ")\\s*:\\s*(.*)$");
  const turns = []; let cur = null, buf = [];
  function flush() { if (cur && buf.join(" ").trim()) turns.push({speaker: cur, text: buf.join(" ").trim()}); }
  script.split(/\r?\n/).forEach(function(raw) {
    const line = raw.trim();
    if (!line) return;
    const m = line.match(re);
    if (m) { flush(); cur = m[1]; buf = [m[2].trim()]; }
    else if (cur) buf.push(line);
  });
  flush();
  return turns;
}

function chunkParagraphs(text, maxChars) {
  const paras = text.split(/\n\s*\n/).map(function(p) { return p.replace(/\s+/g, " ").trim(); }).filter(Boolean);
  const chunks = []; let cur = "";
  paras.forEach(function(p) {
    if (cur && (cur.length + p.length + 1) > maxChars) { chunks.push(cur); cur = ""; }
    cur = cur ? cur + "\n" + p : p;
  });
  if (cur) chunks.push(cur);
  return chunks.length ? chunks : [text];
}

function chunkTurns(turns, maxChars) {
  const chunks = []; let cur = [], len = 0;
  turns.forEach(function(t) {
    const piece = t.speaker + ": " + t.text;
    if (cur.length && (len + piece.length + 1) > maxChars) { chunks.push(cur); cur = []; len = 0; }
    cur.push(piece); len += piece.length + 1;
  });
  if (cur.length) chunks.push(cur);
  return chunks.map(function(c) { return c.join("\n"); });
}

async function poolMap(items, worker, concurrency) {
  const results = new Array(items.length);
  let next = 0;
  async function run() {
    while (true) {
      const i = next++;
      if (i >= items.length) return;
      results[i] = await worker(items[i], i);
    }
  }
  const runners = [];
  for (let k = 0; k < Math.min(concurrency, items.length); k++) runners.push(run());
  await Promise.all(runners);
  return results;
}

function concatPcm(parts) {
  const silence = new Uint8Array(Math.floor(SAMPLE_RATE * 0.2) * 2); // 200ms
  const pieces = []; let total = 0;
  parts.forEach(function(p, i) {
    if (i) { pieces.push(silence); total += silence.length; }
    pieces.push(p); total += p.length;
  });
  const out = new Uint8Array(total); let off = 0;
  pieces.forEach(function(p) { out.set(p, off); off += p.length; });
  return out;
}

function pcmToMp3(pcm) {
  if (typeof lamejs === "undefined") throw new Error("MP3 인코더(lamejs) 로드 실패");
  const samples = new Int16Array(pcm.buffer, pcm.byteOffset, pcm.length >> 1);
  const enc = new lamejs.Mp3Encoder(1, SAMPLE_RATE, 128);
  const block = 1152, out = [];
  for (let i = 0; i < samples.length; i += block) {
    const buf = enc.encodeBuffer(samples.subarray(i, i + block));
    if (buf.length) out.push(new Uint8Array(buf));
  }
  const tail = enc.flush();
  if (tail.length) out.push(new Uint8Array(tail));
  return new Blob(out, {type: "audio/mpeg"});
}

function setStatus(msg) { document.getElementById("audio-status").textContent = msg; }

async function synthesize(s, script) {
  const roles = ROLES[s.lang][s.speakers];
  if (s.speakers === "1") {
    const chunks = chunkParagraphs(script, MAX_CHUNK_CHARS);
    const cfg = speechSingle(roles[0].voice);
    let done = 0;
    const parts = await poolMap(chunks, async function(c) {
      const pcm = await ttsCall(c, cfg);
      setStatus("🔊 음성 합성 " + (++done) + "/" + chunks.length);
      return pcm;
    }, POOL);
    return concatPcm(parts);
  }
  const labels = roles.map(function(r) { return r.label; });
  const turns = parseTurns(script, labels);
  if (!turns.length) throw new Error("대본에서 화자 라벨을 찾지 못했습니다");
  if (s.speakers === "2") {
    const chunks = chunkTurns(turns, MAX_CHUNK_CHARS);
    const cfg = speechMulti(roles);
    const prefix = TTS_PREFIX[s.lang] || TTS_PREFIX.ko;
    let done = 0;
    const parts = await poolMap(chunks, async function(c) {
      const pcm = await ttsCall(prefix + c, cfg);
      setStatus("🔊 음성 합성 " + (++done) + "/" + chunks.length);
      return pcm;
    }, POOL);
    return concatPcm(parts);
  }
  // 3 speakers: per-turn single-voice (Gemini multi-speaker caps at 2)
  const voiceMap = {}; roles.forEach(function(r) { voiceMap[r.label] = r.voice; });
  let done = 0;
  const parts = await poolMap(turns, async function(t) {
    const pcm = await ttsCall(t.text, speechSingle(voiceMap[t.speaker] || roles[0].voice));
    setStatus("🔊 음성 합성 " + (++done) + "/" + turns.length);
    return pcm;
  }, POOL);
  return concatPcm(parts);
}

let _audioUrl = null;
async function runAudioGen() {
  if (!GKEY) { setStatus("Gemini 키가 없습니다 (로컬 전용)"); return; }
  const go = document.getElementById("audio-go");
  go.disabled = true;
  const s = collectSettings();
  saveSettings(s);
  try {
    setStatus("✍️ 대본 생성 중... (gemini-2.5-pro)");
    const script = await callScript(buildScriptPrompt(s));
    if (!script) throw new Error("대본이 비어 있습니다");
    setStatus("🔊 음성 합성 중...");
    const pcm = await synthesize(s, script);
    setStatus("🎚️ MP3 인코딩 중...");
    const blob = pcmToMp3(pcm);
    if (_audioUrl) URL.revokeObjectURL(_audioUrl);
    _audioUrl = URL.createObjectURL(blob);
    const el = document.getElementById("audio-el");
    el.src = _audioUrl;
    if ("preservesPitch" in el) el.preservesPitch = true;
    const dl = document.getElementById("audio-dl");
    dl.href = _audioUrl;
    dl.download = (CTX.title || "audio_overview").slice(0, 60).replace(/[^\w가-힣 -]/g, "").trim().replace(/\s+/g, "_") + ".mp3";
    document.getElementById("audio-player").classList.add("show");
    const dur = pcm.length / 2 / SAMPLE_RATE;
    setStatus("✅ 완료 (약 " + Math.round(dur) + "초)");
  } catch (e) {
    console.error(e);
    setStatus("오류: " + (e.message || e));
  } finally {
    go.disabled = false;
  }
}

document.addEventListener("DOMContentLoaded", function() {
  // Deployed pages have the key stripped (window._GEMINI_KEY = ""): disable
  // the button so it can't be clicked into a dead end.
  if (!GKEY) {
    const ob = document.getElementById("audio-open");
    if (ob) { ob.disabled = true; ob.title = "로컬(localhost)에서만 생성할 수 있습니다";
              ob.innerHTML = "🎧 Audio Overview (로컬 전용)"; }
  }
  if (!document.getElementById("audio-modal-bg")) return;
  wireAudioModal();
  const sp = document.getElementById("audio-speed");
  const el = document.getElementById("audio-el");
  if (sp && el) sp.addEventListener("input", function() {
    el.playbackRate = parseFloat(sp.value);
    document.getElementById("audio-speed-val").textContent = parseFloat(sp.value).toFixed(2) + "x";
  });
});
"""


def audio_script_block(ctx):
    """Wrap AUDIO_JS with the injected Gemini key + per-paper context."""
    if not _GEMINI_KEY:
        return ""
    prefix = ("window._GEMINI_KEY = " + json.dumps(_GEMINI_KEY) + ";\n"
              "window._AUDIO = " + json.dumps(ctx, ensure_ascii=False) + ";\n")
    # lamejs (pure-JS MP3 encoder) loaded first so PCM→MP3 is available on click.
    return ('<script src="https://cdn.jsdelivr.net/npm/lamejs@1.2.1/lame.min.js"></script>\n'
            "<script>\n" + prefix + AUDIO_JS + "\n</script>")


def parse_scores(md):
    """Extract evaluation scores from markdown table or list format."""
    scores = {}
    for label, key in [("Novelty", "novelty"), ("Technical Soundness", "tech"),
                        ("Significance", "sig"), ("Clarity", "clarity"), ("Overall", "overall")]:
        # Table: | Label | X/5 |
        m = re.search(rf'\|\s*{label}\s*\|\s*(\d+(?:\.\d+)?)\s*/\s*5\s*\|', md)
        if not m:
            # List: - Label: X/5
            m = re.search(rf'-\s*{label}\s*:\s*(\d+(?:\.\d+)?)\s*/\s*5', md)
        if m:
            scores[key] = m.group(1)
    return scores


def _get_indent(line):
    """Return indent level (number of leading spaces / 2)."""
    stripped = line.lstrip()
    return (len(line) - len(stripped)) // 2 if stripped else 0


def _is_ul(s):
    return bool(re.match(r'^[-*]\s', s))


def _is_ol(s):
    return bool(re.match(r'^\d+\.\s', s))


def _list_content(s):
    if _is_ul(s):
        return re.sub(r'^[-*]\s+', '', s)
    if _is_ol(s):
        return re.sub(r'^\d+\.\s*', '', s)
    return s


def md_section_to_html(text, slug_dir=None):
    """Convert markdown body text to HTML (within a section)."""
    lines = text.strip().split('\n')
    out = []
    in_table = False
    table_header_done = False
    # List state: stack of (tag, indent_level)
    list_stack = []

    def close_lists_to(target_depth):
        while len(list_stack) > target_depth:
            tag, _ = list_stack.pop()
            out.append(f'</{tag}>')

    def close_all_lists():
        close_lists_to(0)

    i = 0
    while i < len(lines):
        line = lines[i]
        s = line.strip()
        indent = _get_indent(line)

        # Table row
        if s.startswith('|') and '|' in s[1:]:
            close_all_lists()
            if '---' in s:
                i += 1
                continue
            cells = [c.strip() for c in s.split('|')[1:-1]]
            if not in_table:
                out.append('<table>')
                in_table = True
                table_header_done = False
            if not table_header_done:
                out.append('<tr>' + ''.join(f'<th>{esc(c)}</th>' for c in cells) + '</tr>')
                table_header_done = True
            else:
                out.append('<tr>' + ''.join(f'<td>{esc(c)}</td>' for c in cells) + '</tr>')
            i += 1
            continue
        elif in_table:
            out.append('</table>')
            in_table = False

        # List items (any indent level)
        if _is_ul(s) or _is_ol(s):
            tag = 'ol' if _is_ol(s) else 'ul'
            content = _inline(_list_content(s))

            if not list_stack:
                # Start new list
                out.append(f'<{tag}>')
                list_stack.append((tag, indent))
            elif indent > list_stack[-1][1]:
                # Deeper indent → nested list inside last <li>
                # Remove closing </li> from last item to nest inside it
                if out and out[-1].endswith('</li>'):
                    out[-1] = out[-1][:-5]  # strip </li>
                out.append(f'<{tag}>')
                list_stack.append((tag, indent))
            elif indent < list_stack[-1][1]:
                # Shallower → close inner lists
                while list_stack and list_stack[-1][1] > indent:
                    t, _ = list_stack.pop()
                    out.append(f'</{t}>')
                    out.append('</li>')  # close parent <li>
                # Check if tag type matches
                if list_stack and list_stack[-1][0] != tag:
                    t, _ = list_stack.pop()
                    out.append(f'</{t}>')
                    out.append(f'<{tag}>')
                    list_stack.append((tag, indent))
            else:
                # Same level, check tag switch
                if list_stack[-1][0] != tag:
                    t, _ = list_stack.pop()
                    out.append(f'</{t}>')
                    out.append(f'<{tag}>')
                    list_stack.append((tag, indent))

            out.append(f'<li>{content}</li>')
            i += 1
            continue

        # Empty line inside list — look ahead to see if list continues
        if not s and list_stack:
            continues = False
            for j in range(i + 1, len(lines)):
                ps = lines[j].strip()
                if not ps:
                    continue
                if _is_ul(ps) or _is_ol(ps):
                    continues = True
                break
            if not continues:
                close_all_lists()
            i += 1
            continue

        # Non-list content → close any open lists
        if list_stack:
            close_all_lists()

        # Image + optional inline caption: ![alt](src) *caption*
        img_m = re.match(r'!\[([^\]]*)\]\(([^)]+)\)\s*(.*)', s)
        if img_m:
            alt, src, rest = img_m.group(1), img_m.group(2), img_m.group(3).strip()
            # Defensive: drop the reference entirely if the figure file is
            # missing on disk. Some older reviews reference figures that
            # were never extracted or were pruned later; rendering them
            # as-is produces broken <img> tags on the published page.
            # We also peek ahead to eat any adjacent italic-only caption
            # line so it does not end up orphaned after the drop.
            file_ok = True
            if slug_dir and not src.startswith(('http://', 'https://', 'data:')):
                abs_path = os.path.join(slug_dir, src)
                if not os.path.exists(abs_path):
                    file_ok = False
            if not file_ok:
                i += 1
                while i < len(lines) and not lines[i].strip():
                    i += 1
                if i < len(lines):
                    nxt_line = lines[i].strip()
                    if (nxt_line.startswith('*') and nxt_line.endswith('*')
                            and not nxt_line.startswith('**')):
                        i += 1
                continue
            out.append(f'<div class="review-fig"><img src="{esc(src)}" alt="{esc(alt)}">')
            # Inline caption on same line
            if rest and rest.startswith('*') and rest.endswith('*'):
                out.append(f'<p class="fig-caption">{_inline(rest)}</p></div>')
            else:
                out.append('</div>')
                # Check next line for caption
            i += 1
            continue

        # Italic-only line (figure caption) — attaches to preceding review-fig
        if s.startswith('*') and s.endswith('*') and not s.startswith('**'):
            if out and out[-1] == '</div>' and len(out) >= 2 and 'review-fig' in out[-2]:
                out.pop()
                out.append(f'<p class="fig-caption">{_inline(s)}</p></div>')
            else:
                out.append(f'<p class="fig-caption">{_inline(s)}</p>')
            i += 1
            continue

        # HR
        if s == '---' or s == '***':
            out.append('<hr>')
            i += 1
            continue

        # H3
        if s.startswith('### '):
            out.append(f'<h3>{_inline(s[4:])}</h3>')
            i += 1
            continue

        # Empty line
        if not s:
            i += 1
            continue

        # Paragraph
        out.append(f'<p>{_inline(s)}</p>')
        i += 1

    close_all_lists()
    if in_table:
        out.append('</table>')
    return '\n'.join(out)


def _inline(text):
    """Process inline markdown: bold, italic, links, code."""
    text = re.sub(r'`([^`]+)`', r'<code>\1</code>', text)
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'(?<!\*)\*([^*]+?)\*(?!\*)', r'<em>\1</em>', text)
    text = re.sub(r'\[([^\]]+)\]\((https?://[^)]+)\)', r'<a href="\2" target="_blank">\1</a>', text)
    # Remove empty markdown links: [](url) → just the URL or nothing
    def _fix_empty_link(m):
        url = m.group(1)
        # Empty DOI link like [](https://doi.org/) → remove entirely
        if url.rstrip('/') == 'https://doi.org':
            return 'N/A'
        # Non-empty URL with empty text → show URL as link
        return f'<a href="{url}" target="_blank">{url}</a>'
    text = re.sub(r'\[\]\((https?://[^)]+)\)', _fix_empty_link, text)
    # DOI auto-link — skip DOIs already inside <a> tags (href or link text)
    def _doi_auto_link(match):
        start = match.start()
        # Check if this DOI is inside an <a> tag by looking for unclosed <a before it
        before = text[:start]
        last_a_open = before.rfind('<a ')
        last_a_close = before.rfind('</a>')
        if last_a_open > last_a_close:
            return match.group(0)  # inside <a>...</a>, don't wrap
        return f'<a href="https://doi.org/{match.group(1)}" target="_blank">{match.group(1)}</a>'
    text = re.sub(r'(10\.\d{4,}/[^\s<"]+)', _doi_auto_link, text)
    return text


def convert_review(md_path, topic, slug_dir):
    """Convert review.md to index.html with canonical template."""
    with open(md_path, 'r', encoding='utf-8') as f:
        md = f.read()

    # Strip YAML frontmatter (중첩 포함, DOI 등 값 내부 --- 구분)
    while md.startswith("---"):
        lines = md.split("\n")
        end_line = None
        for i, line in enumerate(lines[1:], 1):
            if line.strip() == "---":
                end_line = i
                break
        if end_line is not None:
            md = "\n".join(lines[end_line + 1:]).lstrip("\n")
        else:
            break

    # Strip Related Papers section (auto-generated for Obsidian)
    md = re.sub(r'\n## Related Papers\n[\s\S]*?(?=\n## |\Z)', '', md)

    theme = THEMES.get(topic, THEMES["ai4s"])

    # Extract title
    title_m = re.search(r'^#\s+(.+)', md, re.MULTILINE)
    title = title_m.group(1).strip() if title_m else slug_dir

    # Extract metadata blockquote
    meta_m = re.search(r'^>\s*\*\*저자\*\*.*$', md, re.MULTILINE)
    meta_line = meta_m.group(0)[2:].strip() if meta_m else ""
    # Second line of blockquote (리뷰 모드)
    mode_m = re.search(r'^>\s*\*\*리뷰 모드\*\*:\s*(.+)', md, re.MULTILINE)
    mode = mode_m.group(1).strip() if mode_m else ""

    # Extract scores
    scores = parse_scores(md)

    # Split into sections by ## headers
    sections = re.split(r'^##\s+', md, flags=re.MULTILINE)
    # First section is everything before first ##
    parsed_sections = []
    for sec in sections[1:]:  # skip preamble
        lines = sec.split('\n', 1)
        sec_title = lines[0].strip()
        sec_body = lines[1] if len(lines) > 1 else ""
        parsed_sections.append((sec_title, sec_body))

    # Build HTML body
    body_parts = []

    # Title
    body_parts.append(f'<h1>{esc(title)}</h1>')
    # Audio Overview button (localhost-only; disabled when no key on deploy)
    body_parts.append(audio_bar_html())

    # Metadata
    if meta_line:
        meta_html = _inline(meta_line)
        # Zotero "Open PDF" button — same inline style as the Deep Research
        # reference list buttons in build_topic_index.py, so the affordance
        # looks identical wherever it appears. Only rendered when we have a
        # PDF attachment key for this slug (otherwise harmless skip).
        # slug_dir is a full path (docs/papers/<slug>) — strip to bare slug for lookup
        zkey = _ZOTERO_KEYS.get(os.path.basename(slug_dir), "")
        pdf_btn = ""
        if zkey:
            pdf_btn = (
                f' <a href="zotero://open-pdf/library/items/{esc(zkey)}" '
                f'title="Open PDF in Zotero" '
                f'style="margin-left:0.5rem; font-size:0.75rem; color:#555; '
                f'text-decoration:none; padding:0.05rem 0.4rem; '
                f'border-radius:3px; background:#f0f0f0; '
                f'border:1px solid #ddd;">'
                f'&#x1F4C4; PDF</a>'
            )
        body_parts.append(f'<blockquote><p>{meta_html}{pdf_btn}</p></blockquote>')

    body_parts.append('<hr>')

    # Sections (eval badges moved INTO Evaluation section)
    for sec_title, sec_body in parsed_sections:
        sec_html = md_section_to_html(sec_body, slug_dir)

        if sec_title.startswith('Essence') or '한줄 요약' in sec_title:
            if not sec_html.strip():
                continue
            body_parts.append(f'<div class="essence-box"><h2>Essence</h2>\n{sec_html}</div>')
        elif sec_title.startswith('평가') or sec_title.lower().startswith('eval'):
            # Evaluation section — render as badges (not table)
            badges = []
            for label, key in [("Novelty", "novelty"), ("Technical Soundness", "tech"),
                               ("Significance", "sig"), ("Clarity", "clarity"), ("Overall", "overall")]:
                if key in scores:
                    badges.append(f'<span class="eval-badge">{label}: {scores[key]}/5</span>')
            badges_html = f'<div class="eval-badges">{" ".join(badges)}</div>' if badges else ""
            # Extract 총평 from section body
            verdict_html = ""
            vm = re.search(r'\*\*총평\*\*:\s*([\s\S]+?)(?:\Z)', sec_body)
            if vm:
                verdict_html = f'<p><strong>총평</strong>: {_inline(vm.group(1).strip())}</p>'
            body_parts.append(f'<div class="section-box"><h2>Evaluation</h2>\n{badges_html}\n{verdict_html}</div>')
        else:
            body_parts.append(f'<div class="section-box"><h2>{esc(sec_title)}</h2>\n{sec_html}</div>')

    # Related papers (connections)
    connections = _load_connections()
    slug_dir_name = os.path.basename(slug_dir)
    outgoing = connections.get(slug_dir_name, [])
    # Incoming: 이 논문을 참조하는 다른 논문들
    incoming = []
    for src_slug, src_conns in connections.items():
        if src_slug == slug_dir_name:
            continue
        for c in src_conns:
            if c.get("slug") == slug_dir_name:
                incoming.append({
                    "slug": src_slug,
                    "relation": c.get("relation", "alternative"),
                    "reason": c.get("reason", ""),
                })
    conns = outgoing + incoming
    if conns:
        # Load paper titles and dates for link text and sorting
        index_path = os.path.join(PAPERS, "_papers_index.json")
        slug_titles = {}
        slug_dates = {}
        if os.path.exists(index_path):
            with open(index_path, "r", encoding="utf-8") as f:
                for p in json.load(f):
                    slug_titles[p["slug"]] = p.get("title", p["slug"])
                    slug_dates[p["slug"]] = p.get("date", "")

        type_labels = {
            "alternative": "다른 접근",
            "extension": "후속 연구",
            "foundation": "기반 연구",
            "counterpoint": "반론/비판",
            "application": "응용 사례",
        }

        # Dedup within the same relation: a paper appearing twice as e.g.
        # "alternative" for the same source is redundant. The same paper
        # is still allowed to show up under *different* relation types
        # (e.g. both "alternative" and "application") because those carry
        # distinct meanings. We keep the first occurrence so upstream
        # ordering (if any) is preserved; the explicit sort below then
        # places every surviving entry in the canonical order.
        _seen_pairs = set()
        _deduped = []
        for c in conns:
            key = (c.get("relation", ""), c.get("slug", ""))
            if key in _seen_pairs:
                continue
            _seen_pairs.add(key)
            _deduped.append(c)
        conns = _deduped

        # 정렬: 1차 관계 유형, 2차 시간순
        rel_order = {"foundation": 0, "alternative": 1, "extension": 2,
                      "application": 3, "counterpoint": 4}
        conns.sort(key=lambda c: (
            rel_order.get(c.get("relation", ""), 9),
            slug_dates.get(c.get("slug", ""), ""),
        ))

        conn_items = []
        for c in conns:
            cslug = c.get("slug", "")
            rel = c.get("relation", "alternative")
            reason = c.get("reason", "")
            ctitle = slug_titles.get(cslug, cslug)
            label = type_labels.get(rel, rel)
            conn_items.append(
                f'<div class="conn-item {esc(rel)}">'
                f'<div class="conn-type">{esc(label)}</div>'
                f'<div class="conn-title"><a href="../{esc(cslug)}/index.html">{esc(ctitle)}</a></div>'
                f'<div class="conn-reason">{esc(reason)}</div>'
                f'</div>'
            )
        body_parts.append(
            '<div class="connections-box">'
            '<h2>같이 보면 좋은 논문</h2>'
            + "\n".join(conn_items)
            + '</div>'
        )

    # Back link
    body_parts.append(f'<div class="back"><a href="{theme["back_href"]}">&larr; 목록으로 돌아가기</a></div>')

    # Audio Overview context: title + cleaned review + related papers, embedded
    # for the browser-side script prompt. slug_titles/type_labels exist only
    # when conns was non-empty (defined inside the block above).
    audio_connections = []
    if conns:
        for c in conns:
            audio_connections.append({
                "title": slug_titles.get(c.get("slug", ""), c.get("slug", "")),
                "relation": type_labels.get(c.get("relation", ""), c.get("relation", "")),
                "reason": c.get("reason", ""),
            })
    audio_ctx = {"title": title, "review": md, "connections": audio_connections}

    # Assemble
    css = get_css(theme) + "\n" + get_audio_css(theme)
    html = f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>{esc(title)}</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/font-kopub/1.0/kopubdotum.css">
<script>window.MathJax={{tex:{{inlineMath:[['$','$'],['\\\\(','\\\\)']],displayMath:[['$$','$$'],['\\\\[','\\\\]']]}}}};</script>
<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js" async></script>
<style>
{css}
</style>
</head>
<body>
{chr(10).join(body_parts)}
{audio_modal_html()}
<div id="lightbox" class="lightbox"><img id="lightbox-img" alt=""></div>
<script>
document.addEventListener('DOMContentLoaded', function() {{
  const lb = document.getElementById('lightbox');
  const lbImg = document.getElementById('lightbox-img');
  document.addEventListener('click', function(e) {{
    const img = e.target.closest('.review-fig img');
    if (img) {{ lbImg.src = img.src; lb.classList.add('active'); }}
  }});
  lb.addEventListener('click', function() {{ lb.classList.remove('active'); lbImg.src = ''; }});
  document.addEventListener('keydown', function(e) {{
    if (e.key === 'Escape' && lb.classList.contains('active')) {{ lb.classList.remove('active'); lbImg.src = ''; }}
  }});
}});
</script>
{audio_script_block(audio_ctx)}
<footer style="text-align:center;padding:2rem 0 1rem;color:#999;font-size:0.85rem;border-top:1px solid #eee;margin-top:3rem;">
Developed by Jehyun Lee, KIST AIX Strategy Department | jehyun.lee@gmail.com
</footer>
</body>
</html>"""
    return html


def detect_topic(slug, index_path=None):
    """Detect topic from _papers_index.json."""
    if index_path and os.path.exists(index_path):
        with open(index_path, 'r', encoding='utf-8') as f:
            idx = json.load(f)
        for p in idx:
            if p['slug'] == slug:
                topics = p.get('topics', [])
                if topics:
                    return topics[0]
                return p.get('primary_topic', 'ai4s')
    return "ai4s"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--topic', default=None, help='Force topic (ai4s/scisci)')
    parser.add_argument('--slugs', default=None, help='Slug range: 251-258')
    parser.add_argument('--all', action='store_true', help='Regenerate all')
    args = parser.parse_args()

    index_path = os.path.join(PAPERS, "_papers_index.json")

    # Determine which slugs to process
    all_slugs = sorted(d for d in os.listdir(PAPERS)
                       if os.path.isdir(os.path.join(PAPERS, d)) and re.match(r'^\d{3,}_', d))

    if args.slugs:
        start, end = args.slugs.split('-')
        def _slug_num(d):
            m = re.match(r'^(\d+)_', d)
            return int(m.group(1)) if m else 0
        slugs = [d for d in all_slugs if _slug_num(d) >= int(start) and _slug_num(d) <= int(end)]
    elif args.all:
        slugs = all_slugs
    else:
        slugs = all_slugs

    converted = 0
    skipped = 0
    for slug in slugs:
        md_path = os.path.join(PAPERS, slug, "review.md")
        html_path = os.path.join(PAPERS, slug, "index.html")
        if not os.path.exists(md_path):
            skipped += 1
            continue

        topic = args.topic or detect_topic(slug, index_path)
        slug_dir = os.path.join(PAPERS, slug)
        html = convert_review(md_path, topic, slug_dir)
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(html)
        converted += 1

    print(f"Converted: {converted}, Skipped: {skipped}")


if __name__ == "__main__":
    main()
