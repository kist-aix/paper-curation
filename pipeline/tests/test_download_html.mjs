// Behaviour test for the ".html 다운로드" button injected by review_to_html.py.
//
// Why this exists — two defects shipped in the previous version:
//
//   1. On a file:// page the button promised "이미지 임베딩 중…" and delivered
//      nothing. Measured in Chromium against the real page:
//        fetch('figures/fig1.png') → TypeError: Failed to fetch
//        canvas.drawImage → toDataURL → SecurityError: Tainted canvases …
//      Both paths fail on exactly the origin the canvas fallback claimed to
//      cover, so every image kept its 'figures/…' RELATIVE src while the copy
//      landed in ~/Downloads — where no figures/ exists. Silently broken.
//   2. The copy was a verbatim clone of the document, so it carried the
//      build-time local key (window._GEMINI_KEY = "AIza…") into a file whose
//      whole purpose is to be shared.
//
// The point of the button is that the file can be SENT and still show its
// figures, so the fix is a build-time payload (_figs_inline.js) pulled in with
// the one channel file:// does not block — a dynamic <script src> (also
// measured). These tests lock that the payload is used, that http(s) still
// prefers the lossless original bytes, and that keys never ride along.
//
// The REAL _DL_JS is extracted from review_to_html.py (no copy — a copy is what
// drifts) and executed against a minimal DOM.
//
// Run:  node pipeline/tests/test_download_html.mjs
// Read-only / scratch-only; never writes into docs/ or the repo.

import { execFileSync } from "node:child_process";
import { fileURLToPath } from "node:url";
import { dirname, resolve, join } from "node:path";
import { existsSync, mkdtempSync, writeFileSync, readFileSync } from "node:fs";
import { tmpdir } from "node:os";

const __dirname = dirname(fileURLToPath(import.meta.url));
const REPO = resolve(__dirname, "..", "..");
const TARGET = join(REPO, "pipeline", "review_to_html.py");

let failures = 0;
function assert(cond, msg) {
  if (cond) { console.log("  ok  - " + msg); }
  else { console.error("  FAIL- " + msg); failures++; }
}

// ── extract the real template (ast, no import: review_to_html reads config.json) ──
const scratch = mkdtempSync(join(tmpdir(), "dlhtml-"));
const outJs = join(scratch, "download_page.js");
const extractor = join(scratch, "extract.py");
writeFileSync(extractor, [
  "import ast, sys",
  "tree = ast.parse(open(sys.argv[1], encoding='utf-8').read())",
  "vals = {}",
  "def ev(n):",
  "    if isinstance(n, ast.Constant): return n.value",
  "    if isinstance(n, ast.Name): return vals[n.id]",
  "    if isinstance(n, ast.BinOp) and isinstance(n.op, ast.Add):",
  "        return ev(n.left) + ev(n.right)",
  "    if isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute) \\",
  "            and n.func.attr == 'replace':",
  "        return ev(n.func.value).replace(*[ev(a) for a in n.args])",
  "    raise SystemExit('unsupported expression in _DL_JS assignment')",
  "for node in tree.body:",
  "    if isinstance(node, ast.Assign) and len(node.targets) == 1 \\",
  "            and isinstance(node.targets[0], ast.Name) \\",
  "            and node.targets[0].id in ('PAYLOAD_NAME', '_DL_SCRUB_JS', '_DL_JS'):",
  "        vals[node.targets[0].id] = ev(node.value)",
  "js = vals['_DL_JS']",
  "assert 'downloadPageHtml' in js and '_dlScrubKeys' in js",
  "assert vals['PAYLOAD_NAME'] in js, 'payload filename was not substituted into the JS'",
  "assert 'PAYLOAD_SRC' not in js, 'PAYLOAD_SRC placeholder left unsubstituted'",
  "open(sys.argv[2], 'w', encoding='utf-8').write(js)",
  "print('extracted', len(js), 'chars')",
].join("\n"), "utf-8");

const pyCandidate = process.env.PAPER_CURATION_PY312
  || "/opt/homebrew/Caskroom/miniconda/base/envs/py312/bin/python";
const py = existsSync(pyCandidate) ? pyCandidate : "python3";

console.log("[1] emission: extract real _DL_JS + node --check");
let DL_JS = "";
try {
  console.log("  " + execFileSync(py, [extractor, TARGET, outJs], { encoding: "utf-8" }).trim());
  execFileSync(process.execPath, ["--check", outJs], { encoding: "utf-8" });
  DL_JS = readFileSync(outJs, "utf-8");
  assert(true, "node --check passed on the emitted download template");
} catch (e) {
  assert(false, "extraction/parse: " + (e && e.message ? e.message.split("\n")[0] : e));
}
if (!DL_JS) { console.error("\nFAILED: could not extract template"); process.exit(1); }

// ── minimal DOM ──────────────────────────────────────────────────────────────
class El {
  constructor(tag, attrs = {}, textContent = "") {
    this.tag = tag; this.attrs = { ...attrs }; this.textContent = textContent;
    this.children = []; this.complete = true; this.naturalWidth = 640; this.disabled = false;
  }
  getAttribute(k) { return k in this.attrs ? this.attrs[k] : null; }
  setAttribute(k, v) { this.attrs[k] = String(v); }
  cloneNode() {
    const c = new El(this.tag, this.attrs, this.textContent);
    c.children = this.children.map((x) => x.cloneNode(true));
    return c;
  }
  *walk() { for (const c of this.children) { yield c; yield* c.walk(); } }
  querySelectorAll(sel) {
    const out = [];
    for (const n of this.walk()) {
      if (sel === "img" && n.tag === "img") out.push(n);
      else if (sel === "script" && n.tag === "script") out.push(n);
      else if (sel === "a[data-portable]" && n.tag === "a" && n.attrs["data-portable"]) out.push(n);
    }
    return out;
  }
  get outerHTML() {
    const a = Object.keys(this.attrs).map((k) => ` ${k}="${this.attrs[k]}"`).join("");
    if (this.tag === "img") return `<${this.tag}${a}>`;
    const kids = this.children.map((c) => c.outerHTML).join("");
    return `<${this.tag}${a}>${this.textContent}${kids}</${this.tag}>`;
  }
}

// Shaped like the baked Gemini key but deliberately NOT a plausible credential:
// this repo is public and a realistic AIzaSy… literal only invites scanner noise.
const LIVE_KEY = "AIza_FAKE_TEST_KEY_NOT_A_CREDENTIAL";

function buildPage() {
  const html = new El("html");
  const body = new El("body");
  html.children.push(body);
  const btn = new El("button", { class: "dl-btn" }, ".html 다운로드");
  const note = new El("span", { class: "dl-note", id: "dl-note" });
  const bar = new El("div", { class: "dl-bar" });
  bar.children.push(btn, note);
  body.children.push(bar);
  body.children.push(new El("img", { src: "figures/fig1.png", alt: "Figure 1" }));
  body.children.push(new El("img", { src: "figures/fig2.webp", alt: "Figure 2" }));
  body.children.push(new El("img", { src: "data:image/png;base64,AAAA", alt: "inline" }));
  body.children.push(new El("a", {
    href: "../088_Neighbour/index.html", "data-portable": "https://doi.org/10.1234/x",
  }, "이웃 논문"));
  body.children.push(new El("script", {},
    'window._GEMINI_KEY = "' + LIVE_KEY + '";\n'
    + 'window._LOCAL_EMAILS = ["me@example.com"];\n'
    + 'window._AUDIO_MODE = "paper";'));
  // key read back into a variable — code, not a literal: must survive untouched
  body.children.push(new El("script", {},
    'let GKEY = (window._GEMINI_KEY || "");\nwindow._GEMINI_KEY = GKEY;'));
  return { html, btn, note };
}

// figures/fig1.png + figures/fig2.webp, as review_to_html.write_figure_payload writes them
const PAYLOAD = {
  "figures/fig1.png": "data:image/webp;base64,UklGRkFBS0Ux",
  "figures/fig2.webp": "data:image/webp;base64,UklGRkZJRzI=",
};

async function run(protocol, href, fetchImpl, payload) {
  const page = buildPage();
  const win = { _PAGE_SLUG: "10911_Test_Slug" };
  const stats = { fetch: 0, canvas: 0, revoked: 0, timers: [], clicks: 0, payloadLoads: 0 };
  const anchor = { href: "", download: "", click() { stats.clicks++; } };
  const head = {
    appendChild(s) {
      // simulate the browser fetching+running the payload script
      s.parentNode = head;
      stats.payloadLoads++;
      queueMicrotask(() => {
        if (payload) { win._FIG_INLINE = payload; s.onload(); }
        else { s.onerror(); }
      });
    },
    removeChild(s) { s.parentNode = null; stats.removed = (stats.removed || 0) + 1; },
  };
  const document = {
    documentElement: page.html,
    head,
    querySelector: (s) => (s === ".dl-btn" ? page.btn : null),
    getElementById: (id) => (id === "dl-note" ? page.note : null),
    querySelectorAll: (s) => page.html.querySelectorAll(s),
    createElement: (t) => {
      if (t === "a") return anchor;
      if (t === "script") return { tag: "script", src: "", parentNode: null };
      if (t === "canvas") {
        stats.canvas++;
        return {
          getContext: () => ({ drawImage() {} }),
          toDataURL() {
            const err = new Error("Tainted canvases may not be exported.");
            err.name = "SecurityError";
            throw err;   // exactly what Chromium does for a file:// image
          },
        };
      }
      return new El(t);
    },
  };
  let captured = null;
  class FakeURL extends URL {}
  FakeURL.createObjectURL = (b) => { captured = b; return "blob:fake"; };
  FakeURL.revokeObjectURL = () => { stats.revoked++; };
  class FakeFileReader {
    readAsDataURL(blob) {
      blob.arrayBuffer()
        .then((buf) => {
          this.result = "data:" + (blob.type || "application/octet-stream")
            + ";base64," + Buffer.from(buf).toString("base64");
          this.onload();
        })
        .catch((e) => this.onerror(e));
    }
  }
  const fakeSetTimeout = (fn, ms) => { stats.timers.push(ms); return 1; };
  const factory = new Function(
    "document", "location", "window", "Blob", "URL", "FileReader", "fetch", "setTimeout",
    DL_JS + "\nreturn downloadPageHtml;",
  );
  const download = factory(
    document, { protocol, href }, win,
    Blob, FakeURL, FakeFileReader,
    (src, opts) => { stats.fetch++; return fetchImpl(src, opts); },
    fakeSetTimeout,
  );
  await download();
  return { page, stats, anchor, html: captured ? await captured.text() : "" };
}

const okFetch = async (src) => ({
  ok: true, status: 200,
  blob: async () => new Blob([Buffer.from("REALBYTES:" + src)], { type: "image/png" }),
});
const missFetch = async (src) => (src.indexOf("fig1") !== -1
  ? { ok: false, status: 404, blob: async () => new Blob([]) }
  : okFetch(src));

console.log("[2] file:// — the payload makes the copy genuinely sendable");
{
  const r = await run("file:", "file:///Users/me/docs/papers/10911_Test/index.html", okFetch, PAYLOAD);
  assert(r.stats.fetch === 0, "fetch is never attempted on file:// (it always throws there)");
  assert(r.stats.canvas === 0, "canvas is never attempted on file:// (it is always tainted there)");
  assert(r.stats.payloadLoads === 1,
    "the payload is loaded exactly once for the whole page (got " + r.stats.payloadLoads + ")");
  assert(r.html.indexOf('src="' + PAYLOAD["figures/fig1.png"] + '"') !== -1
    && r.html.indexOf('src="' + PAYLOAD["figures/fig2.webp"] + '"') !== -1,
    "every figure carries its embedded bytes — the file shows images anywhere");
  assert(r.html.indexOf('src="figures/') === -1 && r.html.indexOf("file:///Users/me") === -1,
    "no local path survives in the copy (relative or absolute)");
  assert(r.html.indexOf('src="data:image/png;base64,AAAA"') !== -1,
    "an already-inline data: image is left alone");
  assert(r.html.indexOf("_figs_inline.js") === -1,
    "the injected payload <script> is removed and never lands in the copy");
  assert(/2장 포함/.test(r.page.note.textContent) && /그대로 보내도 그림이 보입니다/.test(r.page.note.textContent),
    "the note confirms the copy is sendable (got: " + r.page.note.textContent + ")");
  assert(r.page.btn.textContent === ".html 다운로드" && r.page.btn.disabled === false,
    "button label + enabled state are restored");
  assert(r.stats.clicks === 1 && r.anchor.download === "10911_Test_Slug.html",
    "the download happens, named after the slug");
  assert(r.stats.revoked === 0 && r.stats.timers.length === 1 && r.stats.timers[0] >= 1000,
    "the object URL is revoked on a timer, not synchronously (Safari drops the save otherwise)");
}

console.log("[2b] file:// with a missing/stale payload — degrades loudly, not silently");
{
  const r = await run("file:", "file:///Users/me/docs/papers/10911_Test/index.html", okFetch, null);
  assert(r.html.indexOf('src="file:///Users/me/docs/papers/10911_Test/figures/fig1.png"') !== -1,
    "images fall back to absolute file: URLs so the copy still renders on this machine");
  assert(r.html.indexOf('src="figures/') === -1,
    "no relative src survives (the copy lands in ~/Downloads, not next to figures/)");
  assert(/하나도 넣지 못/.test(r.page.note.textContent)
    && /_figs_inline\.js/.test(r.page.note.textContent)
    && /review_to_html\.py --slugs 10911/.test(r.page.note.textContent),
    "the note names the missing payload and the exact command that rebuilds it (got: "
    + r.page.note.textContent + ")");
  assert(r.stats.clicks === 1, "the download still happens");
}

console.log("[3] secrets never ride along in the copy");
{
  const r = await run("file:", "file:///Users/me/p/index.html", okFetch, PAYLOAD);
  assert(r.html.indexOf(LIVE_KEY) === -1, "the baked Google API key is gone from the copy");
  assert(r.html.indexOf('_GEMINI_KEY = ""') !== -1, "the key slot is emptied, not deleted");
  assert(r.html.indexOf("_LOCAL_EMAILS = []") !== -1, "local recipient emails are emptied");
  assert(r.html.indexOf("window._GEMINI_KEY = GKEY;") !== -1,
    "an identifier assignment is code, not a literal — it must survive intact");
  const livePage = r.page.html.outerHTML;
  assert(livePage.indexOf(LIVE_KEY) !== -1,
    "the live page still has its key (only the copy is scrubbed)");
}

console.log("[4] http(s) — the original bytes win over the payload");
{
  const r = await run("http:", "http://localhost:8000/papers/10911_Test/index.html", okFetch, PAYLOAD);
  assert(r.stats.fetch === 2, "each non-inline image is fetched once (got " + r.stats.fetch + ")");
  assert(r.stats.canvas === 0, "canvas is not needed when fetch succeeds");
  assert(r.stats.payloadLoads === 0,
    "the payload is not downloaded when fetch already returns the lossless original");
  const inlined = (r.html.match(/src="data:image\/png;base64,/g) || []).length;
  assert(inlined === 3, "both figures are inlined as data URIs (+1 pre-existing, got " + inlined + ")");
  assert(r.html.indexOf('src="figures/') === -1, "no figure keeps a relative path");
  assert(r.html.indexOf(LIVE_KEY) === -1, "the key is scrubbed on this path too");
  assert(r.page.note.textContent.indexOf("자기완결") !== -1,
    "the note confirms a self-contained file (got: " + r.page.note.textContent + ")");
}

console.log("[5] http(s) — a figure fetch that fails is rescued by the payload");
{
  const r = await run("http:", "http://localhost:8000/p/index.html", missFetch, PAYLOAD);
  assert(r.stats.canvas === 1, "a 404 falls through to the canvas attempt");
  assert(r.stats.payloadLoads === 1, "then to the payload");
  assert(r.html.indexOf('src="' + PAYLOAD["figures/fig1.png"] + '"') !== -1,
    "the unfetchable figure is embedded from the payload instead");
  assert(r.html.indexOf('src="figures/') === -1, "nothing is left pointing at a relative path");
  assert(/2장 포함/.test(r.page.note.textContent),
    "the note reports a complete file (got: " + r.page.note.textContent + ")");
}

console.log("[5b] partial failure is reported, not swallowed");
{
  const r = await run("http:", "http://localhost:8000/p/index.html", missFetch, {
    "figures/fig2.webp": PAYLOAD["figures/fig2.webp"],   // fig1 missing from payload too
  });
  assert(r.html.indexOf('src="figures/fig1.png"') !== -1,
    "an image that could not be read anywhere keeps its original src");
  assert(/1\/2/.test(r.page.note.textContent)
    && /review_to_html\.py --slugs 10911/.test(r.page.note.textContent),
    "the note reports the count and how to fix it (got: " + r.page.note.textContent + ")");
  assert(r.stats.clicks === 1, "a partial result is still downloaded");
}

console.log("[6] portable links are rewritten in the copy only");
{
  const r = await run("file:", "file:///Users/me/p/index.html", okFetch, PAYLOAD);
  assert(r.html.indexOf('href="https://doi.org/10.1234/x"') !== -1,
    "a data-portable neighbour link becomes an absolute DOI URL in the copy");
  assert(r.page.html.outerHTML.indexOf('href="../088_Neighbour/index.html"') !== -1,
    "the live page keeps its relative link");
}

if (failures) { console.error("\nFAILED: " + failures + " assertion(s)"); process.exit(1); }
console.log("\nALL PASS");
