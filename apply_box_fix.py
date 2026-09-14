"""
Move the service page white boxes clear of the photographs, on all 22 pages.

Run from the repo root:

    python apply_box_fix.py

Appends one marked block to site/css/pages.css. Safe to run twice: if the
block is already there it is replaced, not duplicated.
Writes site/css/pages.css.bak2.
"""

import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
CSS = os.path.join(ROOT, "site", "css", "pages.css")

START = "/* ==== svcd floating boxes, clear of the photographs ==== */"
END = "/* ==== end svcd floating boxes ==== */"

BLOCK = START + """
/* The white panels drop below each image and push out past its edge, so
   nothing ever covers a photograph. Deeper shadow and a load-in keep them
   reading as floating panels. Image heights are fixed in the rules above:
   hero 480px, obligation figure 400px, so the offsets are exact. */

.svcd-hero-visual { padding-bottom: 158px; }
.svcd-float {
  left: -46px; top: 452px; bottom: auto; transform: none; width: 336px;
  border-radius: 18px; padding: 20px 22px;
  background: rgba(255,255,255,.97);
  backdrop-filter: blur(6px);
  box-shadow: 0 30px 70px rgba(11,47,56,.30), 0 3px 8px rgba(11,47,56,.10);
  animation: bpFloatIn .7s cubic-bezier(.22,1,.36,1) both .15s;
}
.svcd-float-2 {
  right: -28px; bottom: auto; top: 476px;
  border-radius: 16px;
  box-shadow: 0 26px 60px rgba(11,47,56,.30), 0 3px 8px rgba(11,47,56,.10);
  animation: bpFloatIn .7s cubic-bezier(.22,1,.36,1) both .3s;
}

.svcd-figure { padding-bottom: 150px; }
.svcd-figure-card {
  right: -24px; left: 40px; bottom: auto; top: 376px; width: auto;
  border-radius: 18px;
  box-shadow: 0 30px 70px rgba(11,47,56,.22), 0 3px 8px rgba(11,47,56,.08);
}
.svcd-figure-card .svcd-spec { padding: 6px 0; }

.svcd-band-scrim {
  background: radial-gradient(ellipse 68% 98% at 50% 50%,
    rgba(11,47,56,.84) 0%, rgba(11,47,56,.56) 58%, rgba(11,47,56,.32) 100%);
}

@keyframes bpFloatIn {
  from { opacity: 0; transform: translateY(18px); }
  to   { opacity: 1; transform: translateY(0); }
}
@media (prefers-reduced-motion: reduce) {
  .svcd-float, .svcd-float-2 { animation: none; }
}

@media (max-width: 900px) {
  .svcd-hero-visual { padding-bottom: 0; }
  .svcd-float { position: static; width: auto; margin: -34px 16px 0; animation: none; }
  .svcd-float-2 { position: static; margin: 14px 16px 0; animation: none; }
  .svcd-figure { padding-bottom: 0; }
  .svcd-figure-card { position: static; margin: -30px 16px 0; width: auto; }
}
""" + END + "\n"

if not os.path.exists(CSS):
    sys.exit("Not found: %s\nRun this from the repo root." % CSS)

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

open(CSS + ".bak2", "wb").write(raw.encode("utf-8"))
open(CSS, "wb").write((text.replace("\n", "\r\n") if crlf else text).encode("utf-8"))
print("pages.css: %s. Backup at site/css/pages.css.bak2" % what)
