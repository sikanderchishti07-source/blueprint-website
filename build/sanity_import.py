"""One-time move of the existing blog articles into Sanity.

Run once on the go-live day, AFTER a normal build (python build.py) and BEFORE
filling projectId in content/sanity.json:

    python sanity_import.py <projectId> <write-token>

It reads the 5 current articles (English text, the Arabic text from the
built /ar/ pages, cover pictures, dates) and creates them in Sanity. Safe to
run again: it replaces the same five documents rather than adding copies.

    python sanity_import.py --dry-run      writes sanity_import_preview.json only
"""
import html as _html
import json
import mimetypes
import os
import re
import sys
import uuid
import urllib.request
from html.parser import HTMLParser

HERE = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.join(HERE, "..", "site")
API_VERSION = "2025-02-19"
DATASET = "production"


# ---- HTML -> Portable Text ------------------------------------------------------
def _key():
    return uuid.uuid4().hex[:12]


class _ToBlocks(HTMLParser):
    BLOCK = {"p": "normal", "h2": "h2", "h3": "h3", "h4": "h3", "blockquote": "blockquote"}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.blocks, self.cur, self.marks, self.list = [], None, [], None

    def _start_block(self, style, list_item=None):
        self.cur = {"_type": "block", "_key": _key(), "style": style, "markDefs": [], "children": []}
        if list_item:
            self.cur["listItem"], self.cur["level"] = list_item, 1

    def _end_block(self):
        if self.cur is not None:
            kids = self.cur["children"]
            if kids:
                kids[0]["text"] = kids[0]["text"].lstrip()
                kids[-1]["text"] = kids[-1]["text"].rstrip()
            self.cur["children"] = [k for k in kids if k["text"]] or [{"_type": "span", "_key": _key(), "text": "", "marks": []}]
            if any(k["text"] for k in self.cur["children"]):
                self.blocks.append(self.cur)
        self.cur = None

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in ("ul", "ol"):
            self.list = "bullet" if tag == "ul" else "number"
        elif tag == "li":
            self._end_block()
            self._start_block("normal", self.list or "bullet")
        elif tag in self.BLOCK:
            self._end_block()
            style = "lead" if tag == "p" and "lead" in (a.get("class") or "") else self.BLOCK[tag]
            self._start_block(style)
        elif tag in ("strong", "b"):
            self.marks.append("strong")
        elif tag in ("em", "i"):
            self.marks.append("em")
        elif tag == "a" and self.cur is not None:
            k = _key()
            self.cur["markDefs"].append({"_type": "link", "_key": k, "href": a.get("href", "")})
            self.marks.append(k)
        elif tag == "br" and self.cur is not None:
            self._text("\n")

    def handle_endtag(self, tag):
        if tag in ("ul", "ol"):
            self._end_block()
            self.list = None
        elif tag == "li" or tag in self.BLOCK:
            self._end_block()
        elif tag in ("strong", "b", "em", "i", "a") and self.marks:
            self.marks.pop()

    def _text(self, t):
        if self.cur is None:
            if not t.strip():
                return
            self._start_block("normal")
        t = re.sub(r"\s+", " ", t) if t != "\n" else t
        kids = self.cur["children"]
        if kids and kids[-1]["marks"] == list(self.marks):
            kids[-1]["text"] += t
        else:
            kids.append({"_type": "span", "_key": _key(), "text": t, "marks": list(self.marks)})

    def handle_data(self, data):
        self._text(data)


def html_to_blocks(html):
    p = _ToBlocks()
    p.feed(html)
    p.close()
    p._end_block()
    return p.blocks


# ---- reading the current articles ----------------------------------------------------
def _arabic_body(slug):
    path = os.path.join(SITE, "ar", "blog-%s.html" % slug)
    h = open(path, encoding="utf-8").read()
    start = h.index('<div class="article-body">') + len('<div class="article-body">')
    end = h.index('<div class="not-prose', start)
    return h[start:end]


def current_articles():
    sys.path.insert(0, HERE)
    import pages_extra as X
    import ar_pages as A
    import datetime
    out = []
    for a in X.ARTICLES:
        slug = a["slug"]
        d = datetime.datetime.strptime(a["date"], "%B %d, %Y").date().isoformat()
        out.append({
            "slug": slug, "date": d,
            "titleEn": a["title"], "titleAr": A._lookup(a["title"]),
            "summaryEn": a["summary"], "summaryAr": A._lookup(a["summary"]),
            "category": a["cat"], "minutes": int(a["read"].split()[0]),
            "bodyEn": X.ARTICLE_BODIES[slug], "bodyAr": _arabic_body(slug),
            "image": os.path.join(SITE, a["img"]),
        })
    return out


def documents(image_refs):
    docs = []
    for a in current_articles():
        missing = [k for k in ("titleAr", "summaryAr") if not a[k]]
        if missing:
            raise SystemExit("STOP: no Arabic %s found for %s" % (missing, a["slug"]))
        docs.append({
            "_id": "post-" + a["slug"], "_type": "post",
            "titleEn": a["titleEn"], "titleAr": a["titleAr"],
            "slug": {"_type": "slug", "current": a["slug"]},
            "publishedAt": a["date"], "category": a["category"],
            "coverImage": {"_type": "image", "asset": {"_type": "reference", "_ref": image_refs[a["slug"]]}},
            "summaryEn": a["summaryEn"], "summaryAr": a["summaryAr"],
            "bodyEn": html_to_blocks(a["bodyEn"]), "bodyAr": html_to_blocks(a["bodyAr"]),
            "actionRequired": False, "readingMinutes": a["minutes"],
        })
    return docs


# ---- talking to Sanity ----------------------------------------------------------------
def _request(url, token, data, ctype):
    req = urllib.request.Request(url, data=data, method="POST",
                                 headers={"Authorization": "Bearer " + token, "Content-Type": ctype})
    with urllib.request.urlopen(req, timeout=120) as r:
        return json.loads(r.read().decode("utf-8"))


def upload_image(pid, token, path):
    url = "https://%s.api.sanity.io/v%s/assets/images/%s?filename=%s" % (pid, API_VERSION, DATASET, os.path.basename(path))
    ctype = mimetypes.guess_type(path)[0] or "image/webp"
    return _request(url, token, open(path, "rb").read(), ctype)["document"]["_id"]


def main():
    args = sys.argv[1:]
    if args[:1] == ["--dry-run"]:
        refs = {a["slug"]: "image-preview-1600x900-webp" for a in current_articles()}
        out = os.path.join(HERE, "sanity_import_preview.json")
        json.dump(documents(refs), open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        print("Preview written:", out)
        return
    if len(args) != 2:
        print(__doc__)
        sys.exit(1)
    pid, token = args
    refs = {}
    for a in current_articles():
        print("uploading picture  ", os.path.basename(a["image"]))
        refs[a["slug"]] = upload_image(pid, token, a["image"])
    docs = documents(refs)
    body = json.dumps({"mutations": [{"createOrReplace": d} for d in docs]}).encode("utf-8")
    _request("https://%s.api.sanity.io/v%s/data/mutate/%s" % (pid, API_VERSION, DATASET), token, body, "application/json")
    for d in docs:
        print("created article    ", d["titleEn"])
    print("\nDone. %d articles are now in Sanity." % len(docs))


if __name__ == "__main__":
    main()
