"""Search-engine files and structured data.

- sitemap.xml: every page in both languages, with language pairs linked (hreflang).
- robots.txt: lets search engines in, keeps them out of /admin/, points to the sitemap.
- JSON-LD (structured data) in each page's <head>: the business on the home and contact
  pages, an article on each blog post, a service on each service page, and a breadcrumb.
Everything follows partials.SITE_URL, so moving to a new domain is still one line.
"""
import json, os, re
from datetime import datetime
import partials as P

NAME = {"en": "BluePrint Environmental Services", "ar": "بلوبرنت للخدمات البيئية"}
HOME = {"en": "Home", "ar": "الرئيسية"}
SERVICES = {"en": "Services", "ar": "الخدمات"}
BLOG = {"en": "Blog", "ar": "المدونة"}

# Contact details come from site/js/config.js so they are never typed twice.
def _config():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "site", "js", "config.js")
    txt = open(path, encoding="utf-8").read()
    get = lambda k: (re.search(k + r"\s*:\s*'([^']*)'", txt) or [None, ""])[1]
    return {"phone": get("PHONE_TEL"), "email": get("EMAIL"), "address": get("ADDRESS_LINE1")}


def _clean_title(title):
    return re.split(r"\s+\|\s+", title)[0].strip()


def _business(lang):
    c = _config()
    return {
        "@type": "ProfessionalService",
        "@id": P.SITE_URL + "/#business",
        "name": NAME[lang],
        "alternateName": NAME["ar" if lang == "en" else "en"],
        "url": P.SITE_URL + ("/ar/" if lang == "ar" else "/"),
        "logo": P.SITE_URL + "/assets/logo/blueprint-logo.png",
        "image": P.SITE_URL + "/assets/og/index.jpg",
        "email": c["email"],
        "telephone": c["phone"],
        "address": {
            "@type": "PostalAddress",
            "streetAddress": "3704 Abi Jafar Al Mansur, Al Yarmouk District",
            "addressLocality": "Riyadh",
            "postalCode": "13251-7669",
            "addressCountry": "SA",
        },
        "areaServed": {"@type": "Country", "name": "Saudi Arabia"},
        "openingHoursSpecification": {
            "@type": "OpeningHoursSpecification",
            "dayOfWeek": ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"],
            "opens": "09:00", "closes": "18:00",
        },
        "sameAs": [
            "https://www.linkedin.com/company/alemad-alarabi/",
            "https://x.com/blueprint_env",
            "https://www.instagram.com/blueprint_env",
        ],
    }


def _crumbs(lang, page, title):
    home = P.SITE_URL + ("/ar/" if lang == "ar" else "/")
    items = [(HOME[lang], home)]
    if page.startswith("service-"):
        items.append((SERVICES[lang], P._url(lang, "services.html")))
    elif page.startswith("blog-"):
        items.append((BLOG[lang], P._url(lang, "blog.html")))
    items.append((_clean_title(title), P._url(lang, page)))
    return {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": u} for i, (n, u) in enumerate(items)]}


def _date(s):
    for fmt in ("%B %d, %Y", "%b %d, %Y", "%Y-%m-%d", "%d %B %Y"):
        try:
            return datetime.strptime(str(s).strip(), fmt).strftime("%Y-%m-%d")
        except ValueError:
            pass
    return None


def schema(lang, page, title, description, blog=None):
    if page == "404.html":
        return ""
    graph = []
    if page in ("index.html", "contact.html", "about.html"):
        graph.append(_business(lang))
    if page.startswith("service-"):
        graph.append({"@type": "Service", "name": _clean_title(title), "description": description,
                      "serviceType": _clean_title(title), "areaServed": {"@type": "Country", "name": "Saudi Arabia"},
                      "provider": {"@type": "ProfessionalService", "@id": P.SITE_URL + "/#business", "name": NAME[lang]},
                      "url": P._url(lang, page)})
    if page.startswith("blog-"):
        art = {"@type": "BlogPosting", "headline": _clean_title(title)[:110], "description": description,
               "url": P._url(lang, page), "inLanguage": lang,
               "image": P.SITE_URL + "/assets/og/" + (page[:-5] + ".jpg"),
               "author": {"@type": "Organization", "name": NAME[lang], "url": P.SITE_URL + "/"},
               "publisher": {"@type": "Organization", "name": NAME[lang],
                             "logo": {"@type": "ImageObject", "url": P.SITE_URL + "/assets/logo/blueprint-logo.png"}}}
        d = _date((blog or {}).get(page[5:-5], {}).get("date", ""))
        if d:
            art["datePublished"] = d
        graph.append(art)
    if page != "index.html":
        graph.append(_crumbs(lang, page, title))
    if not graph:
        return ""
    data = {"@context": "https://schema.org", "@graph": graph}
    js = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    return '\n  <script type="application/ld+json">' + js + "</script>\n"


def add_schema(html, lang, page, title, description, blog=None):
    return html.replace("</head>", schema(lang, page, title, description, blog) + "</head>", 1)


def write_files(out_dir, en_pages, ar_pages):
    """sitemap.xml and robots.txt in the site root."""
    skip = {"404.html"}
    rows = []
    for lang, pages in (("en", en_pages), ("ar", ar_pages)):
        for page in sorted(pages):
            if page in skip:
                continue
            u = P._url(lang, page)
            alt = ""
            if page in ar_pages and page in en_pages:
                alt = ('\n    <xhtml:link rel="alternate" hreflang="en" href="%s"/>'
                       '\n    <xhtml:link rel="alternate" hreflang="ar" href="%s"/>'
                       '\n    <xhtml:link rel="alternate" hreflang="x-default" href="%s"/>'
                       % (P._url("en", page), P._url("ar", page), P._url("en", page)))
            rows.append("  <url>\n    <loc>%s</loc>%s\n  </url>" % (u, alt))
    xml = ('<?xml version="1.0" encoding="UTF-8"?>\n'
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
           'xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' + "\n".join(rows) + "\n</urlset>\n")
    robots = ("User-agent: *\nAllow: /\nDisallow: /admin/\n\nSitemap: " + P.SITE_URL + "/sitemap.xml\n")
    for name, data in (("sitemap.xml", xml), ("robots.txt", robots)):
        path = os.path.join(out_dir, name)
        old = open(path, encoding="utf-8").read() if os.path.exists(path) else None
        if old != data:
            with open(path, "w", encoding="utf-8", newline="\n") as f:
                f.write(data)


def short_title(title, limit=65):
    """Search results cut titles at about 60 characters. When a title is too long,
    use the short brand name so the page's own words stay visible."""
    if len(title) <= limit:
        return title
    for long, short in ((" | BluePrint Environmental Services", " | BluePrint"),
                        (" | بلوبرنت للخدمات البيئية", " | بلوبرنت")):
        if title.endswith(long):
            return title[: -len(long)] + short
    return title
