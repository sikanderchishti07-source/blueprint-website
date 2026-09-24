# Arabic pages, built into site/ar/.
#
# AR_FILES lists the pages that have an Arabic version. A link to any page not
# listed falls back to its English version, so nothing is ever a dead link.
# To add a page: write its word map in ar_text.py, then list it here.

import home_ar
import ar_i18n
import ar_text as T

AR_FILES = ["index.html", "about.html", "contact.html", "services.html",
            "technology.html", "careers.html"]

AR_PAGES = {}

_HOME_EXTRA = ("js/cards.js", "js/cover.js", "js/carousel.js")


def setup(PAGES):
    """Called by build.py once every English page is known."""
    available = set(AR_FILES)
    AR_PAGES["index.html"] = (
        "بلوبرنت للخدمات البيئية | استشارات بيئية معتمدة في المملكة العربية السعودية",
        "بلوبرنت للخدمات البيئية، استشارات بيئية معتمدة في المملكة العربية السعودية: "
        "التراخيص البيئية، ودراسات تقييم الأثر البيئي، وتراخيص إدارة النفايات، "
        "والسجلات البيئية، والرصد البيئي.",
        home_ar.home(available), _HOME_EXTRA)
    for f in AR_FILES:
        if f == "index.html":
            continue
        if f not in PAGES or f not in T.PAGES:
            print("  [ar_pages] skipped %s: no English page or no word map" % f)
            continue
        _t, _d, body, extra = PAGES[f]
        title, desc = T.META[f]
        AR_PAGES[f] = (title, desc, ar_i18n.build(f, body, T.PAGES[f], T.COMMON), extra)
