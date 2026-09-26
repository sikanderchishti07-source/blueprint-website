"""Branded "page not found" page (404) in English and Arabic.

Vercel shows site/404.html for any address that does not exist. That page can be
opened from any folder depth, so it carries <base href="/"> and its links work from
anywhere. Addresses under /ar/ are sent on to the Arabic version, ar/404.html.
"""

LINKS = {
    "en": [("service-environmental-permit.html", "fa-file-signature", "Environmental permit"),
           ("service-waste-management-permit.html", "fa-recycle", "MWAN waste permit"),
           ("service-air-quality-monitoring.html", "fa-smog", "Air quality monitoring"),
           ("compliance-finder.html", "fa-magnifying-glass", "Compliance Finder"),
           ("equipment.html", "fa-toolbox", "Equipment catalogue"),
           ("blog.html", "fa-newspaper", "Blog")],
    "ar": [("service-environmental-permit.html", "fa-file-signature", "الترخيص البيئي"),
           ("service-waste-management-permit.html", "fa-recycle", "ترخيص إدارة النفايات"),
           ("service-air-quality-monitoring.html", "fa-smog", "رصد جودة الهواء"),
           ("compliance-finder.html", "fa-magnifying-glass", "أداة تحديد المتطلبات"),
           ("equipment.html", "fa-toolbox", "كتالوج المعدات"),
           ("blog.html", "fa-newspaper", "المدونة")],
}

TEXT = {
    "en": dict(eb="Error 404", h1="We couldn't find that page",
               p="The link may be old, or the address may have a typo. Everything else is still here.",
               home="Back to home", services="Our services", contact="Contact us",
               popular="Popular pages", title="Page not found | BluePrint",
               desc="The page you were looking for could not be found."),
    "ar": dict(eb="خطأ 404", h1="لم نتمكن من العثور على هذه الصفحة",
               p="ربما يكون الرابط قديماً أو أن في العنوان خطأ مطبعياً. بقية الموقع متاحة كما هي.",
               home="العودة إلى الرئيسية", services="خدماتنا", contact="تواصل معنا",
               popular="صفحات يكثر زيارتها", title="الصفحة غير موجودة | بلوبرنت",
               desc="تعذر العثور على الصفحة التي تبحث عنها."),
}


def body(lang):
    t = TEXT[lang]
    arrow = "fa-arrow-right"  # rtl.css turns it round on Arabic pages
    links = "".join(
        f'<li><a href="{href}"><i class="fas {icon}" aria-hidden="true"></i><span>{name}</span>'
        f'<i class="fas {arrow} nf-go" aria-hidden="true"></i></a></li>' for href, icon, name in LINKS[lang])
    return f"""
<section class="nf-sec">
  <div class="nf-in">
    <p class="nf-eb">{t["eb"]}</p>
    <div class="nf-num" aria-hidden="true">404</div>
    <h1>{t["h1"]}</h1>
    <p class="nf-p">{t["p"]}</p>
    <div class="nf-ctas">
      <a class="nf-c1" href="index.html">{t["home"]}</a>
      <a class="nf-c2" href="services.html">{t["services"]}</a>
      <a class="nf-c2" href="contact.html">{t["contact"]}</a>
    </div>
    <h2 class="nf-h2">{t["popular"]}</h2>
    <ul class="nf-links">{links}</ul>
  </div>
</section>
"""


def finish(html, lang):
    """Make the page work from any address and keep it out of search results."""
    base = "/ar/" if lang == "ar" else "/"
    extra = f'<base href="{base}" />\n  <meta name="robots" content="noindex" />'
    if lang == "en":
        extra += ('\n  <script>if(/^\\/ar\\//.test(location.pathname)&&!/\\/ar\\/404\\.html$/.test(location.pathname))'
                  'location.replace("/ar/404.html")</script>')
    return html.replace("<head>", "<head>\n  " + extra, 1)
