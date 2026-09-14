"""
Wire the nine batch 5 hero images into their pages.

These nine span three source files:
  build/svc_permitting.py   periodic-environmental-report
  build/svc_monitoring.py   pollution-control-equipment, reporting-compliance
  build/svc_specialist.py   the remaining six

Only hero_img is set. detail_img and band_img keep whatever they use now.

Run from the repo root:

    python patch_batch5.py

Unzip batch5-images.zip into site/assets/img/ first.
Writes a .bak5 beside each file it edits.
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
        f = "svc-%s-hero.webp" % slug
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
            sys.exit("%s: no hero_img within 40 lines of slug=\"%s\". Nothing "
                     "written to this file." % (relpath, slug))

        indent = re.match(r"\s*", lines[hero_i]).group(0)
        lines[hero_i] = '%shero_img="assets/img/svc-%s-hero.webp",' % (indent, slug)
        done.append("  %-32s %s" % (slug, os.path.basename(relpath)))

    out = "\n".join(lines)
    open(src + ".bak5", "wb").write(raw.encode("utf-8"))
    open(src, "wb").write((out.replace("\n", "\r\n") if crlf else out).encode("utf-8"))

print("Patched:")
print("\n".join(done))
print("\nBackups at *.py.bak5")
print("Rebuild: cd build && python build.py && npx tailwindcss -c tailwind.config.js "
      "-i tailwind.input.css -o ../site/css/tailwind.css --minify")
