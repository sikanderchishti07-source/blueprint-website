# BluePrint, About page.
# Every factual claim here traces to a document: the commercial registration
# certificate, the National Address proof, or the capability deck.
# Nothing about team size, project count, client names, founding year or
# affiliations appears, because none of it has been evidenced.

DISCIPLINES = [
    ("fa-file-signature", "Environmental Assessment &amp; Management",
     "Impact assessment, permitting packages, management plans and site assessment, "
     "from licensing through to decommissioning."),
    ("fa-leaf", "Climate Change &amp; Sustainability",
     "Carbon accounting, ESG reporting, decarbonisation pathways and green building "
     "certification support."),
    ("fa-seedling", "Ecological &amp; Biological Surveys",
     "Terrestrial and marine ecology, ornithological survey, protected species work "
     "and habitat mapping."),
    ("fa-water", "Marine Environment",
     "Habitat mapping, water and sediment sampling, in-situ water quality, "
     "oceanographic and bathymetric survey."),
    ("fa-recycle", "Remediation &amp; Rehabilitation",
     "Site investigation and risk assessment, conceptual site models, and in-situ "
     "and ex-situ remediation."),
    ("fa-project-diagram", "Environmental Modelling",
     "Dispersion, hydrodynamic, hydrological, groundwater and noise modelling, "
     "run on established industry software."),
    ("fa-flask", "Laboratory &amp; Field Services",
     "Sampling, testing, field measurement and monitoring programmes, with analysis "
     "and technical interpretation."),
]

MODELS = [
    ("Atmospheric dispersion", "AERMOD, CALPUFF"),
    ("Hydrodynamic", "DHI-MIKE, CORMIX"),
    ("Watershed hydrology and hydraulics", "HEC-RAS, HEC-HMS, WMS, Civil 3D, ArcGIS"),
    ("Groundwater flow and water quality", "MODFLOW"),
    ("Noise", "SoundPlan"),
]

REGISTRY = [
    ("Registered name", "Blueprint Environmental Services Company"),
    ("Commercial registration", "7054759928"),
    ("Entity type", "Limited liability company"),
    ("Registration status", "Active"),
    ("Registered address", "3704 Abi Jafar Al Mansur, Al Yarmouk District, Riyadh 13251-7669"),
    ("National short address", "RFYB3704"),
    ("Country", "Kingdom of Saudi Arabia"),
]


def _disciplines():
    out = []
    for icon, title, body in DISCIPLINES:
        out.append(
            '<article class="abt-disc">'
            '<span class="abt-disc-ic"><i class="fas ' + icon + '"></i></span>'
            '<h3>' + title + '</h3>'
            '<p>' + body + '</p>'
            '</article>'
        )
    return "\n".join(out)


def _models():
    out = []
    for kind, tools in MODELS:
        out.append(
            '<div class="abt-mdl-row">'
            '<span class="abt-mdl-kind">' + kind + '</span>'
            '<span class="abt-mdl-tools">' + tools + '</span>'
            '</div>'
        )
    return "\n".join(out)


def _registry():
    out = []
    for label, value in REGISTRY:
        out.append(
            '<div class="abt-reg-row">'
            '<dt>' + label + '</dt>'
            '<dd>' + value + '</dd>'
            '</div>'
        )
    return "\n".join(out)


def about():
    return """
<!-- ============================================================
     ABOUT, hero
     ============================================================ -->
<section class="abt-hero">
  <div class="abt-hero-inner">
    <nav class="abt-crumb" aria-label="Breadcrumb">
      <a href="index.html">Home</a><span>/</span><span>About</span>
    </nav>
    <p class="abt-eyebrow"><i class="dot"></i>Accredited environmental consultancy &middot; Riyadh</p>
    <h1>A consultancy built around the permit</h1>
    <p class="abt-lede">BluePrint Environmental Services is a Saudi environmental consultancy
       working across the Kingdom and the wider GCC. We carry out the studies, measurements and
       reporting that environmental licensing requires, and we understand the process the
       submission has to survive.</p>
    <div class="abt-hero-facts">
      <div><strong>7</strong><span>Service disciplines</span></div>
      <div><strong>Riyadh</strong><span>Registered office</span></div>
      <div><strong>KSA &amp; GCC</strong><span>Area of work</span></div>
    </div>
  </div>
</section>

<!-- ============================================================
     ABOUT, position
     ============================================================ -->
<section class="abt-pos">
  <div class="abt-wrap">
    <div class="abt-pos-grid">
      <div>
        <div class="showcase-eyebrow">What sets us apart</div>
        <h2>Technical work is only half of an approval</h2>
        <p>Most environmental consultancies can take a measurement. Fewer can tell you which
           method your permit names, which authority reviews it, and what a reviewer will send
           back. That second half is where projects lose months.</p>
        <p>We work from the conditions outward. Before fieldwork is quoted, the obligation is
           read and the parameters, methods and frequencies it actually requires are confirmed.
           The result is a submission built in the form the regulator expects, rather than a
           technically sound report that has to be done twice.</p>
        <p>The same principle runs through everything below. Data that does not match the method
           named in your permit is not accepted, however carefully it was collected.</p>
      </div>
      <aside class="abt-pos-card">
        <h3>How we work</h3>
        <ul class="abt-ticks">
          <li>The permit conditions are read before anything is quoted</li>
          <li>Methods and locations follow the standard, not site convenience</li>
          <li>Findings are reported in the reviewer's format</li>
          <li>Where a regulatory specific is unconfirmed, it is flagged rather than assumed</li>
          <li>Exceedances are recorded with cause and corrective action, not omitted</li>
        </ul>
        <a href="services.html" class="abt-card-link">See the full service list
           <i class="fas fa-arrow-right" style="font-size:.7rem;"></i></a>
      </aside>
    </div>
  </div>
</section>

<!-- ============================================================
     ABOUT, disciplines
     ============================================================ -->
<section class="abt-disc-sec">
  <div class="abt-wrap">
    <div class="abt-sec-head">
      <div class="showcase-eyebrow">What we cover</div>
      <h2>Seven disciplines under one consultancy</h2>
      <p>Compliance rarely stays inside one specialism. A single permit can call for air
         measurement, an ecological baseline, a dispersion model and a management plan, and
         splitting those across providers is where the gaps appear.</p>
    </div>
    <div class="abt-disc-grid">
      {disciplines}
    </div>
  </div>
</section>

<!-- ============================================================
     ABOUT, modelling capability
     ============================================================ -->
<section class="abt-mdl-sec">
  <div class="abt-wrap">
    <div class="abt-mdl-grid">
      <div class="abt-mdl-copy">
        <div class="showcase-eyebrow" style="color:var(--bp-sage,#9fd3cf);">Technical capability</div>
        <h2>Modelling on established software</h2>
        <p>Predictive work is only as defensible as the tool and the assumptions behind it, which
           is why we name both. Every model we run is built on software a reviewer already knows,
           with the inputs and assumptions stated in the report rather than buried.</p>
        <a href="contact.html" class="abt-mdl-cta">Discuss a modelling requirement
           <i class="fas fa-arrow-right" style="font-size:.7rem;"></i></a>
      </div>
      <div class="abt-mdl-list">
        {models}
      </div>
    </div>
  </div>
</section>

<!-- ============================================================
     ABOUT, credentials
     ============================================================ -->
<section class="abt-cred-sec">
  <div class="abt-wrap">
    <div class="abt-sec-head">
      <div class="showcase-eyebrow">Credentials</div>
      <h2>Licensed, registered and accredited</h2>
      <p>Accreditation is what makes data admissible. Results submitted by an unaccredited party
         are commonly rejected at review even where the underlying work was sound.</p>
    </div>
    <div class="abt-cred-row">
      <a href="technology.html#standards" class="abt-cred">NCEC licensed</a>
      <a href="technology.html#standards" class="abt-cred">MWAN registered</a>
      <a href="technology.html#standards" class="abt-cred">Royal Commission for Jubail &amp; Yanbu</a>
      <a href="technology.html#standards" class="abt-cred">IAS accredited</a>
      <a href="technology.html#standards" class="abt-cred">ISO 9001 / 14001 / 45001</a>
    </div>
    <p class="abt-cred-note">Certificates and licence numbers are listed in full on the
       <a href="technology.html#standards">laboratory and accreditations page</a>.</p>
  </div>
</section>

<!-- ============================================================
     ABOUT, registered details
     ============================================================ -->
<section class="abt-reg-sec">
  <div class="abt-wrap">
    <div class="abt-reg-grid">
      <div>
        <div class="showcase-eyebrow">Company details</div>
        <h2>Registered in the Kingdom</h2>
        <p>BluePrint Environmental Services Company is a limited liability company registered
           with the Ministry of Commerce, holding an active commercial registration. Our
           registered office is in Al Yarmouk, Riyadh.</p>
      </div>
      <dl class="abt-reg">
        {registry}
      </dl>
    </div>
  </div>
</section>

<!-- ============================================================
     ABOUT, CTA
     ============================================================ -->
<section class="abt-cta">
  <div class="abt-wrap abt-cta-inner">
    <h2>Tell us what you are being asked to submit</h2>
    <p>The first consultation is free and carries no obligation. We will tell you which permits
       and studies apply to your activity, what each involves, and a realistic timeline.</p>
    <div class="abt-cta-btns">
      <a href="contact.html" class="abt-btn-p"><i class="fas fa-paper-plane"
         style="font-size:.78rem;"></i> Free consultation</a>
      <a data-wa="Hello BluePrint, I would like to ask about your environmental services."
         class="abt-btn-g"><i class="fab fa-whatsapp"></i> WhatsApp us</a>
    </div>
  </div>
</section>
""".replace("{disciplines}", _disciplines()) \
   .replace("{models}", _models()) \
   .replace("{registry}", _registry())
