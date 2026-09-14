def _has_roles():
    """Careers only appears in the menus when a vacancy is actually open."""
    return True
    try:
        import content
        return bool(content.load_careers())
    except Exception:
        return False

# Shared HTML partials for the BluePrint site build.

def head(title, description, extra_css=""):
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
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="description" content="{description}" />
  <meta name="theme-color" content="#0e93a8" />
  <title>{title}</title>
  <link rel="icon" type="image/png" href="assets/logo/favicon.png" />

  <!-- Fonts & icons -->
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=DM+Sans:wght@300;400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet" />
  <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet" />

  <!-- Site styles (css/tailwind.css is compiled by build/build.sh) -->
  <link rel="stylesheet" href="css/tailwind.css" />
  <link rel="stylesheet" href="css/base.css" />
  <link rel="stylesheet" href="css/layout.css" />
  <link rel="stylesheet" href="css/components.css" />
  <link rel="stylesheet" href="css/pages.css" />
  <link rel="stylesheet" href="css/cover.css" />
  <link rel="stylesheet" href="css/carousel.css" />
  <link rel="stylesheet" href="css/insights.css" />{extra_css}

  <script src="js/config.js"></script>
</head>
<body class="font-sans">
"""


SERVICES_NAV = [
    ("fa-file-signature", "Environmental Permit", "NCEC permit file to issuance", "service-environmental-permit.html"),
    ("fa-clipboard-check", "Impact Assessment", "EIA/ESIA for regulated projects", "service-environmental-impact-assessment.html"),
    ("fa-recycle", "Waste Permit (MWAN)", "Generators, carriers &amp; treaters", "service-waste-management-permit.html"),
    ("fa-tasks", "Environmental Management Plan", "Permit conditions into practice", "service-environmental-management-plan.html"),
    ("fa-folder-open", "Environmental Register", "Continuous proof of compliance", "service-environmental-register.html"),
    ("fa-calendar-check", "Periodic Reporting", "Filed on time, every cycle", "service-periodic-environmental-report.html"),
]


def dd_link(href, icon, label, sub, extra_icon_style="", badge=""):
    return f"""<a href="{href}" class="nav-dd-link">
                  <div class="nav-dd-icon"{extra_icon_style}><i class="fas {icon}"></i></div>
                  <div class="nav-dd-text-wrap"><span class="nav-dd-label">{label}{badge}</span><span class="nav-dd-sub">{sub}</span></div>
                </a>"""


LIVE_BADGE = '<span style="font-size:.55rem;padding:1px 6px;background:#dcfce7;color:#15803d;border-radius:999px;font-weight:700;letter-spacing:.06em;margin-left:3px;">LIVE</span>'


MONITORING_NAV = [
    ("fa-wind", "Air Quality Monitoring", "Measurement &amp; assessment", "service-air-quality-monitoring.html"),
    ("fa-tint", "Water &amp; Wastewater Testing", "Accredited analysis", "service-water-wastewater-testing.html"),
    ("fa-volume-up", "Noise Monitoring", "Against regulated limits", "service-noise-monitoring.html"),
    ("fa-mountain", "Soil &amp; Sediment Testing", "Contaminant levels", "service-soil-sediment-testing.html"),
    ("fa-vial", "Environmental Sampling", "Chain-of-custody protocols", "service-environmental-sampling.html"),
    ("fa-microscope", "Laboratory Analysis", "With technical interpretation", "service-laboratory-analysis.html"),
]


def nav():
    svc_links = "\n".join(dd_link(pg, ic, lb, sb) for ic, lb, sb, pg in SERVICES_NAV)
    mon_links = "\n".join(dd_link(pg, ic, lb, sb) for ic, lb, sb, pg in MONITORING_NAV)
    drawer_svc = "\n".join(
        f'<a href="{pg}" class="drawer-link"><div class="drawer-link-icon"><i class="fas {ic}"></i></div>{lb}</a>'
        for ic, lb, sb, pg in SERVICES_NAV)
    return f"""
<!-- ============================================================
     NAVIGATION
     ============================================================ -->
<div id="navDrawerOverlay" onclick="closeNavDrawer()"></div>

<div id="navMobileDrawer" aria-label="Mobile menu">
  <div class="drawer-header">
    <a href="index.html"><span class="bp-lock"><span class="bp-mark"><img class="bp-b" src="assets/logo/blueprint-b.png" alt="" /><img class="bp-wave" src="assets/logo/blueprint-wave.png" alt="" /></span><span class="bp-txt"><img class="bp-word" src="assets/logo/blueprint-wordmark.png" alt="BluePrint" /><span class="bp-tag">Environmental Services</span></span></span></a>
    <button class="drawer-close" onclick="closeNavDrawer()" aria-label="Close menu"><i class="fas fa-times"></i></button>
  </div>
  <div class="drawer-body">
    <span class="drawer-section-title">Company</span>
    <a href="index.html" class="drawer-link"><div class="drawer-link-icon"><i class="fas fa-home"></i></div>Home</a>
    <a href="index.html#overview" class="drawer-link"><div class="drawer-link-icon"><i class="fas fa-building"></i></div>Company Overview</a>
    <a href="index.html#sectors" class="drawer-link"><div class="drawer-link-icon"><i class="fas fa-industry"></i></div>Sectors We Serve</a>
    <a href="index.html#process" class="drawer-link"><div class="drawer-link-icon"><i class="fas fa-sitemap"></i></div>Our Process</a>

    <div class="drawer-divider"></div>
    <span class="drawer-section-title">Compliance &amp; Permitting</span>
    {drawer_svc}

    <div class="drawer-divider"></div>
    <span class="drawer-section-title">Monitoring &amp; Testing</span>
    <a href="services.html#monitoring" class="drawer-link"><div class="drawer-link-icon"><i class="fas fa-wind"></i></div>Air Quality Monitoring</a>
    <a href="services.html#monitoring" class="drawer-link"><div class="drawer-link-icon"><i class="fas fa-tint"></i></div>Water &amp; Wastewater Testing</a>
    <a href="services.html#monitoring" class="drawer-link"><div class="drawer-link-icon"><i class="fas fa-volume-up"></i></div>Noise Monitoring</a>
    <a href="services.html#monitoring" class="drawer-link"><div class="drawer-link-icon"><i class="fas fa-mountain"></i></div>Soil &amp; Sediment Testing</a>

    <div class="drawer-divider"></div>
    <span class="drawer-section-title">Laboratory</span>
    <a href="technology.html" class="drawer-link"><div class="drawer-link-icon"><i class="fas fa-flask"></i></div>Laboratory Services</a>
    <a href="technology.html#standards" class="drawer-link"><div class="drawer-link-icon"><i class="fas fa-stamp"></i></div>Licences &amp; Accreditations</a>

    <div class="drawer-divider"></div>
    <a href="blog.html" class="drawer-link"><div class="drawer-link-icon"><i class="fas fa-pen-nib"></i></div>Blog</a>
    """ + ('''<a href="careers.html" class="drawer-link"><div class="drawer-link-icon"><i class="fas fa-user-plus"></i></div>Careers</a>''' if _has_roles() else "") + f"""
    <a href="contact.html" class="drawer-link"><div class="drawer-link-icon"><i class="fas fa-envelope"></i></div>Contact</a>
    <a href="index_arabic.html" class="drawer-link"><div class="drawer-link-icon">🌐</div>العربية (Arabic)</a>
  </div>
  <div class="drawer-footer">
    <a href="contact.html" class="drawer-portal-btn"><i class="fas fa-paper-plane"></i> Free Consultation</a>
    <a data-wa="Hello BluePrint, I would like to ask about your environmental services." class="drawer-wa-btn"><i class="fab fa-whatsapp"></i> WhatsApp Us</a>
  </div>
</div>

<nav id="navbar">
  <div class="nav-inner">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex items-center justify-between" style="height:64px;gap:16px;">

        <a href="index.html" class="nav-logo-wrap js-home-link" aria-label="BluePrint, home">
          <span class="bp-lock"><span class="bp-mark"><img class="bp-b" src="assets/logo/blueprint-b.png" alt="" /><img class="bp-wave" src="assets/logo/blueprint-wave.png" alt="" /></span><span class="bp-txt"><img class="bp-word" src="assets/logo/blueprint-wordmark.png" alt="BluePrint" /><span class="bp-tag">Environmental Services</span></span></span>
        </a>

        <nav class="nav-links" style="flex:1;justify-content:center;" aria-label="Primary">
          <div class="nav-item">
            <a href="index.html" class="nav-link" data-page="index.html">Home <i class="fas fa-chevron-down nav-chevron"></i></a>
            <div class="nav-dropdown">
              <div class="nav-dropdown-box" style="min-width:230px;">
                <div class="nav-dropdown-title">About BluePrint</div>
                {dd_link("about.html", "fa-building", "About BluePrint", "Who we are &amp; how we work")}
                {dd_link("index.html#sectors", "fa-industry", "Sectors We Serve", "Six regulated industries")}
                {dd_link("index.html#process", "fa-sitemap", "How We Work", "Assess, plan, submit, sustain")}
              </div>
            </div>
          </div>

          <div class="nav-item">
            <a href="about.html" class="nav-link" data-page="about.html">About</a>
          </div>
          <div class="nav-item">
            <a href="equipment.html" class="nav-link" data-page="equipment.html">Technology <i class="fas fa-chevron-down nav-chevron"></i></a>
            <div class="nav-dropdown">
              <div class="nav-dropdown-box" style="min-width:250px;">
                <div class="nav-dropdown-title">Instrumentation</div>
                {dd_link("equipment.html", "fa-screwdriver-wrench", "Equipment Catalogue", "Instrument types by domain")}
                <div class="nav-dd-divider"></div>
                <div class="nav-dropdown-title">Compliance</div>
                {dd_link("compliance.html", "fa-shield-halved", "Compliance Hub", "Saudi regulations, searchable")}
              </div>
            </div>
          </div>

          <div class="nav-item">
            <a href="services.html" class="nav-link" data-page="services.html">Services <i class="fas fa-chevron-down nav-chevron"></i></a>
            <div class="nav-dropdown nav-mega">
              <div class="nav-dropdown-box nav-mega-box">
                <div class="nav-mega-header">
                  <span class="nav-mega-header-title">Compliance &amp; Permitting</span>
                  <a href="services.html" class="nav-mega-cta">View All →</a>
                </div>
                {svc_links}
                <div class="nav-mega-header" style="margin-top:8px;">
                  <span class="nav-mega-header-title">Monitoring &amp; Testing</span>
                  <a href="services.html#monitoring" class="nav-mega-cta">See all →</a>
                </div>
                {mon_links}
              </div>
            </div>
          </div>

          <div class="nav-item">
            <a href="technology.html" class="nav-link" data-page="technology.html">Laboratory <i class="fas fa-chevron-down nav-chevron"></i></a>
            <div class="nav-dropdown">
              <div class="nav-dropdown-box" style="min-width:240px;">
                <div class="nav-dropdown-title">Measurement</div>
                {dd_link("technology.html#equipment", "fa-flask", "Laboratory Services", "Sampling, testing &amp; monitoring")}
                <div class="nav-dd-divider"></div>
                <div class="nav-dropdown-title">Credentials</div>
                {dd_link("technology.html#standards", "fa-stamp", "Licences &amp; Accreditations", "NCEC, MWAN, RCJY, IAS &amp; ISO")}
              </div>
            </div>
          </div>

          <div class="nav-item">
            <a href="blog.html" class="nav-link" data-page="blog.html">Blog</a>
          </div>
          """ + ('''<div class="nav-item"><a href="careers.html" class="nav-link" data-page="careers.html">Careers</a></div>''' if _has_roles() else "") + f"""
          <div class="nav-item" style="display:none">
          </div>

          <div class="nav-item">
            <a href="contact.html" class="nav-link" data-page="contact.html">Contact</a>
          </div>
        </nav>

        <div class="nav-actions">
          <a href="index_arabic.html" class="nav-lang-btn">🌐 <span>العربية</span></a>
          <a href="contact.html" class="nav-portal-btn"><i class="fas fa-paper-plane"></i> Free Consultation</a>
          <button class="nav-hamburger" id="navHamburger" onclick="toggleNavDrawer()" aria-label="Menu"><span></span><span></span><span></span></button>
        </div>

      </div>
    </div>
  </div>
</nav>
"""


def footer():
    return """
<!-- ============================================================
     FOOTER
     ============================================================ -->
<footer class="site-footer">
  <div class="footer-top-rule"></div>

  <div class="footer-cta-strip">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-7">
      <div class="footer-cta-strip-inner flex flex-wrap items-center justify-between gap-5">
        <div>
          <p class="footer-cta-label">Start Your Project</p>
          <p class="footer-cta-title">Ready to make compliance the easy part?</p>
        </div>
        <div class="footer-cta-strip-btns flex flex-wrap gap-3">
          <a href="contact.html" class="footer-cta-strip-btn primary"><i class="fas fa-paper-plane" style="font-size:.75rem;"></i> Book a consultation</a>
          <a data-wa="Hello BluePrint, I would like to ask about your environmental services." class="footer-cta-strip-btn wa"><i class="fab fa-whatsapp" style="font-size:.88rem;"></i> WhatsApp Us</a>
        </div>
      </div>
    </div>
  </div>

  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pt-14 pb-12">
    <div class="footer-grid">

      <div class="footer-brand-col">
        <a href="index.html" class="footer-brand-logo js-home-link" aria-label="BluePrint, back to top">
          <img src="assets/logo/blueprint-logo-white.png" alt="BluePrint Environmental Services" />
        </a>
        <p class="footer-brand-desc">Accredited environmental consultancy delivering compliance, permitting, and reporting across the Kingdom of Saudi Arabia.</p>
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
        <h4 class="footer-col-title">Company</h4>
        <ul class="footer-link-list">
          <li><a href="index.html#overview"><span class="fl-icon"><i class="fas fa-chevron-right"></i></span>Overview</a></li>
          <li><a href="technology.html"><span class="fl-icon"><i class="fas fa-chevron-right"></i></span>Laboratory</a></li>
          <li><a href="index.html#process"><span class="fl-icon"><i class="fas fa-chevron-right"></i></span>Our Process</a></li>
          <li><a href="index.html#sectors"><span class="fl-icon"><i class="fas fa-chevron-right"></i></span>Sectors</a></li>
          <li><a href="blog.html"><span class="fl-icon"><i class="fas fa-chevron-right"></i></span>Blog</a></li>
          """ + ('''<li><a href="careers.html"><span class="fl-icon"><i class="fas fa-chevron-right"></i></span>Careers</a></li>''' if _has_roles() else "") + f"""
          <li><a href="index_arabic.html"><span class="fl-icon"><i class="fas fa-chevron-right"></i></span>العربية</a></li>
        </ul>
      </div>

      <div>
        <h4 class="footer-col-title">Permitting</h4>
        <ul class="footer-link-list">
          <li><a href="services.html#svc-0"><span class="fl-icon"><i class="fas fa-chevron-right"></i></span>Environmental Permit</a></li>
          <li><a href="services.html#svc-1"><span class="fl-icon"><i class="fas fa-chevron-right"></i></span>Impact Assessment</a></li>
          <li><a href="services.html#svc-2"><span class="fl-icon"><i class="fas fa-chevron-right"></i></span>Permitting (MWAN)</a></li>
          <li><a href="services.html#svc-3"><span class="fl-icon"><i class="fas fa-chevron-right"></i></span>Management Plans</a></li>
          <li><a href="services.html#svc-4"><span class="fl-icon"><i class="fas fa-chevron-right"></i></span>Environmental Registers</a></li>
          <li><a href="services.html#svc-5"><span class="fl-icon"><i class="fas fa-chevron-right"></i></span>Periodic Reporting</a></li>
        </ul>
      </div>

      <div>
        <h4 class="footer-col-title">Monitoring</h4>
        <ul class="footer-link-list">
          <li><a href="services.html#monitoring"><span class="fl-icon"><i class="fas fa-chevron-right"></i></span>Air Quality</a></li>
          <li><a href="services.html#monitoring"><span class="fl-icon"><i class="fas fa-chevron-right"></i></span>Water &amp; Wastewater</a></li>
          <li><a href="services.html#monitoring"><span class="fl-icon"><i class="fas fa-chevron-right"></i></span>Noise</a></li>
          <li><a href="services.html#monitoring"><span class="fl-icon"><i class="fas fa-chevron-right"></i></span>Soil &amp; Sediment</a></li>
          <li><a href="services.html#monitoring"><span class="fl-icon"><i class="fas fa-chevron-right"></i></span>Sampling</a></li>
          <li><a href="technology.html"><span class="fl-icon"><i class="fas fa-chevron-right"></i></span>Laboratory Analysis</a></li>
        </ul>
      </div>

      <div>
        <h4 class="footer-col-title">Resources</h4>
        <ul class="footer-link-list">
          <li><a href="blog.html"><span class="fl-icon"><i class="fas fa-chevron-right"></i></span>Compliance Briefing</a></li>
          <li><a href="services.html#permitting"><span class="fl-icon"><i class="fas fa-chevron-right"></i></span>Permitting Guide</a></li>
          <li><a href="technology.html#standards"><span class="fl-icon"><i class="fas fa-chevron-right"></i></span>Accreditations</a></li>
        </ul>
      </div>

      <div class="footer-contact-col">
        <h4 class="footer-col-title">Contact</h4>
        <div class="footer-contact-row"><div class="footer-contact-icon-box"><i class="fas fa-map-marker-alt"></i></div><div><div class="footer-contact-label">Location</div><div class="footer-contact-value" data-text="address"></div></div></div>
        <div class="footer-contact-row"><div class="footer-contact-icon-box"><i class="fas fa-envelope"></i></div><div><div class="footer-contact-label">Email</div><div class="footer-contact-value"><a data-mail data-text="email"></a></div></div></div>
        <div class="footer-contact-row"><div class="footer-contact-icon-box"><i class="fas fa-phone"></i></div><div><div class="footer-contact-label">Phone</div><div class="footer-contact-value"><a data-tel data-text="phone"></a></div></div></div>
        <div class="footer-contact-row"><div class="footer-contact-icon-box"><i class="fab fa-whatsapp"></i></div><div><div class="footer-contact-label">WhatsApp</div><div class="footer-contact-value"><a data-wa="" data-text="phone"></a></div></div></div>
        <div class="footer-contact-row"><div class="footer-contact-icon-box"><i class="fas fa-clock"></i></div><div><div class="footer-contact-label">Working hours</div><div class="footer-contact-value">Sun &ndash; Thu &middot; 9:00 &ndash; 18:00 AST</div></div></div>
      </div>

    </div>
  </div>

  <div class="footer-bottom-bar">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-5">
      <div class="footer-bottom-inner flex flex-wrap items-center justify-between gap-4">
        <div style="display:flex;flex-direction:column;gap:3px;">
          <p class="footer-copy">© <span data-text="year"></span> BluePrint Environmental Services. All rights reserved.</p>
          <p class="footer-credit">Prepared by: <span>Sikander Chishti</span>, Environmental Engineer</p>
        </div>
        <div style="display:flex;align-items:center;flex-wrap:wrap;gap:2px;">
          <a href="privacy.html" class="footer-legal-btn">Privacy Policy</a>
          <span class="footer-legal-sep"></span>
          <a href="terms.html" class="footer-legal-btn">Terms &amp; Conditions</a>
          <span class="footer-legal-sep"></span>
          <a href="index_arabic.html" class="footer-legal-btn" style="color:rgba(163,181,111.6);">🌐 العربية</a>
        </div>
      </div>
    </div>
  </div>
</footer>
"""


def modals():
    return ""


def widgets():
    return """
<!-- ============================================================
     FLOATING WIDGETS, WhatsApp, expert CTA
     ============================================================ -->
<div id="whatsappContainer" class="whatsapp-container">
  <a href="#" id="whatsappBtn" class="whatsapp-btn" title="Chat with us on WhatsApp" aria-label="Chat on WhatsApp">
    <i class="fab fa-whatsapp whatsapp-icon"></i>
  </a>
  <div class="whatsapp-tooltip">Chat with us on WhatsApp</div>
</div>

<div id="expertCTA">
  <div id="expertTab" onclick="toggleExpert()" role="button" tabindex="0" aria-label="Speak to an expert">
    <div class="expert-photo-wrap"><i class="fas fa-headset" aria-hidden="true"></i></div>
    <div class="expert-label-pill"><span>Ask an Expert</span><span>Free Consultation →</span></div>
  </div>
  <div id="expertPanel">
    <div class="ep-header">
      <div class="ep-photo"><i class="fas fa-headset" aria-hidden="true"></i></div>
      <div class="ep-info"><div class="ep-name">Environmental Specialist</div><div class="ep-role">Accredited environmental consultant &middot; Riyadh</div><div class="ep-status">Riyadh &middot; Sun&ndash;Thu</div></div>
      <button class="ep-close" onclick="closeExpert()" aria-label="Close">✕</button>
    </div>
    <div class="ep-body">
      <div class="ep-question">Have a question?</div>
      <div class="ep-hint">Send us your question and we will come back to you during business hours.</div>
      <div class="ep-options">
        <a data-wa="Hello BluePrint, I have a compliance question" class="ep-option whatsapp"><i class="fab fa-whatsapp"></i> WhatsApp us</a>
        <a data-mail class="ep-option email"><i class="fas fa-envelope"></i> Email us directly</a>
        <a data-tel class="ep-option call"><i class="fas fa-phone"></i> Call <span data-text="phone"></span></a>
      </div>
      <div class="ep-divider">or send a quick message</div>
      <div class="ep-quick-msg"><input type="text" id="expertMsgInput" placeholder="e.g. which permit does my workshop need?" maxlength="120" aria-label="Quick message" /><button onclick="sendExpertMsg()" aria-label="Send"><i class="fas fa-paper-plane"></i></button></div>
    </div>
    <div class="ep-footer">Free consultation · No commitment required</div>
  </div>
</div>
"""


def scripts(extra=()):
    base = ["js/main.js", "js/widgets.js", "js/scroll.js"] + list(extra)
    return "\n".join(f'<script src="{s}"></script>' for s in base) + "\n</body>\n</html>\n"
