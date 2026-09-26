def _has_roles():
    """Careers only appears in the menus when a vacancy is actually open."""
    return True
    try:
        import content
        return bool(content.load_careers())
    except Exception:
        return False

# Shared HTML partials for the BluePrint site build.
#
# Every partial takes lang="en" or lang="ar". The markup is written once;
# only the words differ, and they come from STR below. Arabic wording follows
# the terminology glossary approved by the client. Change a word here and it
# changes on every page of that language.
#
# AR_AVAILABLE is set by build.py to the file names that have an Arabic
# version. The language button on an English page goes to that page's Arabic
# twin when one exists, otherwise to the Arabic home page.

AR_AVAILABLE = set()


STR = {
 "en": {
  "html_attrs": 'lang="en"',
  "menu": "Mobile menu", "close_menu": "Close menu", "menu_btn": "Menu",
  "tag": "Environmental Services", "home_aria": "BluePrint, home", "top_aria": "BluePrint, back to top",
  "sec_company": "Company", "home": "Home", "overview": "Company Overview",
  "sectors": "Sectors We Serve", "process": "Our Process",
  "sec_permit": "Compliance &amp; Permitting", "sec_monitor": "Monitoring &amp; Testing",
  "sec_lab": "Laboratory", "lab_services": "Laboratory Services",
  "licences": "Licences &amp; Accreditations",
  "blog": "Blog", "careers": "Careers", "contact": "Contact",
  "lang_drawer": "العربية (Arabic)", "lang_btn": "العربية", "lang_short": "العربية",
  "free": "Free Consultation", "wa_us": "WhatsApp Us",
  "wa_msg": "Hello BluePrint, I would like to ask about your environmental services.",
  "primary": "Primary",
  "about_bp": "About BluePrint", "about_sub": "Who we are &amp; how we work",
  "sectors_sub": "Six regulated industries", "how": "How We Work",
  "how_sub": "Assess, plan, submit, sustain",
  "about": "About", "technology": "Technology", "instrumentation": "Instrumentation",
  "equip": "Equipment Catalogue", "equip_sub": "Instrument types by domain",
  "compliance": "Compliance", "hub": "Compliance Hub", "hub_sub": "Saudi regulations, searchable",
  "finder": "Compliance Finder", "finder_sub": "Which permits apply to you",
  "services": "Services", "view_all": "View All →", "see_all": "See all →",
  "measurement": "Measurement", "lab_sub": "Sampling, testing &amp; monitoring",
  "credentials": "Credentials", "licences_sub": "NCEC, MWAN, RCJY, IAS &amp; ISO",
  # footer
  "start": "Start Your Project", "ready": "Ready to make compliance the easy part?",
  "book": "Book a consultation",
  "brand_desc": "Accredited environmental consultancy delivering compliance, permitting, and reporting across the Kingdom of Saudi Arabia.",
  "f_overview": "Overview", "f_lab": "Laboratory", "f_process": "Our Process", "f_sectors": "Sectors",
  "f_permitting": "Permitting",
  "f_p0": "Environmental Permit", "f_p1": "Impact Assessment", "f_p2": "Permitting (MWAN)",
  "f_p3": "Management Plans", "f_p4": "Environmental Registers", "f_p5": "Periodic Reporting",
  "f_monitoring": "Monitoring",
  "f_m0": "Air Quality", "f_m1": "Water &amp; Wastewater", "f_m2": "Noise",
  "f_m3": "Soil &amp; Sediment", "f_m4": "Sampling", "f_m5": "Laboratory Analysis",
  "f_resources": "Resources", "f_briefing": "Compliance Briefing", "f_guide": "Permitting Guide",
  "f_accred": "Accreditations",
  "f_location": "Location", "f_email": "Email", "f_phone": "Phone", "f_wa": "WhatsApp",
  "f_hours": "Working hours", "f_hours_v": "Sun &ndash; Thu &middot; 9:00 &ndash; 18:00 AST",
  "address": '<div class="footer-contact-value" data-text="address"></div>',
  "copy": "BluePrint Environmental Services. All rights reserved.",
  "credit": 'Prepared by: <span>Sikander Chishti</span>, Environmental Engineer',
  "privacy": "Privacy Policy", "terms": "Terms &amp; Conditions",
  "lang_footer": "🌐 العربية",
  # widgets
  "wa_title": "Chat with us on WhatsApp", "wa_aria": "Chat on WhatsApp",
  "expert_aria": "Speak to an expert", "ask": "Ask an Expert", "free_arrow": "Free Consultation →",
  "ep_name": "Environmental Specialist",
  "ep_role": "Accredited environmental consultant &middot; Riyadh",
  "ep_status": "Riyadh &middot; Sun&ndash;Thu", "close": "Close",
  "ep_q": "Have a question?",
  "ep_hint": "Send us your question and we will come back to you during business hours.",
  "ep_wa_msg": "Hello BluePrint, I have a compliance question",
  "ep_wa": "WhatsApp us", "ep_mail": "Email us directly", "ep_call": "Call",
  "ep_or": "or send a quick message",
  "ep_ph": "e.g. which permit does my workshop need?", "ep_quick": "Quick message", "send": "Send",
  "ep_foot": "Free consultation · No commitment required",
 },
 "ar": {
  "html_attrs": 'lang="ar" dir="rtl"',
  "menu": "القائمة", "close_menu": "إغلاق القائمة", "menu_btn": "القائمة",
  "tag": "Environmental Services", "home_aria": "بلوبرنت، الرئيسية", "top_aria": "بلوبرنت، العودة إلى الأعلى",
  "sec_company": "الشركة", "home": "الرئيسية", "overview": "نبذة عن الشركة",
  "sectors": "القطاعات التي نخدمها", "process": "آلية العمل",
  "sec_permit": "الالتزام البيئي والتراخيص", "sec_monitor": "الرصد والفحص",
  "sec_lab": "المختبر", "lab_services": "خدمات المختبر",
  "licences": "التراخيص والاعتمادات",
  "blog": "المدونة", "careers": "الوظائف", "contact": "تواصل معنا",
  "lang_drawer": "English (الإنجليزية)", "lang_btn": "English", "lang_short": "English",
  "free": "استشارة مجانية", "wa_us": "تواصل عبر واتساب",
  "wa_msg": "السلام عليكم، أود الاستفسار عن خدماتكم البيئية.",
  "primary": "القائمة الرئيسية",
  "about_bp": "عن بلوبرنت", "about_sub": "من نحن وكيف نعمل",
  "sectors_sub": "ستة قطاعات خاضعة للتنظيم", "how": "آلية العمل",
  "how_sub": "التقييم، التخطيط، التقديم، الاستدامة",
  "about": "من نحن", "technology": "التقنية", "instrumentation": "الأجهزة",
  "equip": "دليل الأجهزة", "equip_sub": "أنواع الأجهزة حسب المجال",
  "compliance": "الالتزام البيئي", "hub": "مركز الالتزام", "hub_sub": "الأنظمة السعودية مع البحث",
  "finder": "أداة تحديد المتطلبات", "finder_sub": "ما التراخيص التي تنطبق عليك",
  "services": "الخدمات", "view_all": "عرض الكل ←", "see_all": "عرض الكل ←",
  "measurement": "القياس", "lab_sub": "أخذ العينات والفحص والرصد",
  "credentials": "الاعتمادات", "licences_sub": "NCEC وMWAN وRCJY وIAS وISO",
  # footer
  "start": "ابدأ مشروعك", "ready": "هل أنت مستعد لجعل الالتزام البيئي الجزء الأسهل؟",
  "book": "احجز استشارة",
  "brand_desc": "استشارات بيئية معتمدة تقدّم خدمات الالتزام البيئي والتراخيص والتقارير في أنحاء المملكة العربية السعودية.",
  "f_overview": "نبذة عامة", "f_lab": "المختبر", "f_process": "آلية العمل", "f_sectors": "القطاعات",
  "f_permitting": "التراخيص",
  "f_p0": "الترخيص البيئي", "f_p1": "دراسة تقييم الأثر البيئي", "f_p2": "ترخيص إدارة النفايات",
  "f_p3": "خطط الإدارة البيئية", "f_p4": "السجل البيئي", "f_p5": "التقرير البيئي الدوري",
  "f_monitoring": "الرصد",
  "f_m0": "جودة الهواء", "f_m1": "المياه ومياه الصرف", "f_m2": "الضوضاء",
  "f_m3": "التربة والرواسب", "f_m4": "أخذ العينات", "f_m5": "التحليل المختبري",
  "f_resources": "الموارد", "f_briefing": "الموجز التنظيمي", "f_guide": "دليل التراخيص",
  "f_accred": "الاعتمادات",
  "f_location": "الموقع", "f_email": "البريد الإلكتروني", "f_phone": "الهاتف", "f_wa": "واتساب",
  "f_hours": "ساعات العمل", "f_hours_v": "الأحد &ndash; الخميس &middot; 9:00 &ndash; 18:00",
  "address": '<div class="footer-contact-value">3704 أبي جعفر المنصور، حي اليرموك، الرياض <span dir="ltr">13251-7669</span>، المملكة العربية السعودية</div>',
  "copy": "بلوبرنت للخدمات البيئية. جميع الحقوق محفوظة.",
  "credit": 'إعداد: <span>Sikander Chishti</span>، مهندس بيئي',
  "privacy": "سياسة الخصوصية", "terms": "الشروط والأحكام",
  "lang_footer": "🌐 English",
  # widgets
  "wa_title": "تحدث معنا عبر واتساب", "wa_aria": "واتساب",
  "expert_aria": "تحدث مع خبير", "ask": "اسأل خبيراً", "free_arrow": "استشارة مجانية ←",
  "ep_name": "أخصائي بيئي",
  "ep_role": "مستشار بيئي معتمد &middot; الرياض",
  "ep_status": "الرياض &middot; الأحد&ndash;الخميس", "close": "إغلاق",
  "ep_q": "لديك سؤال؟",
  "ep_hint": "أرسل سؤالك وسنعود إليك خلال ساعات العمل.",
  "ep_wa_msg": "السلام عليكم، لدي سؤال عن الالتزام البيئي",
  "ep_wa": "راسلنا عبر واتساب", "ep_mail": "راسلنا عبر البريد", "ep_call": "اتصل على",
  "ep_or": "أو أرسل رسالة سريعة",
  "ep_ph": "مثال: ما الترخيص الذي تحتاجه منشأتي؟", "ep_quick": "رسالة سريعة", "send": "إرسال",
  "ep_foot": "استشارة مجانية · دون أي التزام",
 },
}


def _lang_href(lang, page):
    """Where the language button points from this page."""
    page = page or "index.html"
    if lang == "ar":
        return "../" + page
    return "ar/" + (page if page in AR_AVAILABLE else "index.html")


# ---- link previews, icons and language links -------------------------------
# The site's public address. Change this one line when the site moves to its
# own domain: preview links, canonical addresses and language links follow.
SITE_URL = "https://blueprint-website-wheat.vercel.app"

import os as _os
_OG_DIR = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "..", "site", "assets", "og")


def _q(s):
    return str(s).replace('"', "&quot;")


def _url(lang, page):
    path = "" if page == "index.html" else page
    return SITE_URL + ("/ar/" if lang == "ar" else "/") + path


def _alternates(lang, page):
    """hreflang links, only when the page exists in both languages."""
    if lang == "en" and page not in AR_AVAILABLE:
        return ""
    return (f'\n  <link rel="alternate" hreflang="en" href="{_url("en", page)}" />'
            f'\n  <link rel="alternate" hreflang="ar" href="{_url("ar", page)}" />'
            f'\n  <link rel="alternate" hreflang="x-default" href="{_url("en", page)}" />')


def _head_meta(title, description, lang, page):
    stem = page[:-5]
    img = stem + ".jpg" if _os.path.exists(_os.path.join(_OG_DIR, stem + ".jpg")) else "default.jpg"
    img_url = SITE_URL + "/assets/og/" + img
    ar = lang == "ar"
    site = "بلوبرنت للخدمات البيئية" if ar else "BluePrint Environmental Services"
    locale, other = ("ar_SA", "en_US") if ar else ("en_US", "ar_SA")
    twin = ar or page in AR_AVAILABLE
    kind = "article" if page.startswith("blog-") else "website"
    t, d, u = _q(title), _q(description), _url(lang, page)
    alt_locale = f'\n  <meta property="og:locale:alternate" content="{other}" />' if twin else ""
    return f"""
  <link rel="icon" href="/favicon.ico" sizes="48x48" />
  <link rel="icon" type="image/png" sizes="32x32" href="/assets/icons/favicon-32.png" />
  <link rel="apple-touch-icon" href="/assets/icons/apple-touch-icon.png" />
  <link rel="manifest" href="/site.webmanifest" />
  <link rel="canonical" href="{u}" />

  <!-- Link previews (WhatsApp, LinkedIn, X, iMessage) -->
  <meta property="og:type" content="{kind}" />
  <meta property="og:site_name" content="{site}" />
  <meta property="og:title" content="{t}" />
  <meta property="og:description" content="{d}" />
  <meta property="og:url" content="{u}" />
  <meta property="og:image" content="{img_url}" />
  <meta property="og:image:width" content="1200" />
  <meta property="og:image:height" content="630" />
  <meta property="og:image:alt" content="{t}" />
  <meta property="og:locale" content="{locale}" />{alt_locale}
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="{t}" />
  <meta name="twitter:description" content="{d}" />
  <meta name="twitter:image" content="{img_url}" />"""


import preloader as PL

def head(title, description, extra_css="", lang="en", page=None):
    s = STR[lang]
    page = page or "index.html"
    if lang == "ar":
        fonts = ('<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Arabic:wght@300;400;500;600;700'
                 '&family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Inter:wght@300;400;500;600&family=DM+Sans:wght@300;400;500;600'
                 '&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet" />')
        rtl = '\n  <link rel="stylesheet" href="css/rtl.css" />'
        alt = _alternates(lang, page)
    else:
        fonts = ('<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Inter:wght@300;400;500;600'
                 '&family=DM+Sans:wght@300;400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet" />')
        rtl = ""
        alt = _alternates(lang, page)
    return f"""<!DOCTYPE html>
<!--
  ============================================================
  GENERATED FILE, DO NOT EDIT THIS HTML BY HAND.

  This page is assembled by build/build.py from:
      build/partials.py   (nav, footer, modals, widgets)
      build/pages.py      (this page's content)

  Any change made directly to this file will be ERASED the next
  time someone runs build/build.sh. Edit the Python source above
  and rebuild instead.

  Safe to edit by hand: everything in site/css/ and site/js/
  (except site/css/tailwind.css, which is also generated).
  ============================================================
-->
<html {s["html_attrs"]}>
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="description" content="{description}" />
  <meta name="theme-color" content="#0e93a8" />
  <title>{title}</title>
{_head_meta(title, description, lang, page)}{alt}

  <!-- Fonts & icons -->
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  {fonts}
  <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet" />

  <!-- Site styles (css/tailwind.css is compiled by build/build.sh) -->
  <link rel="stylesheet" href="css/tailwind.css" />
  <link rel="stylesheet" href="css/base.css" />
  <link rel="stylesheet" href="css/layout.css" />
  <link rel="stylesheet" href="css/components.css" />
  <link rel="stylesheet" href="css/pages.css" />
  <link rel="stylesheet" href="css/cover.css" />
  <link rel="stylesheet" href="css/carousel.css" />
  <link rel="stylesheet" href="css/insights.css" />{extra_css}{rtl}

  <script src="js/config.js"></script>
{PL.HEAD}</head>
<body class="font-sans{'' if page in ('index.html', 'ar/index.html') else ' bp-inner'}">
{PL.body(lang)}"""


# (icon, English label, English sub, page, Arabic label, Arabic sub)
SERVICES_NAV = [
    ("fa-file-signature", "Environmental Permit", "NCEC permit file to issuance", "service-environmental-permit.html",
     "الترخيص البيئي", "ملف الترخيص حتى الإصدار"),
    ("fa-clipboard-check", "Impact Assessment", "EIA/ESIA for regulated projects", "service-environmental-impact-assessment.html",
     "دراسة تقييم الأثر البيئي", "للمشاريع الخاضعة للتنظيم"),
    ("fa-recycle", "Waste Permit (MWAN)", "Generators, carriers &amp; treaters", "service-waste-management-permit.html",
     "ترخيص إدارة النفايات", "للمنتجين والناقلين والمعالجين"),
    ("fa-tasks", "Environmental Management Plan", "Permit conditions into practice", "service-environmental-management-plan.html",
     "خطة الإدارة البيئية", "اشتراطات الترخيص في الممارسة اليومية"),
    ("fa-folder-open", "Environmental Register", "Continuous proof of compliance", "service-environmental-register.html",
     "السجل البيئي", "إثبات مستمر للالتزام"),
    ("fa-calendar-check", "Periodic Reporting", "Filed on time, every cycle", "service-periodic-environmental-report.html",
     "التقرير البيئي الدوري", "يُقدَّم في موعده كل دورة"),
]


def dd_link(href, icon, label, sub, extra_icon_style="", badge=""):
    return f"""<a href="{href}" class="nav-dd-link">
                  <div class="nav-dd-icon"{extra_icon_style}><i class="fas {icon}"></i></div>
                  <div class="nav-dd-text-wrap"><span class="nav-dd-label">{label}{badge}</span><span class="nav-dd-sub">{sub}</span></div>
                </a>"""


LIVE_BADGE = '<span style="font-size:.55rem;padding:1px 6px;background:#dcfce7;color:#15803d;border-radius:999px;font-weight:700;letter-spacing:.06em;margin-left:3px;">LIVE</span>'


MONITORING_NAV = [
    ("fa-wind", "Air Quality Monitoring", "Measurement &amp; assessment", "service-air-quality-monitoring.html",
     "رصد جودة الهواء", "القياس والتقييم"),
    ("fa-tint", "Water &amp; Wastewater Testing", "Accredited analysis", "service-water-wastewater-testing.html",
     "فحص المياه ومياه الصرف", "تحليل معتمد"),
    ("fa-volume-up", "Noise Monitoring", "Against regulated limits", "service-noise-monitoring.html",
     "رصد الضوضاء", "مقارنةً بالحدود النظامية"),
    ("fa-mountain", "Soil &amp; Sediment Testing", "Contaminant levels", "service-soil-sediment-testing.html",
     "فحص التربة والرواسب", "مستويات الملوثات"),
    ("fa-vial", "Environmental Sampling", "Chain-of-custody protocols", "service-environmental-sampling.html",
     "أخذ العينات البيئية", "وفق بروتوكولات سلسلة الحيازة"),
    ("fa-microscope", "Laboratory Analysis", "With technical interpretation", "service-laboratory-analysis.html",
     "التحليل المختبري", "مع تفسير فني للنتائج"),
]

# the four monitoring links the drawer shows, in drawer order
_DRAWER_MON = [("fa-wind", 0), ("fa-tint", 1), ("fa-volume-up", 2), ("fa-mountain", 3)]


def _pick(row, lang):
    ic, en_l, en_s, pg, ar_l, ar_s = row
    return (ic, ar_l, ar_s, pg) if lang == "ar" else (ic, en_l, en_s, pg)


def _lockup(s):
    return ('<span class="bp-lock"><span class="bp-mark"><img class="bp-b" src="assets/logo/blueprint-b.png" alt="" />'
            '<img class="bp-wave" src="assets/logo/blueprint-wave.png" alt="" /></span><span class="bp-txt">'
            '<img class="bp-word" src="assets/logo/blueprint-wordmark.png" alt="BluePrint" />'
            f'<span class="bp-tag">{s["tag"]}</span></span></span>')


def nav(lang="en", page=None):
    s = STR[lang]
    lh = _lang_href(lang, page)
    svc = [_pick(r, lang) for r in SERVICES_NAV]
    mon = [_pick(r, lang) for r in MONITORING_NAV]
    svc_links = "\n".join(dd_link(pg, ic, lb, sb) for ic, lb, sb, pg in svc)
    mon_links = "\n".join(dd_link(pg, ic, lb, sb) for ic, lb, sb, pg in mon)
    drawer_svc = "\n".join(
        f'<a href="{pg}" class="drawer-link"><div class="drawer-link-icon"><i class="fas {ic}"></i></div>{lb}</a>'
        for ic, lb, sb, pg in svc)
    drawer_mon = "\n    ".join(
        f'<a href="services.html#monitoring" class="drawer-link"><div class="drawer-link-icon"><i class="fas {ic}"></i></div>{mon[i][1]}</a>'
        for ic, i in _DRAWER_MON)
    careers_d = (f'<a href="careers.html" class="drawer-link"><div class="drawer-link-icon"><i class="fas fa-user-plus"></i></div>{s["careers"]}</a>'
                 if _has_roles() else "")
    careers_n = (f'<div class="nav-item"><a href="careers.html" class="nav-link" data-page="careers.html">{s["careers"]}</a></div>'
                 if _has_roles() else "")
    lock = _lockup(s)
    return f"""
<!-- ============================================================
     NAVIGATION
     ============================================================ -->
<div id="navDrawerOverlay" onclick="closeNavDrawer()"></div>

<div id="navMobileDrawer" aria-label="{s["menu"]}">
  <div class="drawer-header">
    <a href="index.html">{lock}</a>
    <button class="drawer-close" onclick="closeNavDrawer()" aria-label="{s["close_menu"]}"><i class="fas fa-times"></i></button>
  </div>
  <div class="drawer-body">
    <span class="drawer-section-title">{s["sec_company"]}</span>
    <a href="index.html" class="drawer-link"><div class="drawer-link-icon"><i class="fas fa-home"></i></div>{s["home"]}</a>
    <a href="index.html#overview" class="drawer-link"><div class="drawer-link-icon"><i class="fas fa-building"></i></div>{s["overview"]}</a>
    <a href="index.html#sectors" class="drawer-link"><div class="drawer-link-icon"><i class="fas fa-industry"></i></div>{s["sectors"]}</a>
    <a href="index.html#process" class="drawer-link"><div class="drawer-link-icon"><i class="fas fa-sitemap"></i></div>{s["process"]}</a>

    <div class="drawer-divider"></div>
    <span class="drawer-section-title">{s["sec_permit"]}</span>
    {drawer_svc}

    <div class="drawer-divider"></div>
    <span class="drawer-section-title">{s["sec_monitor"]}</span>
    {drawer_mon}

    <div class="drawer-divider"></div>
    <span class="drawer-section-title">{s["sec_lab"]}</span>
    <a href="technology.html" class="drawer-link"><div class="drawer-link-icon"><i class="fas fa-flask"></i></div>{s["lab_services"]}</a>
    <a href="technology.html#standards" class="drawer-link"><div class="drawer-link-icon"><i class="fas fa-stamp"></i></div>{s["licences"]}</a>

    <div class="drawer-divider"></div>
    <a href="compliance-finder.html" class="drawer-link"><div class="drawer-link-icon"><i class="fas fa-list-check"></i></div>{s["finder"]}</a>
    <a href="blog.html" class="drawer-link"><div class="drawer-link-icon"><i class="fas fa-pen-nib"></i></div>{s["blog"]}</a>
    {careers_d}
    <a href="contact.html" class="drawer-link"><div class="drawer-link-icon"><i class="fas fa-envelope"></i></div>{s["contact"]}</a>
    <a href="{lh}" class="drawer-link"><div class="drawer-link-icon">🌐</div>{s["lang_drawer"]}</a>
  </div>
  <div class="drawer-footer">
    <a href="contact.html" class="drawer-portal-btn"><i class="fas fa-paper-plane"></i> {s["free"]}</a>
    <a data-wa="{s["wa_msg"]}" class="drawer-wa-btn"><i class="fab fa-whatsapp"></i> {s["wa_us"]}</a>
  </div>
</div>

<nav id="navbar">
  <div class="nav-inner">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex items-center justify-between" style="height:64px;gap:16px;">

        <a href="index.html" class="nav-logo-wrap js-home-link" aria-label="{s["home_aria"]}">
          {lock}
        </a>

        <nav class="nav-links" style="flex:1;justify-content:center;" aria-label="{s["primary"]}">
          <div class="nav-item">
            <a href="index.html" class="nav-link" data-page="index.html">{s["home"]} <i class="fas fa-chevron-down nav-chevron"></i></a>
            <div class="nav-dropdown">
              <div class="nav-dropdown-box" style="min-width:230px;">
                <div class="nav-dropdown-title">{s["about_bp"]}</div>
                {dd_link("about.html", "fa-building", s["about_bp"], s["about_sub"])}
                {dd_link("index.html#sectors", "fa-industry", s["sectors"], s["sectors_sub"])}
                {dd_link("index.html#process", "fa-sitemap", s["how"], s["how_sub"])}
              </div>
            </div>
          </div>

          <div class="nav-item">
            <a href="about.html" class="nav-link" data-page="about.html">{s["about"]}</a>
          </div>
          <div class="nav-item">
            <a href="equipment.html" class="nav-link" data-page="equipment.html">{s["technology"]} <i class="fas fa-chevron-down nav-chevron"></i></a>
            <div class="nav-dropdown">
              <div class="nav-dropdown-box" style="min-width:250px;">
                <div class="nav-dropdown-title">{s["instrumentation"]}</div>
                {dd_link("equipment.html", "fa-screwdriver-wrench", s["equip"], s["equip_sub"])}
                <div class="nav-dd-divider"></div>
                <div class="nav-dropdown-title">{s["compliance"]}</div>
                {dd_link("compliance.html", "fa-shield-halved", s["hub"], s["hub_sub"])}
                {dd_link("compliance-finder.html", "fa-list-check", s["finder"], s["finder_sub"])}
              </div>
            </div>
          </div>

          <div class="nav-item">
            <a href="services.html" class="nav-link" data-page="services.html">{s["services"]} <i class="fas fa-chevron-down nav-chevron"></i></a>
            <div class="nav-dropdown nav-mega">
              <div class="nav-dropdown-box nav-mega-box">
                <div class="nav-mega-header">
                  <span class="nav-mega-header-title">{s["sec_permit"]}</span>
                  <a href="services.html" class="nav-mega-cta">{s["view_all"]}</a>
                </div>
                {svc_links}
                <div class="nav-mega-header" style="margin-top:8px;">
                  <span class="nav-mega-header-title">{s["sec_monitor"]}</span>
                  <a href="services.html#monitoring" class="nav-mega-cta">{s["see_all"]}</a>
                </div>
                {mon_links}
              </div>
            </div>
          </div>

          <div class="nav-item">
            <a href="technology.html" class="nav-link" data-page="technology.html">{s["sec_lab"]} <i class="fas fa-chevron-down nav-chevron"></i></a>
            <div class="nav-dropdown">
              <div class="nav-dropdown-box" style="min-width:240px;">
                <div class="nav-dropdown-title">{s["measurement"]}</div>
                {dd_link("technology.html#equipment", "fa-flask", s["lab_services"], s["lab_sub"])}
                <div class="nav-dd-divider"></div>
                <div class="nav-dropdown-title">{s["credentials"]}</div>
                {dd_link("technology.html#standards", "fa-stamp", s["licences"], s["licences_sub"])}
              </div>
            </div>
          </div>

          <div class="nav-item">
            <a href="blog.html" class="nav-link" data-page="blog.html">{s["blog"]}</a>
          </div>
          {careers_n}
          <div class="nav-item" style="display:none">
          </div>

          <div class="nav-item">
            <a href="contact.html" class="nav-link" data-page="contact.html">{s["contact"]}</a>
          </div>
        </nav>

        <div class="nav-actions">
          <a href="{lh}" class="nav-lang-btn">🌐 <span>{s["lang_btn"]}</span></a>
          <a href="contact.html" class="nav-portal-btn"><i class="fas fa-paper-plane"></i> {s["free"]}</a>
          <button class="nav-hamburger" id="navHamburger" onclick="toggleNavDrawer()" aria-label="{s["menu_btn"]}"><span></span><span></span><span></span></button>
        </div>

      </div>
    </div>
  </div>
</nav>
"""


def _fl(href, label):
    return f'<li><a href="{href}"><span class="fl-icon"><i class="fas fa-chevron-right"></i></span>{label}</a></li>'


def footer(lang="en", page=None):
    s = STR[lang]
    lh = _lang_href(lang, page)
    careers = _fl("careers.html", s["careers"]) if _has_roles() else ""
    return f"""
<!-- ============================================================
     FOOTER
     ============================================================ -->
<footer class="site-footer">
  <div class="footer-top-rule"></div>

  <div class="footer-cta-strip">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-7">
      <div class="footer-cta-strip-inner flex flex-wrap items-center justify-between gap-5">
        <div>
          <p class="footer-cta-label">{s["start"]}</p>
          <p class="footer-cta-title">{s["ready"]}</p>
        </div>
        <div class="footer-cta-strip-btns flex flex-wrap gap-3">
          <a href="contact.html" class="footer-cta-strip-btn primary"><i class="fas fa-paper-plane" style="font-size:.75rem;"></i> {s["book"]}</a>
          <a data-wa="{s["wa_msg"]}" class="footer-cta-strip-btn wa"><i class="fab fa-whatsapp" style="font-size:.88rem;"></i> {s["wa_us"]}</a>
        </div>
      </div>
    </div>
  </div>

  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pt-14 pb-12">
    <div class="footer-grid">

      <div class="footer-brand-col">
        <a href="index.html" class="footer-brand-logo js-home-link" aria-label="{s["top_aria"]}">
          {_lockup(s)}
        </a>
        <p class="footer-brand-desc">{s["brand_desc"]}</p>
        <div class="footer-cert-row">
          <span class="footer-cert-badge"><i class="fas fa-stamp"></i> NCEC</span>
          <span class="footer-cert-badge"><i class="fas fa-recycle"></i> MWAN</span>
          <span class="footer-cert-badge"><i class="fas fa-industry"></i> RCJY</span>
          <span class="footer-cert-badge"><i class="fas fa-globe-americas"></i> IAS</span>
          <span class="footer-cert-badge"><i class="fas fa-award"></i> ISO 9001</span>
          <span class="footer-cert-badge"><i class="fas fa-leaf"></i> ISO 14001</span>
          <span class="footer-cert-badge"><i class="fas fa-hard-hat"></i> ISO 45001</span>
        </div>
        <div class="footer-social-row">
          <a href="https://www.linkedin.com/company/alemad-alarabi/" target="_blank" rel="noopener" class="footer-social-btn" aria-label="LinkedIn"><i class="fab fa-linkedin-in"></i></a>
          <a href="https://x.com/blueprint_env" target="_blank" rel="noopener" class="footer-social-btn" aria-label="X"><i class="fab fa-twitter"></i></a>
          <a href="https://www.instagram.com/blueprint_env" target="_blank" rel="noopener" class="footer-social-btn" aria-label="Instagram"><i class="fab fa-instagram"></i></a>
          <a data-wa="" class="footer-social-btn wa" aria-label="WhatsApp"><i class="fab fa-whatsapp"></i></a>
        </div>
      </div>

      <div>
        <h4 class="footer-col-title">{s["sec_company"]}</h4>
        <ul class="footer-link-list">
          {_fl("index.html#overview", s["f_overview"])}
          {_fl("technology.html", s["f_lab"])}
          {_fl("index.html#process", s["f_process"])}
          {_fl("index.html#sectors", s["f_sectors"])}
          {_fl("blog.html", s["blog"])}
          {careers}
          {_fl(lh, s["lang_short"])}
        </ul>
      </div>

      <div>
        <h4 class="footer-col-title">{s["f_permitting"]}</h4>
        <ul class="footer-link-list">
          {_fl("services.html#svc-0", s["f_p0"])}
          {_fl("services.html#svc-1", s["f_p1"])}
          {_fl("services.html#svc-2", s["f_p2"])}
          {_fl("services.html#svc-3", s["f_p3"])}
          {_fl("services.html#svc-4", s["f_p4"])}
          {_fl("services.html#svc-5", s["f_p5"])}
        </ul>
      </div>

      <div>
        <h4 class="footer-col-title">{s["f_monitoring"]}</h4>
        <ul class="footer-link-list">
          {_fl("services.html#monitoring", s["f_m0"])}
          {_fl("services.html#monitoring", s["f_m1"])}
          {_fl("services.html#monitoring", s["f_m2"])}
          {_fl("services.html#monitoring", s["f_m3"])}
          {_fl("services.html#monitoring", s["f_m4"])}
          {_fl("technology.html", s["f_m5"])}
        </ul>
      </div>

      <div>
        <h4 class="footer-col-title">{s["f_resources"]}</h4>
        <ul class="footer-link-list">
          {_fl("blog.html", s["f_briefing"])}
          {_fl("services.html#permitting", s["f_guide"])}
          {_fl("technology.html#standards", s["f_accred"])}
        </ul>
      </div>

      <div class="footer-contact-col">
        <h4 class="footer-col-title">{s["contact"]}</h4>
        <div class="footer-contact-row"><div class="footer-contact-icon-box"><i class="fas fa-map-marker-alt"></i></div><div><div class="footer-contact-label">{s["f_location"]}</div>{s["address"]}</div></div>
        <div class="footer-contact-row"><div class="footer-contact-icon-box"><i class="fas fa-envelope"></i></div><div><div class="footer-contact-label">{s["f_email"]}</div><div class="footer-contact-value"><a data-mail data-text="email"></a></div></div></div>
        <div class="footer-contact-row"><div class="footer-contact-icon-box"><i class="fas fa-phone"></i></div><div><div class="footer-contact-label">{s["f_phone"]}</div><div class="footer-contact-value"><a data-tel data-text="phone" dir="ltr"></a></div></div></div>
        <div class="footer-contact-row"><div class="footer-contact-icon-box"><i class="fab fa-whatsapp"></i></div><div><div class="footer-contact-label">{s["f_wa"]}</div><div class="footer-contact-value"><a data-wa="" data-text="phone" dir="ltr"></a></div></div></div>
        <div class="footer-contact-row"><div class="footer-contact-icon-box"><i class="fas fa-clock"></i></div><div><div class="footer-contact-label">{s["f_hours"]}</div><div class="footer-contact-value">{s["f_hours_v"]}</div></div></div>
      </div>

    </div>
  </div>

  <div class="footer-bottom-bar">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-5">
      <div class="footer-bottom-inner flex flex-wrap items-center justify-between gap-4">
        <div style="display:flex;flex-direction:column;gap:3px;">
          <p class="footer-copy">© <span data-text="year"></span> {s["copy"]}</p>
          <p class="footer-credit">{s["credit"]}</p>
        </div>
        <div style="display:flex;align-items:center;flex-wrap:wrap;gap:2px;">
          <a href="privacy.html" class="footer-legal-btn">{s["privacy"]}</a>
          <span class="footer-legal-sep"></span>
          <a href="terms.html" class="footer-legal-btn">{s["terms"]}</a>
          <span class="footer-legal-sep"></span>
          <a href="{lh}" class="footer-legal-btn" style="color:rgba(163,181,111.6);">{s["lang_footer"]}</a>
        </div>
      </div>
    </div>
  </div>
</footer>
"""


def modals():
    return ""


def widgets(lang="en"):
    s = STR[lang]
    return f"""
<!-- ============================================================
     FLOATING WIDGETS, WhatsApp, expert CTA
     ============================================================ -->
<div id="whatsappContainer" class="whatsapp-container">
  <a href="#" id="whatsappBtn" class="whatsapp-btn" title="{s["wa_title"]}" aria-label="{s["wa_aria"]}">
    <i class="fab fa-whatsapp whatsapp-icon"></i>
  </a>
  <div class="whatsapp-tooltip">{s["wa_title"]}</div>
</div>

<div id="expertCTA">
  <div id="expertTab" onclick="toggleExpert()" role="button" tabindex="0" aria-label="{s["expert_aria"]}">
    <div class="expert-photo-wrap"><i class="fas fa-headset" aria-hidden="true"></i></div>
    <div class="expert-label-pill"><span>{s["ask"]}</span><span>{s["free_arrow"]}</span></div>
  </div>
  <div id="expertPanel">
    <div class="ep-header">
      <div class="ep-photo"><i class="fas fa-headset" aria-hidden="true"></i></div>
      <div class="ep-info"><div class="ep-name">{s["ep_name"]}</div><div class="ep-role">{s["ep_role"]}</div><div class="ep-status">{s["ep_status"]}</div></div>
      <button class="ep-close" onclick="closeExpert()" aria-label="{s["close"]}">✕</button>
    </div>
    <div class="ep-body">
      <div class="ep-question">{s["ep_q"]}</div>
      <div class="ep-hint">{s["ep_hint"]}</div>
      <div class="ep-options">
        <a data-wa="{s["ep_wa_msg"]}" class="ep-option whatsapp"><i class="fab fa-whatsapp"></i> {s["ep_wa"]}</a>
        <a data-mail class="ep-option email"><i class="fas fa-envelope"></i> {s["ep_mail"]}</a>
        <a data-tel class="ep-option call"><i class="fas fa-phone"></i> {s["ep_call"]} <span data-text="phone" dir="ltr"></span></a>
      </div>
      <div class="ep-divider">{s["ep_or"]}</div>
      <div class="ep-quick-msg"><input type="text" id="expertMsgInput" placeholder="{s["ep_ph"]}" maxlength="120" aria-label="{s["ep_quick"]}" /><button onclick="sendExpertMsg()" aria-label="{s["send"]}"><i class="fas fa-paper-plane"></i></button></div>
    </div>
    <div class="ep-footer">{s["ep_foot"]}</div>
  </div>
</div>
"""


def scripts(extra=(), lang="en"):
    base = ["js/main.js", "js/widgets.js", "js/scroll.js"] + list(extra)
    return "\n".join(f'<script src="{s}"></script>' for s in base) + "\n</body>\n</html>\n"


# ---------------------------------------------------------------------------
# Arabic pages live one folder down, in site/ar/. Two fixes run over each one:
#   assets, css and js are one level up, so they get "../";
#   a link to a page that has no Arabic version yet falls back to the English
#   page rather than a missing file. As pages are translated, those links
#   switch over by themselves.
# ---------------------------------------------------------------------------
import re as _re


def ar_paths(html, available):
    html = _re.sub(r'(?<![\w./-])(assets|css|js)/', r'../\1/', html)

    def fix(m):
        attr, q, target, rest = m.group(1), m.group(2), m.group(3), m.group(4)
        if target in available:
            return m.group(0)
        return f'{attr}={q}../{target}{rest}{q}'

    html = _re.sub(r'(href)=(["\'])([a-z0-9-]+\.html)([^"\']*)\2', fix, html)
    return html
