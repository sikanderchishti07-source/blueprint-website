# Arabic (RTL) home page, mirrors the English home page content.

from arabic_home import BODY

HEAD = """<!DOCTYPE html>
<!--
  ============================================================
  GENERATED FILE, DO NOT EDIT THIS HTML BY HAND.
  Assembled by build/build.py from build/arabic.py.
  ============================================================
-->
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="description" content="بلوبرنت للخدمات البيئية, استشارات بيئية معتمدة في المملكة العربية السعودية: التصاريح البيئية، دراسات تقييم الأثر، تصاريح إدارة النفايات، السجلات البيئية، والقياسات والرصد البيئي." />
  <meta name="theme-color" content="#0e93a8" />
  <title>بلوبرنت للخدمات البيئية | استشارات بيئية معتمدة في السعودية</title>
  <link rel="icon" type="image/png" href="assets/logo/favicon.png" />
  <link rel="alternate" hreflang="en" href="index.html" />

  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Arabic:wght@300;400;500;600;700&family=Plus+Jakarta+Sans:wght@400;600;700;800&display=swap" rel="stylesheet" />
  <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet" />

  <link rel="stylesheet" href="css/tailwind.css" />
  <link rel="stylesheet" href="css/base.css" />
  <link rel="stylesheet" href="css/layout.css" />
  <link rel="stylesheet" href="css/components.css" />
  <link rel="stylesheet" href="css/pages.css" />
  <link rel="stylesheet" href="css/rtl.css" />

  <script src="js/config.js"></script>
</head>
<body class="font-sans">
"""

NAV = """
<div id="navDrawerOverlay" onclick="closeNavDrawer()"></div>

<div id="navMobileDrawer" aria-label="القائمة">
  <div class="drawer-header">
    <a href="index_arabic.html" class="drawer-logo"><img src="assets/logo/blueprint-logo.png" alt="بلوبرنت" /></a>
    <button class="drawer-close" onclick="closeNavDrawer()" aria-label="إغلاق">&times;</button>
  </div>
  <div class="drawer-links">
    <a href="index_arabic.html" class="drawer-link"><div class="drawer-link-icon"><i class="fas fa-home"></i></div>الرئيسية</a>
    <a href="services.html" class="drawer-link"><div class="drawer-link-icon"><i class="fas fa-clipboard-list"></i></div>خدماتنا</a>
    <a href="technology.html" class="drawer-link"><div class="drawer-link-icon"><i class="fas fa-flask"></i></div>المختبر</a>
    <a href="blog.html" class="drawer-link"><div class="drawer-link-icon"><i class="fas fa-pen-nib"></i></div>المدونة</a>
    <a href="contact.html" class="drawer-link"><div class="drawer-link-icon"><i class="fas fa-envelope"></i></div>تواصل معنا</a>
    <a href="index.html" class="drawer-link"><div class="drawer-link-icon">🌐</div>English</a>
  </div>
  <div class="drawer-footer">
    <a href="contact.html" class="drawer-portal-btn"><i class="fas fa-paper-plane"></i> استشارة مجانية</a>
    <a data-wa="السلام عليكم، أود الاستفسار عن خدماتكم البيئية." class="drawer-wa-btn"><i class="fab fa-whatsapp"></i> واتساب</a>
  </div>
</div>

<nav id="navbar">
  <div class="nav-inner">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex items-center justify-between" style="height:64px;gap:16px;">

        <a href="index_arabic.html" class="nav-logo-wrap" aria-label="بلوبرنت, الرئيسية">
          <img src="assets/logo/blueprint-logo.png" alt="بلوبرنت للخدمات البيئية" />
        </a>

        <nav class="nav-links" style="flex:1;justify-content:center;" aria-label="القائمة الرئيسية">
          <div class="nav-item"><a href="index_arabic.html" class="nav-link">الرئيسية</a></div>
          <div class="nav-item"><a href="services.html" class="nav-link">خدماتنا</a></div>
          <div class="nav-item"><a href="technology.html" class="nav-link">المختبر</a></div>
          <div class="nav-item"><a href="blog.html" class="nav-link">المدونة</a></div>
          <div class="nav-item"><a href="contact.html" class="nav-link">تواصل معنا</a></div>
        </nav>

        <div class="nav-right">
          <a href="index.html" class="nav-lang-btn"><i class="fas fa-globe"></i> English</a>
          <a href="contact.html" class="nav-portal-btn"><i class="fas fa-paper-plane"></i> استشارة مجانية</a>
          <button class="nav-burger" onclick="toggleNavDrawer()" aria-label="القائمة"><span></span><span></span><span></span></button>
        </div>

      </div>
    </div>
  </div>
</nav>

"""

FOOTER = """
<footer class="site-footer">
  <div class="footer-top-rule"></div>
  <div class="footer-cta-strip">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-7">
      <div class="footer-cta-strip-inner flex flex-wrap items-center justify-between gap-5">
        <div>
          <p class="footer-cta-label">ابدأ مشروعك</p>
          <p class="footer-cta-title">هل أنت مستعد لجعل الامتثال أسهل جزء في عملك؟</p>
        </div>
        <div class="footer-cta-strip-btns flex flex-wrap gap-3">
          <a href="#contact" class="footer-cta-strip-btn primary"><i class="fas fa-paper-plane" style="font-size:.75rem;"></i> احجز استشارة</a>
          <a data-wa="مرحباً بلوبرنت، أود الاستفسار عن خدماتكم البيئية." class="footer-cta-strip-btn wa"><i class="fab fa-whatsapp" style="font-size:.88rem;"></i> واتساب</a>
        </div>
      </div>
    </div>
  </div>

  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pt-14 pb-12">
    <div class="footer-grid">
      <div class="footer-brand-col">
        <a href="index_arabic.html" class="footer-brand-logo"><img src="assets/logo/blueprint-logo-white.png" alt="بلوبرنت للخدمات البيئية" /></a>
        <p class="footer-brand-desc">استشارات بيئية معتمدة تقدّم خدمات الامتثال والتصاريح والتقارير في أنحاء المملكة العربية السعودية.</p>
        <div class="footer-cert-row">
          <span class="footer-cert-badge">المركز الوطني للالتزام البيئي</span>
          <span class="footer-cert-badge">المركز الوطني لإدارة النفايات</span>
          <span class="footer-cert-badge">الهيئة الملكية</span>
          <span class="footer-cert-badge">آيزو 9001</span>
          <span class="footer-cert-badge">آيزو 14001</span>
          <span class="footer-cert-badge">آيزو 45001</span>
        </div>
        <div class="footer-social-row">
          <a href="https://www.linkedin.com/company/alemad-alarabi/" target="_blank" rel="noopener" class="footer-social-btn" aria-label="لينكدإن"><i class="fab fa-linkedin-in"></i></a>
          <a href="https://x.com/blueprint_env" target="_blank" rel="noopener" class="footer-social-btn" aria-label="إكس"><i class="fab fa-twitter"></i></a>
          <a href="https://www.instagram.com/blueprint_env" target="_blank" rel="noopener" class="footer-social-btn" aria-label="إنستغرام"><i class="fab fa-instagram"></i></a>
          <a data-wa="" class="footer-social-btn wa" aria-label="واتساب"><i class="fab fa-whatsapp"></i></a>
        </div>
      </div>

      <div>
        <h4 class="footer-col-title">التصاريح</h4>
        <ul class="footer-link-list">
          <li><a href="#services">التصريح البيئي</a></li>
          <li><a href="#services">تقييم الأثر البيئي</a></li>
          <li><a href="#services">تصريح إدارة النفايات</a></li>
          <li><a href="#services">خطة الإدارة البيئية</a></li>
          <li><a href="#services">السجل البيئي</a></li>
          <li><a href="#services">التقرير الدوري</a></li>
        </ul>
      </div>

      <div>
        <h4 class="footer-col-title">الرصد والقياس</h4>
        <ul class="footer-link-list">
          <li><a href="#services">جودة الهواء</a></li>
          <li><a href="#services">المياه ومياه الصرف</a></li>
          <li><a href="#services">الضوضاء</a></li>
          <li><a href="#services">التربة والرواسب</a></li>
          <li><a href="#services">أخذ العينات</a></li>
          <li><a href="#services">التحاليل المخبرية</a></li>
        </ul>
      </div>

      <div>
        <h4 class="footer-col-title">الشركة</h4>
        <ul class="footer-link-list">
          <li><a href="#overview">من نحن</a></li>
          <li><a href="#sectors">القطاعات</a></li>
          <li><a href="#process">منهجية العمل</a></li>
          <li><a href="#contact">تواصل معنا</a></li>
          <li><a href="index.html">English</a></li>
        </ul>
      </div>

      <div class="footer-contact-col">
        <h4 class="footer-col-title">للتواصل</h4>
        <div class="footer-contact-row"><div class="footer-contact-icon-box"><i class="fas fa-map-marker-alt"></i></div><div><div class="footer-contact-label">الموقع</div><div class="footer-contact-value">الرياض، المملكة العربية السعودية</div></div></div>
        <div class="footer-contact-row"><div class="footer-contact-icon-box"><i class="fas fa-envelope"></i></div><div><div class="footer-contact-label">البريد</div><div class="footer-contact-value"><a data-mail data-text="email"></a></div></div></div>
        <div class="footer-contact-row"><div class="footer-contact-icon-box"><i class="fas fa-phone"></i></div><div><div class="footer-contact-label">الهاتف</div><div class="footer-contact-value"><a data-tel data-text="phone" style="direction:ltr;display:inline-block;"></a></div></div></div>
        <div class="footer-contact-row"><div class="footer-contact-icon-box"><i class="fas fa-clock"></i></div><div><div class="footer-contact-label">ساعات العمل</div><div class="footer-contact-value">الأحد &ndash; الخميس &middot; ٩:٠٠ &ndash; ١٨:٠٠</div></div></div>
      </div>
    </div>
  </div>

  <div class="footer-bottom-bar">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-5">
      <div class="footer-bottom-inner flex flex-wrap items-center justify-between gap-4">
        <p class="footer-copy">© <span data-text="year"></span> بلوبرنت للخدمات البيئية. جميع الحقوق محفوظة.</p>
        <div style="display:flex;align-items:center;flex-wrap:wrap;gap:2px;">
          <a href="privacy.html" class="footer-legal-btn">سياسة الخصوصية</a>
          <span class="footer-legal-sep"></span>
          <a href="terms.html" class="footer-legal-btn">الشروط والأحكام</a>
          <span class="footer-legal-sep"></span>
          <a href="index.html" class="footer-legal-btn" style="color:rgba(163,181,111.6);">🌐 English</a>
        </div>
      </div>
    </div>
  </div>
</footer>

<div id="whatsappContainer" class="whatsapp-container">
  <a href="#" id="whatsappBtn" class="whatsapp-btn" title="تواصل معنا عبر واتساب" aria-label="واتساب">
    <i class="fab fa-whatsapp whatsapp-icon"></i>
  </a>
  <div class="whatsapp-tooltip">تواصل معنا عبر واتساب</div>
</div>

<script src="js/cards-ar.js"></script>
<script src="js/cards.js"></script>
<script src="js/main.js"></script>
<script src="js/widgets.js"></script>
</body>
</html>
"""


def arabic():
    return HEAD + NAV + BODY + FOOTER
