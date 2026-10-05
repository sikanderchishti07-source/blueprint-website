"""Blog posts and job vacancies from Sanity (the staff editor).

Switched on by content/sanity.json: when "projectId" is filled in, every build
reads the published posts and vacancies from Sanity and the files in
content/blog and content/careers are no longer used. Empty projectId = old
behaviour, nothing changes.

Each item comes back with the same keys the page templates already use
(title, date, summary, img, html, ...) plus the Arabic versions (title_ar,
summary_ar, html_ar, ...), which ar_pages.py uses for the /ar/ pages.

If Sanity is switched on but cannot be reached, the build stops with a clear
message instead of publishing a site without its articles; Vercel then keeps
the last good version online.
"""
import datetime
import html as _html
import json
import os
import re
import urllib.parse
import urllib.request

_HERE = os.path.dirname(os.path.abspath(__file__))
_CFG_PATH = os.path.join(_HERE, "..", "content", "sanity.json")

MONTHS_AR = ["يناير", "فبراير", "مارس", "أبريل", "مايو", "يونيو",
             "يوليو", "أغسطس", "سبتمبر", "أكتوبر", "نوفمبر", "ديسمبر"]

# Blog categories: the editor offers these; the Arabic name is fixed here.
CATEGORIES = {
    "Permitting": "التراخيص",
    "Waste Permits": "تراخيص النفايات",
    "Renewals": "التجديد",
    "Inspections": "التفتيش",
    "Quarries & Mining": "المحاجر والتعدين",
    "Monitoring": "الرصد",
    "Reporting": "التقارير",
    "Air Quality": "جودة الهواء",
    "Water": "المياه",
    "Marine": "البيئة البحرية",
    "Climate & ESG": "المناخ والاستدامة",
    "Regulatory update": "تحديث تنظيمي",
    "Insight": "رؤى",
}

JOB_TYPES = {"Full time": "دوام كامل", "Part time": "دوام جزئي",
             "Contract": "عقد", "Internship": "تدريب"}


def config():
    try:
        with open(_CFG_PATH, encoding="utf-8") as f:
            cfg = json.load(f)
    except (OSError, ValueError):
        return None
    pid = (os.environ.get("SANITY_PROJECT_ID") or cfg.get("projectId") or "").strip()
    if not pid:
        return None
    cfg["projectId"] = pid
    cfg.setdefault("dataset", "production")
    cfg.setdefault("apiVersion", "2025-02-19")
    return cfg


def enabled():
    return config() is not None


# ---- fetching ---------------------------------------------------------------
_CACHE = {}


def _query(groq):
    cfg = config()
    if groq in _CACHE:
        return _CACHE[groq]
    # the live API (not the CDN) so a build started by "Publish" sees the new post
    base = os.environ.get("SANITY_API_BASE") or "https://%s.api.sanity.io" % cfg["projectId"]
    url = "%s/v%s/data/query/%s?query=%s" % (base, cfg["apiVersion"], cfg["dataset"],
                                             urllib.parse.quote(groq))
    try:
        with urllib.request.urlopen(url, timeout=30) as r:
            data = json.loads(r.read().decode("utf-8"))
    except Exception as e:  # noqa: BLE001
        raise SystemExit("\nSTOP: could not read the blog from Sanity (%s).\n"
                         "Nothing was built. Check the internet connection and content/sanity.json.\n" % e)
    _CACHE[groq] = data.get("result") or []
    return _CACHE[groq]


# ---- images -----------------------------------------------------------------
def image_url(img):
    """Sanity image field -> CDN address (without size options)."""
    ref = ((img or {}).get("asset") or {}).get("_ref", "")
    m = re.match(r"image-([A-Za-z0-9]+)-(\d+x\d+)-(\w+)$", ref)
    if not m:
        return ""
    cfg = config()
    return "https://cdn.sanity.io/images/%s/%s/%s-%s.%s" % (
        cfg["projectId"], cfg["dataset"], m.group(1), m.group(2), m.group(3))


# ---- Portable Text (Sanity's rich text) -> HTML ----------------------------
def _esc(s):
    return _html.escape(s or "", quote=False)


def _span_html(span, defs):
    text = _esc(span.get("text", "")).replace("\n", "<br>")
    for mark in reversed(span.get("marks") or []):
        if mark == "strong":
            text = "<strong>" + text + "</strong>"
        elif mark == "em":
            text = "<em>" + text + "</em>"
        elif mark in defs and defs[mark].get("_type") == "link":
            href = _html.escape(defs[mark].get("href", ""), quote=True)
            ext = href.startswith("http") and "blueprint" not in href
            text = '<a href="%s"%s>%s</a>' % (href, ' target="_blank" rel="noopener"' if ext else "", text)
    return text


def portable_to_html(blocks):
    out, lst = [], None          # lst = (tag, items)

    def close():
        nonlocal lst
        if lst:
            out.append("<%s>%s</%s>" % (lst[0], "".join("<li>%s</li>" % i for i in lst[1]), lst[0]))
            lst = None

    for b in blocks or []:
        if b.get("_type") == "image":
            close()
            src = image_url(b)
            if src:
                alt = _html.escape(b.get("alt", "") or "", quote=True)
                out.append('<figure><img src="%s?w=1000&amp;fit=max&amp;auto=format&amp;q=80" alt="%s" loading="lazy" />'
                           '%s</figure>' % (src, alt, "<figcaption>%s</figcaption>" % _esc(b["caption"]) if b.get("caption") else ""))
            continue
        if b.get("_type") != "block":
            continue
        defs = {d.get("_key"): d for d in b.get("markDefs") or []}
        inner = "".join(_span_html(s, defs) for s in b.get("children") or []).strip()
        if b.get("listItem"):
            tag = "ol" if b["listItem"] == "number" else "ul"
            if not lst or lst[0] != tag:
                close()
                lst = (tag, [])
            lst[1].append(inner)
            continue
        close()
        if not inner:
            continue
        style = b.get("style") or "normal"
        if style in ("h2", "h3", "h4"):
            out.append("<%s>%s</%s>" % (style, inner, style))
        elif style == "blockquote":
            out.append("<blockquote>%s</blockquote>" % inner)
        elif style == "lead":
            out.append('<p class="lead">%s</p>' % inner)
        else:
            out.append("<p>%s</p>" % inner)
    close()
    return "\n".join(out)


def _words(blocks):
    n = 0
    for b in blocks or []:
        for s in b.get("children") or []:
            n += len((s.get("text") or "").split())
    return n


# ---- dates and reading time ---------------------------------------------------
def _date(s):
    try:
        return datetime.date.fromisoformat((s or "")[:10])
    except ValueError:
        return None


def date_en(d, long_month_first=True):
    if not d:
        return ""
    return ("%s %d, %d" % (d.strftime("%B"), d.day, d.year)) if long_month_first else \
           ("%d %s %d" % (d.day, d.strftime("%B"), d.year))


def date_ar(d):
    return "%d %s %d" % (d.day, MONTHS_AR[d.month - 1], d.year) if d else ""


def read_en(n):
    return "%d min read" % n


def read_ar(n):
    if n == 1:
        return "دقيقة للقراءة"
    if n == 2:
        return "دقيقتان للقراءة"
    if 3 <= n <= 10:
        return "%d دقائق للقراءة" % n
    return "%d دقيقة للقراءة" % n


# ---- the two content types ----------------------------------------------------
_POSTS = None
_JOBS = None


def posts():
    """Published blog posts, newest first, in the same shape as content.load_blog()."""
    global _POSTS
    if _POSTS is not None:
        return [dict(p) for p in _POSTS]
    rows = _query('*[_type == "post" && defined(slug.current) && !(_id in path("drafts.**"))]'
                  ' | order(publishedAt desc, _createdAt desc)')
    out = []
    for r in rows:
        d = _date(r.get("publishedAt"))
        cat = r.get("category") or "Insight"
        mins = r.get("readingMinutes") or max(1, round(_words(r.get("bodyEn")) / 200))
        img = image_url(r.get("coverImage")) or "assets/img/card-1.webp"
        cdn = img.startswith("https://")
        item = {
            "source": "sanity",
            "slug": r["slug"]["current"],
            "title": (r.get("titleEn") or "").strip(),
            "title_ar": (r.get("titleAr") or "").strip(),
            "summary": (r.get("summaryEn") or "").strip(),
            "summary_ar": (r.get("summaryAr") or "").strip(),
            "category": cat,
            "category_ar": CATEGORIES.get(cat, cat),
            "date": date_en(d),
            "date_ar": date_ar(d),
            "read": read_en(mins),
            "read_ar": read_ar(mins),
            "html": portable_to_html(r.get("bodyEn")),
            "html_ar": portable_to_html(r.get("bodyAr")),
            "action": "true" if r.get("actionRequired") else "",
            "img": img,
            # home page cards use the address as it is, so give them a sized version
            "image": img + "?w=720&h=480&fit=crop&auto=format&q=80" if cdn else img,
        }
        item["fb"], item["cat"], item["excerpt"] = item["img"], item["category"], item["summary"]
        if item["title"]:
            out.append(item)
    _POSTS = out
    return [dict(p) for p in out]


def vacancies():
    """Open vacancies, newest first, in the same shape as content.load_careers()."""
    global _JOBS
    if _JOBS is not None:
        return [dict(j) for j in _JOBS]
    rows = _query('*[_type == "vacancy" && defined(slug.current) && status != "closed"'
                  ' && !(_id in path("drafts.**"))] | order(datePosted desc, _createdAt desc)')
    out = []
    for r in rows:
        closing = _date(r.get("closingDate"))
        jt = r.get("employmentType") or "Full time"
        item = {
            "source": "sanity",
            "slug": r["slug"]["current"],
            "title": (r.get("titleEn") or "").strip(),
            "title_ar": (r.get("titleAr") or "").strip(),
            "department": (r.get("departmentEn") or "").strip(),
            "department_ar": (r.get("departmentAr") or "").strip(),
            "location": (r.get("locationEn") or "Riyadh, Saudi Arabia").strip(),
            "location_ar": (r.get("locationAr") or "الرياض، المملكة العربية السعودية").strip(),
            "type": jt,
            "type_ar": JOB_TYPES.get(jt, jt),
            "closing": date_en(closing, long_month_first=False),
            "closing_ar": date_ar(closing),
            "summary": (r.get("summaryEn") or "").strip(),
            "summary_ar": (r.get("summaryAr") or "").strip(),
            "html": portable_to_html(r.get("descriptionEn")),
            "html_ar": portable_to_html(r.get("descriptionAr")),
            "date": (r.get("datePosted") or "")[:10],
            "status": "open",
        }
        if item["title"]:
            out.append(item)
    _JOBS = out
    return [dict(j) for j in out]
