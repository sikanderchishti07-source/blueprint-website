"""
Remove the statement band overlay entirely.

The photograph shows through untouched. The sentence and the button carry
their own contrast with a shadow, which is what keeps white text readable
over the pale sky in these images.

If you want it completely bare with no shadow either, set BARE = True below.

Run from the repo root, safe to re-run:

    python band_no_scrim.py
"""

import os
import sys

BARE = False          # True = no shadow at all, photo completely untouched

ROOT = os.path.dirname(os.path.abspath(__file__))
CSS = os.path.join(ROOT, "site", "css", "pages.css")
if not os.path.exists(CSS):
    sys.exit("Not found: %s\nRun this from the repo root." % CSS)

START = "/* ==== svcd band scrim, lighter and less blue ==== */"
END = "/* ==== end svcd band scrim ==== */"

if BARE:
    BODY = """
.svcd-band-scrim { background: none; }
.svcd-band-quote { text-shadow: none; }
"""
else:
    BODY = """
/* No overlay. The photograph is untouched and the text carries its own
   contrast, a tight shadow for edge definition and a wide soft one to lift
   it off bright sky. */
.svcd-band-scrim { background: none; }
.svcd-band-quote {
  text-shadow: 0 1px 2px rgba(0,0,0,.55),
               0 2px 12px rgba(0,0,0,.55),
               0 8px 40px rgba(0,0,0,.45);
}
.svcd-band-cta { box-shadow: 0 8px 30px rgba(0,0,0,.35); }
"""

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

open(CSS + ".baknoscrim", "wb").write(raw.encode("utf-8"))
open(CSS, "wb").write((text.replace("\n", "\r\n") if crlf else text).encode("utf-8"))
print("pages.css: %s (BARE = %s)" % (what, BARE))
print("CSS only, no rebuild needed. Commit and push.")
