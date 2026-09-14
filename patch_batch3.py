"""
Wire the batch 3 images into four monitoring pages.

air-quality-monitoring lives in build/service_pages.py (it is the base entry).
The other three live in build/svc_monitoring.py.

Run from the repo root:

    python patch_batch3.py

Unzip batch3-images.zip into site/assets/img/ first.
Writes a .bak3 beside each file it edits.
"""

import os
import re
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
IMGDIR = os.path.join(ROOT, "site", "assets", "img")

TARGETS = [
    ("build/service_pages.py", ["air-quality-monitoring"]),
    ("build/svc_monitoring.py", ["water-wastewater-testing",
                                 "noise-monitoring",
                                 "soil-sediment-testing"]),
]

missing = []
for _, slugs in TARGETS:
    for slug in slugs:
        for slot in ("hero", "detail", "band"):
            f = "svc-%s-%s.webp" % (slug, slot)
            if not os.path.exists(os.path.join(IMGDIR, f)):
                missing.append(f)
if missing:
    sys.exit("Missing in site/assets/img/:\n  " + "\n  ".join(missing))


def trio(indent, slug):
    return (
        '%shero_img="assets/img/svc-%s-hero.webp",\n'
        '%sdetail_img="assets/img/svc-%s-detail.webp",\n'
        '%sband_img="assets/img/svc-%s-band.webp",'
        % (indent, slug, indent, slug, indent, slug)
    )


for relpath, slugs in TARGETS:
    src = os.path.join(ROOT, *relpath.split("/"))
    if not os.path.exists(src):
        sys.exit("Not found: %s\nRun this from the repo root." % src)

    raw = open(src, "rb").read().decode("utf-8")
    crlf = "\r\n" in raw
    lines = raw.replace("\r\n", "\n").split("\n")
    done = []

    for slug in slugs:
        idx = [i for i, L in enumerate(lines)
               if re.search(r'slug\s*=\s*["\']%s["\']' % re.escape(slug), L)]

        if idx:
            # normal case: find the hero_img that follows the slug line
            if len(idx) != 1:
                sys.exit("%s: %d lines with slug=\"%s\", expected 1. Nothing written."
                         % (relpath, len(idx), slug))
            start = idx[0]
            hero_i = None
            for i in range(start, min(start + 40, len(lines))):
                if re.search(r'\bhero_img\s*=', lines[i]):
                    hero_i = i
                    break
            if hero_i is None:
                sys.exit("%s: no hero_img near slug=\"%s\". Nothing written."
                         % (relpath, slug))
        else:
            # base entry with no slug= line: take the first hero_img in the file
            hits = [i for i, L in enumerate(lines) if re.search(r'\bhero_img\s*=', L)]
            if len(hits) != 1:
                sys.exit("%s: no slug=\"%s\" and %d hero_img lines, cannot choose. "
                         "Nothing written." % (relpath, slug, len(hits)))
            hero_i = hits[0]

        indent = re.match(r"\s*", lines[hero_i]).group(0)
        lines[hero_i] = trio(indent, slug)

        end = len(lines)
        for i in range(hero_i + 1, len(lines)):
            if re.search(r'slug\s*=\s*["\']', lines[i]):
                end = i
                break
        for i in range(hero_i + 1, end):
            if lines[i] is not None and re.search(r'\b(detail_img|band_img)\s*=', lines[i]):
                lines[i] = None
        lines = [L for L in lines if L is not None]
        done.append("  %-30s %s" % (slug, os.path.basename(relpath)))

    out = "\n".join(lines)
    open(src + ".bak3", "wb").write(raw.encode("utf-8"))
    open(src, "wb").write((out.replace("\n", "\r\n") if crlf else out).encode("utf-8"))
    print("\n".join(done))

print("\nDone. Backups at *.py.bak3")
print("Rebuild: cd build && python build.py && npx tailwindcss -c tailwind.config.js "
      "-i tailwind.input.css -o ../site/css/tailwind.css --minify")
