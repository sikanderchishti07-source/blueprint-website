# Arabic pages, built into site/ar/.
#
# Each entry: file name -> (title, meta description, body HTML, extra scripts).
# The file name must match the English page it translates, so the language
# button can pair them. Add a page here once its Arabic body is written;
# until then, Arabic links to it fall back to the English page.

from arabic_home import BODY as HOME_BODY

AR_PAGES = {
    "index.html": (
        "بلوبرنت للخدمات البيئية | استشارات بيئية معتمدة في المملكة العربية السعودية",
        "بلوبرنت للخدمات البيئية، استشارات بيئية معتمدة في المملكة العربية السعودية: "
        "التراخيص البيئية، ودراسات تقييم الأثر البيئي، وتراخيص إدارة النفايات، "
        "والسجلات البيئية، والرصد البيئي.",
        HOME_BODY,
        ("js/cards-ar.js", "js/cards.js"),
    ),
}
