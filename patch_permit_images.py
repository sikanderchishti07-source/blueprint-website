"""
Wire the three generated images into the environmental-permit entry only.

Run from the repo root:

    python patch_permit_images.py

Unzip permit-images.zip into site/assets/img/ first.
Writes build/svc_permitting.py.bak.
"""

import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(ROOT, "build", "svc_permitting.py")
IMGDIR = os.path.join(ROOT, "site", "assets", "img")

FILES = [
    "svc-environmental-permit-hero.webp",
    "svc-environmental-permit-detail.webp",
    "svc-environmental-permit-band.webp",
]

OLD = ('    group="permitting", num="01", slug="environmental-permit",\n'
       '    hero_img="assets/img/svc-permit.jpg",')

NEW = ('    group="permitting", num="01", slug="environmental-permit",\n'
       '    hero_img="assets/img/svc-environmental-permit-hero.webp",\n'
       '    detail_img="assets/img/svc-environmental-permit-detail.webp",\n'
       '    band_img="assets/img/svc-environmental-permit-band.webp",')

if not os.path.exists(SRC):
    sys.exit("Not found: %s\nRun this from the repo root." % SRC)

missing = [f for f in FILES if not os.path.exists(os.path.join(IMGDIR, f))]
if missing:
    sys.exit("Missing in site/assets/img/:\n  " + "\n  ".join(missing))

raw = open(SRC, "rb").read().decode("utf-8")
crlf = "\r\n" in raw
text = raw.replace("\r\n", "\n")

n = text.count(OLD)
if n != 1:
    sys.exit("Anchor matched %d times, expected 1. File not changed.\n"
             "Send me the two lines around slug=\"environmental-permit\" "
             "and I will re-cut the anchor." % n)

out = text.replace(OLD, NEW)
open(SRC + ".bak", "wb").write(raw.encode("utf-8"))
open(SRC, "wb").write((out.replace("\n", "\r\n") if crlf else out).encode("utf-8"))

print("Patched environmental-permit: hero, detail and band now point at the new webp files.")
print("Backup at build/svc_permitting.py.bak")
