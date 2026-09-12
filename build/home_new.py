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

<!-- ACCREDITED & TRUSTED -->
<section id="accreditations" class="py-20 bg-white">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="acr-split scroll-reveal">
      <div class="acr-panel">
        <div class="acr-kick">Accredited &amp; trusted</div>
        <h2>Accredited where it matters</h2>
        <p>Permit files are only accepted from accredited parties. Every credential below names the authority that issued it.</p>
        <div class="acr-big"><b>20+</b><span>Licensed environmental activities</span></div>
      </div>
      <div class="acr-grid">
        <div class="acr-card"><img src="assets/accred/accred-ncec.png" alt="National Center for Environmental Compliance" loading="lazy" /><b>Environmental consulting licence</b><span>NCEC</span></div>
        <div class="acr-card"><img src="assets/accred/accred-mwan.png" alt="National Center for Waste Management" loading="lazy" /><b>Waste management provider</b><span>MWAN</span></div>
        <div class="acr-card"><img src="assets/accred/accred-rcjy.png" alt="Royal Commission for Jubail and Yanbu" loading="lazy" /><b>Approved service provider</b><span>Royal Commission, Jubail &amp; Yanbu</span></div>
        <div class="acr-card"><img src="assets/accred/accred-ias.png" alt="International Accreditation Service" loading="lazy" /><b>Laboratory &amp; inspection</b><span>IAS</span></div>
        <div class="acr-card"><img src="assets/accred/accred-iso-14001.png" alt="ISO 14001 certified" loading="lazy" /><b>ISO 14001</b><span>Environmental management</span></div>
        <div class="acr-card"><img src="assets/accred/accred-iso.png" alt="ISO certified" loading="lazy" /><b>ISO 9001 &amp; 45001</b><span>Quality, health &amp; safety</span></div>
      </div>
    </div>

    <div class="grid md:grid-cols-3 gap-8 scroll-reveal pt-12 mt-12" style="border-top:1px solid var(--bp-border);">
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
    ("assets/img/sector-industrial.webp", "fa-industry", "Industrial",
     "Factories &amp; Manufacturing",
     "The heaviest environmental obligations in the Kingdom, and the most expensive consequences for getting them wrong.",
     "Permit, EMP, periodic reporting", "service-environmental-permit.html"),
    ("assets/img/sector-light-industry.webp", "fa-tools", "Light industry",
     "Workshops &amp; Garages",
     "Small premises, real obligations. Most owners find out when a licence renewal is blocked.",
     "Simplified permit track", "service-environmental-permit.html"),
    ("assets/img/sector-healthcare.webp", "fa-hospital", "Healthcare",
     "Healthcare &amp; Veterinary",
     "Medical waste carries the strictest handling rules, enforced from the day a clinic opens.",
     "MWAN waste permit, manifests", "service-waste-management-permit.html"),
    ("assets/img/sector-infrastructure.webp", "fa-hard-hat", "Infrastructure",
     "Construction &amp; Infrastructure",
     "Impacts are temporary but intense, and enforcement happens on the ground.",
     "CEMP, dust and noise monitoring", "service-environmental-management-plan.html"),
    ("assets/img/sector-commercial.webp", "fa-store", "Commercial",
     "Commercial &amp; Retail",
     "The simplified track still ties the permit to your commercial licence.",
     "Simplified permit, waste contract", "service-environmental-permit.html"),
    ("assets/img/sector-extraction.webp", "fa-mountain", "Extraction",
     "Quarries &amp; Mining Sites",
     "Rehabilitation is committed to years before it comes due, and does not lapse.",
     "EIA, rehabilitation plan", "service-treatment-rehabilitation.html"),
]


def home():
    proc = "".join(
        f"""        <div class="relative scroll-reveal group h-full flex flex-col"><div class="w-14 h-14 ml-6 bg-white rounded-xl flex items-center justify-center text-xl font-bold text-bp-ink relative z-20 flex-shrink-0">{n}</div><div class="bg-white/5 rounded-2xl overflow-hidden border border-white/10 group-hover:border-white/30 transition-colors duration-300 flex-1" style="margin-top:-1.75rem"><div style="height:1.75rem"></div><img src="{img}" alt="{t}" loading="lazy" class="w-full h-32 object-cover opacity-85 group-hover:opacity-100 transition-opacity duration-500" onerror="this.style.display='none'" /><div class="p-6"><h4 class="font-bold text-base mb-2 text-bp-sage">{t}</h4><p class="text-sm leading-relaxed text-gray-300">{d}</p></div></div></div>\n"""
        for n, img, t, d in PROCESS)
    clients = "".join(
        f"""      <div class="logo-item"><img src="assets/brand/client-{slug}.png" alt="{name}" loading="lazy" /></div>\n"""
        for slug, name in CLIENTS) * 2
    sect = "".join(
        f"""      <a href="{href}" class="sect-card"><span class="sect-img" style="background-image:url(\'{img}\')"></span><span class="sect-scrim"></span><span class="sect-shine"></span><span class="sect-edge"></span><span class="sect-tag">{cat}</span><span class="sect-body"><span class="sect-t"><i class="fas {icon}"></i>{title}</span><span class="sect-d">{desc}</span><span class="sect-rev"><span class="sect-obl"><b>Typically</b>{obl}</span><span class="sect-go">See the service <i class="fas fa-arrow-right"></i></span></span></span></a>\n"""
        for img, icon, cat, title, desc, obl, href in SECTORS)
    return HOME.replace("PROCESS_CARDS", proc).replace("SECTOR_CARDS", sect).replace("CLIENT_LOGOS", clients)
