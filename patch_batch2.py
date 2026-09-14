"""
Wire the batch 2 images into four permitting pages.

Run from the repo root:

    python patch_batch2.py

Unzip batch2-images.zip into site/assets/img/ first.
Writes build/svc_permitting.py.bak2.
"""

import os
import re
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(ROOT, "build", "svc_permitting.py")
IMGDIR = os.path.join(ROOT, "site", "assets", "img")

SLUGS = [
    "environmental-impact-assessment",
    "waste-management-permit",
    "environmental-management-plan",
    "environmental-register",
]
SLOTS = ["hero", "detail", "band"]

if not os.path.exists(SRC):
    sys.exit("Not found: %s\nRun this from the repo root." % SRC)

missing = []
for slug in SLUGS:
    for slot in SLOTS:
        f = "svc-%s-%s.webp" % (slug, slot)
        if not os.path.exists(os.path.join(IMGDIR, f)):
            missing.append(f)
if missing:
    sys.exit("Missing in site/assets/img/:\n  " + "\n  ".join(missing))

raw = open(SRC, "rb").read().decode("utf-8")
crlf = "\r\n" in raw
lines = raw.replace("\r\n", "\n").split("\n")

report = []
for slug in SLUGS:
    idx = [i for i, L in enumerate(lines)
           if re.search(r'slug\s*=\s*["\']%s["\']' % re.escape(slug), L)]
    if len(idx) != 1:
        sys.exit("Found %d lines with slug=\"%s\", expected 1. Nothing written."
                 % (len(idx), slug))
    start = idx[0]

    hero_i = None
    for i in range(start, min(start + 40, len(lines))):
        if re.search(r'\bhero_img\s*=', lines[i]):
            hero_i = i
            break
    if hero_i is None:
        sys.exit("No hero_img within 40 lines of slug=\"%s\". Nothing written." % slug)

    indent = re.match(r"\s*", lines[hero_i]).group(0)
    lines[hero_i] = (
        '%shero_img="assets/img/svc-%s-hero.webp",\n'
        '%sdetail_img="assets/img/svc-%s-detail.webp",\n'
        '%sband_img="assets/img/svc-%s-band.webp",'
        % (indent, slug, indent, slug, indent, slug)
    )

    # drop any detail_img / band_img already set later in this same entry
    end = len(lines)
    for i in range(hero_i + 1, len(lines)):
        if re.search(r'slug\s*=\s*["\']', lines[i]):
            end = i
            break
    for i in range(hero_i + 1, end):
        if lines[i] is not None and re.search(r'\b(detail_img|band_img)\s*=', lines[i]):
            lines[i] = None

    report.append("  %-34s line %d" % (slug, hero_i))
    lines = [L for L in lines if L is not None]

out = "\n".join(lines)
open(SRC + ".bak2", "wb").write(raw.encode("utf-8"))
open(SRC, "wb").write((out.replace("\n", "\r\n") if crlf else out).encode("utf-8"))

print("Patched:")
print("\n".join(report))
print("\nBackup at build/svc_permitting.py.bak2")
print("Rebuild: cd build && python build.py && npx tailwindcss -c tailwind.config.js "
      "-i tailwind.input.css -o ../site/css/tailwind.css --minify")
