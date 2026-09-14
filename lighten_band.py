"""
Take more of the blue out of the statement band.

The previous pass was still tinted, because both scrim layers were mixed from
a teal base. This shifts them to a near-neutral dark and drops the opacity
again, so the photograph reads as a photograph. The text keeps its contrast
from a stronger shadow rather than from the wash.

Run from the repo root, as many times as you like:

    python lighten_band.py

Safe to re-run: the block is marked and gets replaced, not stacked.
"""

import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
CSS = os.path.join(ROOT, "site", "css", "pages.css")
if not os.path.exists(CSS):
    sys.exit("Not found: %s\nRun this from the repo root." % CSS)

START = "/* ==== svcd band scrim, lighter and less blue ==== */"
END = "/* ==== end svcd band scrim ==== */"

BLOCK = START + """
/* Near neutral, low opacity. The flat layer stops the text dropping out over
   bright sky, the radial adds a little weight behind the sentence only, and
   the shadow does the rest. */
.svcd-band-scrim {
  background:
    linear-gradient(rgba(8,14,16,.18), rgba(8,14,16,.18)),
    radial-gradient(ellipse 56% 86% at 50% 50%,
      rgba(6,12,14,.46) 0%, rgba(6,12,14,.20) 62%, rgba(6,12,14,.04) 100%);
}
.svcd-band-quote { text-shadow: 0 2px 10px rgba(4,10,12,.85), 0 6px 34px rgba(4,10,12,.7); }
.svcd-band-cta { box-shadow: 0 10px 34px rgba(4,10,12,.4); }
""" + END + "\n"

raw = open(CSS, "rb").read().decode("utf-8")
crlf = "\r\n" in raw
text = raw.replace("\r\n", "\n")

if START in text:
    a = text.index(START)
    b = text.index(END) + len(END)
    text = text[:a] + BLOCK.rstrip("\n") + text[b:]
    what = "replaced the existing block"
else:
    text = text.rstrip("\n") + "\n\n" + BLOCK
    what = "appended a new block"

open(CSS + ".bakband", "wb").write(raw.encode("utf-8"))
open(CSS, "wb").write((text.replace("\n", "\r\n") if crlf else text).encode("utf-8"))
print("pages.css: %s" % what)
print("No rebuild of build.py needed, this is CSS only. Just commit and push.")
