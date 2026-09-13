"""
Wire the three generated images into the environmental-permit entry only.

Run from the repo root:

    python patch_permit_images.py

Unzip permit-images.zip into site/assets/img/ first.
Writes build/svc_permitting.py.bak.
"""

import os
import re
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(ROOT, "build", "svc_permitting.py")
IMGDIR = os.path.join(ROOT, "site", "assets", "img")

SLUG = "environmental-permit"
HERO = "assets/img/svc-environmental-permit-hero.webp"
DETAIL = "assets/img/svc-environmental-permit-detail.webp"
BAND = "assets/img/svc-environmental-permit-band.webp"

if not os.path.exists(SRC):
    sys.exit("Not found: %s\nRun this from the repo root." % SRC)

missing = [f for f in (HERO, DETAIL, BAND)
           if not os.path.exists(os.path.join(IMGDIR, f.split("/")[-1]))]
if missing:
    sys.exit("Missing in site/assets/img/:\n  "
             + "\n  ".join(f.split("/")[-1] for f in missing))

raw = open(SRC, "rb").read().decode("utf-8")
crlf = "\r\n" in raw
lines = raw.replace("\r\n", "\n").split("\n")

# The slug line: exact value, so waste-management-permit cannot match.
slug_idx = [i for i, L in enumerate(lines)
            if re.search(r'slug\s*=\s*["\']%s["\']' % re.escape(SLUG), L)]
if len(slug_idx) != 1:
    sys.exit("Found %d lines with slug=\"%s\", expected 1." % (len(slug_idx), SLUG))
start = slug_idx[0]

# The next hero_img line after it.
hero_idx = None
for i in range(start, min(start + 40, len(lines))):
    if re.search(r'\bhero_img\s*=', lines[i]):
        hero_idx = i
        break
if hero_idx is None:
    sys.exit("No hero_img line within 40 lines of the slug. Lines seen:\n"
             + "\n".join("%4d %s" % (i, lines[i])
                         for i in range(start, min(start + 40, len(lines)))))

print("slug line   %4d  %s" % (start, lines[start].strip()))
print("hero line   %4d  %s" % (hero_idx, lines[hero_idx].strip()))

indent = re.match(r"\s*", lines[hero_idx]).group(0)
lines[hero_idx] = (
    '%shero_img="%s",\n'
    '%sdetail_img="%s",\n'
    '%sband_img="%s",' % (indent, HERO, indent, DETAIL, indent, BAND)
)

# Drop any detail_img / band_img already set further down in this entry,
# so the new ones are not overridden.
end = len(lines)
for i in range(hero_idx + 1, len(lines)):
    if re.search(r'slug\s*=\s*["\']', lines[i]):
        end = i
        break
killed = []
for i in range(hero_idx + 1, end):
    if re.search(r'\b(detail_img|band_img)\s*=', lines[i]):
        killed.append(lines[i].strip())
        lines[i] = None
lines = [L for L in lines if L is not None]

out = "\n".join(lines)
open(SRC + ".bak", "wb").write(raw.encode("utf-8"))
open(SRC, "wb").write((out.replace("\n", "\r\n") if crlf else out).encode("utf-8"))

for k in killed:
    print("removed     %s" % k)
print("\nPatched. Backup at build/svc_permitting.py.bak")
