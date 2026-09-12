from cover_markup import COVER
from carousel_markup import CAROUSEL
from insights import insights
import content as _C

HOME = """
""" + COVER + """

<section id="overview" class="py-28 bg-white">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="grid lg:grid-cols-2 gap-12 items-center">
      <div class="scroll-reveal">
        <div class="inline-block px-4 py-2 bg-bp-light rounded-full text-bp-primary font-semibold text-sm mb-6">Who we are</div>
        <h2 class="text-2xl lg:text-3xl font-bold text-bp-ink mb-4 leading-tight">Built for the Kingdom&rsquo;s <span class="text-bp-olive">new rulebook</span></h2>
        <p class="text-gray-600 text-sm leading-relaxed mb-3">A Riyadh-based environmental consultancy, formed to meet the demand created by the Kingdom's accelerating environmental regulation &mdash; pairing Saudi competencies with international expertise.</p>
        <p class="text-gray-600 text-sm leading-relaxed mb-5">Clients range from government authorities to industrial and commercial operators &mdash; oil and gas, petrochemicals, manufacturing, power and desalination, cement, food, agriculture and urban development.</p>
        <div class="space-y-3 mb-6">
          <div class="flex items-start space-x-4"><div class="w-6 h-6 rounded-full bg-bp-primary flex items-center justify-center flex-shrink-0 mt-1"><i class="fas fa-check text-white text-xs"></i></div><div><h4 class="font-bold text-bp-ink">Our mission</h4><p class="text-gray-600 text-sm leading-relaxed">Innovative environmental solutions to the highest quality and safety standards, keeping clients fully compliant.</p></div></div>
          <div class="flex items-start space-x-4"><div class="w-6 h-6 rounded-full bg-bp-olive flex items-center justify-center flex-shrink-0 mt-1"><i class="fas fa-check text-white text-xs"></i></div><div><h4 class="font-bold text-bp-ink">Our vision</h4><p class="text-gray-600 text-sm leading-relaxed">Supporting national policy and growing the Kingdom&rsquo;s environmental sector into a regional reference for green innovation.</p></div></div>
        </div>
        <div class="flex flex-wrap gap-3">
          <span class="px-4 py-2 bg-bp-light text-bp-primary rounded-lg font-medium text-sm">NCEC Licensed</span>
          <span class="px-4 py-2 bg-bp-light text-bp-primary rounded-lg font-medium text-sm">MWAN Registered</span>
          <span class="px-4 py-2 bg-bp-light text-bp-primary rounded-lg font-medium text-sm">RCJY Approved</span>
        </div>
      </div>
      <div class="relative scroll-reveal">
        <div class="absolute -inset-4 rounded-3xl opacity-20 blur-2xl" style="background:var(--bp-grad);"></div>
        <div class="relative bg-white rounded-3xl shadow-2xl overflow-hidden">
          <img src="assets/img/about.jpg" alt="Saudi Red Sea coastline where desert meets protected shoreline" class="w-full h-52 object-cover" loading="lazy" />
          <div class="p-7">
            <h3 class="text-xl font-bold text-bp-ink mb-5">Aligned with Vision 2030</h3>
            <div class="space-y-2.5">
              <div class="flex items-start gap-3 p-3.5 bg-gray-50 rounded-xl"><span class="font-display font-extrabold text-bp-primary">01</span><div><p class="font-semibold text-bp-ink text-sm">Vibrant Society</p><p class="text-xs text-gray-600 mt-1">A cleaner, healthier environment that improves quality of life across the Kingdom.</p></div></div>
              <div class="flex items-start gap-3 p-3.5 bg-gray-50 rounded-xl"><span class="font-display font-extrabold text-bp-primary">02</span><div><p class="font-semibold text-bp-ink text-sm">Thriving Economy</p><p class="text-xs text-gray-600 mt-1">Responsible industrial growth through compliant waste and environmental management.</p></div></div>
              <div class="flex items-start gap-3 p-3.5 bg-gray-50 rounded-xl"><span class="font-display font-extrabold text-bp-primary">03</span><div><p class="font-semibold text-bp-ink text-sm">Ambitious Nation</p><p class="text-xs text-gray-600 mt-1">Advancing circular-economy practice and environmental governance.</p></div></div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- SERVICES — three cards, click to expand -->
""" + CAROUSEL + """

<section id="services" class="svc-section" style="background:var(--bp-page);">
  <div class="svc-container mx-auto px-4 sm:px-6 lg:px-8">
    <div class="svc-head text-center scroll-reveal">
      <div class="showcase-eyebrow">What we do</div>
      <h2 class="svc-h2 font-bold text-bp-ink mb-3 tracking-tight">Take on any obligation</h2>
      <p class="text-gray-600 text-sm max-w-lg mx-auto leading-relaxed">Three service lines covering the whole compliance lifecycle.</p>
    </div>

    <div class="svc-showcase scroll-reveal">
      <div class="svc-stage" id="svcStage"></div>
      <p class="svc-hint">Hover a card to preview &middot; click to open the full list</p>
    </div>
  </div>
</section>

<!-- FULL-SCREEN SERVICE OVERLAY -->
<div class="svc-overlay" id="svcOverlay" role="dialog" aria-modal="true" aria-hidden="true" aria-label="Service list">
  <div class="svc-ov-bg" id="svcOvBg" aria-hidden="true"></div>
  <div class="svc-ov-scrim" aria-hidden="true"></div>
  <button class="svc-ov-close" id="svcOvClose" onclick="closeSvcOverlay()" aria-label="Close">&times;</button>
  <div class="svc-ov-inner">
    <div class="svc-ov-head">
      <div class="svc-ov-kicker" id="svcOvKicker"></div>
      <h2 id="svcOvTitle"></h2>
      <p id="svcOvBlurb"></p>
    </div>
    <div class="svc-ov-grid" id="svcOvGrid"></div>
    <div class="svc-ov-foot">
      <a href="services.html" class="svc-ov-btn" id="svcOvLink">See full detail <i class="fas fa-arrow-right" style="font-size:.7rem;"></i></a>
      <a href="contact.html" class="svc-ov-btn ghost">Talk to a consultant</a>
    </div>
  </div>
</div>

<!-- WHAT IT MEANS FOR YOU — alternating feature blocks -->
<section class="py-28 bg-white">
  <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 space-y-20">

    <div class="grid lg:grid-cols-2 gap-12 items-center scroll-reveal">
      <div>
        <div class="showcase-eyebrow">Before you build</div>
        <h3 class="text-2xl lg:text-3xl font-bold text-bp-ink mb-4 leading-tight">Get licensed without losing a quarter</h3>
        <p class="text-gray-600 leading-relaxed mb-5">Most delays are not technical. They come from a misclassified activity or a file missing one supporting study. We classify first, then build the submission around what the reviewer will actually ask for.</p>
        <a href="services.html#svc-0" class="btn-ghost">Environmental permits <i class="fas fa-arrow-right" style="font-size:.7rem;"></i></a>
      </div>
      <div class="rounded-2xl overflow-hidden shadow-lg"><img src="assets/img/feature-1.jpg" alt="Coastal industrial development" class="w-full h-72 object-cover" loading="lazy" /></div>
    </div>

    <div class="grid lg:grid-cols-2 gap-12 items-center scroll-reveal">
      <div class="rounded-2xl overflow-hidden shadow-lg lg:order-1"><img src="assets/img/feature-2.jpg" alt="Desert landscape under monitoring" class="w-full h-72 object-cover" loading="lazy" /></div>
      <div class="lg:order-2">
        <div class="showcase-eyebrow">While you operate</div>
        <h3 class="text-2xl lg:text-3xl font-bold text-bp-ink mb-4 leading-tight">Never scramble for an inspection again</h3>
        <p class="text-gray-600 leading-relaxed mb-5">Inspectors ask for the register first. We keep yours current, run the measurements your permit specifies, and file the periodic reports on schedule &mdash; so an inspection is a document check, not a fire drill.</p>
        <a href="services.html#monitoring" class="btn-ghost">Monitoring &amp; reporting <i class="fas fa-arrow-right" style="font-size:.7rem;"></i></a>
      </div>
    </div>

    <div class="grid lg:grid-cols-2 gap-12 items-center scroll-reveal">
      <div>
        <div class="showcase-eyebrow">When it renews</div>
        <h3 class="text-2xl lg:text-3xl font-bold text-bp-ink mb-4 leading-tight">Renewals decided long before you apply</h3>
        <p class="text-gray-600 leading-relaxed mb-5">Renewal review examines the whole permit term, not the application. Clients on ongoing reporting renew from a record that was maintained throughout &mdash; rather than assembled, and audited, at the last minute.</p>
        <a href="blog-environmental-permit-renewal.html" class="btn-ghost">Read the renewal guide <i class="fas fa-arrow-right" style="font-size:.7rem;"></i></a>
      </div>
      <div class="rounded-2xl overflow-hidden shadow-lg"><img src="assets/img/feature-3.jpg" alt="Shoreline and protected vegetation" class="w-full h-72 object-cover" loading="lazy" /></div>
    </div>

  </div>
</section>

""" + insights(_C.load_blog()) + """

<!-- HOW WE WORK -->
<section id="process" class="py-28 text-white relative" style="background:var(--bp-blue-ink);">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
    <div class="text-center mb-20 scroll-reveal">
      <div class="text-xs uppercase text-bp-sage font-semibold mb-4" style="letter-spacing:.22em;">How we work</div>
      <h2 class="text-4xl lg:text-5xl font-bold mb-5 tracking-tight">Compliance without the guesswork</h2>
      <p class="text-gray-300 text-base max-w-2xl mx-auto leading-relaxed">A systematic workflow from the first site visit through to reporting that keeps you compliant cycle after cycle</p>
    </div>
    <div class="relative">
      <div class="hidden lg:block absolute left-0 right-0 h-px bg-white/15" style="top:11.5rem;"></div>
      <div class="grid sm:grid-cols-2 lg:grid-cols-5 gap-5">
PROCESS_CARDS      </div>
    </div>
  </div>
</section>

<!-- ACCREDITED & TRUSTED (merged: credentials + accreditations + why us) -->
<section id="accreditations" class="py-28 bg-white">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">

    <div class="text-center mb-16 scroll-reveal">
      <div class="showcase-eyebrow">Accredited &amp; trusted</div>
      <h2 class="text-4xl lg:text-5xl font-bold text-bp-ink mb-5 tracking-tight">Accredited where it matters</h2>
      <p class="text-gray-600 text-base max-w-xl mx-auto leading-relaxed">Permit files are only accepted from accredited parties. We hold active registration with every authority that matters.</p>
    </div>

    <div class="grid md:grid-cols-4 gap-5 mb-14 scroll-reveal">
      <div class="text-center px-5 py-8 rounded-2xl" style="background:var(--bp-blue-tint);">
        <div class="text-4xl font-bold stat-number mb-2">20+</div>
        <p class="text-sm text-gray-600 font-medium">Licensed environmental activities</p>
      </div>
      <div class="text-center px-5 py-8 rounded-2xl" style="background:var(--bp-blue-tint);">
        <div class="text-4xl font-bold stat-number mb-2">7</div>
        <p class="text-sm text-gray-600 font-medium">Licences &amp; accreditations held</p>
      </div>
      <div class="text-center px-5 py-8 rounded-2xl" style="background:var(--bp-blue-tint);">
        <div class="text-4xl font-bold stat-number mb-2">7</div>
        <p class="text-sm text-gray-600 font-medium">Service categories</p>
      </div>
      <div class="text-center px-5 py-8 rounded-2xl" style="background:var(--bp-blue-tint);">
        <div class="text-4xl font-bold stat-number mb-2">KSA</div>
        <p class="text-sm text-gray-600 font-medium">Riyadh-based, Kingdom-wide</p>
      </div>
    </div>

    <div class="flex flex-wrap justify-center gap-3 mb-16 scroll-reveal">
      <span class="px-5 py-3 bg-white border rounded-xl text-sm font-semibold text-bp-ink" style="border-color:var(--bp-border);">NCEC Licence</span>
      <span class="px-5 py-3 bg-white border rounded-xl text-sm font-semibold text-bp-ink" style="border-color:var(--bp-border);">MWAN Registration</span>
      <span class="px-5 py-3 bg-white border rounded-xl text-sm font-semibold text-bp-ink" style="border-color:var(--bp-border);">Royal Commission for Jubail &amp; Yanbu</span>
      <span class="px-5 py-3 bg-white border rounded-xl text-sm font-semibold text-bp-ink" style="border-color:var(--bp-border);">IAS Accreditation</span>
      <span class="px-5 py-3 bg-white border rounded-xl text-sm font-semibold text-bp-ink" style="border-color:var(--bp-border);">ISO 9001:2015</span>
      <span class="px-5 py-3 bg-white border rounded-xl text-sm font-semibold text-bp-ink" style="border-color:var(--bp-border);">ISO 14001</span>
      <span class="px-5 py-3 bg-white border rounded-xl text-sm font-semibold text-bp-ink" style="border-color:var(--bp-border);">ISO 45001:2018</span>
    </div>

    <div class="grid md:grid-cols-3 gap-8 scroll-reveal pt-12" style="border-top:1px solid var(--bp-border);">
      <div class="flex items-start gap-4">
        <span class="w-11 h-11 rounded-xl bg-bp-light text-bp-primary flex items-center justify-center flex-shrink-0"><i class="fas fa-stamp"></i></span>
        <div><h4 class="font-bold text-bp-ink mb-1">Reports authorities accept</h4><p class="text-sm text-gray-600 leading-relaxed">Government-accredited and NCEC-aligned, so your file clears review the first time.</p></div>
      </div>
      <div class="flex items-start gap-4">
        <span class="w-11 h-11 rounded-xl bg-bp-light text-bp-primary flex items-center justify-center flex-shrink-0"><i class="fas fa-sliders-h"></i></span>
        <div><h4 class="font-bold text-bp-ink mb-1">Built around your facility</h4><p class="text-sm text-gray-600 leading-relaxed">Solutions shaped to your sector and activity, never a generic template.</p></div>
      </div>
      <div class="flex items-start gap-4">
        <span class="w-11 h-11 rounded-xl bg-bp-light text-bp-primary flex items-center justify-center flex-shrink-0"><i class="fas fa-handshake"></i></span>
        <div><h4 class="font-bold text-bp-ink mb-1">One partner, whole lifecycle</h4><p class="text-sm text-gray-600 leading-relaxed">Licensing, studies and reporting under a single accountable team.</p></div>
      </div>
    </div>

  </div>
</section>

<!-- TRUSTED BY -->
<section id="clients" class="py-24 bg-white">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="text-center mb-14 scroll-reveal">
      <div class="showcase-eyebrow">Trusted by</div>
      <h2 class="text-4xl lg:text-5xl font-bold text-bp-ink mb-5 tracking-tight">Our partners and clients</h2>
      <p class="text-gray-600 text-base max-w-xl mx-auto leading-relaxed">Organisations across industry, energy, infrastructure and government that rely on our environmental work.</p>
    </div>
  </div>
  <div class="logo-marquee scroll-reveal" aria-label="Client logos">
    <div class="logo-track">
CLIENT_LOGOS    </div>
  </div>
</section>\n\n<!-- SECTORS -->
<section id="sectors" class="py-28" style="background:var(--bp-page);">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="text-center mb-16 scroll-reveal">
      <div class="inline-block px-4 py-2 bg-bp-light rounded-full text-bp-primary font-semibold text-sm mb-4">Who we serve</div>
      <h2 class="text-4xl lg:text-5xl font-bold text-bp-ink mb-5 tracking-tight">Every regulated sector</h2>
      <p class="text-gray-600 text-base max-w-xl mx-auto leading-relaxed">We tailor compliance strategy to the obligations, risks and inspection cycles of your industry.</p>
    </div>
    <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-6 scroll-reveal">
SECTOR_CARDS    </div>
  </div>
</section>

"""

PROCESS = [
    (1, "assets/img/svc-permit.jpg", "Project scoping",
     "Site visit and regulatory review, then a written scope agreed before any fieldwork begins."),
    (2, "assets/img/svc-field.jpg", "Site assessment",
     "Field reconnaissance, existing conditions, and the receptor locations that apply to your activity."),
    (3, "assets/img/svc-sampling.jpg", "Field measurement",
     "Sampling and monitoring carried out to the standard your permit requires."),
    (4, "assets/img/svc-report.jpg", "Laboratory analysis",
     "Analysis and data validation against the applicable limit values."),
    (5, "assets/img/svc-register.jpg", "Reporting",
     "A submission-ready report, then register upkeep that keeps you compliant cycle after cycle."),
]

CLIENTS = [
    ("aramco", "Saudi Aramco"),
    ("neom", "NEOM"),
    ("red-sea", "The Red Sea Development Company"),
    ("pif", "Public Investment Fund"),
    ("zatca", "Zakat, Tax and Customs Authority"),
    ("sabic", "SABIC"),
    ("maaden", "Ma'aden"),
    ("mewa", "Ministry of Environment, Water and Agriculture"),
    ("saudi-electricity", "Saudi Electricity Company"),
    ("national-water", "National Water Company"),
    ("mawani", "MAWANI, Saudi Ports Authority"),
    ("ncm", "National Center for Meteorology"),
    ("saudi-water-authority", "Saudi Water Authority"),
    ("gami", "General Authority for Military Industries"),
    ("sami", "SAMI"),
    ("kaec", "King Abdullah Economic City"),
    ("yasref", "YASREF"),
    ("samref", "SAMREF"),
    ("luberef", "Luberef"),
    ("yansab", "Yansab"),
    ("nomac", "NOMAC"),
    ("veolia", "Veolia"),
    ("unilever", "Unilever"),
    ("abdul-latif-jameel", "Abdul Latif Jameel"),
    ("qassim-cement", "Qassim Cement"),
    ("arabian-cement", "Arabian Cement"),
    ("najran-cement", "Najran Cement"),
    ("hail-cement", "Hail Cement"),
    ("marafiq", "Marafiq"),
    ("petro-rabigh", "Petro Rabigh"),
    ("cruise-saudi", "Cruise Saudi"),
    ("jeddah-airports", "Jeddah Airports"),
]

SECTORS = [
    ("assets/img/svc-lab.jpg", "fa-industry", "Industrial",
     "Factories &amp; Manufacturing",
     "Manufacturing carries the heaviest environmental obligations in the Kingdom — and the most expensive consequences for getting them wrong."),
    ("assets/img/svc-soil.jpg", "fa-tools", "Light industry",
     "Workshops &amp; Garages",
     "Small premises, real obligations. Most workshop owners only discover the requirement when a licence renewal gets blocked."),
    ("assets/img/svc-noise.jpg", "fa-hospital", "Healthcare",
     "Healthcare &amp; Veterinary",
     "Medical waste carries the strictest handling rules in the Kingdom — and clinics are inspected against them from the day they open."),
    ("assets/img/svc-field.jpg", "fa-hard-hat", "Infrastructure",
     "Construction &amp; Infrastructure",
     "Impacts are temporary but intense, and enforcement happens on the ground — where the site team either follows the plan or does not."),
    ("assets/img/spec-marine.jpg", "fa-store", "Commercial",
     "Commercial &amp; Retail",
     "Retail and service premises sit on the simplified track — but the permit is still a condition of your commercial licence."),
    ("assets/img/spec-ecology.jpg", "fa-mountain", "Extraction",
     "Quarries &amp; Mining Sites",
     "Extraction sites commit to a rehabilitation obligation years before it comes due — and it does not lapse."),
]


def home():
    proc = "".join(
        f"""        <div class="relative scroll-reveal group h-full flex flex-col"><div class="w-14 h-14 ml-6 bg-white rounded-xl flex items-center justify-center text-xl font-bold text-bp-ink relative z-20 flex-shrink-0">{n}</div><div class="bg-white/5 rounded-2xl overflow-hidden border border-white/10 group-hover:border-white/30 transition-colors duration-300 flex-1" style="margin-top:-1.75rem"><div style="height:1.75rem"></div><img src="{img}" alt="{t}" loading="lazy" class="w-full h-32 object-cover opacity-85 group-hover:opacity-100 transition-opacity duration-500" onerror="this.style.display='none'" /><div class="p-6"><h4 class="font-bold text-base mb-2 text-bp-sage">{t}</h4><p class="text-sm leading-relaxed text-gray-300">{d}</p></div></div></div>\n"""
        for n, img, t, d in PROCESS)
    clients = "".join(
        f"""      <div class="logo-item"><img src="assets/brand/client-{slug}.png" alt="{name}" loading="lazy" /></div>\n"""
        for slug, name in CLIENTS) * 2
    sect = "".join(
        f"""      <a href="services.html" class="group relative overflow-hidden rounded-2xl shadow-lg cursor-pointer block"><img src="{img}" alt="{title}" class="w-full h-64 object-cover transform group-hover:scale-110 transition-transform duration-500" /><div class="absolute inset-0 opacity-90" style="background:linear-gradient(to top,#0b2f38 0%,rgba(11, 47, 56,.5) 50%,transparent 100%);"></div><div class="absolute bottom-0 left-0 right-0 p-6 text-white"><div class="flex items-center space-x-2 mb-2"><i class="fas {icon} text-bp-sage"></i><span class="text-sm font-medium text-bp-sage">{cat}</span></div><h3 class="text-xl font-bold mb-2">{title}</h3><p class="text-sm text-gray-300">{desc}</p></div></a>\n"""
        for img, icon, cat, title, desc in SECTORS)
    return HOME.replace("PROCESS_CARDS", proc).replace("SECTOR_CARDS", sect).replace("CLIENT_LOGOS", clients)
