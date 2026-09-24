# Arabic pages, built into site/ar/.
#
# AR_FILES lists the pages that have an Arabic version. Each must match the
# English file name it translates, so the language button can pair them.
# A link to a page not listed here falls back to the English page.

AR_FILES = ["index.html"]

import home_ar

AR_PAGES = {
    "index.html": (
        "بلوبرنت للخدمات البيئية | استشارات بيئية معتمدة في المملكة العربية السعودية",
        "بلوبرنت للخدمات البيئية، استشارات بيئية معتمدة في المملكة العربية السعودية: "
        "التراخيص البيئية، ودراسات تقييم الأثر البيئي، وتراخيص إدارة النفايات، "
        "والسجلات البيئية، والرصد البيئي.",
        home_ar.home(set(AR_FILES)),
        ("js/cards.js", "js/cover.js", "js/carousel.js"),
    ),
}
