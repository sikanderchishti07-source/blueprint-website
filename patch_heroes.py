"""
Service page hero images.

Replaces the placeholder svc-card-N.webp used by each of the eight
carousel service pages with its own generated hero.

Matches by the nearest slug above each img= line, so it does not depend
on the order the services appear in the file.

Run once from the repo root:

    python patch_heroes.py

Unzip service-heroes.zip into site/assets/img/ first.
Writes build/svc_cards.py.bak. Changes nothing unless all eight match.
"""

import os
import re
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(ROOT, "build", "svc_cards.py")
IMGDIR = os.path.join(ROOT, "site", "assets", "img")

HEROES = {
    "environmental-studies":        "svq-environmental-studies.webp",
    "marine-environment-services":  "svq-marine-environment-services.webp",
    "terrestrial-environment":      "svq-terrestrial-environment.webp",
    "veterinary-biosecurity":       "svq-veterinary-biosecurity.webp",
    "test-boreholes":               "svq-test-boreholes.webp",
    "hydrogeology-geotechnics":     "svq-hydrogeology-geotechnics.webp",
    "treatment-rehabilitation":     "svq-treatment-rehabilitation.webp",
    "environmental-training":       "svq-environmental-training.webp",
}

if not os.path.exists(SRC):
    sys.exit("Not found: " + SRC + "\nRun this from the repo root.")

missing = [f for f in HEROES.values() if not os.path.exists(os.path.join(IMGDIR, f))]
if missing:
    sys.exit("Missing in site/assets/img/:\n  " + "\n  ".join(missing)
             + "\nUnzip service-heroes.zip there first.")

raw = open(SRC, "rb").read()
bom = raw.startswith(b"\xef\xbb\xbf")
text = raw.decode("utf-8-sig")
crlf = "\r\n" in text
text = text.replace("\r\n", "\n")

if "svq-environmental-studies.webp" in text:
    sys.exit("svc_cards.py already patched. Restore build/svc_cards.py.bak to redo it.")

lines = text.split("\n")

# walk the file, remembering the most recent slug we saw
slug_re = re.compile(r'["\']([a-z][a-z0-9-]{4,})["\']')
img_re = re.compile(r'(img\s*=\s*["\'])assets/img/svc-card-\d\.webp(["\'])')

current = None
changed = {}
for i, line in enumerate(lines):
    for m in slug_re.finditer(line):
        if m.group(1) in HEROES:
            current = m.group(1)
    m = img_re.search(line)
    if m:
        if current is None:
            sys.exit("Found an img= line at %d with no slug above it. Nothing changed." % (i + 1))
        if current in changed:
            sys.exit("Slug %s matched twice. Nothing changed." % current)
        lines[i] = img_re.sub(r"\1assets/img/" + HEROES[current] + r"\2", line)
        changed[current] = i + 1

if len(changed) != 8:
    sys.exit("Matched %d of 8 services (%s). Nothing changed."
             % (len(changed), ", ".join(sorted(changed))))

open(SRC + ".bak", "wb").write(raw)
out = "\n".join(lines)
if crlf:
    out = out.replace("\n", "\r\n")
data = out.encode("utf-8")
if bom:
    data = b"\xef\xbb\xbf" + data
open(SRC, "wb").write(data)

for slug in HEROES:
    print("  line %-5d %-30s -> %s" % (changed[slug], slug, HEROES[slug]))
print("\npatched build/svc_cards.py  (8 heroes)")
print("\nNow rebuild:")
print("  cd build")
print("  python build.py")
print("  npx tailwindcss -c tailwind.config.js -i tailwind.input.css -o ../site/css/tailwind.css --minify")
