"""
Logo animation 7 - the wave unfurls.

Splits the B mark into two layers (blue B, olive wave) so the wave can
animate on its own, and plays the unfurl once when the home page loads.
Other pages show the logo still.

Run once from the repo root:

    python patch_logo_anim.py

Unzip logo-unfurl.zip into site/assets/logo/ first.
Writes a .bak beside each file. Changes nothing unless every anchor matches.
"""

import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
PARTIALS = os.path.join(ROOT, "build", "partials.py")
CSS = os.path.join(ROOT, "site", "css", "pages.css")
JS = os.path.join(ROOT, "site", "js", "main.js")
LOGODIR = os.path.join(ROOT, "site", "assets", "logo")

for p in (PARTIALS, CSS, JS):
    if not os.path.exists(p):
        sys.exit("Not found: " + p + "\nRun this from the repo root.")

missing = [f for f in ("blueprint-b.png", "blueprint-wave.png")
           if not os.path.exists(os.path.join(LOGODIR, f))]
if missing:
    sys.exit("Missing in site/assets/logo/: " + ", ".join(missing)
             + "\nUnzip logo-unfurl.zip there first.")


def read(path):
    raw = open(path, "rb").read()
    bom = raw.startswith(b"\xef\xbb\xbf")
    text = raw.decode("utf-8-sig")
    crlf = "\r\n" in text
    return text.replace("\r\n", "\n"), bom, crlf


def write(path, text, bom, crlf):
    if crlf:
        text = text.replace("\n", "\r\n")
    data = text.encode("utf-8")
    if bom:
        data = b"\xef\xbb\xbf" + data
    open(path, "wb").write(data)


def backup(path):
    if not os.path.exists(path + ".bak"):
        open(path + ".bak", "wb").write(open(path, "rb").read())


# ── 1. markup: one mark image becomes two stacked layers ────────
OLD = '<img class="bp-mark" src="assets/logo/blueprint-mark.png" alt="" />'
NEW = ('<span class="bp-mark">'
       '<img class="bp-b" src="assets/logo/blueprint-b.png" alt="" />'
       '<img class="bp-wave" src="assets/logo/blueprint-wave.png" alt="" />'
       '</span>')

text, bom, crlf = read(PARTIALS)

if "bp-wave" in text:
    sys.exit("partials.py already patched. Restore build/partials.py.bak to redo it.")
if "bp-lock" not in text:
    sys.exit("The logo lockup is not in partials.py. Run patch_logo.py first.")

hits = text.count(OLD)
if hits != 2:
    sys.exit("Expected 2 mark images in partials.py, found %d. Nothing changed." % hits)

text = text.replace(OLD, NEW)
backup(PARTIALS)
write(PARTIALS, text, bom, crlf)
print("patched build/partials.py  (%d marks split into layers)" % hits)


# ── 2. styles ───────────────────────────────────────────────────
MARK = "/* Logo - wave unfurl */"
BLOCK = """

""" + MARK + """
/* the two layers share one box so they stack exactly */
#navbar .bp-mark,
.drawer-header .bp-mark {
  position: relative;
  display: block;
  flex: 0 0 auto;
  width: 35px;
  height: 42px;
}
#navbar .bp-mark img,
.drawer-header .bp-mark img {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: contain;
  display: block;
}
.drawer-header .bp-mark { width: 28px; height: 34px; }

/* the unfurl, home page only, once per load */
.bp-home #navbar .bp-wave {
  transform-origin: 18% 88%;
  animation: bpUnfurl 1.5s cubic-bezier(.34, 1.02, .36, 1) .2s both;
}
@keyframes bpUnfurl {
  0%   { transform: scale(.18) rotate(-26deg); opacity: 0; }
  55%  { opacity: 1; }
  100% { transform: none; opacity: 1; }
}
.bp-home #navbar .bp-b {
  animation: bpMarkIn .55s ease both;
}
@keyframes bpMarkIn {
  from { opacity: 0; transform: scale(.94); }
  to   { opacity: 1; transform: none; }
}
.bp-home #navbar .bp-txt {
  animation: bpTextIn .7s cubic-bezier(.2, .7, .3, 1) .95s both;
}
@keyframes bpTextIn {
  from { opacity: 0; transform: translateX(-10px); }
  to   { opacity: 1; transform: none; }
}

/* visitors who asked their device to stop animations get a still logo */
@media (prefers-reduced-motion: reduce) {
  .bp-home #navbar .bp-wave,
  .bp-home #navbar .bp-b,
  .bp-home #navbar .bp-txt { animation: none; }
}
"""

css, cbom, ccrlf = read(CSS)
if MARK in css:
    print("pages.css: styles already present, skipped")
else:
    backup(CSS)
    write(CSS, css + BLOCK, cbom, ccrlf)
    print("patched site/css/pages.css")


# ── 3. flag the home page so the animation is scoped to it ──────
JSMARK = "/* Logo unfurl runs on the home page only */"
JSBLOCK = """

""" + JSMARK + """
(function () {
  var p = (location.pathname.split('/').pop() || 'index.html').toLowerCase();
  if (p === '' || p === 'index.html') {
    document.documentElement.classList.add('bp-home');
  }
})();
"""

js, jbom, jcrlf = read(JS)
if JSMARK in js:
    print("main.js: home flag already present, skipped")
else:
    backup(JS)
    write(JS, js.rstrip() + "\n" + JSBLOCK, jbom, jcrlf)
    print("patched site/js/main.js")

print("\nNow rebuild:")
print("  cd build")
print("  python build.py")
print("  npx tailwindcss -c tailwind.config.js -i tailwind.input.css -o ../site/css/tailwind.css --minify")
