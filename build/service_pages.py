# Service detail pages, one per service, English and Arabic.
# Content is factual about KSA environmental regulation; nothing about
# BluePrint's history, clients or scale is asserted here.

SERVICES = {}

SERVICES["air-quality-monitoring"] = dict(
    group="monitoring", num="01",
    slug="air-quality-monitoring",
    title="Air Quality Monitoring &amp; Testing",
    tagline="Measurement that stands up to review",
    lede="Ambient and stack air quality measured to the method your permit specifies, "
         "reported in the form the regulator expects.",
    hero_img="assets/img/svc-air-hero.jpg",
    detail_img="assets/img/svc-air-detail.jpg",
    band_img="assets/img/svc-air-lab.jpg",
    band_quote="Data that does not match the method named in your permit is not accepted, however carefully it was collected.",
    faq_title="Before you commission monitoring",
    float_head=("fa-wind", "What gets measured"),
    float_rows=[("8+", "Parameters measured", "PM, NO&#8322;, SO&#8322;, CO, O&#8323;, VOCs"),
                ("24/7", "Campaign coverage", "Where the condition requires it"),
                ("1", "Accredited method", "Named in your permit")],
    float2=("fa-certificate", "Accredited", "Results the regulator accepts"),
    meta="Accredited ambient and stack air quality monitoring in Saudi Arabia, PM10, PM2.5, "
         "NOx, SO2, CO, VOCs and dust, measured to NCEC-referenced methods and reported for compliance.",

    problem_title="What the regulator actually asks for",
    problem_body=[
        "Air quality conditions appear in almost every environmental permit issued in the Kingdom, "
        "but the wording is specific: a named parameter, a named method, a stated frequency and a "
        "defined measurement point. Data that does not match all four is not accepted, however "
        "carefully it was collected.",
        "The other half of the problem is timing. Some parameters need seasonal coverage or repeated "
        "campaigns before the result means anything. Facilities that commission monitoring a month "
        "before a reporting deadline routinely discover they cannot produce a defensible dataset in time.",
    ],
    problem_points=[
        ("Parameter", "Exactly which pollutants your activity must report"),
        ("Method", "The sampling and analysis standard the condition references"),
        ("Frequency", "How often, and over what averaging period"),
        ("Location", "Boundary, receptor or stack, and how many points"),
    ],

    included_title="What we deliver",
    included=[
        ("Ambient air quality monitoring",
         "PM10, PM2.5, NO&#8322;, SO&#8322;, CO, O&#8323; and VOCs measured at facility boundaries or nominated receptors, "
         "with meteorological data recorded alongside so results can be interpreted."),
        ("Stack and point-source emissions",
         "Isokinetic sampling and analysis of point-source emissions, with flow, temperature and moisture "
         "recorded so concentrations can be converted to the reference conditions your permit uses."),
        ("Dust and particulate deposition",
         "Deposition gauges and directional dust monitoring for construction, quarrying and materials "
         "handling operations where nuisance dust is the primary concern."),
        ("Indoor and workplace air quality",
         "Measurement inside process areas and enclosed spaces where occupational exposure or "
         "ventilation performance is in question."),
        ("Interpretation and reporting",
         "Results compared against the limits that apply to your activity, with the exceedances, "
         "the likely causes and the corrective actions stated plainly."),
    ],

    process_title="How a monitoring campaign runs",
    process=[
        ("Scope", "We read your permit conditions and identify every air parameter, method and frequency "
                  "they require, before quoting anything."),
        ("Plan", "Measurement points are chosen against the standard, not convenience: boundary positions, "
                 "receptor locations and stack ports are fixed and documented."),
        ("Measure", "Field teams deploy calibrated instruments and follow chain-of-custody for any samples "
                    "sent for laboratory analysis."),
        ("Report", "Results are compiled against the applicable limits and issued in the format your "
                   "periodic report requires, with raw data retained for audit."),
    ],

    applies_title="Who needs air quality monitoring",
    applies=[
        ("Factories &amp; manufacturing",
         "Process emissions, solvent use and combustion sources put most manufacturing facilities into "
         "an ambient monitoring obligation, and often a stack testing one as well. The parameters depend "
         "on the process rather than the size of the plant, which is why two similar-looking facilities "
         "can carry very different requirements."),
        ("Cement, quarrying &amp; materials",
         "Dust is the defining issue: deposition at site boundaries, PM10 at the nearest receptors, and "
         "directional monitoring where a complaint has been raised. These sites are also the most likely "
         "to face community pressure, so the record matters beyond the permit."),
        ("Power &amp; desalination",
         "Combustion plant carries stack emission limits and, above certain thresholds, continuous "
         "monitoring obligations. Reporting cycles are frequent and the data volume is significant, so "
         "the reporting workflow matters as much as the measurement itself."),
        ("Petrochemicals &amp; refining",
         "VOCs, fugitive emissions and flare-related parameters sit alongside conventional stack testing. "
         "Fugitive emissions in particular need a survey approach rather than fixed-point measurement, "
         "and the method has to be agreed before work starts."),
        ("Construction &amp; infrastructure",
         "Impacts are temporary but intensive, and monitoring is usually tied to a construction "
         "environmental management plan rather than an operating permit. Dust and plant emissions are "
         "the common parameters, measured at the site boundary."),
        ("Waste management",
         "Landfill gas, odour and combustion emissions each need a different technique. Odour in "
         "particular is assessed rather than simply measured, which means the survey design carries "
         "more weight than the instrument used."),
    ],

    grid_title="What you get out of it",
    caps=[
        ("Reviewed before you commit",
         "We read the conditions and tell you what actually applies before any scope is agreed, so you are "
         "not paying for work the regulator never asked for.",
         "assets/img/sector-1.jpg", "1st", "time through review"),
        ("Defensible documentation",
         "Everything is produced to the standard the condition references, with the method and evidence "
         "recorded alongside the result.",
         "assets/img/sector-2.jpg", "100%", "method-referenced"),
        ("Nothing filed at the last minute",
         "Work is scheduled against your obligations so the deadline is met from a maintained record "
         "rather than a scramble.",
         "assets/img/sector-3.jpg", "On time", "every cycle"),
        ("One accountable team",
         "The people who scoped the work carry it through submission and answer the reviewer's questions "
         "directly.",
         "assets/img/svc-air-detail.jpg", "Single", "point of contact"),
    ],
    faqs=[
        ("How do I know which parameters my facility has to monitor?",
         "They are named in your environmental permit conditions. If the wording is unclear, or the "
         "permit predates a change in your process, we review it and tell you what applies before "
         "any work is quoted."),
        ("Does monitoring have to be done by an accredited party?",
         "For results submitted to a regulator, yes, accreditation is what makes the data admissible. "
         "Measurements taken by an unaccredited party are commonly rejected at review even when the "
         "underlying work was sound."),
        ("How long does a campaign take?",
         "A single ambient survey can be completed in days. Parameters requiring seasonal coverage or "
         "repeated campaigns run over months. The permit condition determines this, not the budget."),
        ("What happens if a result exceeds the limit?",
         "We tell you immediately rather than at report stage, identify the likely source, and set out "
         "the corrective action. An exceedance with a documented response is a far better position at "
         "inspection than one discovered later."),
        ("Can you take over monitoring from another provider?",
         "Yes. We review the existing dataset first, because gaps and method inconsistencies in "
         "historical data tend to surface at permit renewal."),
    ],
)


def service_page(s, page_header, related):
    problem_paras = "".join(f'<p class="text-gray-600 leading-relaxed mb-4">{p}</p>' for p in s["problem_body"])
    problem_pts = "".join(f'''
          <div class="svcd-spec">
            <span class="svcd-spec-k">{k}</span>
            <span class="svcd-spec-v">{v}</span>
          </div>''' for k, v in s["problem_points"])

    included = "".join(f'''
      <div class="svcd-inc scroll-reveal">
        <span class="svcd-inc-n">{i:02d}</span>
        <div><h3>{t}</h3><p>{d}</p></div>
      </div>''' for i, (t, d) in enumerate(s["included"], 1))

    process = "".join(f'''
      <div class="svcd-step scroll-reveal">
        <span class="svcd-step-n">{i:02d}</span>
        <h3>{t}</h3><p>{d}</p>
      </div>''' for i, (t, d) in enumerate(s["process"], 1))

    # sectors become tabs with an image, as on the reference
    tabs = "".join(f'''<button class="svcd-tab{" active" if i==0 else ""}" onclick="svcdTab({i})" type="button">{t}</button>'''
                   for i, (t, d) in enumerate(s["applies"]))
    panes = "".join(f'''
        <div class="svcd-pane{" active" if i==0 else ""}" data-pane="{i}">
          <div class="svcd-pane-img" style="background-image:url(\'assets/img/sector-{(i%3)+1}.jpg\')"></div>
          <div class="svcd-pane-body">
            <h3>{t}</h3>
            <p>{d}</p>
            <a href="contact.html" class="svcd-pane-link">Discuss your site <i class="fas fa-arrow-right"></i></a>
          </div>
        </div>''' for i, (t, d) in enumerate(s["applies"]))

    def _frow(r):
        if len(r) == 3:
            return (f'<div class="svcd-float-row"><span class="svcd-float-num">{r[0]}</span>'
                    f'<div><b>{r[1]}</b><span>{r[2]}</span></div></div>')
        return f'<div class="svcd-float-row"><div><b>{r[0]}</b><span>{r[1]}</span></div></div>'
    float_rows = "".join(_frow(r) for r in s["float_rows"])

    caps = "".join(f'''
      <div class="svcd-cap-item scroll-reveal">
        <div class="svcd-cap-media">
          <div class="svcd-cap-img" style="background-image:url(\'{img}\')"></div>
          <div class="svcd-cap-badge"><b>{badge}</b><span>{badge_sub}</span></div>
        </div>
        <div class="svcd-cap-body">
          <h3>{t}</h3>
          <p>{d}</p>
        </div>
      </div>''' for t, d, img, badge, badge_sub in s.get("caps", []))

    faqs = "".join(f'''
      <details class="svcd-faq">
        <summary>{q}<i class="fas fa-plus"></i></summary>
        <div class="svcd-faq-a">{a}</div>
      </details>''' for q, a in s["faqs"])

    rel = "".join(f'''
      <a href="service-{r[0]}.html" class="svcd-rel">
        <span class="svcd-rel-n">{r[2]}</span>
        <span class="svcd-rel-t">{r[1]}</span>
        <i class="fas fa-arrow-right"></i>
      </a>''' for r in related)

    return f'''
<!-- HERO, split, image card with floating spec panel -->
<section class="svcd-hero">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="crumb"><a href="index.html">Home</a><i class="fas fa-chevron-right" style="font-size:.55rem;"></i><a href="services.html">Services</a></div>
    <div class="svcd-hero-grid">
      <div class="svcd-hero-copy">
        <div class="svcd-kicker">{s.get("group_label","Compliance &amp; Permitting")}</div>
        <h1>{s["title"]}</h1>
        <p class="svcd-tagline">{s["tagline"]}</p>
        <p class="svcd-lede">{s["lede"]}</p>
        <div class="svcd-hero-cta">
          <a href="contact.html" class="btn-primary">Book a free consultation</a>
          <a data-wa="Hello BluePrint, I would like to ask about {s["title"]}." class="btn-ghost"><i class="fab fa-whatsapp"></i> Ask a question</a>
        </div>
      </div>
      <div class="svcd-hero-visual">
        <div class="svcd-hero-img" style="background-image:url(\'{s["hero_img"]}\')"></div>
        <div class="svcd-float">
          <div class="svcd-float-head"><i class="fas {s["float_head"][0]}"></i><span>{s["float_head"][1]}</span></div>
          {float_rows}
        </div>
        <div class="svcd-float-2">
          <i class="fas {s.get("float2", ("fa-check-circle","Accredited","NCEC &amp; MWAN"))[0]}"></i>
          <div><b>{s.get("float2", ("fa-check-circle","Accredited","NCEC &amp; MWAN"))[1]}</b>
          <span>{s.get("float2", ("fa-check-circle","Accredited","NCEC &amp; MWAN"))[2]}</span></div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- THE OBLIGATION, text with supporting image -->
<section class="py-24 bg-white">
  <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="grid lg:grid-cols-2 gap-16 items-center">
      <div class="scroll-reveal">
        <div class="showcase-eyebrow">The obligation</div>
        <h2 class="text-3xl lg:text-4xl font-bold text-bp-ink mb-5 tracking-tight">{s["problem_title"]}</h2>
        {problem_paras}
      </div>
      <div class="svcd-figure scroll-reveal">
        <div class="svcd-figure-img" style="background-image:url(\'{s.get("detail_img","assets/img/svc-air-detail.jpg")}\')"></div>
        <div class="svcd-figure-card">
          <span class="svcd-figure-k">{s.get("spec_label","Every condition specifies")}</span>
          {problem_pts}
        </div>
      </div>
    </div>
  </div>
</section>

<!-- SCOPE -->
<section class="py-24" style="background:var(--bp-page);">
  <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="text-center mb-14 scroll-reveal">
      <div class="showcase-eyebrow">Scope of work</div>
      <h2 class="text-3xl lg:text-4xl font-bold text-bp-ink tracking-tight">{s["included_title"]}</h2>
    </div>
    <div class="svcd-inc-grid">{included}</div>
  </div>
</section>

<!-- PROCESS -->
<section class="py-24 text-white" style="background:var(--bp-blue-ink);">
  <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="text-center mb-14 scroll-reveal">
      <div class="showcase-eyebrow" style="color:var(--bp-sage);">Process</div>
      <h2 class="text-3xl lg:text-4xl font-bold tracking-tight">{s["process_title"]}</h2>
    </div>
    <div class="svcd-steps">{process}</div>
  </div>
</section>

<!-- STATEMENT BAND over image -->
<section class="svcd-band">
  <div class="svcd-band-img" style="background-image:url(\'{s.get("band_img","assets/img/svc-air-lab.jpg")}\')" aria-hidden="true"></div>
  <div class="svcd-band-scrim" aria-hidden="true"></div>
  <div class="max-w-4xl mx-auto px-6 relative z-10 text-center">
    <p class="svcd-band-quote">{s.get("band_quote","Compliance is decided by the record, not by intention.")}</p>
    <a href="contact.html" class="svcd-band-cta">Have your conditions reviewed <i class="fas fa-arrow-right" style="font-size:.7rem;"></i></a>
  </div>
</section>

<!-- CAPABILITY GRID, small images with data overlays -->
<section class="py-24 bg-white">
  <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="text-center mb-16 scroll-reveal">
      <div class="showcase-eyebrow">Why it matters</div>
      <h2 class="text-3xl lg:text-4xl font-bold text-bp-ink tracking-tight">{s.get("grid_title","What you get out of it")}</h2>
    </div>
    <div class="svcd-cap">{caps}</div>
  </div>
</section>

<!-- SECTORS, tabbed, like the reference -->
<section class="py-24 bg-white">
  <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="text-center mb-12 scroll-reveal">
      <div class="showcase-eyebrow">Applicability</div>
      <h2 class="text-3xl lg:text-4xl font-bold text-bp-ink tracking-tight">{s["applies_title"]}</h2>
    </div>
    <div class="svcd-tabs scroll-reveal">{tabs}</div>
    <div class="svcd-panes scroll-reveal">{panes}</div>
  </div>
</section>

<!-- FAQ -->
<section class="py-24" style="background:var(--bp-page);">
  <div class="max-w-3xl mx-auto px-4 sm:px-6">
    <div class="text-center mb-12 scroll-reveal">
      <div class="showcase-eyebrow">Questions</div>
      <h2 class="text-3xl lg:text-4xl font-bold text-bp-ink tracking-tight">{s.get("faq_title","Common questions")}</h2>
    </div>
    <div class="scroll-reveal">{faqs}</div>
  </div>
</section>

<!-- RELATED -->
<section class="py-20 bg-white">
  <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
    <h2 class="text-2xl font-bold text-bp-ink mb-8 tracking-tight">Related services</h2>
    <div class="svcd-rels">{rel}</div>
  </div>
</section>

<section class="py-20 text-white" style="background:var(--bp-grad);">
  <div class="max-w-3xl mx-auto px-4 text-center">
    <h2 class="font-display text-3xl md:text-4xl font-bold mb-4">Not sure what your permit requires?</h2>
    <p class="text-white/80 mb-8">Send us the conditions and we will tell you exactly which parameters, methods and frequencies apply. No charge for the review.</p>
    <div class="flex flex-wrap justify-center gap-3">
      <a href="contact.html" class="px-7 py-3.5 bg-white text-bp-ink rounded-xl font-bold">Book a free consultation</a>
      <a data-wa="Hello BluePrint, I would like to ask about {s["title"]}." class="px-7 py-3.5 border-2 border-white/60 text-white rounded-xl font-bold inline-flex items-center gap-2"><i class="fab fa-whatsapp"></i> WhatsApp</a>
    </div>
  </div>
</section>

<script>
function svcdTab(i) {{
  document.querySelectorAll('.svcd-tab').forEach(function (b, n) {{ b.classList.toggle('active', n === i); }});
  document.querySelectorAll('.svcd-pane').forEach(function (p, n) {{ p.classList.toggle('active', n === i); }});
}}
</script>
'''
