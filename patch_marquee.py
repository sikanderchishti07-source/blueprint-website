"""
Two-strip client logo marquee.

Run once from the repo root:

    python patch_marquee.py

Edits build/home_new.py, site/css/pages.css and site/js/main.js.
Writes a .bak beside each file first. Safe to abort: it changes
nothing unless every anchor is found.
"""

import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
HOME = os.path.join(ROOT, "build", "home_new.py")
CSS = os.path.join(ROOT, "site", "css", "pages.css")
JS = os.path.join(ROOT, "site", "js", "main.js")


def read(path):
    """Return (text, bom, crlf) with newlines normalised to \\n."""
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


for p in (HOME, CSS, JS):
    if not os.path.exists(p):
        sys.exit("Not found: " + p + "\nRun this from the repo root.")


# ── 1. home_new.py ──────────────────────────────────────────────
home, home_bom, home_crlf = read(HOME)

OLD_MARKUP = (
    '  <div class="logo-marquee scroll-reveal" aria-label="Client logos">\n'
    '    <div class="logo-track">\n'
    'CLIENT_LOGOS    </div>\n'
    '  </div>'
)
NEW_MARKUP = (
    '  <div class="logo-marquee scroll-reveal" aria-label="Client logos">\n'
    'CLIENT_LOGOS  </div>'
)

OLD_BUILD = (
    '    clients = "".join(\n'
    '        f"""      <div class="logo-item">'
    '<img src="assets/brand/client-{slug}.png" alt="{name}" loading="lazy" /></div>\\n"""\n'
    '        for slug, name in CLIENTS) * 2'
)
NEW_BUILD = (
    '    def _logo_row(items, cls=""):\n'
    '        cells = "".join(\n'
    '            f"""      <div class="logo-item">'
    '<img src="assets/brand/client-{slug}.png" alt="{name}" loading="lazy" /></div>\\n"""\n'
    '            for slug, name in items)\n'
    '        return f\'    <div class="logo-track{cls}">\\n\' + cells * 2 + "    </div>\\n"\n'
    '\n'
    '    _half = (len(CLIENTS) + 1) // 2\n'
    '    clients = _logo_row(CLIENTS[:_half]) + _logo_row(CLIENTS[_half:], " rev")'
)

NEW_CLIENTS = '''CLIENTS = [
    ("aramco", "Saudi Aramco"),
    ("neom", "NEOM"),
    ("red-sea", "Red Sea Global"),
    ("pif", "Public Investment Fund"),
    ("zatca", "Zakat, Tax and Customs Authority"),
    ("sabic", "SABIC"),
    ("maaden", "Ma'aden"),
    ("mewa", "Ministry of Environment, Water and Agriculture"),
    ("saudi-electricity", "Saudi Electricity Company"),
    ("national-water", "National Water Company"),
    ("mawani", "MAWANI, Saudi Ports Authority"),
    ("ncm", "National Center for Meteorology"),
    ("saudi-water-authority", "Saudi Water Authority"),
    ("gami", "General Authority for Military Industries"),
    ("sami", "SAMI"),
    ("kaec", "King Abdullah Economic City"),
    ("diriyah", "Diriyah"),
    ("qiddiya", "Qiddiya"),
    ("yasref", "YASREF"),
    ("samref", "SAMREF"),
    ("luberef", "Luberef"),
    ("yansab", "Yansab"),
    ("nomac", "NOMAC"),
    ("veolia", "Veolia"),
    ("unilever", "Unilever"),
    ("abdul-latif-jameel", "Abdul Latif Jameel"),
    ("qassim-cement", "Qassim Cement"),
    ("arabian-cement", "Arabian Cement"),
    ("najran-cement", "Najran Cement"),
    ("hail-cement", "Hail Cement"),
    ("marafiq", "Marafiq"),
    ("petro-rabigh", "Petro Rabigh"),
    ("cruise-saudi", "Cruise Saudi"),
    ("jeddah-airports", "Jeddah Airports"),
    ("man-enterprise", "MAN Enterprise"),
    ("el-seif", "El Seif"),
    ("al-bawani", "Al Bawani"),
]'''

if "AramcoCLIENTS" in home or "logo-track{cls}" in home:
    sys.exit("home_new.py looks already patched or damaged.\n"
             "Restore build/home_new.py.bak first.")
if OLD_MARKUP not in home:
    sys.exit("home_new.py: logo marquee markup not found, nothing changed.")
if OLD_BUILD not in home:
    sys.exit("home_new.py: client logo builder not found, nothing changed.")

if "CLIENTS = [" not in home:
    sys.exit("home_new.py: CLIENTS list not found, nothing changed.")

home = home.replace(OLD_MARKUP, NEW_MARKUP)
home = home.replace(OLD_BUILD, NEW_BUILD)

# offsets must be found AFTER the replacements above, or the splice lands
# in the wrong place
start = home.find("CLIENTS = [")
end = home.find("\n]", start)
if start == -1 or end == -1:
    sys.exit("home_new.py: CLIENTS list not found, nothing changed.")
home = home[:start] + NEW_CLIENTS + home[end + 2:]

backup(HOME)
write(HOME, home, home_bom, home_crlf)
print("patched build/home_new.py")


# ── 2. pages.css ────────────────────────────────────────────────
css, css_bom, css_crlf = read(CSS)
MARK = "/* Trusted by - two strips, opposite directions */"
CSS_BLOCK = """

""" + MARK + """
/* Two tracks stacked. The second runs the other way. Each track holds
   half the logos, so the duration is halved to keep the same speed. */
.logo-marquee { padding: 18px 0; }
.logo-marquee .logo-track { animation-duration: 62s; }
.logo-marquee .logo-track + .logo-track { margin-top: 10px; }
.logo-marquee .logo-track.rev { animation-direction: reverse; }
.logo-marquee:hover .logo-track { animation-play-state: paused; }

/* Full colour, no hover magnifier */
.logo-item { transform: none !important; width: 190px; height: 86px; margin: 0 30px; }
.logo-item img { filter: none; opacity: 1; }

/* Fade the strip edges so logos enter and leave instead of cutting off */
.logo-marquee {
  -webkit-mask-image: linear-gradient(to right, transparent, #000 7%, #000 93%, transparent);
          mask-image: linear-gradient(to right, transparent, #000 7%, #000 93%, transparent);
}

@media (max-width: 640px) {
  .logo-item { width: 132px; height: 62px; margin: 0 16px; }
  .logo-marquee .logo-track { animation-duration: 46s; }
}
@media (prefers-reduced-motion: reduce) {
  .logo-marquee .logo-track { animation: none; }
}
"""

if MARK in css:
    print("pages.css: block already present, skipped")
else:
    backup(CSS)
    write(CSS, css + CSS_BLOCK, css_bom, css_crlf)
    print("patched site/css/pages.css")


# ── 3. main.js — drop the centre magnifier ──────────────────────
js, js_bom, js_crlf = read(JS)
JS_ANCHOR = "/* Client logo strip - logos grow as they cross the centre of the band */"

if JS_ANCHOR not in js:
    print("main.js: magnifier block not found, skipped")
else:
    backup(JS)
    js = js[:js.index(JS_ANCHOR)].rstrip() + "\n"
    write(JS, js, js_bom, js_crlf)
    print("patched site/js/main.js")

print("\nDone. Now rebuild:")
print("  cd build")
print("  python build.py")
print("  npx tailwindcss -c tailwind.config.js -i tailwind.input.css -o ../site/css/tailwind.css --minify")
