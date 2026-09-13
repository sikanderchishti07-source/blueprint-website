"""
Option 4 logo lockup.

Replaces the single blueprint-logo.png image in the navbar and the mobile
drawer with: the B mark, your BluePrint wordmark, and the tagline set as
live text so it stays readable at navbar size.

Run once from the repo root:

    python patch_logo.py

Unzip blueprint-logo-parts.zip into site/assets/logo/ first.
Writes a .bak beside each file. Changes nothing unless every anchor matches.
"""

import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
PARTIALS = os.path.join(ROOT, "build", "partials.py")
CSS = os.path.join(ROOT, "site", "css", "pages.css")
LOGODIR = os.path.join(ROOT, "site", "assets", "logo")

for p in (PARTIALS, CSS):
    if not os.path.exists(p):
        sys.exit("Not found: " + p + "\nRun this from the repo root.")

missing = [f for f in ("blueprint-mark.png", "blueprint-wordmark.png")
           if not os.path.exists(os.path.join(LOGODIR, f))]
if missing:
    sys.exit("Missing in site/assets/logo/: " + ", ".join(missing)
             + "\nUnzip blueprint-logo-parts.zip there first.")


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


# ── the lockup markup (no braces, so it is safe inside an f-string) ──
LOCK = (
    '<span class="bp-lock">'
    '<img class="bp-mark" src="assets/logo/blueprint-mark.png" alt="" />'
    '<span class="bp-txt">'
    '<img class="bp-word" src="assets/logo/blueprint-wordmark.png" alt="BluePrint" />'
    '<span class="bp-tag">Environmental Services</span>'
    '</span></span>'
)

OLD_NAV = ('<img src="assets/logo/blueprint-logo.png" '
           'alt="BluePrint Environmental Services" />')

text, bom, crlf = read(PARTIALS)

if "bp-lock" in text:
    sys.exit("partials.py already patched. Restore build/partials.py.bak to redo it.")

hits = text.count(OLD_NAV)
if hits != 2:
    sys.exit("Expected 2 logo images in partials.py, found %d. Nothing changed." % hits)

text = text.replace(OLD_NAV, LOCK)
backup(PARTIALS)
write(PARTIALS, text, bom, crlf)
print("patched build/partials.py  (%d logo images replaced)" % hits)


# ── styles ──────────────────────────────────────────────────────
MARK = "/* Logo lockup - mark, wordmark, live tagline */"
BLOCK = """

""" + MARK + """
.bp-lock { display: flex; align-items: center; gap: 13px; }
.bp-mark { height: 48px; width: auto; display: block; flex: 0 0 auto; }
.bp-txt  { display: block; line-height: 1; }
.bp-word { height: 21px; width: auto; display: block; }
.bp-tag  {
  display: block;
  font-family: var(--font-body, inherit);
  font-size: 9.5px;
  font-weight: 600;
  letter-spacing: .17em;
  text-transform: uppercase;
  color: #7c8a90;
  margin-top: 6px;
  white-space: nowrap;
}
/* the old single-image rule must not size the new pieces */
.nav-logo-wrap img { height: auto; }
.nav-logo-wrap:hover .bp-lock { transform: scale(1.02); }
.bp-lock { transition: transform .25s ease; }

/* mobile drawer header sits in a tighter space */
.drawer-header .bp-mark { height: 36px; }
.drawer-header .bp-word { height: 16px; }
.drawer-header .bp-tag  { font-size: 8px; letter-spacing: .15em; margin-top: 5px; }

@media (max-width: 640px) {
  .bp-lock { gap: 10px; }
  .bp-mark { height: 38px; }
  .bp-word { height: 17px; }
  .bp-tag  { font-size: 8px; letter-spacing: .14em; margin-top: 5px; }
}
"""

css, cbom, ccrlf = read(CSS)
if MARK in css:
    print("pages.css: styles already present, skipped")
else:
    backup(CSS)
    write(CSS, css + BLOCK, cbom, ccrlf)
    print("patched site/css/pages.css")

print("\nNow rebuild:")
print("  cd build")
print("  python build.py")
print("  npx tailwindcss -c tailwind.config.js -i tailwind.input.css -o ../site/css/tailwind.css --minify")
