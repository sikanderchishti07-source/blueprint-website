# BluePrint, About page.
# Layout: hero with image, story, why choose us, coverage, process,
# technical capability, accreditations, registered details, CTA.
#
# Every factual claim traces to a document: the commercial registration
# certificate, the National Address proof, or the capability deck.
# No founding year, team size, project count, client name or affiliation
# appears, because none of those have been evidenced.

HERO_IMG  = "assets/img/card-1.jpg"
STORY_IMG = "assets/img/process-lab.webp"
REG_IMG   = "assets/img/card-2.jpg"

APART = [
    ("fa-stamp", "Regulatory expertise",
     "We read the permit conditions first, so the parameters, methods and frequencies "
     "are confirmed before any fieldwork is quoted."),
    ("fa-flask", "Accredited analysis",
     "Sampling, testing and field measurement carried out to the methods your conditions "
     "name, because unaccredited data is commonly rejected at review."),
    ("fa-layer-group", "Seven disciplines, one consultancy",
     "A single permit can call for air measurement, an ecological baseline, a model and a "
     "management plan. Splitting those across providers is where gaps appear."),
    ("fa-shield-halved", "Evidence over assertion",
     "Where a regulatory specific is unconfirmed we flag it rather than assume it, and "
     "exceedances are reported with cause and corrective action."),
]

DISCIPLINES = [
    ("fa-file-signature", "Environmental Assessment &amp; Management",
     "Impact assessment, permitting packages, management plans and site assessment, from "
     "licensing through to decommissioning."),
    ("fa-leaf", "Climate Change &amp; Sustainability",
     "Carbon accounting, ESG reporting, decarbonisation pathways and green building "
     "certification support."),
    ("fa-seedling", "Ecological &amp; Biological Surveys",
     "Terrestrial and marine ecology, ornithological survey, protected species work and "
     "habitat mapping."),
    ("fa-water", "Marine Environment",
     "Habitat mapping, water and sediment sampling, in-situ water quality, oceanographic "
     "and bathymetric survey."),
    ("fa-recycle", "Remediation &amp; Rehabilitation",
     "Site investigation and risk assessment, conceptual site models, and in-situ and "
     "ex-situ remediation."),
    ("fa-project-diagram", "Environmental Modelling",
     "Dispersion, hydrodynamic, hydrological, groundwater and noise modelling on "
     "established industry software."),
    ("fa-vial", "Laboratory &amp; Field Services",
     "Sampling, testing, field measurement and monitoring programmes, with analysis and "
     "technical interpretation."),
]

PROCESS = [
    ("01", "fa-comments", "Understand",
     "We read your permit conditions and confirm which obligations actually apply to your activity."),
    ("02", "fa-sitemap", "Plan",
     "Scope, methods, locations and frequencies are agreed in writing before fieldwork begins."),
    ("03", "fa-microscope", "Execute",
     "Measurement, sampling and analysis carried out to the standard the condition names."),
    ("04", "fa-file-lines", "Deliver",
     "Results interpreted and reported in the form the reviewer expects, then filed on schedule."),
]

MODELS = [
    ("Atmospheric dispersion", "AERMOD, CALPUFF"),
    ("Hydrodynamic", "DHI-MIKE, CORMIX"),
    ("Watershed hydrology &amp; hydraulics", "HEC-RAS, HEC-HMS, WMS, Civil 3D, ArcGIS"),
    ("Groundwater flow &amp; water quality", "MODFLOW"),
    ("Noise", "SoundPlan"),
]

CREDS = [
    ("NCEC", "National Center for Environmental Compliance"),
    ("MWAN", "National Center for Waste Management"),
    ("RCJY", "Royal Commission for Jubail &amp; Yanbu"),
    ("IAS", "International Accreditation Service"),
    ("ISO", "Quality, environment &amp; safety management"),
]

REGISTRY = [
    ("fa-building", "Registered", "Limited liability company"),
    ("fa-id-card", "7054759928", "Commercial registration"),
    ("fa-location-dot", "Riyadh", "Registered office"),
]

REG_ROWS = [
    ("Registered name", "Blueprint Environmental Services Company"),
    ("Entity type", "Limited liability company"),
    ("Registration status", "Active"),
    ("Registered address", "3704 Abi Jafar Al Mansur, Al Yarmouk District, Riyadh 13251-7669"),
    ("National short address", "RFYB3704"),
]


def _apart():
    return "\n".join(
        '<article class="abt-ap"><span class="abt-ap-ic"><i class="fas ' + i + '"></i></span>'
        '<h3>' + t + '</h3><p>' + b + '</p></article>'
        for i, t, b in APART)


def _disciplines():
    return "\n".join(
        '<article class="abt-disc"><span class="abt-disc-ic"><i class="fas ' + i + '"></i></span>'
        '<h3>' + t + '</h3><p>' + b + '</p></article>'
        for i, t, b in DISCIPLINES)


def _process():
    return "\n".join(
        '<article class="abt-step"><span class="abt-step-num">' + n + '</span>'
        '<span class="abt-step-ic"><i class="fas ' + i + '"></i></span>'
        '<h3>' + t + '</h3><p>' + b + '</p></article>'
        for n, i, t, b in PROCESS)


def _models():
    return "\n".join(
        '<div class="abt-mdl-row"><span class="abt-mdl-kind">' + k + '</span>'
        '<span class="abt-mdl-tools">' + v + '</span></div>'
        for k, v in MODELS)


def _creds():
    return "\n".join(
        '<a href="technology.html#standards" class="abt-cred">'
        '<span class="abt-cred-abbr">' + s + '</span>'
        '<span class="abt-cred-full">' + f + '</span></a>'
        for s, f in CREDS)


def _regcards():
    return "\n".join(
        '<div class="abt-regcard"><i class="fas ' + i + '"></i>'
        '<div><strong>' + v + '</strong><span>' + l + '</span></div></div>'
        for i, v, l in REGISTRY)


def _regrows():
    return "\n".join(
        '<div class="abt-reg-row"><dt>' + l + '</dt><dd>' + v + '</dd></div>'
        for l, v in REG_ROWS)


_TPL = """
<!-- ============================================================
     ABOUT, hero
     ============================================================ -->
<section class="abt-hero">
  <div class="abt-hero-media" style="background-image:url('{hero_img}')" aria-hidden="true"></div>
  <div class="abt-hero-veil" aria-hidden="true"></div>
  <div class="abt-wrap abt-hero-inner">
    <nav class="abt-crumb" aria-label="Breadcrumb">
      <a href="index.html">Home</a><span>/</span><span>About Us</span>
    </nav>
    <p class="abt-eyebrow">About BluePrint Environmental Services</p>
    <h1>Your partner in<br /><span>environmental compliance</span></h1>
    <blockquote class="abt-lede">BluePrint Environmental Services is a Saudi environmental
      consultancy working across the Kingdom and the wider GCC. We deliver the studies,
      measurements and reporting that environmental licensing requires, built to the methods
      your permit names and in the form the regulator expects.</blockquote>
    <div class="abt-hero-facts">
      <div><strong>7</strong><span>Service disciplines</span></div>
      <div><strong>Riyadh</strong><span>Registered office</span></div>
      <div><strong>KSA &amp; GCC</strong><span>Area of work</span></div>
    </div>
  </div>
</section>

<!-- ============================================================
     ABOUT, story
     ============================================================ -->
<section class="abt-story">
  <div class="abt-wrap abt-story-grid">
    <div class="abt-story-copy">
      <div class="showcase-eyebrow">Our story</div>
      <h2>Technical work is only half of an approval</h2>
      <p>Most environmental consultancies can take a measurement. Fewer can tell you which
         method your permit names, which authority reviews it, and what a reviewer will send
         back. That second half is where projects lose months.</p>
      <p>We work from the conditions outward. Before fieldwork is quoted, the obligation is read
         and the parameters, methods and frequencies it actually requires are confirmed. The
         result is a submission built to be accepted first time, rather than a technically sound
         report that has to be done twice.</p>
      <a href="services.html" class="abt-ghost-btn">Our services
         <i class="fas fa-arrow-right" style="font-size:.7rem;"></i></a>
    </div>
    <figure class="abt-story-media">
      <img src="{story_img}" alt="Analytical instruments and sample vials on a laboratory bench"
           loading="lazy" />
      <figcaption>Accurate data.<br />Defensible method.<br />Accepted submissions.</figcaption>
    </figure>
  </div>
</section>

<!-- ============================================================
     ABOUT, what sets us apart
     ============================================================ -->
<section class="abt-ap-sec">
  <div class="abt-wrap abt-ap-grid">
    <div class="abt-ap-head">
      <div class="showcase-eyebrow">Why choose us</div>
      <h2>What sets us apart</h2>
      <p>We go beyond the measurement. Our approach combines technical method, regulatory
         knowledge and a record that holds up when someone asks to see it.</p>
    </div>
    <div class="abt-ap-cards">
      {apart}
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
      <p>Compliance rarely stays inside one specialism, so the whole obligation is handled in
         one place rather than split across providers.</p>
    </div>
    <div class="abt-disc-grid">
      {disciplines}
    </div>
  </div>
</section>

<!-- ============================================================
     ABOUT, process
     ============================================================ -->
<section class="abt-proc-sec">
  <div class="abt-wrap abt-proc-grid">
    <div class="abt-proc-head">
      <div class="showcase-eyebrow">Our process</div>
      <h2>How we work</h2>
      <p>A clear route from the first reading of your conditions through to a filed submission,
         with nothing assumed along the way.</p>
    </div>
    <div class="abt-steps">
      {process}
    </div>
  </div>
</section>

<!-- ============================================================
     ABOUT, technical capability
     ============================================================ -->
<section class="abt-mdl-sec">
  <div class="abt-wrap abt-mdl-grid">
    <div class="abt-mdl-copy">
      <p class="abt-eyebrow">Technical capability</p>
      <h2>Modelling on established software</h2>
      <p>Predictive work is only as defensible as the tool and the assumptions behind it, which
         is why we name both. Every model runs on software a reviewer already knows, with the
         inputs stated in the report rather than buried.</p>
      <a href="contact.html" class="abt-mdl-cta">Discuss a modelling requirement
         <i class="fas fa-arrow-right" style="font-size:.7rem;"></i></a>
    </div>
    <div class="abt-mdl-list">
      {models}
    </div>
  </div>
</section>

<!-- ============================================================
     ABOUT, accreditations
     ============================================================ -->
<section class="abt-cred-sec">
  <div class="abt-wrap abt-cred-grid">
    <div class="abt-cred-head">
      <div class="showcase-eyebrow">Licences &amp; accreditations</div>
      <h2>Held to recognised standards</h2>
      <p>Accreditation is what makes data admissible. Results submitted by an unaccredited party
         are commonly rejected at review even where the underlying work was sound.</p>
      <a href="technology.html#standards" class="abt-ghost-btn">See the credentials
         <i class="fas fa-arrow-right" style="font-size:.7rem;"></i></a>
    </div>
    <div class="abt-cred-row">
      {creds}
    </div>
  </div>
</section>

<!-- ============================================================
     ABOUT, registered details
     ============================================================ -->
<section class="abt-reg-sec">
  <div class="abt-wrap abt-reg-grid">
    <figure class="abt-reg-media">
      <img src="{reg_img}" alt="Environmental technician recording field measurements on site"
           loading="lazy" />
      <div class="abt-reg-cards">
        {regcards}
      </div>
    </figure>
    <div class="abt-reg-copy">
      <div class="showcase-eyebrow">Registered in the Kingdom</div>
      <h2>Verifiable, not just stated</h2>
      <p>BluePrint Environmental Services Company is a limited liability company registered with
         the Ministry of Commerce, holding an active commercial registration. Our registered
         office is in Al Yarmouk, Riyadh, and the details below can be checked against the
         public register.</p>
      <dl class="abt-reg">
        {regrows}
      </dl>
    </div>
  </div>
</section>

<!-- ============================================================
     ABOUT, CTA
     ============================================================ -->
<section class="abt-cta">
  <div class="abt-wrap abt-cta-inner">
    <p class="abt-eyebrow">Let us take the obligation off your desk</p>
    <h2>Ready to work together?</h2>
    <p class="abt-cta-p">Tell us what you are being asked to submit. The first consultation is
       free and carries no obligation, and you will leave it knowing which permits and studies
       apply, what each involves, and a realistic timeline.</p>
    <div class="abt-cta-btns">
      <a href="contact.html" class="abt-btn-p"><i class="fas fa-paper-plane"
         style="font-size:.78rem;"></i> Contact us</a>
      <a data-wa="Hello BluePrint, I would like to ask about your environmental services."
         class="abt-btn-g"><i class="fab fa-whatsapp"></i> WhatsApp us</a>
    </div>
  </div>
</section>
"""


def about():
    html = _TPL
    for key, val in (
        ("{hero_img}", HERO_IMG),
        ("{story_img}", STORY_IMG),
        ("{reg_img}", REG_IMG),
        ("{apart}", _apart()),
        ("{disciplines}", _disciplines()),
        ("{process}", _process()),
        ("{models}", _models()),
        ("{creds}", _creds()),
        ("{regcards}", _regcards()),
        ("{regrows}", _regrows()),
    ):
        html = html.replace(key, val)
    return html
