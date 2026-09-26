# Compliance Finder: page body, promo block and the Arabic text they need.
# The questions, rules and results live in site/js/finder.js (both languages).

TITLE = "Which permits apply to you?"
SUB = ("Three quick questions, and you will see the permits, studies and monitoring a facility "
       "like yours is normally asked for. It takes under a minute.")
PROMO_H = "Not sure which permits apply?"
PROMO_P = "Answer three quick questions and see what a facility like yours is normally asked for."
PROMO_B = "Try the Compliance Finder"


def page(page_header):
    return page_header(TITLE, SUB, "Compliance Finder") + """
<section class="cf-sec">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="cf-box" id="cfWrap" aria-live="polite"></div>
    <noscript><p class="cf-note">The Compliance Finder needs JavaScript. You can also <a href="contact.html">contact us</a> directly.</p></noscript>
  </div>
</section>
"""


def promo(bg="#fff"):
    return f"""
<section class="cf-promo-sec" style="background:{bg};">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="cf-promo scroll-reveal">
      <div><h3>{PROMO_H}</h3><p>{PROMO_P}</p></div>
      <a class="cf-go" href="compliance-finder.html">{PROMO_B} <i class="fas fa-arrow-right"></i></a>
    </div>
  </div>
</section>
"""


AR_TEXT = {
    TITLE: "ما التراخيص التي تنطبق عليك؟",
    SUB: "ثلاثة أسئلة سريعة تعرض لك التراخيص والدراسات وأعمال الرصد التي تُطلب عادةً من منشأة مثل منشأتك. تستغرق أقل من دقيقة.",
    "Compliance Finder": "أداة تحديد المتطلبات",
    PROMO_H: "لست متأكداً من التراخيص التي تنطبق عليك؟",
    PROMO_P: "أجب عن ثلاثة أسئلة سريعة لترى ما يُطلب عادةً من منشأة مثل منشأتك.",
    PROMO_B: "جرّب أداة تحديد المتطلبات",
    "The Compliance Finder needs JavaScript. You can also": "تحتاج هذه الأداة إلى تفعيل جافاسكربت في المتصفح. ويمكنك أيضاً",
    "contact us": "التواصل معنا",
    "directly.": "مباشرةً.",
}
META_AR = ("أداة تحديد المتطلبات البيئية | بلوبرنت",
           "أجب عن ثلاثة أسئلة لتعرف التراخيص والدراسات وأعمال الرصد البيئي التي تُطلب عادةً من منشأتك في المملكة العربية السعودية.")

PROMO_AR = {k: AR_TEXT[k] for k in (PROMO_H, PROMO_P, PROMO_B)}
