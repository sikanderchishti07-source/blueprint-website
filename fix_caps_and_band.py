"""
Two changes:

1. The four "What you get out of it" capability cards use leftover beach and
   coastline photos (sector-1/2/3.jpg) plus the old air detail shot. Swap them
   for four purpose-made images. Same four on every service page, matching the
   copy, which is also the same on every page.

2. The statement band scrim is a flat teal wash that swallows the photograph
   behind it. Replace it with a lighter, more neutral treatment and carry the
   text contrast with a shadow instead.

Run from the repo root:

    python fix_caps_and_band.py

Unzip cap-images.zip into site/assets/img/ first.
Writes .bakcaps beside every file it edits.
"""

import os
import re
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
IMGDIR = os.path.join(ROOT, "site", "assets", "img")

NEW = {
    "assets/img/sector-1.jpg": "assets/img/cap-scoped.webp",
    "assets/img/sector-2.jpg": "assets/img/cap-accredited.webp",
    "assets/img/sector-3.jpg": "assets/img/cap-schedule.webp",
}
FOURTH = "assets/img/cap-interpreted.webp"

for f in list(NEW.values()) + [FOURTH]:
    p = os.path.join(IMGDIR, os.path.basename(f))
    if not os.path.exists(p):
        sys.exit("Missing: site/assets/img/%s\nUnzip cap-images.zip there first."
                 % os.path.basename(f))

# ---- 1. capability card images -------------------------------------------
# home_new.py is skipped: the sector images belong to the home page sectors
# section and must stay as they are there.
PY = [f for f in os.listdir(os.path.join(ROOT, "build"))
      if f.endswith(".py") and f != "home_new.py"]

total = 0
for name in sorted(PY):
    src = os.path.join(ROOT, "build", name)
    raw = open(src, "rb").read().decode("utf-8")
    crlf = "\r\n" in raw
    text = raw.replace("\r\n", "\n")
    before = text

    for old, new in NEW.items():
        text = text.replace('"%s"' % old, '"%s"' % new)
        text = text.replace("'%s'" % old, "'%s'" % new)

    # the fourth card, in the per-file caps lists
    text = re.sub(r'"assets/img/svc-air-detail\.jpg"(\s*,\s*"(?:Clear|Single)")',
                  '"%s"\\1' % FOURTH, text)
    # the fourth card, in build.py's shared _CAP_IMGS list
    text = text.replace("'assets/img/cap-schedule.webp', 'assets/img/svc-air-detail.jpg'",
                        "'assets/img/cap-schedule.webp', '%s'" % FOURTH)
    # the "who this is for" pane images cycle the same beach photos
    text = text.replace(
        "url(\\'assets/img/sector-{(i%3)+1}.jpg\\')",
        "url(\\'{_PANE_IMGS[i%4]}\\')")

    if text != before:
        n = len(re.findall(r'cap-(?:scoped|accredited|schedule|interpreted)', text))
        open(src + ".bakcaps", "wb").write(raw.encode("utf-8"))
        open(src, "wb").write((text.replace("\n", "\r\n") if crlf else text).encode("utf-8"))
        print("  %-22s %d capability image references updated" % (name, n))
        total += n

# the pane markup now indexes a list, so declare it at the top of the file
SP = os.path.join(ROOT, "build", "service_pages.py")
raw = open(SP, "rb").read().decode("utf-8")
crlf = "\r\n" in raw
text = raw.replace("\r\n", "\n")
DECL = ("_PANE_IMGS = ['assets/img/cap-scoped.webp', 'assets/img/cap-accredited.webp',\n"
        "              'assets/img/cap-schedule.webp', 'assets/img/cap-interpreted.webp']\n\n")
if "_PANE_IMGS[" in text and "_PANE_IMGS =" not in text:
    lines = text.split("\n")
    i = 0
    while i < len(lines) and (lines[i].startswith("#") or not lines[i].strip()):
        i += 1
    lines.insert(i, DECL.rstrip("\n"))
    text = "\n".join(lines)
    open(SP + ".bakcaps2", "wb").write(raw.encode("utf-8"))
    open(SP, "wb").write((text.replace("\n", "\r\n") if crlf else text).encode("utf-8"))
    print("  service_pages.py       pane image list declared")

if total == 0:
    sys.exit("No capability images were changed. Nothing written.")

# ---- 2. band scrim --------------------------------------------------------
CSS = os.path.join(ROOT, "site", "css", "pages.css")
raw = open(CSS, "rb").read().decode("utf-8")
crlf = "\r\n" in raw
text = raw.replace("\r\n", "\n")

START = "/* ==== svcd band scrim, lighter and less blue ==== */"
END = "/* ==== end svcd band scrim ==== */"
BLOCK = START + """
/* A flat neutral layer keeps the sentence legible everywhere, a soft radial
   adds weight behind it only, and the text shadow carries the contrast the
   scrim used to. Both layers shift off teal toward a neutral dark. */
.svcd-band-scrim {
  background:
    linear-gradient(rgba(14,36,40,.30), rgba(14,36,40,.30)),
    radial-gradient(ellipse 60% 90% at 50% 50%,
      rgba(10,30,34,.62) 0%, rgba(10,30,34,.34) 60%, rgba(10,30,34,.12) 100%);
}
.svcd-band-quote { text-shadow: 0 2px 26px rgba(6,20,24,.75); }
""" + END + "\n"

if START in text:
    a = text.index(START)
    b = text.index(END) + len(END)
    text = text[:a] + BLOCK.rstrip("\n") + text[b:]
    what = "replaced"
else:
    text = text.rstrip("\n") + "\n\n" + BLOCK
    what = "appended"

open(CSS + ".bakcaps", "wb").write(raw.encode("utf-8"))
open(CSS, "wb").write((text.replace("\n", "\r\n") if crlf else text).encode("utf-8"))
print("  pages.css              band scrim block %s" % what)

print("\nBackups at *.bakcaps")
print("Rebuild: cd build && python build.py && npx tailwindcss -c tailwind.config.js "
      "-i tailwind.input.css -o ../site/css/tailwind.css --minify")
