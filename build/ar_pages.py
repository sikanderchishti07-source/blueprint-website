# Arabic pages, built into site/ar/.
#
# Every English page now has an Arabic twin. The home page has its own
# builder (home_ar.py); About, Contact, Services, Laboratory and Careers use
# the maps in ar_text.py; everything else uses the large map in ar_text2.py.
# If an English page is added later without Arabic words, the build prints its
# untranslated lines, and links to it still work, falling back to English.

import re
import home_ar
import ar_i18n
import ar_text as T
import ar_text2 as T2

AR_FILES = []          # filled by setup(); kept for older callers
AR_PAGES = {}

_HOME_EXTRA = ("js/cards.js", "js/cover.js", "js/carousel.js")
_BRAND = "بلوبرنت للخدمات البيئية"

# glossary: the permit is ترخيص, never تصريح
_GLOSS = (("تصاريح", "تراخيص"), ("تصريح", "ترخيص"))


def _gloss(s):
    for a, b in _GLOSS:
        s = s.replace(a, b)
    return s


# phrases used only in page titles, not on the pages themselves
_TITLE_ONLY = {"Environmental Compliance Blog": "مدونة الالتزام البيئي"}
_ALL = None


def _all_text():
    """Every English-to-Arabic phrase the site has, from all the maps."""
    global _ALL
    if _ALL is None:
        _ALL = dict(home_ar.TEXT)
        for _t, _a, _r in T.PAGES.values():
            _ALL.update(dict(_t))
        _ALL.update(dict(T.COMMON_TEXT))
        _ALL.update(T2.TEXT)
        _ALL.update(_TITLE_ONLY)
    return _ALL


def _lookup(s):
    """English phrase to Arabic from any map, or None."""
    d = _all_text()
    for key in (s, s.replace("&", "&amp;"), " ".join(s.split())):
        if key in d:
            return d[key]
    return None


def _meta(fname, title_en, desc_en):
    if fname in T.META:
        return T.META[fname]
    parts = [p.strip() for p in title_en.split("|")]
    head = _lookup(parts[0]) or parts[0]
    extra = {"Careers": "الوظائف"}
    mid = [extra.get(p) for p in parts[1:-1] if extra.get(p)]
    title = " | ".join([head] + mid + [_BRAND])
    desc = _lookup(desc_en) or (head + "، " + _BRAND + "، استشارات بيئية معتمدة في المملكة العربية السعودية.")
    return title, re.sub(r"<[^>]+>", "", desc)


def _compliance_raw():
    import compliance as C
    raw = []
    for r in C.REGS:
        en = ('<h3>' + r["title_en"] + '</h3>'
              '<p class="cmp-ar" dir="rtl" lang="ar">' + r["title_ar"] + '</p>'
              '<p class="cmp-desc">' + r["summary_en"] + '</p>')
        ar = ('<h3>' + _gloss(r["title_ar"]) + '</h3>'
              '<p class="cmp-ar cmp-en-ref" dir="ltr" lang="en">' + r["title_en"] + '</p>'
              '<p class="cmp-desc">' + _gloss(r["summary_ar"]) + '</p>')
        raw.append((en, ar))
    raw.append(("count.textContent = shown + (shown === 1 ? ' regulation' : ' regulations');",
                "count.textContent = 'عدد الأنظمة: ' + shown;"))
    return raw


# WhatsApp buttons carry their pre-filled message in data-wa; translate it so
# an Arabic visitor sends an Arabic message.
_WA_FIXED = {
    "Hello BluePrint, I would like to ask about your environmental services.":
        "السلام عليكم، أود الاستفسار عن خدماتكم البيئية.",
    "Hello BluePrint, I would like to arrange a site visit.":
        "السلام عليكم، أود ترتيب زيارة للموقع.",
}
_WA_ASK = re.compile(r"^Hello BluePrint, I would like to ask about (.+?)\.?$")


def _data_wa(html, lookup):
    def fix(m):
        val = m.group(1)
        if val in _WA_FIXED:
            return 'data-wa="' + _WA_FIXED[val] + '"'
        a = _WA_ASK.match(val)
        if a:
            name = lookup.get(a.group(1))
            if name:
                return 'data-wa="السلام عليكم، أود الاستفسار عن خدمة ' + name + '."'
            return 'data-wa="' + _WA_FIXED["Hello BluePrint, I would like to ask about your environmental services."] + '"'
        if val in lookup:
            return 'data-wa="' + lookup[val] + '"'
        return m.group(0)
    return re.sub(r'data-wa="([^"]*[A-Za-z][^"]*)"', fix, html)


# A number followed by "+" (8+, 20+) flips to "+8" inside Arabic text unless it
# is isolated as left-to-right.
def _ltr_numbers(html):
    parts = re.split(r"(<script\b.*?</script>)", html, flags=re.S)
    for i in range(0, len(parts), 2):
        parts[i] = re.sub(r">(\s*)(\d[\d,.]*\+)(\s*)<",
                          lambda m: ">" + m.group(1) + '<bdi dir="ltr">' + m.group(2) + "</bdi>" + m.group(3) + "<",
                          parts[i])
    return "".join(parts)


def setup(PAGES):
    """Called by build.py once every English page is known."""
    AR_FILES[:] = list(PAGES)
    available = set(PAGES)
    AR_PAGES["index.html"] = (
        _BRAND + " | استشارات بيئية معتمدة في المملكة العربية السعودية",
        _BRAND + "، استشارات بيئية معتمدة في المملكة العربية السعودية: التراخيص البيئية، "
        "ودراسات تقييم الأثر البيئي، وتراخيص إدارة النفايات، والسجلات البيئية، والرصد البيئي.",
        home_ar.home(available), _HOME_EXTRA)
    # every map the site has, so a phrase translated for one page works on all
    common = dict(home_ar.TEXT)
    for _t, _a, _r in T.PAGES.values():
        common.update(dict(_t))
    common.update(dict(T.COMMON_TEXT))
    common_attr = dict(home_ar.ATTR)
    for _t, _a, _r in T.PAGES.values():
        common_attr.update(dict(_a))
    common_attr.update(dict(T.COMMON_ATTR))
    for f, (title_en, desc_en, body, extra) in PAGES.items():
        if f == "index.html":
            continue
        title, desc = _meta(f, title_en, desc_en)
        if f in T.PAGES:
            html = ar_i18n.build(f, body, T.PAGES[f], T.COMMON)
        else:
            raw = _compliance_raw() if f == "compliance.html" else ()
            text = dict(common); text.update(T2.TEXT)
            attr = dict(common_attr); attr.update(T2.ATTR)
            html = ar_i18n.build_map(f, body, text, attr, raw)
        AR_PAGES[f] = (title, desc, html, extra)
    lookup = dict(common); lookup.update(T2.TEXT)
    for f, (title, desc, html, extra) in list(AR_PAGES.items()):
        AR_PAGES[f] = (title, desc, _ltr_numbers(_data_wa(html, lookup)), extra)
