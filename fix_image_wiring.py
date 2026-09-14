"""
Fix the service page image wiring.

Both svc_monitoring.py and svc_specialist.py build every service through one
shared _S() helper that hardcodes a single set of images, so all nine monitoring
pages and all six specialist pages show the same pictures. This rewrites those
three lines in each helper to derive the paths from the slug, which is already
a parameter, so every page picks up its own images.

Run from the repo root:

    python fix_image_wiring.py

Writes build/svc_monitoring.py.bakfix and build/svc_specialist.py.bakfix.
Verifies every referenced image exists before writing anything.
"""

import os
import re
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))

NEW = ('                hero_img=f"assets/img/svc-{slug}-hero.webp",\n'
       '                detail_img=f"assets/img/svc-{slug}-detail.webp",\n'
       '                band_img=f"assets/img/svc-{slug}-band.webp",')

JOBS = [
    ("build/svc_monitoring.py", "MONITORING",
     '                hero_img="assets/img/svc-soil-sediment-testing-hero.webp",\n'
     '                detail_img="assets/img/svc-soil-sediment-testing-detail.webp",\n'
     '                band_img="assets/img/svc-soil-sediment-testing-band.webp",'),
    ("build/svc_specialist.py", "SPECIALIST",
     '                hero_img=img, detail_img="assets/img/svc-air-detail.jpg",\n'
     '                band_img="assets/img/svc-air-lab.jpg",'),
]

# check every image first, write nothing if any is absent
missing = []
for relpath, var, _ in JOBS:
    src = os.path.join(ROOT, *relpath.split("/"))
    if not os.path.exists(src):
        sys.exit("Not found: %s\nRun this from the repo root." % src)
    text = open(src, "rb").read().decode("utf-8")
    for slug in re.findall(r'%s\["([^"]+)"\]' % var, text):
        for slot in ("hero", "detail", "band"):
            p = os.path.join(ROOT, "site", "assets", "img",
                             "svc-%s-%s.webp" % (slug, slot))
            if not os.path.exists(p):
                missing.append(os.path.basename(p))
if missing:
    sys.exit("Missing images, nothing written:\n  " + "\n  ".join(missing))

for relpath, var, old in JOBS:
    src = os.path.join(ROOT, *relpath.split("/"))
    raw = open(src, "rb").read().decode("utf-8")
    crlf = "\r\n" in raw
    text = raw.replace("\r\n", "\n")

    if text.count(old) != 1:
        sys.exit("%s: expected 1 match for the image block, found %d. "
                 "Nothing written to this file."
                 % (relpath, text.count(old)))

    text = text.replace(old, NEW)

    # the helper must be an f-string user now, so confirm slug is in scope
    if "def _S(slug," not in text:
        sys.exit("%s: _S does not take slug as its first parameter, stopping."
                 % relpath)

    open(src + ".bakfix", "wb").write(raw.encode("utf-8"))
    open(src, "wb").write((text.replace("\n", "\r\n") if crlf else text).encode("utf-8"))
    n = len(re.findall(r'%s\["([^"]+)"\]' % var, text))
    print("  %-24s %d services now use their own images" % (os.path.basename(relpath), n))

print("\nBackups at *.py.bakfix")
print("Rebuild: cd build && python build.py && npx tailwindcss -c tailwind.config.js "
      "-i tailwind.input.css -o ../site/css/tailwind.css --minify")
