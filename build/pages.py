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


# ───────────────────────────── HOME ─────────────────────────────
def home():
    return """
<!-- HERO -->
<section class="relative min-h-screen flex items-center hero-gradient overflow-hidden">
  <div id="particles" class="absolute inset-0 overflow-hidden" aria-hidden="true"></div>
  <div class="relative z-10 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-32">
    <div class="grid lg:grid-cols-2 gap-12 items-center">
      <div class="text-white space-y-8 animate-slide-up">
        <div class="inline-flex items-center space-x-2 px-4 py-2 bg-white/10 rounded-full backdrop-blur-sm border border-white/20">
          <span class="w-2 h-2 bg-green-400 rounded-full animate-pulse"></span>
          <span class="text-sm font-medium">Delivering Excellence Since 2014</span>
        </div>
        <h1 class="text-4xl sm:text-5xl lg:text-7xl font-bold leading-tight">Air Quality <br><span class="text-bp-sage">Monitoring</span> &amp;<br>Environmental<br>Consultancy</h1>
        <p class="text-xl text-gray-200 max-w-lg leading-relaxed">Delivering precision environmental monitoring solutions across the Kingdom of Saudi Arabia with cutting-edge technology and regulatory expertise.</p>
        <div class="flex flex-wrap gap-4">
          <a href="services.html" class="px-8 py-4 bg-white text-bp-ink rounded-full font-bold hover:bg-bp-sage hover:text-bp-ink transition-all transform hover:scale-105 shadow-xl">Explore Services</a>
          <button onclick="openCalculator()" class="px-8 py-4 border-2 border-white text-white rounded-full font-bold hover:bg-white hover:text-bp-ink transition-all flex items-center gap-2"><i class="fas fa-calculator"></i> Free Calculator</button>
        </div>
        <div class="flex flex-wrap gap-2 pt-2">
          <button onclick="openPortal()" class="flex items-center gap-2 px-4 py-2 bg-white/15 backdrop-blur-sm rounded-full text-sm border border-white/30 hover:bg-white/25 transition-all"><i class="fas fa-folder-open text-bp-sage"></i> Client Portal</button>
          <button onclick="openCalculator('carbon')" class="flex items-center gap-2 px-4 py-2 bg-white/15 backdrop-blur-sm rounded-full text-sm border border-white/30 hover:bg-white/25 transition-all"><i class="fas fa-leaf text-green-300"></i> Carbon Calculator</button>
          <a href="resources.html#env-news-section" class="flex items-center gap-2 px-4 py-2 bg-white/15 backdrop-blur-sm rounded-full text-sm border border-white/30 hover:bg-white/25 transition-all"><i class="fas fa-newspaper text-bp-sage"></i> News Bulletin</a>
          <span class="flex items-center gap-2 px-4 py-2 bg-white/15 backdrop-blur-sm rounded-full text-sm border border-white/30"><i class="fas fa-robot text-bp-sage"></i> AI Chatbot Live</span>
        </div>
      </div>
      <div class="relative hidden lg:block">
        <img src="https://images.unsplash.com/photo-1497436072909-60f360e1d4b1?w=800&h=600&fit=crop" alt="Environmental Monitoring" class="rounded-3xl shadow-2xl transform hover:scale-105 transition-transform duration-700 object-cover h-[500px] w-full" />
        <div class="absolute -bottom-6 -left-6 bg-white rounded-2xl p-6 shadow-2xl animate-float">
          <div class="flex items-center space-x-4">
            <div class="w-12 h-12 bg-green-100 rounded-full flex items-center justify-center text-green-600"><i class="fas fa-leaf text-xl"></i></div>
            <div><p class="text-2xl font-bold text-bp-ink">1000+</p><p class="text-sm text-gray-600">Projects Completed</p></div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div class="absolute bottom-0 left-0 right-0" aria-hidden="true">
    <svg viewBox="0 0 1440 120" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M0 120L60 110C120 100 240 80 360 70C480 60 600 60 720 65C840 70 960 80 1080 85C1200 90 1320 90 1380 90L1440 90V120H1380C1320 120 1200 120 1080 120C960 120 840 120 720 120C600 120 480 120 360 120C240 120 120 120 60 120H0Z" fill="#f5f7fb" /></svg>
  </div>
</section>

<!-- STATS BAR -->
<section class="py-20 -mt-20 relative z-20">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="grid grid-cols-2 md:grid-cols-4 gap-6">
      <div class="bg-white rounded-2xl p-8 shadow-lg hover:shadow-xl transition-shadow text-center group"><div class="text-4xl font-bold stat-number mb-2 group-hover:scale-110 transition-transform inline-block">10+</div><p class="text-gray-600 font-medium">Years Experience</p></div>
      <div class="bg-white rounded-2xl p-8 shadow-lg hover:shadow-xl transition-shadow text-center group"><div class="text-4xl font-bold stat-number mb-2 group-hover:scale-110 transition-transform inline-block">1000+</div><p class="text-gray-600 font-medium">Completed Projects</p></div>
      <div class="bg-white rounded-2xl p-8 shadow-lg hover:shadow-xl transition-shadow text-center group"><div class="text-4xl font-bold stat-number mb-2 group-hover:scale-110 transition-transform inline-block">50+</div><p class="text-gray-600 font-medium">Specialists</p></div>
      <div class="bg-white rounded-2xl p-8 shadow-lg hover:shadow-xl transition-shadow text-center group"><div class="text-4xl font-bold stat-number mb-2 group-hover:scale-110 transition-transform inline-block">5</div><p class="text-gray-600 font-medium">Regional Offices</p></div>
    </div>
  </div>
</section>

<!-- COMPANY OVERVIEW -->
<section id="overview" class="py-24 bg-white">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="grid lg:grid-cols-2 gap-16 items-center">
      <div class="scroll-reveal">
        <div class="inline-block px-4 py-2 bg-bp-light rounded-full text-bp-primary font-semibold text-sm mb-6">About BluePrint</div>
        <h2 class="text-4xl font-bold text-bp-ink mb-6 leading-tight">Environmental Excellence for a <span class="text-bp-olive">Sustainable Future</span></h2>
        <p class="text-gray-600 text-lg leading-relaxed mb-6">BluePrint Environmental Services is a leading environmental consultancy based in Riyadh, KSA, providing integrated environmental solutions to industrial, infrastructure, and development clients.</p>
        <div class="space-y-4 mb-8">
          <div class="flex items-start space-x-4"><div class="w-6 h-6 rounded-full bg-bp-primary flex items-center justify-center flex-shrink-0 mt-1"><i class="fas fa-check text-white text-xs"></i></div><div><h4 class="font-bold text-bp-ink">Mission</h4><p class="text-gray-600">To deliver world-class environmental consultancy that ensures sustainable development through scientific excellence and regulatory compliance.</p></div></div>
          <div class="flex items-start space-x-4"><div class="w-6 h-6 rounded-full bg-bp-olive flex items-center justify-center flex-shrink-0 mt-1"><i class="fas fa-check text-white text-xs"></i></div><div><h4 class="font-bold text-bp-ink">Vision</h4><p class="text-gray-600">To be the most trusted environmental partner across the Middle East.</p></div></div>
        </div>
        <div class="flex flex-wrap gap-3">
          <span class="px-4 py-2 bg-bp-light text-bp-primary rounded-lg font-medium text-sm">ISO Accredited</span>
          <span class="px-4 py-2 bg-bp-light text-bp-primary rounded-lg font-medium text-sm">NCEC Compliant</span>
          <span class="px-4 py-2 bg-bp-light text-bp-primary rounded-lg font-medium text-sm">US EPA Methods</span>
        </div>
      </div>
      <div class="relative scroll-reveal">
        <div class="absolute -inset-4 rounded-3xl opacity-20 blur-2xl" style="background:var(--bp-grad);"></div>
        <div class="relative bg-white rounded-3xl shadow-2xl overflow-hidden">
          <img src="https://images.unsplash.com/photo-1532601224476-15c79f2f7a51?w=600&h=400&fit=crop" alt="Our Presence" class="w-full h-64 object-cover" />
          <div class="p-8">
            <h3 class="text-2xl font-bold text-bp-ink mb-6">Our Presence</h3>
            <div class="space-y-4">
              <div class="flex items-center justify-between p-4 bg-gray-50 rounded-xl"><div class="flex items-center space-x-3"><i class="fas fa-building text-bp-primary"></i><span class="font-medium">Head Office</span></div><span class="text-gray-600">Riyadh, KSA</span></div>
              <div class="flex items-center justify-between p-4 bg-gray-50 rounded-xl"><div class="flex items-center space-x-3"><i class="fas fa-code-branch text-bp-olive"></i><span class="font-medium">Branches</span></div><span class="text-gray-600">Jeddah, Dammam</span></div>
              <div class="flex items-center justify-between p-4 bg-gray-50 rounded-xl"><div class="flex items-center space-x-3"><i class="fas fa-globe text-bp-sage"></i><span class="font-medium">International</span></div><span class="text-gray-600">Cairo, Milan</span></div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- SERVICES PREVIEW -->
<section id="services" class="py-24" style="background:var(--bp-page);">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="text-center mb-14 scroll-reveal">
      <div class="showcase-eyebrow">Our Expertise</div>
      <h2 class="text-4xl font-bold text-bp-ink mb-4">Solutions for every environmental challenge</h2>
      <p class="text-gray-600 max-w-2xl mx-auto">Full-spectrum environmental monitoring and consultancy across the Kingdom of Saudi Arabia.</p>
    </div>
    <div class="svc-preview scroll-reveal">
      <a href="services.html#svc-0" class="svc-preview-card"><div class="svc-preview-icon"><i class="fas fa-wind"></i></div><div><div class="svc-preview-name">Ambient Air Quality</div><div class="svc-preview-short">PM2.5, PM10, NO₂, SO₂ &amp; ozone</div></div></a>
      <a href="services.html#svc-1" class="svc-preview-card"><div class="svc-preview-icon"><i class="fas fa-smog"></i></div><div><div class="svc-preview-name">Stack Emission Testing</div><div class="svc-preview-short">US EPA Method 5/9 · Industrial stacks</div></div></a>
      <a href="services.html#svc-2" class="svc-preview-card"><div class="svc-preview-icon"><i class="fas fa-building"></i></div><div><div class="svc-preview-name">Indoor Air Quality</div><div class="svc-preview-short">TVOC, formaldehyde, CO₂ profiling</div></div></a>
      <a href="services.html#svc-3" class="svc-preview-card"><div class="svc-preview-icon"><i class="fas fa-mountain"></i></div><div><div class="svc-preview-name">Environmental Impact Assessment</div><div class="svc-preview-short">EIA/ESIA · NCEC / IFC standards</div></div></a>
      <a href="services.html#svc-4" class="svc-preview-card"><div class="svc-preview-icon"><i class="fas fa-tint"></i></div><div><div class="svc-preview-name">Water &amp; Soil Analysis</div><div class="svc-preview-short">Heavy metals, VOCs · ISO/IEC 17025</div></div></a>
      <a href="services.html#svc-5" class="svc-preview-card"><div class="svc-preview-icon"><i class="fas fa-leaf"></i></div><div><div class="svc-preview-name">Environmental Management Plans</div><div class="svc-preview-short">EMP design · ISO 14001 audit support</div></div></a>
    </div>
    <div class="text-center mt-10 scroll-reveal"><a href="services.html" class="btn-primary">View all services <i class="fas fa-arrow-right" style="font-size:.75rem;"></i></a></div>
  </div>
</section>

<!-- MONITORING PROCESS -->
<section id="process" class="py-24 text-white relative overflow-hidden" style="background:var(--bp-blue-ink);">
  <div class="absolute inset-0 opacity-10" aria-hidden="true">
    <div class="absolute top-0 left-0 w-96 h-96 bg-bp-primary rounded-full blur-3xl"></div>
    <div class="absolute bottom-0 right-0 w-96 h-96 bg-bp-olive rounded-full blur-3xl"></div>
  </div>
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
    <div class="text-center mb-16 scroll-reveal">
      <div class="inline-block px-4 py-2 bg-white/10 rounded-full text-bp-sage font-semibold text-sm mb-4 backdrop-blur-sm">Our Methodology</div>
      <h2 class="text-4xl font-bold mb-4">Data Collection &amp; Monitoring Process</h2>
      <p class="text-gray-300 max-w-2xl mx-auto">A systematic, standards-based workflow from site mobilisation to compliance reporting</p>
    </div>
    <div class="relative">
      <div class="hidden md:block absolute top-1/2 left-0 right-0 h-1 process-line rounded-full transform -translate-y-1/2"></div>
      <div class="grid md:grid-cols-5 gap-8">
""" + "".join(f"""        <div class="relative scroll-reveal group"><div class="w-20 h-20 mx-auto bg-white rounded-2xl flex items-center justify-center text-3xl font-bold text-bp-ink shadow-xl relative z-20 transform group-hover:scale-110 group-hover:rotate-3 transition-all">{n}</div><div class="bg-white/10 backdrop-blur-sm rounded-2xl overflow-hidden border border-white/20 hover:bg-white/20 transition-all" style="margin-top:-2.5rem"><div style="height:2.5rem"></div><img src="{img}" alt="{title}" class="w-full h-36 object-cover opacity-80 group-hover:opacity-100 group-hover:scale-105 transition-all duration-500" onerror="this.style.display='none'" /><div class="p-6"><h4 class="font-bold text-lg mb-2 text-bp-sage">{title}</h4><p class="text-sm text-gray-300">{desc}</p></div></div></div>
""" for n, img, title, desc in [
    (1, "https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?w=400&h=180&fit=crop&q=80", "Project Scoping", "Define monitoring objectives, regulatory requirements, receptor locations per NCEC/ISO"),
    (2, "https://images.unsplash.com/photo-1581094794329-c8112a89af12?w=400&h=180&fit=crop&q=80", "Site Assessment", "Field reconnaissance, existing condition evaluation, background concentration measurement"),
    (3, "https://images.unsplash.com/photo-1621451537084-482c73073a0f?w=400&h=180&fit=crop&q=80", "Equipment Deployment", "Installation and calibration of ambient monitors, met stations, and sampling equipment"),
    (4, "https://images.unsplash.com/photo-1563207153-f403bf289096?w=400&h=180&fit=crop&q=80", "Sample Collection", "Systematic collection of air samples, stack test runs, and real-time data logging"),
    (5, "https://images.unsplash.com/photo-1576086213369-97a306d36557?w=400&h=180&fit=crop&q=80", "Lab Analysis", "Accredited lab analysis of filter samples for PM, metals, VOCs with QA/QC controls"),
]) + """      </div>
    </div>
    <div class="mt-20 bg-white/5 rounded-3xl p-8 backdrop-blur-sm border border-white/10 scroll-reveal">
      <h3 class="text-2xl font-bold mb-8 text-center">Reporting Workflow</h3>
      <div class="flex flex-wrap justify-center gap-4">
        <div class="flex items-center space-x-2 bg-white/10 px-6 py-3 rounded-full"><i class="fas fa-database text-bp-sage"></i><span>Data Acquisition</span></div>
        <i class="fas fa-arrow-right text-bp-sage self-center hidden md:block"></i>
        <div class="flex items-center space-x-2 bg-white/10 px-6 py-3 rounded-full"><i class="fas fa-search text-bp-sage"></i><span>QA/QC Validation</span></div>
        <i class="fas fa-arrow-right text-bp-sage self-center hidden md:block"></i>
        <div class="flex items-center space-x-2 bg-white/10 px-6 py-3 rounded-full"><i class="fas fa-chart-line text-bp-sage"></i><span>Statistical Analysis</span></div>
        <i class="fas fa-arrow-right text-bp-sage self-center hidden md:block"></i>
        <div class="flex items-center space-x-2 bg-white/10 px-6 py-3 rounded-full"><i class="fas fa-map-marked-alt text-bp-sage"></i><span>Spatial Mapping</span></div>
        <i class="fas fa-arrow-right text-bp-sage self-center hidden md:block"></i>
        <div class="flex items-center space-x-2 bg-bp-sage text-bp-ink px-6 py-3 rounded-full font-bold"><i class="fas fa-file-contract"></i><span>Report Generation</span></div>
      </div>
    </div>
  </div>
</section>

<!-- LOGO TICKER -->
<section class="logo-ticker-section">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="logo-ticker-header"><h3>Trusted By Leading Organizations</h3><p>Delivering environmental excellence to industry leaders across the Middle East</p></div>
    <div class="logo-ticker-wrapper"><div class="logo-ticker-track" id="logoTrack"></div></div>
  </div>
</section>

<!-- KEY PROJECTS & CLIENT PORTFOLIO -->
<section id="clients" class="py-24 bg-white">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="text-center mb-16 scroll-reveal">
      <div class="inline-block px-4 py-2 bg-bp-light rounded-full text-bp-primary font-semibold text-sm mb-4">Trusted By Industry Leaders</div>
      <h2 class="text-4xl font-bold text-bp-ink mb-4">Key Projects &amp; Client Portfolio</h2>
      <p class="text-gray-600 max-w-2xl mx-auto">Proven track record across Saudi Arabia's major national development programs</p>
    </div>
    <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-6 scroll-reveal">
""" + "".join(f"""      <div class="group relative overflow-hidden rounded-2xl shadow-lg cursor-pointer"><img src="{img}" alt="{title}" class="w-full h-64 object-cover transform group-hover:scale-110 transition-transform duration-500" /><div class="absolute inset-0 opacity-90" style="background:linear-gradient(to top,#04333a 0%,rgba(4, 51, 58,.5) 50%,transparent 100%);"></div><div class="absolute bottom-0 left-0 right-0 p-6 text-white"><div class="flex items-center space-x-2 mb-2"><i class="fas {icon} text-bp-sage"></i><span class="text-sm font-medium text-bp-sage">{cat}</span></div><h3 class="text-xl font-bold mb-2">{title}</h3><p class="text-sm text-gray-300">{desc}</p></div></div>
""" for img, icon, cat, title, desc in [
    ("https://images.unsplash.com/photo-1565008447742-97f6f38c985c?w=400&h=300&fit=crop", "fa-industry", "Industrial", "Riyadh Cement Plant", "Comprehensive ambient air and stack emission monitoring with US EPA methods"),
    ("https://images.unsplash.com/photo-1518005020951-eccb494ad742?w=400&h=300&fit=crop", "fa-tree", "Urban Development", "King Salman Park (KSP)", "Environmental monitoring for Riyadh's largest urban park project"),
    ("https://images.unsplash.com/photo-1544551763-46a013bb70d5?w=400&h=300&fit=crop", "fa-water", "Tourism", "Red Sea Project", "ESIA for mega tourism development including marine ecology and air quality"),
    ("https://images.unsplash.com/photo-1533106958155-d2d702b46d8a?w=400&h=300&fit=crop", "fa-rocket", "Entertainment", "Qiddiya Entertainment City", "Air quality monitoring for one of the world's largest entertainment destinations"),
    ("https://images.unsplash.com/photo-1473341304170-971dccb5ac1e?w=400&h=300&fit=crop", "fa-bolt", "Energy", "Qassim Power Plant", "Combined-cycle power station environmental compliance and CEMS"),
    ("https://images.unsplash.com/photo-1581094794329-c8112a89af12?w=400&h=300&fit=crop", "fa-border-all", "Infrastructure", "12 Land Border Crossings", "ESIA preparation for national border crossing facilities"),
]) + """    </div>
    <div class="mt-16 grid md:grid-cols-4 gap-6 scroll-reveal">
      <div class="text-center p-6 bg-gray-50 rounded-2xl"><i class="fas fa-industry text-4xl text-bp-primary mb-4"></i><h4 class="font-bold text-bp-ink mb-2">Industrial &amp; Energy</h4><p class="text-sm text-gray-600">Riyadh Cement, Qassim Power Plant, Saudi Aramco-linked projects</p></div>
      <div class="text-center p-6 bg-gray-50 rounded-2xl"><i class="fas fa-city text-4xl text-bp-olive mb-4"></i><h4 class="font-bold text-bp-ink mb-2">Mega Development</h4><p class="text-sm text-gray-600">Qiddiya, Red Sea Project, King Salman Park, NEOM</p></div>
      <div class="text-center p-6 bg-gray-50 rounded-2xl"><i class="fas fa-landmark text-4xl text-bp-soft mb-4"></i><h4 class="font-bold text-bp-ink mb-2">Government</h4><p class="text-sm text-gray-600">National Water Company, NCEC, Ministry of Environment</p></div>
      <div class="text-center p-6 bg-gray-50 rounded-2xl"><i class="fas fa-globe text-4xl text-bp-sage mb-4"></i><h4 class="font-bold text-bp-ink mb-2">International</h4><p class="text-sm text-gray-600">5 Capitals UAE, SAIL KSA, SIRC Saudi Arabia</p></div>
    </div>
  </div>
</section>

<!-- WHY CHOOSE -->
<section class="py-24" style="background:var(--bp-page);">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="text-center mb-16 scroll-reveal"><h2 class="text-4xl font-bold text-bp-ink mb-4">Why Choose BluePrint?</h2><p class="text-gray-600">Our competitive advantage in environmental consultancy</p></div>
    <div class="grid md:grid-cols-2 lg:grid-cols-4 gap-6 scroll-reveal">
""" + "".join(f"""      <div class="bg-white p-8 rounded-2xl shadow text-center group hover:bg-bp-ink hover:text-white transition-all duration-300"><div class="w-16 h-16 mx-auto bg-bp-light rounded-full flex items-center justify-center text-bp-primary text-2xl mb-4 group-hover:bg-white transition-all"><i class="fas {icon}"></i></div><h4 class="font-bold text-lg mb-2">{title}</h4><p class="text-sm text-gray-600 group-hover:text-gray-300">{desc}</p></div>
""" for icon, title, desc in [
    ("fa-award", "Accredited Laboratory", "ISO/IEC 17025 accredited for legally defensible results"),
    ("fa-map-marker-alt", "National Reach", "5 offices across KSA, Cairo, and Milan for full coverage"),
    ("fa-cogs", "End-to-End Solutions", "From baseline monitoring to regulatory submissions"),
    ("fa-users", "Specialist Team", "50+ qualified environmental engineers and scientists"),
]) + """    </div>
  </div>
</section>
"""


# ─────────────────────────── SERVICES ───────────────────────────
SERVICE_TABS = [
    ("fa-wind", "Ambient Air Quality", "PM2.5, PM10, NO₂, SO₂ &amp; ozone", "https://images.unsplash.com/photo-1611273426858-450d8e3c9fce", "https://images.unsplash.com/photo-1504711434969-e33886168f5c", "24/7 Monitoring", ""),
    ("fa-smog", "Stack Emission Testing", "US EPA Method 5/9 · Industrial stacks", "https://images.unsplash.com/photo-1565008447742-97f6f38c985c", "https://images.unsplash.com/photo-1473341304170-971dccb5ac1e", "EPA Certified", " olive"),
    ("fa-building", "Indoor Air Quality", "TVOC, formaldehyde, CO₂ profiling", "https://images.unsplash.com/photo-1497366216548-37526070297c", "https://images.unsplash.com/photo-1497366754035-f200581f0b4c", "IAQ Assessment", ""),
    ("fa-mountain", "Environmental Impact Assessment", "EIA/ESIA · NCEC / IFC standards", "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b", "https://images.unsplash.com/photo-1500534314209-a25ddb2bd429", "NCEC / IFC", " olive"),
    ("fa-tint", "Water &amp; Soil Analysis", "Heavy metals, VOCs · ISO/IEC 17025", "https://images.unsplash.com/photo-1505118380757-91f5f5632de0", "https://images.unsplash.com/photo-1559825481-12a05cc00344", "ISO/IEC 17025", ""),
    ("fa-leaf", "Environmental Management Plans", "EMP design · ISO 14001 audit support", "https://images.unsplash.com/photo-1542601906990-b4d3fb778b09", "https://images.unsplash.com/photo-1518531933037-91b2f5f229cc", "ISO 14001", " olive"),
]


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
    return page_header("Environmental services built for regulatory confidence",
                       "Six service lines covering air, emissions, water, soil, impact assessment and environmental management — delivered to NCEC, WHO, US EPA and ISO standards.",
                       "Services") + f"""
<section class="isvc-section" style="padding-top:64px;">
  <div class="isvc-layout">
    <div class="isvc-tabs isvc-reveal" id="isvcTabs">{tabs}
    </div>
    <div class="isvc-panel-wrap isvc-reveal isvc-reveal-delay-1" id="isvcPanelWrap">
      <div class="isvc-progress-bar" id="isvcProgressBar" style="width:16.66%"></div>{panels}
    </div>
  </div>
</section>
"""


# ─────────────────────────── TECHNOLOGY ─────────────────────────
EQUIPMENT = [
    ("https://images.unsplash.com/photo-1611273426858-450d8e3c9fce", "https://images.unsplash.com/photo-1504711434969-e33886168f5c", "US EPA Certified", "fa-microscope", "PM2.5/PM10 Monitors", "Beta Attenuation (BAM) and gravimetric samplers per US EPA standards"),
    ("https://images.unsplash.com/photo-1579165466741-7f35e4755183", "https://images.unsplash.com/photo-1532187643603-ba119ca4109e", "Lab Accredited", "fa-atom", "GC/MS Systems", "VOC, SVOC, BTEX, and TPH analysis with GC-FID/MS systems"),
    ("https://images.unsplash.com/photo-1635070041078-e363dbe005cb", "https://images.unsplash.com/photo-1518005020951-eccb494ad742", "Continuous Monitoring", "fa-wind", "Gas Analyzers", "Electrochemical &amp; UV-fluorescence sensors for NO₂, SO₂, CO, O₃"),
    ("https://images.unsplash.com/photo-1460925895917-afdab827c52f", "https://images.unsplash.com/photo-1551288049-bebda4e38f71", "24/7 Live Feed", "fa-satellite-dish", "Real-Time Data Loggers", "Telemetric data acquisition systems transmitting live air quality indices"),
    ("https://images.unsplash.com/photo-1504608524841-42584120d693", "https://images.unsplash.com/photo-1561553590-267fc716698a", "Auto Weather Station", "fa-cloud-sun", "Meteorological Stations", "Automatic weather stations measuring wind, temperature, humidity, solar radiation"),
    ("https://images.unsplash.com/photo-1473341304170-971dccb5ac1e", "https://images.unsplash.com/photo-1565008447742-97f6f38c985c", "EPA Method 5/17", "fa-smog", "Stack Emission Samplers", "Isokinetic sampling trains per US EPA Method 5/17"),
    ("https://images.unsplash.com/photo-1582719471384-894fbb16e074", "https://images.unsplash.com/photo-1576086213369-97a306d36557", "ISO/IEC 17025", "fa-vial", "ICP-MS Spectrometry", "PerkinElmer NexION for ultra-trace heavy metal analysis"),
    ("https://images.unsplash.com/photo-1600880292203-757bb62b4baf", "https://images.unsplash.com/photo-1581094794329-c8112a89af12", "Field Ready", "fa-mobile-alt", "Portable Field Monitors", "Hand-held multi-gas detectors and personal air samplers"),
]


def technology():
    cards = "".join(f"""
      <div class="equipment-card bg-gray-50 rounded-2xl border-2 border-transparent hover:border-bp-primary cursor-pointer group overflow-hidden">
        <div class="relative w-full h-44 overflow-hidden bg-bp-light">
          <img src="{img}?w=600&h=380&fit=crop&q=80" alt="{title}" loading="lazy" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" onerror="this.src='{fb}?w=600&h=380&fit=crop'" />
          <div class="absolute inset-0 opacity-0 group-hover:opacity-100 transition-opacity duration-300" style="background:linear-gradient(to top,rgba(4, 51, 58,.65),transparent);"></div>
          <span class="absolute bottom-3 left-3 text-xs font-bold text-white bg-bp-olive px-2 py-1 rounded-full opacity-0 group-hover:opacity-100 transition-opacity duration-300">{badge}</span>
        </div>
        <div class="p-5"><div class="flex items-center gap-2 mb-2"><div class="w-7 h-7 bg-bp-light rounded-lg flex items-center justify-center flex-shrink-0"><i class="fas {icon} text-bp-primary text-xs"></i></div><h4 class="font-bold text-bp-ink text-sm">{title}</h4></div><p class="text-xs text-gray-500 leading-relaxed">{desc}</p></div>
      </div>""" for img, fb, badge, icon, title, desc in EQUIPMENT)
    return page_header("AQMS technology &amp; equipment",
                       "State-of-the-art instrumentation for accurate and reliable environmental data, aligned with national and international compliance frameworks.",
                       "Technology") + f"""
<section id="equipment" class="py-20 bg-white">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="grid md:grid-cols-2 lg:grid-cols-4 gap-6 scroll-reveal">{cards}
    </div>
  </div>
</section>

<section id="standards" class="py-24" style="background:var(--bp-page);">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="text-center mb-16 scroll-reveal">
      <h2 class="text-4xl font-bold text-bp-ink mb-4">Compliance &amp; Regulatory Standards</h2>
      <p class="text-gray-600">Ensuring full regulatory alignment across national and international frameworks</p>
    </div>
    <div class="grid md:grid-cols-3 gap-8 scroll-reveal">
      <div class="bg-white p-8 rounded-2xl shadow-lg border-t-4 border-bp-primary hover:-translate-y-2 transition-all"><div class="w-16 h-16 bg-bp-light rounded-2xl flex items-center justify-center text-bp-primary text-2xl mb-6"><i class="fas fa-flag"></i></div><h3 class="text-xl font-bold text-bp-ink mb-4">NCEC — Saudi Arabia</h3><ul class="space-y-2 text-gray-600 text-sm"><li>• National Center for Environmental Compliance</li><li>• Ambient Air Quality Standards (SAAQS)</li><li>• Emission limits for industrial sources</li><li>• Environmental monitoring requirements</li></ul></div>
      <div class="bg-white p-8 rounded-2xl shadow-lg border-t-4 border-bp-soft hover:-translate-y-2 transition-all"><div class="w-16 h-16 bg-bp-light rounded-2xl flex items-center justify-center text-bp-soft text-2xl mb-6"><i class="fas fa-globe-americas"></i></div><h3 class="text-xl font-bold text-bp-ink mb-4">International Standards</h3><ul class="space-y-2 text-gray-600 text-sm"><li>• WHO Air Quality Guidelines 2021</li><li>• US EPA NAAQS Criteria Pollutants</li><li>• IFC Environmental &amp; Social Standards</li><li>• Equator Principles (EP)</li></ul></div>
      <div class="bg-white p-8 rounded-2xl shadow-lg border-t-4 border-bp-olive hover:-translate-y-2 transition-all"><div class="w-16 h-16 rounded-2xl flex items-center justify-center text-bp-olive text-2xl mb-6" style="background:var(--bp-olive-tint);"><i class="fas fa-certificate"></i></div><h3 class="text-xl font-bold text-bp-ink mb-4">ISO Certifications</h3><ul class="space-y-2 text-gray-600 text-sm"><li>• ISO/IEC 17025 — Lab Accreditation</li><li>• ISO 14001 — Environmental Management</li><li>• ISO 14644 — Cleanroom Air Standards</li><li>• ISO 9001 — Quality Management</li></ul></div>
    </div>
    <div class="mt-12 rounded-3xl p-8 text-white scroll-reveal" style="background:var(--bp-grad);">
      <div class="grid md:grid-cols-2 gap-8 items-center">
        <div>
          <h3 class="text-2xl font-bold mb-4">WHO Air Quality Guidelines 2021</h3>
          <p class="text-gray-200 mb-6">BluePrint monitoring programs align with the latest WHO recommendations for protecting public health.</p>
          <div class="flex flex-wrap gap-4">
            <div class="bg-white/20 backdrop-blur-sm px-6 py-3 rounded-xl"><span class="block text-3xl font-bold">5 µg/m³</span><span class="text-sm text-gray-200">PM2.5 Annual</span></div>
            <div class="bg-white/20 backdrop-blur-sm px-6 py-3 rounded-xl"><span class="block text-3xl font-bold">15 µg/m³</span><span class="text-sm text-gray-200">PM10 Annual</span></div>
          </div>
        </div>
        <div class="relative"><img src="https://images.unsplash.com/photo-1576086213369-97a306d36557?w=500&h=300&fit=crop" alt="Laboratory" class="rounded-2xl shadow-2xl opacity-90" loading="lazy" /></div>
      </div>
    </div>
  </div>
</section>
"""


# ─────────────────────────── RESOURCES ──────────────────────────
def resources():
    return page_header("Free tools &amp; live environmental intelligence",
                       "Check which standards apply to your facility, estimate your carbon footprint, and follow curated environmental news from Saudi Arabia and the region.",
                       "Resources") + """
<section id="tools" class="py-20 bg-bp-light">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="grid md:grid-cols-2 gap-8 scroll-reveal">
      <div class="bg-white rounded-3xl p-10 shadow-xl hover:shadow-2xl transition-all group cursor-pointer" onclick="openCalculator('compliance')">
        <div class="w-16 h-16 rounded-2xl flex items-center justify-center text-white text-2xl mb-6 group-hover:scale-110 transition-transform" style="background:var(--bp-grad-blue);"><i class="fas fa-balance-scale"></i></div>
        <h3 class="text-2xl font-bold text-bp-ink mb-3">Regulatory Compliance Checker</h3>
        <p class="text-gray-600 mb-6">Select your industry and location to instantly see which NCEC, WHO, and EPA standards apply to your operations.</p>
        <div class="flex flex-wrap gap-2 mb-6"><span class="px-3 py-1 bg-bp-light text-bp-primary rounded-full text-xs font-medium">NCEC Standards</span><span class="px-3 py-1 bg-bp-light text-bp-primary rounded-full text-xs font-medium">WHO Guidelines</span><span class="px-3 py-1 bg-bp-light text-bp-primary rounded-full text-xs font-medium">US EPA Methods</span></div>
        <button class="w-full py-3 bg-bp-primary text-white rounded-xl font-bold hover:bg-bp-dark transition-all">Check Compliance Requirements →</button>
      </div>
      <div class="bg-white rounded-3xl p-10 shadow-xl hover:shadow-2xl transition-all group cursor-pointer" onclick="openCalculator('carbon')">
        <div class="w-16 h-16 rounded-2xl flex items-center justify-center text-white text-2xl mb-6 group-hover:scale-110 transition-transform" style="background:var(--bp-grad-olive);"><i class="fas fa-leaf"></i></div>
        <h3 class="text-2xl font-bold text-bp-ink mb-3">Carbon Footprint Calculator</h3>
        <p class="text-gray-600 mb-6">Estimate your organization's carbon emissions across Scope 1, 2, and 3 categories with our interactive tool.</p>
        <div class="flex flex-wrap gap-2 mb-6"><span class="px-3 py-1 rounded-full text-xs font-medium text-bp-olive" style="background:var(--bp-olive-tint);">Scope 1, 2 &amp; 3</span><span class="px-3 py-1 rounded-full text-xs font-medium text-bp-olive" style="background:var(--bp-olive-tint);">tCO₂e Output</span><span class="px-3 py-1 rounded-full text-xs font-medium text-bp-olive" style="background:var(--bp-olive-tint);">Reduction Tips</span></div>
        <button class="w-full py-3 bg-bp-olive text-white rounded-xl font-bold hover:opacity-90 transition-all">Calculate Carbon Footprint →</button>
      </div>
    </div>

    <div id="aqi" class="mt-8 bg-white rounded-3xl p-8 shadow-xl scroll-reveal flex flex-wrap items-center justify-between gap-6">
      <div class="flex items-center gap-4">
        <div class="w-14 h-14 rounded-2xl flex items-center justify-center text-white text-xl" style="background:linear-gradient(135deg,#16a34a,#4ade80);"><i class="fas fa-map-marked-alt"></i></div>
        <div><h3 class="text-xl font-bold text-bp-ink">Live Riyadh Air Quality Index</h3><p class="text-sm text-gray-600">Real-time AQI, PM2.5 and PM10 readings — open the live widget in the bottom-left corner of any page.</p></div>
      </div>
      <button onclick="toggleAQI()" class="btn-olive"><i class="fas fa-satellite-dish" style="font-size:.8rem;"></i> Open live AQI</button>
    </div>
  </div>
</section>

<section id="env-news-section">
  <div class="ticker-wrap">
    <div class="ticker-track" id="ticker-track">
      <span class="ticker-item"><span style="width:7px;height:7px;background:#a3b56f;border-radius:50%;display:inline-block;animation:pulse-dot 2s ease-in-out infinite;"></span><span style="color:#a3b56f;font-weight:700;letter-spacing:.1em;font-size:.68rem;">BREAKING</span><span style="color:rgba(255,255,255,.5);">·</span>Loading latest Saudi Arabia environmental news&hellip;</span>
    </div>
  </div>

  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pt-14 pb-6">
    <div class="flex flex-col md:flex-row md:items-end md:justify-between gap-6">
      <div>
        <div class="flex items-center gap-2 mb-3"><div class="live-dot"></div><span style="font-size:.72rem;font-weight:600;color:var(--bp-olive);letter-spacing:.12em;text-transform:uppercase;">Live Feed · Auto-refreshes every 45 min</span></div>
        <h2 class="section-title text-4xl md:text-5xl mb-2">Environmental <span style="color:var(--bp-blue);">News Bulletin</span></h2>
        <p style="font-size:.85rem;color:var(--bp-muted);">Saudi Arabia &amp; Middle East · Curated environmental intelligence</p>
      </div>
      <div class="flex flex-col items-start md:items-end gap-3">
        <div class="flex flex-wrap gap-2">
          <button class="filter-pill active" data-topic="all">All Topics</button>
          <button class="filter-pill" data-topic="air quality">Air Quality</button>
          <button class="filter-pill" data-topic="sustainability">Sustainability</button>
          <button class="filter-pill" data-topic="climate">Climate</button>
          <button class="filter-pill" data-topic="water">Water</button>
        </div>
        <div class="flex items-center gap-3">
          <span id="last-updated" class="news-meta">Fetching news…</span>
          <button class="refresh-btn" onclick="loadNews(true)"><svg id="refresh-icon" width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M3 12a9 9 0 1 0 9-9 9.75 9.75 0 0 0-6.74 2.74L3 8"/><path d="M3 3v5h5"/></svg> Refresh</button>
        </div>
      </div>
    </div>
  </div>

  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pb-10">
    <div class="flex gap-4 flex-wrap">
      <div class="news-stat"><div class="ns-val" id="stat-count">—</div><div class="ns-lbl">Articles</div></div>
      <div class="news-stat"><div class="ns-val" id="stat-sources">—</div><div class="ns-lbl">Sources</div></div>
      <div class="news-stat"><div class="ns-val">KSA</div><div class="ns-lbl">Region</div></div>
    </div>
  </div>

  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pb-16">
    <div id="skeleton-grid" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
      <div class="skeleton" style="height:390px;"></div><div class="skeleton" style="height:390px;"></div><div class="skeleton" style="height:390px;"></div>
      <div class="skeleton" style="height:390px;"></div><div class="skeleton" style="height:390px;"></div><div class="skeleton" style="height:390px;"></div>
    </div>
    <div id="news-grid" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6" style="display:none;"></div>
    <div id="news-error" style="display:none;text-align:center;padding:60px 20px;">
      <div style="font-size:2.5rem;margin-bottom:12px;">📡</div>
      <div class="font-display" style="font-size:1.25rem;font-weight:700;color:var(--bp-text);margin-bottom:8px;">Could not fetch live news</div>
      <div style="font-size:.82rem;color:var(--bp-muted);margin-bottom:24px;">Showing curated articles. Check your API key or network.</div>
      <button onclick="loadNews(true)" class="btn-primary">Try Again</button>
    </div>
  </div>

  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pb-10" style="border-top:1px solid var(--bp-border);">
    <div class="flex flex-wrap items-center justify-between gap-3 pt-6">
      <p class="news-meta">Powered by GNews API · Images via Unsplash · BluePrint Environmental Services</p>
      <p id="next-refresh-label" class="news-meta">Next refresh in: —</p>
    </div>
  </div>
</section>
"""


# ─────────────────────────── CONTACT ────────────────────────────
def contact():
    return page_header("Contact BluePrint today",
                       "Ready to support your environmental monitoring and compliance requirements. Request a consultation, book a site inspection, or reach the team directly.",
                       "Contact") + """
<section id="contact" class="py-20" style="background:var(--bp-page);">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="grid lg:grid-cols-2 gap-16">
      <div class="scroll-reveal">
        <h2 class="text-3xl font-bold text-bp-ink mb-3">Reach the team directly</h2>
        <p class="text-gray-600 text-lg mb-8">Head office in Riyadh, with branches in Jeddah and Dammam and international offices in Cairo and Milan.</p>
        <div class="space-y-6">
          <div class="flex items-start space-x-4"><div class="w-12 h-12 bg-bp-light rounded-xl flex items-center justify-center text-bp-primary flex-shrink-0"><i class="fas fa-map-marker-alt text-xl"></i></div><div><h4 class="font-bold text-bp-ink mb-1">Head Office</h4><p class="text-gray-600" data-text="address"></p></div></div>
          <div class="flex items-start space-x-4"><div class="w-12 h-12 bg-bp-light rounded-xl flex items-center justify-center text-bp-primary flex-shrink-0"><i class="fas fa-envelope text-xl"></i></div><div><h4 class="font-bold text-bp-ink mb-1">Email</h4><p class="text-gray-600"><a data-mail data-text="email" class="hover:text-bp-primary transition-colors"></a></p></div></div>
          <div class="flex items-start space-x-4"><div class="w-12 h-12 bg-bp-light rounded-xl flex items-center justify-center text-bp-primary flex-shrink-0"><i class="fas fa-phone text-xl"></i></div><div><h4 class="font-bold text-bp-ink mb-1">Phone</h4><p class="text-gray-600"><a data-tel data-text="phone" class="hover:text-bp-primary transition-colors"></a></p></div></div>
          <div class="flex items-start space-x-4"><div class="w-12 h-12 bg-bp-light rounded-xl flex items-center justify-center text-bp-primary flex-shrink-0"><i class="fab fa-whatsapp text-xl"></i></div><div><h4 class="font-bold text-bp-ink mb-1">WhatsApp</h4><p class="text-gray-600"><a data-wa="Hi BluePrint" data-text="phone" class="hover:text-bp-primary transition-colors"></a></p></div></div>
          <div class="flex items-start space-x-4"><div class="w-12 h-12 bg-bp-light rounded-xl flex items-center justify-center text-bp-primary flex-shrink-0"><i class="fas fa-globe text-xl"></i></div><div><h4 class="font-bold text-bp-ink mb-1">Website</h4><p class="text-gray-600" data-text="website"></p></div></div>
        </div>
        <div class="mt-10 flex flex-wrap gap-3">
          <button onclick="openBookingModal()" class="btn-olive"><i class="fas fa-calendar-check" style="font-size:.8rem;"></i> Book a site inspection</button>
          <button onclick="openPortal()" class="btn-ghost"><i class="fas fa-user-circle" style="font-size:.8rem;"></i> Client Portal</button>
        </div>
      </div>
      <div class="scroll-reveal">
        <div class="bg-white rounded-3xl p-8 shadow-xl">
          <h3 class="text-2xl font-bold text-bp-ink mb-6">Request a Consultation</h3>
          <div class="space-y-4">
            <div class="grid md:grid-cols-2 gap-4">
              <input type="text" placeholder="First Name" aria-label="First name" class="w-full px-4 py-3 rounded-xl border border-gray-200 focus:border-bp-primary focus:ring-2 focus:ring-bp-primary/20 outline-none transition-all" />
              <input type="text" placeholder="Last Name" aria-label="Last name" class="w-full px-4 py-3 rounded-xl border border-gray-200 focus:border-bp-primary focus:ring-2 focus:ring-bp-primary/20 outline-none transition-all" />
            </div>
            <input type="email" placeholder="Email Address" aria-label="Email address" class="w-full px-4 py-3 rounded-xl border border-gray-200 focus:border-bp-primary focus:ring-2 focus:ring-bp-primary/20 outline-none transition-all" />
            <input type="tel" placeholder="Phone Number" aria-label="Phone number" class="w-full px-4 py-3 rounded-xl border border-gray-200 focus:border-bp-primary focus:ring-2 focus:ring-bp-primary/20 outline-none transition-all" />
            <select aria-label="Service interest" class="w-full px-4 py-3 rounded-xl border border-gray-200 focus:border-bp-primary outline-none transition-all text-gray-600 bg-white">
              <option value="">Select Service Interest</option>
              <option>Ambient Air Quality Monitoring</option>
              <option>Stack Emission Testing</option>
              <option>Indoor Air Quality</option>
              <option>Environmental Impact Assessment</option>
              <option>Other Services</option>
            </select>
            <textarea placeholder="Tell us about your project..." aria-label="Project details" rows="4" class="w-full px-4 py-3 rounded-xl border border-gray-200 focus:border-bp-primary outline-none transition-all resize-none"></textarea>
            <button onclick="sendContactMessage()" class="w-full py-4 bg-bp-primary text-white rounded-xl font-bold hover:bg-bp-dark transition-all shadow-lg">Send Message</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>
"""
