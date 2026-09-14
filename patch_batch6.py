"""
Final patch. Wires detail_img and band_img into the last nine service pages.

Spans three source files:
  build/svc_permitting.py   periodic-environmental-report
  build/svc_monitoring.py   pollution-control-equipment, reporting-compliance
  build/svc_specialist.py   the remaining six

hero_img is left alone, it was set by patch_batch5.

Run from the repo root:

    python patch_batch6.py

Unzip batch6-images.zip into site/assets/img/ first.
Writes a .bak6 beside each file it edits.
"""

import os
import re
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
IMGDIR = os.path.join(ROOT, "site", "assets", "img")

TARGETS = [
    ("build/svc_permitting.py", ["periodic-environmental-report"]),
    ("build/svc_monitoring.py", ["pollution-control-equipment",
                                 "reporting-compliance"]),
    ("build/svc_specialist.py", ["climate-sustainability",
                                 "ecological-surveys",
                                 "marine-environment",
                                 "remediation-rehabilitation",
                                 "environmental-modelling",
                                 "laboratory-services"]),
]

missing = []
for _, slugs in TARGETS:
    for slug in slugs:
        for slot in ("detail", "band"):
            f = "svc-%s-%s.webp" % (slug, slot)
            if not os.path.exists(os.path.join(IMGDIR, f)):
                missing.append(f)
if missing:
    sys.exit("Missing in site/assets/img/:\n  " + "\n  ".join(missing))

done = []
for relpath, slugs in TARGETS:
    src = os.path.join(ROOT, *relpath.split("/"))
    if not os.path.exists(src):
        sys.exit("Not found: %s\nRun this from the repo root." % src)

    raw = open(src, "rb").read().decode("utf-8")
    crlf = "\r\n" in raw
    lines = raw.replace("\r\n", "\n").split("\n")

    for slug in slugs:
        idx = [i for i, L in enumerate(lines)
               if re.search(r'slug\s*=\s*["\']%s["\']' % re.escape(slug), L)]
        if len(idx) != 1:
            sys.exit("%s: %d lines with slug=\"%s\", expected 1. Nothing written "
                     "to this file." % (relpath, len(idx), slug))
        start = idx[0]

        hero_i = None
        for i in range(start, min(start + 40, len(lines))):
            if re.search(r'\bhero_img\s*=', lines[i]):
                hero_i = i
                break
        if hero_i is None:
            sys.exit("%s: no hero_img near slug=\"%s\". Nothing written to this "
                     "file." % (relpath, slug))

        # strip any detail_img / band_img already present in this entry
        end = len(lines)
        for i in range(hero_i + 1, len(lines)):
            if re.search(r'slug\s*=\s*["\']', lines[i]):
                end = i
                break
        for i in range(hero_i + 1, end):
            if lines[i] is not None and re.search(r'\b(detail_img|band_img)\s*=', lines[i]):
                lines[i] = None
        lines = [L for L in lines if L is not None]

        indent = re.match(r"\s*", lines[hero_i]).group(0)
        lines[hero_i] = (
            lines[hero_i].rstrip() + "\n"
            + '%sdetail_img="assets/img/svc-%s-detail.webp",\n' % (indent, slug)
            + '%sband_img="assets/img/svc-%s-band.webp",' % (indent, slug)
        )
        done.append("  %-32s %s" % (slug, os.path.basename(relpath)))

    out = "\n".join(lines)
    open(src + ".bak6", "wb").write(raw.encode("utf-8"))
    open(src, "wb").write((out.replace("\n", "\r\n") if crlf else out).encode("utf-8"))

print("Patched:")
print("\n".join(done))
print("\nBackups at *.py.bak6")
print("Rebuild: cd build && python build.py && npx tailwindcss -c tailwind.config.js "
      "-i tailwind.input.css -o ../site/css/tailwind.css --minify")
