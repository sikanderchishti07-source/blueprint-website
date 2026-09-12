# Carousel service pages, one per card on the home page carousel.
# Content describes capability only. Nothing about BluePrint's history,
# clients, project counts or accreditation scope is asserted here.
# Rows marked CONFIRM must be checked by the owner before they go live.

CONFIRM = '<span class="svq-confirm"><i class="fas fa-circle-exclamation"></i> To be confirmed</span>'

CARDS = {}

CARDS["environmental-studies"] = dict(
    band_quote="A prediction is only as good as the baseline behind it.",
    who=[
              ("Industrial facilities",
               "Process changes and expansions usually trigger a fresh assessment rather than an amendment to the old one."),
              ("Infrastructure projects",
               "Linear schemes cross several receptor types, so the baseline has to cover the whole corridor, not the endpoints."),
              ("Extraction sites",
               "Assessment has to look past the working life of the site to the rehabilitation obligation that follows it."),
              ],
    faqs=[
           ("How early should the study start?",
            "Before the design is fixed. A baseline commissioned after layout decisions are made often finds a constraint that forces rework."),
           ("What if a survey window has passed?",
            "Some parameters can only be surveyed at certain times of year. We tell you at scoping rather than discovering it mid-project."),
           ("Do you handle reviewer queries?",
            "Yes. The people who prepared the study answer the questions on it."),
           ],

    slug="environmental-studies", num="01",
    title="Environmental Studies",
    eyebrow="Environmental studies",
    h1="Impact assessment and baseline studies",
    lede="In-depth impact assessments and baseline studies that support informed decisions and regulatory approval.",
    img="assets/img/svc-card-1.webp",
    chips=["Industrial facilities", "Infrastructure projects", "Extraction sites", "Coastal development"],
    overview_h="What this service covers",
    overview_p="Baseline characterisation of a site, prediction of how a proposed activity will change it, and the "
               "mitigation and monitoring commitments that follow. The study is the document a reviewer reads first.",
    features=[("fa-clipboard-list", "Scoping and terms of reference"),
              ("fa-map", "Field baseline survey"),
              ("fa-chart-line", "Impact prediction with stated method"),
              ("fa-shield-halved", "Mitigation hierarchy"),
              ("fa-calendar-check", "Monitoring plan"),
              ("fa-file-signature", "Submission support")],
    req_rows=[("Authority", "NCEC" + CONFIRM),
              ("Usually needed", "Scoping report, baseline survey, impact assessment, monitoring plan"),
              ("Typical duration", "Site dependent, agreed at scoping before work begins"),
              ("Common hold-up", "Baseline survey commissioned after the design is fixed")],
    standards=["Stated methodology for every prediction", "Field baseline behind every conclusion", "Reporting in the reviewer's format"],
    approach="Scope agreed in writing, field baseline collected to referenced methods, impacts predicted against that "
             "baseline, then reporting in the format the reviewer expects. Each stage names the standard applied.",
    meta="Environmental impact assessment and baseline studies in Saudi Arabia, scoping, field survey, "
         "impact prediction and monitoring plans prepared for regulatory submission.",
)

CARDS["marine-environment-services"] = dict(
    band_quote="Survey scope agreed before the design is fixed costs less than redesign after it.",
    who=[
              ("Ports and terminals",
               "Dredging, berth works and operational discharge each carry their own survey requirement."),
              ("Desalination intakes and outfalls",
               "Intake entrainment and discharge plume behaviour usually need both survey and modelling."),
              ("Coastal development",
               "Habitat present at the shoreline determines what can be built and what has to be avoided."),
              ],
    faqs=[
           ("How long does a marine baseline take?",
            "It depends on the parameters and whether seasonal coverage is required. We state it at scoping."),
           ("Do you cover both water and sediment?",
            "Yes, along with benthic habitat where the assessment calls for it."),
           ("Can you work from an existing dataset?",
            "We review it first. Gaps and method inconsistencies in old data tend to surface at review."),
           ],

    slug="marine-environment-services", num="02",
    title="Marine Environment",
    eyebrow="Marine environment",
    h1="Marine environmental studies and monitoring",
    lede="Water quality, sediment, benthic habitat and oceanographic survey for coastal development and discharge.",
    img="assets/img/svc-card-2.webp",
    chips=["Ports and terminals", "Desalination intakes", "Coastal development", "Dredging and reclamation"],
    overview_h="Marine environmental services",
    overview_p="From coastal baseline assessment to biodiversity monitoring, we produce the survey data and reporting "
               "that marine and coastal projects are required to submit.",
    features=[("fa-water", "Marine baseline studies"),
              ("fa-file-lines", "Impact assessment input"),
              ("fa-droplet", "Water quality monitoring"),
              ("fa-map-location-dot", "Habitat mapping"),
              ("fa-fish", "Biodiversity assessment"),
              ("fa-flask", "Sediment and water sampling")],
    req_rows=[("Authority", "NCEC, plus the sector authority where the site falls in its area" + CONFIRM),
              ("Usually needed", "Baseline survey, impact assessment, monitoring plan"),
              ("Typical duration", "Site dependent, agreed at scoping before work begins"),
              ("Common hold-up", "Survey scope agreed after the design is fixed rather than before")],
    standards=["ISO 5667 sampling" + CONFIRM, "ISO/IEC 17025 laboratory" + CONFIRM, "Reporting in the reviewer's format"],
    approach="Scope agreed in writing, field survey to referenced methods, laboratory analysis, then reporting in the "
             "format the reviewer expects. Each stage names the standard applied.",
    meta="Marine environmental services in Saudi Arabia, baseline surveys, water quality monitoring, "
         "sediment sampling and habitat mapping for coastal and marine projects.",
)

CARDS["terrestrial-environment"] = dict(
    band_quote="Miss the survey window and the whole assessment waits a season.",
    who=[
              ("Infrastructure corridors",
               "Long routes cross several habitat types, and the survey has to cover all of them."),
              ("Solar and wind sites",
               "Large footprints on apparently empty land still carry habitat and species obligations."),
              ("Quarries and mining",
               "Rehabilitation commitments are set against the baseline recorded before extraction starts."),
              ],
    faqs=[
           ("When can surveys be done?",
            "Species activity determines the window. Some can only be surveyed in certain months, which we flag at scoping."),
           ("What if protected species are found?",
            "The finding shapes the mitigation. Discovering it early is far cheaper than discovering it at review."),
           ("Is a desk study enough?",
            "It narrows the scope but rarely replaces field survey where a licence depends on the result."),
           ],

    slug="terrestrial-environment", num="03",
    title="Terrestrial Environment",
    eyebrow="Terrestrial environment",
    h1="Ecology and habitat assessment on land",
    lede="Habitat mapping, baseline ecology and protected species assessment across desert and coastal terrain.",
    img="assets/img/svc-card-3.webp",
    chips=["Infrastructure corridors", "Solar and wind sites", "Quarries and mining", "Urban development"],
    overview_h="Terrestrial ecology services",
    overview_p="Survey of the habitats, flora and fauna present on a site before development, and assessment of what "
               "the proposed activity would do to them.",
    features=[("fa-seedling", "Habitat mapping"),
              ("fa-binoculars", "Flora and fauna survey"),
              ("fa-dove", "Bird and protected species survey"),
              ("fa-layer-group", "Baseline ecological characterisation"),
              ("fa-triangle-exclamation", "Constraint and sensitivity mapping"),
              ("fa-file-lines", "Reporting for assessment input")],
    req_rows=[("Authority", "NCEC" + CONFIRM),
              ("Usually needed", "Baseline ecology survey, protected species assessment, mitigation measures"),
              ("Typical duration", "Seasonally dependent, some species surveys have survey windows"),
              ("Common hold-up", "Survey window missed, delaying the whole assessment by a season")],
    standards=["Survey timing matched to species activity", "Recorded survey effort and conditions", "Reporting in the reviewer's format"],
    approach="Desk study first, then field survey timed to the species in question, then reporting that states the "
             "survey effort and conditions so the result can be assessed rather than taken on trust.",
    meta="Terrestrial ecology services in Saudi Arabia, habitat mapping, baseline ecological survey and "
         "protected species assessment for development and infrastructure projects.",
)

CARDS["veterinary-biosecurity"] = dict(
    band_quote="Procedures a team cannot follow are procedures that will not be followed.",
    who=[
              ("Livestock operations",
               "Animal density and waste volume drive both the biosecurity risk and the environmental obligation."),
              ("Poultry farms",
               "Disease control and litter handling sit alongside each other and are usually inspected together."),
              ("Veterinary clinics",
               "Medical and animal waste carry strict handling rules from the day a clinic opens."),
              ],
    faqs=[
           ("What does a biosecurity review involve?",
            "A site visit, a look at current practice, and a written gap list against what the operation should have in place."),
           ("Do you write the procedures?",
            "Yes, in a form a site team can actually follow rather than a document that sits in a folder."),
           ("Can you train the staff?",
            "Yes. Training is usually the part that makes the procedures stick."),
           ],

    slug="veterinary-biosecurity", num="04",
    title="Veterinary Consultations &amp; Biosecurity",
    eyebrow="Veterinary and biosecurity",
    h1="Veterinary advisory and biosecurity planning",
    lede="Biosecurity planning and veterinary advisory for operations where animal health and the environment meet.",
    img="assets/img/svc-card-4.webp",
    chips=["Livestock operations", "Poultry farms", "Veterinary clinics", "Animal facilities"],
    overview_h="Veterinary and biosecurity services",
    overview_p="Advisory for operations holding animals, covering disease-control measures, waste handling and the "
               "environmental obligations that sit alongside them.",
    features=[("fa-shield-virus", "Biosecurity planning"),
              ("fa-clipboard-check", "Site assessment and gap review"),
              ("fa-recycle", "Animal and medical waste handling"),
              ("fa-droplet", "Effluent and water management"),
              ("fa-chalkboard-user", "Staff procedure and training input"),
              ("fa-file-lines", "Documentation and record systems")],
    req_rows=[("Authority", CONFIRM),
              ("Usually needed", CONFIRM),
              ("Typical duration", "Site dependent, agreed at scoping before work begins"),
              ("Common hold-up", CONFIRM)],
    standards=[CONFIRM, "Documented procedures a site team can follow", "Records kept current rather than reconstructed"],
    approach="Site visit and gap review first, then written procedures the team can actually follow, then a record "
             "system that stays current between inspections.",
    meta="Veterinary consultation and biosecurity planning in Saudi Arabia, site assessment, disease control "
         "measures, animal waste handling and documentation for animal-holding operations.",
)

CARDS["test-boreholes"] = dict(
    band_quote="Design the remediation before the extent is known and you will pay for it twice.",
    who=[
              ("Contaminated land",
               "Delineation determines the scale of the problem and therefore the cost of solving it."),
              ("Development sites",
               "Ground conditions and groundwater shape foundation design as much as any survey."),
              ("Landfill and waste sites",
               "Monitoring wells are often a standing condition rather than a one-off investigation."),
              ],
    faqs=[
           ("How many boreholes do we need?",
            "It depends on the site history and the question being asked. We size the programme after the desk study, not before."),
           ("Do you install monitoring wells?",
            "Yes, where readings are needed over time rather than on a single date."),
           ("What do we get at the end?",
            "A factual report of what was found and an interpretative report on what it means, kept separate."),
           ],

    slug="test-boreholes", num="05",
    title="Test Boreholes",
    eyebrow="Test boreholes",
    h1="Borehole drilling and ground sampling",
    lede="Borehole drilling and sampling to establish ground conditions, groundwater and the extent of contamination.",
    img="assets/img/svc-card-5.webp",
    chips=["Contaminated land", "Development sites", "Industrial facilities", "Landfill and waste sites"],
    overview_h="Borehole investigation services",
    overview_p="Drilling, logging and sampling to find out what is below the surface, ground conditions, groundwater "
               "levels and whether contamination is present and how far it extends.",
    features=[("fa-ruler-vertical", "Borehole drilling and logging"),
              ("fa-vial", "Soil and groundwater sampling"),
              ("fa-gauge", "Monitoring well installation"),
              ("fa-flask", "Laboratory analysis"),
              ("fa-map", "Contamination extent delineation"),
              ("fa-file-lines", "Factual and interpretative reporting")],
    req_rows=[("Authority", CONFIRM),
              ("Usually needed", "Investigation plan, factual report, interpretative report"),
              ("Typical duration", "Depends on borehole count and depth, agreed at scoping"),
              ("Common hold-up", "Investigation sized before the ground risk is understood")],
    standards=["Chain of custody on every sample" + CONFIRM, "Logged to a recognised description scheme" + CONFIRM, "Factual and interpretative reports kept separate"],
    approach="Desk study and site history first, then a borehole programme sized to the actual risk, sampling under "
             "chain of custody, and reporting that separates what was found from what it means.",
    meta="Test borehole drilling and sampling in Saudi Arabia, ground investigation, groundwater monitoring "
         "wells and contamination delineation with factual and interpretative reporting.",
)

CARDS["hydrogeology-geotechnics"] = dict(
    band_quote="Start monitoring too late and you will miss the variation that mattered.",
    who=[
              ("Development projects",
               "Groundwater level and ground conditions shape what can be built and how."),
              ("Extraction and quarrying",
               "Dewatering and its effect on the surrounding water table is usually the central question."),
              ("Remediation sites",
               "Flow direction determines where contamination goes and where to monitor for it."),
              ],
    faqs=[
           ("How long does monitoring need to run?",
            "Long enough to capture seasonal variation where levels change through the year. We state the period at scoping."),
           ("Do you produce modelling input?",
            "Yes, the field data is collected in the form a groundwater model needs."),
           ("Is this separate from a geotechnical survey?",
            "They overlap. Running them together usually avoids drilling the same ground twice."),
           ],

    slug="hydrogeology-geotechnics", num="06",
    title="Hydrogeology &amp; Geotechnics",
    eyebrow="Hydrogeology and geotechnics",
    h1="Groundwater and ground condition investigation",
    lede="Groundwater assessment and geotechnical investigation for development, extraction and remediation.",
    img="assets/img/svc-card-6.webp",
    chips=["Development projects", "Extraction and quarrying", "Remediation sites", "Water resource studies"],
    overview_h="Hydrogeology and geotechnical services",
    overview_p="Site investigation establishing groundwater levels, flow direction, aquifer properties and ground "
               "conditions, reported in the form regulators and design engineers both need.",
    features=[("fa-droplet", "Groundwater level and flow assessment"),
              ("fa-water", "Aquifer characterisation"),
              ("fa-mountain", "Ground condition investigation"),
              ("fa-vial", "In-situ and laboratory testing"),
              ("fa-diagram-project", "Groundwater modelling input"),
              ("fa-file-lines", "Factual and interpretative reporting")],
    req_rows=[("Authority", CONFIRM),
              ("Usually needed", "Desk study, investigation plan, factual and interpretative reports"),
              ("Typical duration", "Monitoring periods can extend over months where levels vary seasonally"),
              ("Common hold-up", "Monitoring started too late to capture seasonal variation")],
    standards=[CONFIRM, "Monitoring period matched to the question being asked", "Reporting referenced to the standards applied"],
    approach="Desk study and records review, borehole programme sized to the ground risk, monitoring installed where "
             "readings are needed over time, then factual and interpretative reporting.",
    meta="Hydrogeology and geotechnical investigation in Saudi Arabia, groundwater assessment, aquifer "
         "characterisation, ground conditions and monitoring for development and remediation projects.",
)

CARDS["treatment-rehabilitation"] = dict(
    band_quote="Validation against a stated objective, not against an impression.",
    who=[
              ("Contaminated industrial land",
               "Historic operations leave contamination that only appears when the site changes hands or use."),
              ("Quarry rehabilitation",
               "The rehabilitation obligation was committed to years earlier and does not lapse."),
              ("Fuel and chemical sites",
               "Hydrocarbon and solvent contamination migrates, so delineation matters as much as treatment."),
              ],
    faqs=[
           ("How do you decide the treatment method?",
            "By appraising options against the actual contamination and the site constraints, after delineation."),
           ("What is validation?",
            "Sampling after treatment to show the stated objective was met, with the evidence retained."),
           ("Can you supervise contractor works?",
            "Yes. Supervision is usually what keeps the validation evidence defensible."),
           ],

    slug="treatment-rehabilitation", num="07",
    title="Treatment &amp; Rehabilitation",
    eyebrow="Treatment and rehabilitation",
    h1="Remediation design and site rehabilitation",
    lede="Remediation design and rehabilitation of contaminated and disturbed land, validated through to closure.",
    img="assets/img/svc-card-7.webp",
    chips=["Contaminated industrial land", "Quarry rehabilitation", "Fuel and chemical sites", "Closure and handover"],
    overview_h="Remediation and rehabilitation services",
    overview_p="Investigation of what is present, design of the treatment that addresses it, and the validation "
               "evidence that shows the objective was actually met.",
    features=[("fa-magnifying-glass", "Site investigation and risk assessment"),
              ("fa-diagram-project", "Remediation option appraisal"),
              ("fa-screwdriver-wrench", "Treatment design"),
              ("fa-seedling", "Land rehabilitation planning"),
              ("fa-clipboard-check", "Validation sampling"),
              ("fa-file-circle-check", "Closure reporting")],
    req_rows=[("Authority", "NCEC" + CONFIRM),
              ("Usually needed", "Risk assessment, remediation plan, validation report"),
              ("Typical duration", "Depends on contamination extent and method, agreed after investigation"),
              ("Common hold-up", "Remediation designed before the extent is properly delineated")],
    standards=["Validation against a stated objective", "Sampling under chain of custody" + CONFIRM, "Closure evidence retained for audit"],
    approach="Investigate and delineate first, appraise the treatment options against the actual risk, design and "
             "supervise the works, then validate against a stated objective rather than an impression.",
    meta="Remediation and land rehabilitation in Saudi Arabia, site investigation, risk assessment, "
         "treatment design and validation to closure for contaminated and disturbed land.",
)

CARDS["environmental-training"] = dict(
    band_quote="Generic training does not survive contact with a specific permit.",
    who=[
              ("Site and operations teams",
               "The people doing the work are the ones an inspector speaks to."),
              ("HSE staff",
               "Environmental obligations sit alongside safety ones and are often the less familiar half."),
              ("New facilities",
               "A team that understands the conditions from day one avoids the first-year violations."),
              ],
    faqs=[
           ("Is training delivered on site?",
            "Usually, so it can be built around the facility's own equipment and records."),
           ("What is left behind afterwards?",
            "A record of the content covered and who attended, which is what gets asked for at inspection."),
           ("Can it be tailored to one permit?",
            "That is the point. We read the conditions first and build the session around them."),
           ],

    slug="environmental-training", num="08",
    title="Environmental Training",
    eyebrow="Environmental training",
    h1="Practical training for site and compliance teams",
    lede="Practical training for site teams on monitoring, permit conditions and environmental record-keeping.",
    img="assets/img/svc-card-8.webp",
    chips=["Site and operations teams", "HSE staff", "Compliance officers", "New facilities"],
    overview_h="Environmental training services",
    overview_p="Training built around the obligations a specific facility actually carries, so the people responsible "
               "understand what their permit requires and how to evidence it.",
    features=[("fa-file-contract", "Understanding permit conditions"),
              ("fa-gauge", "Monitoring and measurement practice"),
              ("fa-folder-open", "Environmental register upkeep"),
              ("fa-recycle", "Waste handling and manifests"),
              ("fa-triangle-exclamation", "Incident response and reporting"),
              ("fa-clipboard-check", "Inspection readiness")],
    req_rows=[("Authority", CONFIRM),
              ("Usually needed", "Training records are commonly requested at inspection" + CONFIRM),
              ("Typical duration", "Scoped to the facility and the team size"),
              ("Common hold-up", "Generic training that does not match the facility's actual conditions")],
    standards=["Built around your own permit conditions", "Attendance and content recorded", CONFIRM],
    approach="We read the facility's conditions first, build the session around what those conditions actually "
             "require, and leave behind a record of what was covered and who attended.",
    meta="Environmental training in Saudi Arabia, practical sessions for site teams on permit conditions, "
         "monitoring practice, environmental registers and inspection readiness.",
)


def card_page(s, related):
    chips = "".join(f'<span class="svq-chip">{c}</span>' for c in s["chips"])

    feats = "".join(f'''
        <div class="svq-f"><i class="fas {ic}"></i><span>{tx}</span></div>''' for ic, tx in s["features"])

    rows = "".join(f'''
          <div class="svq-row"><b>{k}</b><span>{v}</span></div>''' for k, v in s["req_rows"])

    stds = "".join(f'''
          <div class="svq-std"><i class="fas fa-check"></i><span>{x}</span></div>''' for x in s["standards"])

    who = "".join(f'''
        <div class="svq-who scroll-reveal"><h3>{t}</h3><p>{d}</p></div>''' for t, d in s["who"])

    faqs = "".join(f'''
        <details class="svq-faq"><summary>{q}<i class="fas fa-plus"></i></summary>
        <div class="svq-faq-a">{a}</div></details>''' for q, a in s["faqs"])

    rel = "".join(f'''
        <a href="service-{r['slug']}.html" class="svq-rel">
          <span class="svq-rel-img" style="background-image:url('{r['img']}')"></span>
          <span class="svq-rel-t">{r['title']}</span>
        </a>''' for r in related)

    return f'''
<!-- HERO -->
<section class="svq-hero">
  <div class="svq-hero-img" style="background-image:url('{s["img"]}')" aria-hidden="true"></div>
  <div class="svq-hero-scrim" aria-hidden="true"></div>
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
    <div class="crumb crumb-dark"><a href="index.html">Home</a><i class="fas fa-chevron-right" style="font-size:.55rem;"></i><a href="services.html">Services</a><i class="fas fa-chevron-right" style="font-size:.55rem;"></i><span>{s["title"]}</span></div>
    <div class="svq-eyebrow">{s["eyebrow"]}</div>
    <h1 class="svq-h1">{s["h1"]}</h1>
    <p class="svq-lede">{s["lede"]}</p>
    <div class="svq-chips">{chips}</div>
  </div>
</section>

<!-- OVERVIEW + STANDARDS -->
<section class="py-16 bg-white">
  <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="svq-grid">
      <div class="scroll-reveal">
        <div class="showcase-eyebrow">Overview</div>
        <h2 class="text-2xl lg:text-3xl font-bold text-bp-ink mb-4 tracking-tight">{s["overview_h"]}</h2>
        <p class="text-gray-600 leading-relaxed mb-7">{s["overview_p"]}</p>
        <div class="svq-feats">{feats}</div>
        <div class="svq-steps">
          <div class="svq-step"><b>1. Scope</b><span>Agreed in writing before fieldwork</span></div>
          <div class="svq-step"><b>2. Survey</b><span>Field work to stated methods</span></div>
          <div class="svq-step"><b>3. Analyse</b><span>Laboratory and data validation</span></div>
          <div class="svq-step"><b>4. Report</b><span>In the reviewer&rsquo;s format</span></div>
        </div>
      </div>
      <aside class="svq-side scroll-reveal">
        <i class="fas fa-certificate svq-side-ic"></i>
        <h3>Standards applied</h3>
        <p>Every result is reported against the method used, so a reviewer can verify it rather than take it on trust.</p>
        {stds}
        <a href="contact.html" class="svq-btn">Free consultation</a>
      </aside>
    </div>
  </div>
</section>

<!-- REQUIREMENT + APPROACH -->
<section class="py-16" style="background:var(--bp-page);">
  <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="svq-two">
      <div class="scroll-reveal">
        <div class="showcase-eyebrow">The requirement</div>
        <h2 class="text-2xl lg:text-3xl font-bold text-bp-ink mb-5 tracking-tight">What the regulator asks for</h2>
        <div class="svq-req">{rows}</div>
      </div>
      <div class="scroll-reveal svq-approach">
        <div class="showcase-eyebrow">Our approach</div>
        <h2 class="text-2xl lg:text-3xl font-bold text-bp-ink mb-4 tracking-tight">How we run it</h2>
        <p class="text-gray-600 leading-relaxed mb-6">{s["approach"]}</p>
        <a href="contact.html" class="svq-btn">Free consultation</a>
      </div>
    </div>
  </div>
</section>

<!-- STATEMENT BAND -->
<section class="svq-band">
  <div class="svq-band-img" style="background-image:url('{s["img"]}')" aria-hidden="true"></div>
  <div class="svq-band-scrim" aria-hidden="true"></div>
  <div class="max-w-3xl mx-auto px-6 relative z-10 text-center">
    <p class="svq-band-q">{s["band_quote"]}</p>
    <a href="contact.html" class="svq-band-cta">Free consultation <i class="fas fa-arrow-right" style="font-size:.7rem;"></i></a>
  </div>
</section>

<!-- WHO IT IS FOR + FAQ -->
<section class="py-16 bg-white">
  <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="svq-two">
      <div>
        <div class="showcase-eyebrow">Applicability</div>
        <h2 class="text-2xl lg:text-3xl font-bold text-bp-ink mb-6 tracking-tight">Who this is for</h2>
        <div class="svq-whos">{who}</div>
      </div>
      <div>
        <div class="showcase-eyebrow">Questions</div>
        <h2 class="text-2xl lg:text-3xl font-bold text-bp-ink mb-4 tracking-tight">Common questions</h2>
        <div>{faqs}</div>
      </div>
    </div>
  </div>
</section>

<!-- RELATED -->
<section class="py-14" style="background:var(--bp-page);">
  <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="showcase-eyebrow">Related services</div>
    <h2 class="text-xl lg:text-2xl font-bold text-bp-ink mb-6 tracking-tight">Explore our other environmental services</h2>
    <div class="svq-rels">{rel}</div>
  </div>
</section>

<!-- CTA -->
<section class="svq-cta">
  <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 svq-cta-in">
    <div>
      <h2>Free consultation</h2>
      <p>Tell us the site and what is planned, and we will scope the work.</p>
    </div>
    <a href="contact.html" class="svq-cta-btn">Free consultation</a>
  </div>
</section>
'''
