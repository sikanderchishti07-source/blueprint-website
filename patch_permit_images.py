"""
Wire the three generated images into the environmental-permit service page only.

Run once from the repo root:

    python patch_permit_images.py

Unzip permit-images.zip into site/assets/img/ first.

Finds the entry whose slug contains "permit", then sets hero_img, detail_img
and band_img on that entry alone. Every other service keeps its svc-air-*
defaults. Writes build/svc_permitting.py.bak and changes nothing unless all
three slots are resolved.
"""

import os
import re
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(ROOT, "build", "svc_permitting.py")
IMGDIR = os.path.join(ROOT, "site", "assets", "img")

SLOTS = {
    "hero_img":   "assets/img/svc-environmental-permit-hero.webp",
    "detail_img": "assets/img/svc-environmental-permit-detail.webp",
    "band_img":   "assets/img/svc-environmental-permit-band.webp",
}

if not os.path.exists(SRC):
    sys.exit("Not found: %s\nRun this from the repo root." % SRC)

missing = [v.split("/")[-1] for v in SLOTS.values()
           if not os.path.exists(os.path.join(IMGDIR, v.split("/")[-1]))]
if missing:
    sys.exit("Missing in site/assets/img/:\n  " + "\n  ".join(missing)
             + "\nUnzip permit-images.zip there first.")

raw = open(SRC, "rb").read().decode("utf-8")
crlf = "\r\n" in raw
text = raw.replace("\r\n", "\n")

# Every slug literal in the file, in source order.
slug_re = re.compile(r"""["'](?P<slug>[a-z0-9]+(?:-[a-z0-9]+)+)["']""")
slugs = [(m.start(), m.group("slug")) for m in slug_re.finditer(text)]

hits = [(p, s) for p, s in slugs if "permit" in s and "/" not in s]
if not hits:
    print("No slug containing 'permit' found. Slugs seen in this file:")
    for _, s in slugs:
        print("   ", s)
    sys.exit(1)
if len(set(s for _, s in hits)) > 1:
    print("More than one permit-like slug, so I will not guess:")
    for _, s in hits:
        print("   ", s)
    sys.exit(1)

pos, slug = hits[0]
print("Target slug: %s" % slug)

# The entry runs from its slug to the start of the next different slug.
later = [p for p, s in slugs if p > pos and s != slug]
end = later[0] if later else len(text)
block = text[pos:end]

new_block = block
report = []

for key, val in SLOTS.items():
    pat = re.compile(r'(\b%s\s*=\s*)(["\'])(.*?)\2' % key)
    m = pat.search(new_block)
    if m:
        report.append("  %-11s %s  ->  %s" % (key, m.group(3), val))
        new_block = new_block[:m.start()] + '%s"%s"' % (m.group(1), val) + new_block[m.end():]
    else:
        # Slot not set explicitly on this entry: add it after hero_img.
        hm = re.search(r'\bhero_img\s*=\s*["\'].*?["\']\s*,?', new_block)
        if not hm:
            sys.exit("Could not find hero_img on the %s entry, stopping." % slug)
        indent = ""
        line_start = new_block.rfind("\n", 0, hm.start()) + 1
        indent = new_block[line_start:hm.start()]
        ins = '%s="%s",\n%s' % (key, val, indent)
        cut = hm.end()
        if not new_block[hm.start():cut].rstrip().endswith(","):
            new_block = new_block[:cut] + "," + new_block[cut:]
            cut += 1
        new_block = new_block[:cut] + "\n" + indent + ins.rstrip("\n" + indent) + new_block[cut:]
        report.append("  %-11s (added)  ->  %s" % (key, val))

if new_block == block:
    sys.exit("Nothing changed, the entry already points at these files.")

open(SRC + ".bak", "wb").write(raw.encode("utf-8"))
out = text[:pos] + new_block + text[end:]
if crlf:
    out = out.replace("\n", "\r\n")
open(SRC, "wb").write(out.encode("utf-8"))

print("\n".join(report))
print("\nPatched %s (backup at svc_permitting.py.bak)" % os.path.basename(SRC))
print("Now rebuild:  cd build && python build.py && npx tailwindcss -c tailwind.config.js -i tailwind.input.css -o ../site/css/tailwind.css --minify")
