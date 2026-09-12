# Page-specific sections for the BluePrint site build.

def page_header(title, subtitle, crumb):
    return f"""
<section class="page-header">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
    <div class="crumb"><a href="index.html">Home</a><i class="fas fa-chevron-right" style="font-size:.55rem;"></i><span>{crumb}</span></div>
    <h1>{title}</h1>
    <p>{subtitle}</p>
  </div>
</section>
"""


from home_new import home  # noqa: E402  (real BluePrint home content)
from content_new import SERVICE_TABS, SERVICES_JS, LAB_SERVICES, CATEGORIES, ACCREDITATIONS  # noqa: E402


# ─────────────────────────── SERVICES ───────────────────────────
def services():
    tabs = "".join(f"""
      <div class="isvc-tab{' active' if i == 0 else ''}" onclick="selectService({i})" id="svc-{i}">
        <div class="isvc-tab-trigger">
          <div class="isvc-tab-num">0{i+1}</div><div class="isvc-tab-icon"><i class="fas {icon}"></i></div>
          <div class="isvc-tab-body"><div class="isvc-tab-name">{name}</div><div class="isvc-tab-short">{short}</div></div>
          <div class="isvc-tab-chevron"><i class="fas fa-chevron-right"></i></div>
        </div>
        <div class="isvc-accordion-content">
          <img class="isvc-acc-img" src="{img}?w=800&h=400&fit=crop&q=80" alt="" loading="lazy"/>
          <div class="isvc-acc-body" id="isvc-acc-body-{i}"></div>
        </div>
      </div>""" for i, (icon, name, short, img, fb, badge, bcls) in enumerate(SERVICE_TABS))
    panels = "".join(f"""
      <div class="isvc-panel{' active' if i == 0 else ''}" id="isvc-panel-{i}">
        <div class="isvc-panel-img"><img src="{img}?w=1200&h=520&fit=crop&q=80" alt="" onerror="this.src='{fb}?w=1200&h=520&fit=crop'"/><div class="isvc-panel-img-overlay"></div><div class="isvc-panel-badge{bcls}">{badge}</div><div class="isvc-panel-watermark">0{i+1}</div></div>
        <div class="isvc-panel-body" id="isvc-panel-body-{i}"></div>
      </div>""" for i, (icon, name, short, img, fb, badge, bcls) in enumerate(SERVICE_TABS))
    mons = "".join(f'''
        <a href="technology.html#equipment" class="flex items-center gap-3 px-4 py-3.5 bg-white rounded-xl border hover:border-bp-olive transition-all" style="border-color:var(--bp-border);text-decoration:none;">
          <span class="w-9 h-9 rounded-lg flex items-center justify-center text-sm flex-shrink-0" style="background:var(--bp-olive-tint);color:var(--bp-olive);"><i class="fas {ic}"></i></span>
          <span class="font-display font-semibold text-bp-ink text-sm leading-snug">{nm}</span>
        </a>''' for _img, _fb, _bd, ic, nm, _d in LAB_SERVICES)
    cats = "".join(f'''
      <div class="bg-white rounded-2xl p-7 shadow-sm border hover:shadow-lg transition-all" style="border-color:var(--bp-border);">
        <div class="flex items-start justify-between mb-4">
          <div class="w-12 h-12 rounded-xl bg-bp-light flex items-center justify-center text-bp-primary text-lg"><i class="fas {ic}"></i></div>
          <span class="text-xs font-semibold px-3 py-1 rounded-full" style="background:var(--bp-olive-tint);color:var(--bp-olive-deep);">{cnt}</span>
        </div>
        <h3 class="font-display font-bold text-bp-ink text-lg mb-2">{nm}</h3>
        <p class="text-sm text-gray-600 leading-relaxed">{d}</p>
      </div>''' for ic, nm, cnt, d in CATEGORIES)
    return page_header("A full spectrum of environmental services",
                       "From pre-licensing impact assessments to continuous periodic reporting, every service is delivered by accredited consultants who know the Saudi regulatory landscape inside out.",
                       "Services") + f"""
<section id="permitting" class="isvc-section" style="padding-top:56px;">
  <div class="isvc-header" style="margin-bottom:44px;">
    <div class="showcase-eyebrow">Compliance &amp; permitting</div>
    <h2>Getting you licensed, and keeping you licensed</h2>
    <p>The studies, permits and reporting cycles that stand between your facility and a valid environmental licence.</p>
  </div>
  <div class="isvc-layout">
    <div class="isvc-tabs isvc-reveal" id="isvcTabs">{tabs}
    </div>
    <div class="isvc-panel-wrap isvc-reveal isvc-reveal-delay-1" id="isvcPanelWrap">
      <div class="isvc-progress-bar" id="isvcProgressBar" style="width:16.66%"></div>{panels}
    </div>
  </div>
</section>

<section id="monitoring" class="py-28 bg-white">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="text-center mb-16 scroll-reveal">
      <div class="showcase-eyebrow">Monitoring &amp; testing</div>
      <h2 class="text-4xl lg:text-5xl font-bold text-bp-ink mb-5 tracking-tight">The measurements behind the paperwork</h2>
      <p class="text-gray-600 max-w-2xl mx-auto">A permit is only as good as the data behind it. We carry out the sampling and testing your conditions require, to the method they require.</p>
    </div>
    <div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-3 scroll-reveal max-w-5xl mx-auto">{mons}
    </div>
    <div class="text-center mt-10 scroll-reveal"><a href="technology.html" class="btn-olive">Full laboratory services <i class="fas fa-arrow-right" style="font-size:.75rem;"></i></a></div>
  </div>
</section>

<section class="py-28" style="background:var(--bp-page);">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="text-center mb-16 scroll-reveal">
      <div class="showcase-eyebrow">Beyond permitting</div>
      <h2 class="text-4xl lg:text-5xl font-bold text-bp-ink mb-5 tracking-tight">Six further service categories</h2>
      <p class="text-gray-600 max-w-2xl mx-auto">Alongside permitting and monitoring, BluePrint delivers specialist work across sustainability, ecology, marine, remediation, modelling and laboratory services.</p>
    </div>
    <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-6 scroll-reveal">{cats}
    </div>
    <div class="text-center mt-12 scroll-reveal"><a href="contact.html" class="btn-primary">Request a scope <i class="fas fa-arrow-right" style="font-size:.75rem;"></i></a></div>
  </div>
</section>
"""


# ─────────────────────────── TECHNOLOGY ─────────────────────────
def technology():
    cards = "".join(f"""
      <div class="equipment-card bg-gray-50 rounded-2xl border-2 border-transparent hover:border-bp-primary cursor-pointer group overflow-hidden">
        <div class="relative w-full h-44 overflow-hidden bg-bp-light">
          <img src="{img}?w=600&h=380&fit=crop&q=80" alt="{title}" loading="lazy" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" onerror="this.src='{fb}?w=600&h=380&fit=crop'" />
          <div class="absolute inset-0 opacity-0 group-hover:opacity-100 transition-opacity duration-300" style="background:linear-gradient(to top,rgba(11, 47, 56.65),transparent);"></div>
          <span class="absolute bottom-3 left-3 text-xs font-bold text-white bg-bp-olive px-2 py-1 rounded-full opacity-0 group-hover:opacity-100 transition-opacity duration-300">{badge}</span>
        </div>
        <div class="p-5"><div class="flex items-center gap-2 mb-2"><div class="w-7 h-7 bg-bp-light rounded-lg flex items-center justify-center flex-shrink-0"><i class="fas {icon} text-bp-primary text-xs"></i></div><h4 class="font-bold text-bp-ink text-sm">{title}</h4></div><p class="text-xs text-gray-500 leading-relaxed">{desc}</p></div>
      </div>""" for img, fb, badge, icon, title, desc in LAB_SERVICES)
    _unused_accs = "".join(f"""
      <div class="bg-white p-7 rounded-2xl shadow-lg border-t-4 hover:-translate-y-1 transition-all" style="border-top-color:var(--bp-{'olive' if i % 2 else 'blue'});">
        <div class="w-14 h-14 rounded-2xl flex items-center justify-center text-xl mb-5" style="background:var(--bp-{'olive-tint' if i % 2 else 'blue-tint'});color:var(--bp-{'olive' if i % 2 else 'blue'});"><i class="fas {ic}"></i></div>
        <h3 class="text-base font-bold text-bp-ink mb-1 leading-snug">{name}</h3>
        <p class="text-xs font-semibold text-bp-primary mb-3">{body}</p>
        <p class="text-sm text-gray-600 leading-relaxed">{d}</p>
      </div>""" for i, (ic, name, body, d) in enumerate(ACCREDITATIONS))
    return page_header("Laboratory, measurement &amp; accreditation",
                       "Compliance claims need numbers behind them. We measure what your permit requires, to the method it requires, and report it in the form the regulator expects.",
                       "Laboratory") + f"""
<section id="equipment" class="py-28 bg-white">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="grid md:grid-cols-2 lg:grid-cols-4 gap-6 scroll-reveal">{cards}
    </div>
  </div>
</section>

<section id="standards" class="py-28" style="background:var(--bp-page);">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="text-center mb-16 scroll-reveal">
      <div class="showcase-eyebrow">Licences &amp; accreditations</div>
      <h2 class="text-4xl lg:text-5xl font-bold text-bp-ink mb-5 tracking-tight">Testing that carries weight</h2>
      <p class="text-gray-600 max-w-2xl mx-auto">Results are only accepted from accredited parties. <a href="index.html#accreditations" class="text-bp-primary font-semibold">See all seven licences and accreditations &rarr;</a></p>
    </div>
    <div class="rounded-3xl p-8 text-white scroll-reveal" style="background:var(--bp-grad);">
      <div class="grid md:grid-cols-2 gap-8 items-center">
        <div>
          <h3 class="text-2xl font-bold mb-4">Licensed across 20+ environmental activities</h3>
          <p class="text-gray-200 mb-6">BluePrint is licensed and approved by the NCEC, the National Center for Waste Management (MWAN) and the Royal Commission for Jubail &amp; Yanbu, spanning environmental studies and consulting, sustainability and corporate governance, industrial and hazardous waste management, landfill construction and lining, emergency response and site remediation.</p>
          <a href="contact.html" class="inline-flex items-center gap-2 px-6 py-3 bg-white text-bp-ink rounded-full font-bold text-sm hover:bg-bp-sage transition-all">Request our credentials <i class="fas fa-arrow-right" style="font-size:.7rem;"></i></a>
        </div>
        <div class="relative"><img src="assets/img/svc-permit.jpg" alt="Laboratory" class="rounded-2xl shadow-2xl opacity-90" loading="lazy" /></div>
      </div>
    </div>
  </div>
</section>
"""


# ─────────────────────────── CONTACT ────────────────────────────
def contact():
    return page_header("Let&rsquo;s map your path to compliance",
                       "Tell us about your facility and we&rsquo;ll identify the exact studies and permits you need. The initial consultation is free, and there&rsquo;s no obligation.",
                       "Contact") + """
<section id="contact" class="py-20" style="background:var(--bp-page);">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="grid lg:grid-cols-2 gap-16">
      <div class="scroll-reveal">
        <h2 class="text-3xl font-bold text-bp-ink mb-3">Talk to us directly</h2>
        <p class="text-gray-600 text-lg mb-8">Accredited environmental consultants based in Riyadh, working across the Kingdom.</p>
        <div class="space-y-6">
          <div class="flex items-start space-x-4"><div class="w-12 h-12 bg-bp-light rounded-xl flex items-center justify-center text-bp-primary flex-shrink-0"><i class="fas fa-envelope text-xl"></i></div><div><h4 class="font-bold text-bp-ink mb-1">Email</h4><p class="text-gray-600"><a data-mail data-text="email" class="hover:text-bp-primary transition-colors"></a></p></div></div>
          <div class="flex items-start space-x-4"><div class="w-12 h-12 bg-bp-light rounded-xl flex items-center justify-center text-bp-primary flex-shrink-0"><i class="fas fa-phone text-xl"></i></div><div><h4 class="font-bold text-bp-ink mb-1">Phone</h4><p class="text-gray-600"><a data-tel data-text="phone" class="hover:text-bp-primary transition-colors"></a></p></div></div>
          <div class="flex items-start space-x-4"><div class="w-12 h-12 bg-bp-light rounded-xl flex items-center justify-center text-bp-primary flex-shrink-0"><i class="fab fa-whatsapp text-xl"></i></div><div><h4 class="font-bold text-bp-ink mb-1">WhatsApp</h4><p class="text-gray-600"><a data-wa="Hello BluePrint, I would like to ask about your environmental services." data-text="phone" class="hover:text-bp-primary transition-colors"></a></p></div></div>
          <div class="flex items-start space-x-4"><div class="w-12 h-12 bg-bp-light rounded-xl flex items-center justify-center text-bp-primary flex-shrink-0"><i class="fas fa-map-marker-alt text-xl"></i></div><div><h4 class="font-bold text-bp-ink mb-1">Location</h4><p class="text-gray-600" data-text="address"></p></div></div>
          <div class="flex items-start space-x-4"><div class="w-12 h-12 bg-bp-light rounded-xl flex items-center justify-center text-bp-primary flex-shrink-0"><i class="fas fa-clock text-xl"></i></div><div><h4 class="font-bold text-bp-ink mb-1">Working hours</h4><p class="text-gray-600">Sunday &ndash; Thursday &middot; 9:00 AM &ndash; 6:00 PM (AST)</p></div></div>
        </div>
        <div class="mt-10 flex flex-wrap gap-3">
          <a data-wa="Hello BluePrint, I would like to arrange a site visit." class="btn-olive"><i class="fab fa-whatsapp" style="font-size:.9rem;"></i> Arrange a site visit</a>
          <a data-wa="Hello BluePrint, I would like to ask about your environmental services." class="btn-ghost"><i class="fab fa-whatsapp" style="font-size:.9rem;"></i> Chat on WhatsApp</a>
        </div>
      </div>
      <div class="scroll-reveal">
        <div class="bg-white rounded-3xl p-8 shadow-xl mb-6">
          <h3 class="text-2xl font-bold text-bp-ink mb-6">Tell us about your facility</h3>
          <div class="space-y-4">
            <div class="grid md:grid-cols-2 gap-4">
              <input type="text" placeholder="Full Name" aria-label="Full name" class="w-full px-4 py-3 rounded-xl border border-gray-200 focus:border-bp-primary focus:ring-2 focus:ring-bp-primary/20 outline-none transition-all" />
              <input type="text" placeholder="Company" aria-label="Company" class="w-full px-4 py-3 rounded-xl border border-gray-200 focus:border-bp-primary focus:ring-2 focus:ring-bp-primary/20 outline-none transition-all" />
            </div>
            <input type="email" placeholder="Email Address" aria-label="Email address" class="w-full px-4 py-3 rounded-xl border border-gray-200 focus:border-bp-primary focus:ring-2 focus:ring-bp-primary/20 outline-none transition-all" />
            <input type="tel" placeholder="Phone Number" aria-label="Phone number" class="w-full px-4 py-3 rounded-xl border border-gray-200 focus:border-bp-primary focus:ring-2 focus:ring-bp-primary/20 outline-none transition-all" />
            <select aria-label="Service interest" class="w-full px-4 py-3 rounded-xl border border-gray-200 focus:border-bp-primary outline-none transition-all text-gray-600 bg-white">
              <option value="">Which service do you need?</option>
              <option>Environmental Permit (NCEC)</option>
              <option>Environmental Impact Assessment</option>
              <option>Waste Management Permit (MWAN)</option>
              <option>Environmental Management Plan</option>
              <option>Environmental Register</option>
              <option>Periodic Environmental Report</option>
              <option>Environmental Measurements</option>
              <option>Not sure yet, please advise</option>
            </select>
            <textarea placeholder="Your activity, capacity, and roughly what you need&hellip;" aria-label="Facility details" rows="4" class="w-full px-4 py-3 rounded-xl border border-gray-200 focus:border-bp-primary outline-none transition-all resize-none"></textarea>
            <button onclick="sendContactMessage()" class="w-full py-4 bg-bp-primary text-white rounded-xl font-bold hover:bg-bp-dark transition-all shadow-lg">Send Message</button>
          </div>
        </div>
        <div class="bg-white rounded-3xl p-8 shadow-xl">
          <h3 class="text-lg font-bold text-bp-ink mb-5">What happens when you get in touch</h3>
          <div class="space-y-5">
            <div class="flex items-start gap-4"><span class="w-8 h-8 rounded-lg bg-bp-light text-bp-primary font-display font-bold text-sm flex items-center justify-center flex-shrink-0">01</span><div><p class="font-semibold text-bp-ink text-sm">You reach out</p><p class="text-sm text-gray-600 mt-1">Email, call, or WhatsApp us with your activity and roughly what you need.</p></div></div>
            <div class="flex items-start gap-4"><span class="w-8 h-8 rounded-lg bg-bp-light text-bp-primary font-display font-bold text-sm flex items-center justify-center flex-shrink-0">02</span><div><p class="font-semibold text-bp-ink text-sm">A short scoping call</p><p class="text-sm text-gray-600 mt-1">We ask about your activity, capacity, and site so we can classify it correctly.</p></div></div>
            <div class="flex items-start gap-4"><span class="w-8 h-8 rounded-lg bg-bp-light text-bp-primary font-display font-bold text-sm flex items-center justify-center flex-shrink-0">03</span><div><p class="font-semibold text-bp-ink text-sm">You get a written scope</p><p class="text-sm text-gray-600 mt-1">Exactly which permits and studies apply, what each involves, and a realistic timeline.</p></div></div>
          </div>
          <p class="mt-6 pt-5 border-t text-xs text-gray-500" style="border-color:var(--bp-border);">The initial consultation is free and carries no obligation.</p>
        </div>
      </div>
    </div>
  </div>
</section>
"""
