"""
Put a very light teal back over the statement band.

Just enough to sit the text down and tie the band to the brand colour, not
enough to hide the photograph. To go lighter or heavier, change the two
numbers in TINT below and run it again.

Run from the repo root, safe to re-run:

    python band_light_tint.py
"""

import os
import sys

# FLAT = wash over the whole band, MID = extra weight behind the sentence only
FLAT = 0.12
MID = 0.22

ROOT = os.path.dirname(os.path.abspath(__file__))
CSS = os.path.join(ROOT, "site", "css", "pages.css")
if not os.path.exists(CSS):
    sys.exit("Not found: %s\nRun this from the repo root." % CSS)

START = "/* ==== svcd band scrim, lighter and less blue ==== */"
END = "/* ==== end svcd band scrim ==== */"

BODY = """
/* A very light teal. The flat layer is barely there, the radial adds a touch
   behind the sentence, and the text shadow still does most of the work. */
.svcd-band-scrim {
  background:
    linear-gradient(rgba(11,47,56,FLAT), rgba(11,47,56,FLAT)),
    radial-gradient(ellipse 58% 88% at 50% 50%,
      rgba(9,38,46,MID) 0%, rgba(9,38,46,OUT) 62%, rgba(9,38,46,0) 100%);
}
.svcd-band-quote {
  text-shadow: 0 1px 2px rgba(0,0,0,.5),
               0 2px 12px rgba(0,0,0,.5),
               0 8px 40px rgba(0,0,0,.4);
}
.svcd-band-cta { box-shadow: 0 8px 30px rgba(0,0,0,.32); }
"""

BODY = (BODY.replace("FLAT", "%.2f" % FLAT)
            .replace("MID", "%.2f" % MID)
            .replace("OUT", "%.2f" % (MID * 0.45)))

BLOCK = START + BODY + END + "\n"

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

open(CSS + ".baktint", "wb").write(raw.encode("utf-8"))
open(CSS, "wb").write((text.replace("\n", "\r\n") if crlf else text).encode("utf-8"))
print("pages.css: %s  (flat %.2f, centre %.2f)" % (what, FLAT, MID))
print("CSS only, no rebuild needed. Commit and push.")
