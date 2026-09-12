# Blog and legal pages, content mirrored from the client's own site.

ARTICLES = [
    dict(slug="mwan-waste-permit-guide",
         title="The Complete Guide to MWAN Waste Management Permits in Saudi Arabia",
         date="July 20, 2026", read="2 min read",
         img="assets/img/svc-permit.jpg",
         fb="assets/img/svc-waste.jpg",
         cat="Waste Permits",
         summary="Everything facility owners need to know about National Waste Management Center permits, who needs one, the documents required, and how to avoid the delays that catch most applicants."),
    dict(slug="environmental-permit-categories",
         title="Environmental Permit Categories in Saudi Arabia: Which One Applies to You",
         date="July 22, 2026", read="3 min read",
         img="assets/img/svc-air.jpg",
         fb="assets/img/svc-water.jpg",
         cat="Permitting",
         summary="Category 1, 2, or 3 determines the studies you need, what you will pay, and how long licensing takes. Misclassifying your activity is the most expensive mistake we see."),
    dict(slug="environmental-permit-renewal",
         title="Renewing Your Environmental Permit: Start Six Months Early",
         date="July 24, 2026", read="2 min read",
         img="assets/img/svc-lab.jpg",
         fb="assets/img/svc-soil.jpg",
         cat="Renewals",
         summary="Renewal is not a formality. Reviewers examine your compliance history, and an expired permit puts you in violation immediately, with no grace period in practice."),
    dict(slug="environmental-compliance-violations",
         title="The Six Environmental Violations Saudi Inspectors Find Most Often",
         date="July 26, 2026", read="3 min read",
         img="assets/img/svc-noise.jpg",
         fb="assets/img/svc-field.jpg",
         cat="Inspections",
         summary="Almost every finding we see falls into the same handful of categories, and nearly all of them are documentation problems rather than engineering failures."),
    dict(slug="quarry-studies-and-rehabilitation",
         title="Quarry Studies and Rehabilitation: The Obligation That Outlives the Site",
         date="July 27, 2026", read="2 min read",
         img="assets/img/spec-marine.jpg",
         fb="assets/img/spec-ecology.jpg",
         cat="Quarries & Mining",
         summary="Extraction sites commit to a rehabilitation obligation years before it comes due. It does not expire because the quarry closed, sat idle, or changed hands."),
]


def blog(page_header, ARTICLES=None):
    import content as _C
    ARTICLES = ARTICLES or list(reversed(_C.load_blog()))
    feat = ARTICLES[-1]
    rest = list(reversed(ARTICLES[:-1]))

    def _is_update(a):
        return str(a.get('type', '')).lower() == 'update' or 'update' in str(a.get('cat', '')).lower()

    def _slugcat(c):
        return ''.join(ch.lower() if ch.isalnum() else '-' for ch in str(c)).strip('-')

    cats, seen = [], set()
    for a in ARTICLES:
        c = a.get('cat', 'Insight')
        if c not in seen:
            seen.add(c)
            cats.append(c)
    filters = '<button type="button" class="blogf on" data-c="all">All</button>' + "".join(
        f'''<button type="button" class="blogf" data-c="{_slugcat(c)}">{c}</button>''' for c in cats)

    def _badges(a):
        b = ''
        if _is_update(a):
            b += '<span class="blog-tag t-upd">Regulatory update</span>'
        if str(a.get('action', '')).lower() in ('true', 'yes', '1'):
            b += '<span class="blog-tag t-act">Action required</span>'
        return b

    cards = "".join(f'''
      <article class="news-card{" is-update" if _is_update(a) else ""}" data-c="{_slugcat(a.get('cat','Insight'))}">
        <a href="blog-{a['slug']}.html" class="card-img-wrap block">
          <img src="{a['img']}?w=800&h=450&fit=crop&q=80" alt="{a['title']}" loading="lazy" onerror="this.onerror=null;this.src='{a['fb']}?w=800&h=450&fit=crop'" />
          <div class="card-img-overlay"></div>
          <span class="card-badge" style="background:rgba(14, 147, 168.14);color:var(--bp-blue-deep);">{a['cat']}</span>
        </a>
        <div class="card-body">
          <div class="blog-tags">{_badges(a)}</div>
          <h3 class="card-title"><a href="blog-{a['slug']}.html" style="color:inherit;text-decoration:none;">{a['title']}</a></h3>
          <p class="card-desc">{a['summary']}</p>
          <div class="card-footer">
            <span class="card-time">{a['date']} &middot; {a['read']}</span>
            <a href="blog-{a['slug']}.html" class="read-more">Read <i class="fas fa-arrow-right" style="font-size:.65rem;"></i></a>
          </div>
        </div>
      </article>''' for a in rest)

    return page_header("The compliance briefing",
                       "Practical guides and regulatory updates from our consultants, everything you need to keep your facility ahead of Saudi environmental requirements.",
                       "Blog") + f"""
<section class="py-20" style="background:var(--bp-page);">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">

    <a href="blog-{feat['slug']}.html" class="block bg-white rounded-3xl overflow-hidden shadow-lg hover:shadow-2xl transition-all mb-10 scroll-reveal group" style="text-decoration:none;">
      <div class="grid md:grid-cols-2 items-stretch">
        <div class="relative h-64 md:h-auto overflow-hidden">
          <img src="{feat['img']}?w=900&h=700&fit=crop&q=80" alt="{feat['title']}" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" onerror="this.src='{feat['fb']}?w=900&h=700&fit=crop'" />
          <span class="absolute top-4 left-4 text-xs font-bold text-white px-3 py-1.5 rounded-full" style="background:var(--bp-olive);">Latest</span>
        </div>
        <div class="p-8 md:p-10 flex flex-col justify-center">
          <span class="showcase-eyebrow" style="margin-bottom:12px;">{feat['cat']}</span>
          <h2 class="font-display text-2xl md:text-3xl font-bold text-bp-ink leading-snug mb-4">{feat['title']}</h2>
          <p class="text-gray-600 leading-relaxed mb-6">{feat['summary']}</p>
          <div class="flex items-center gap-3 text-sm text-gray-400">
            <span>{feat['date']}</span><span>&middot;</span><span>{feat['read']}</span>
            <span class="ml-auto font-semibold text-bp-primary">Read article <i class="fas fa-arrow-right" style="font-size:.7rem;"></i></span>
          </div>
        </div>
      </div>
    </a>

    <div class="blog-filters scroll-reveal" id="blogFilters">{filters}</div>

    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 scroll-reveal" id="blogGrid">{cards}
    </div>
    <p class="blog-empty" id="blogEmpty">Nothing in this category yet.</p>
  </div>
</section>

<section class="py-20 text-white" style="background:var(--bp-grad);">
  <div class="max-w-3xl mx-auto px-4 text-center">
    <h2 class="font-display text-3xl md:text-4xl font-bold mb-4">Ask our consultants directly.</h2>
    <p class="text-white/80 mb-8 text-lg">Reading up is a great start, but every facility is different. Get advice specific to yours.</p>
    <div class="flex flex-wrap justify-center gap-3">
      <a data-wa="Hello BluePrint, I would like to ask about your environmental services." class="px-7 py-3.5 bg-white text-bp-ink rounded-full font-bold hover:bg-bp-sage transition-all inline-flex items-center gap-2"><i class="fab fa-whatsapp"></i> Chat on WhatsApp</a>
      <a data-tel class="px-7 py-3.5 border-2 border-white/60 text-white rounded-full font-bold hover:bg-white hover:text-bp-ink transition-all inline-flex items-center gap-2"><i class="fas fa-phone" style="font-size:.85rem;"></i> <span data-text="phone"></span></a>
    </div>
  </div>
</section>

<script>
(function () {{
  var bar = document.getElementById('blogFilters');
  if (!bar) return;
  var cards = document.querySelectorAll('#blogGrid .news-card');
  var empty = document.getElementById('blogEmpty');
  bar.addEventListener('click', function (e) {{
    var b = e.target.closest('.blogf');
    if (!b) return;
    bar.querySelectorAll('.blogf').forEach(function (x) {{ x.classList.remove('on'); }});
    b.classList.add('on');
    var c = b.dataset.c, shown = 0;
    cards.forEach(function (card) {{
      var hit = (c === 'all' || card.dataset.c === c);
      card.style.display = hit ? '' : 'none';
      if (hit) shown++;
    }});
    empty.style.display = shown ? 'none' : 'block';
  }});
}})();
</script>
"""


ARTICLE_BODIES = {
"mwan-waste-permit-guide": """
<p class="lead">If your facility generates, transports, treats, or stores waste in Saudi Arabia, the National Waste Management Center (MWAN) almost certainly requires you to hold a valid permit. Yet most first-time applicants underestimate the preparation involved, and pay for it in weeks of avoidable delays.</p>

<h2>Who needs an MWAN permit?</h2>
<p>MWAN&rsquo;s licensing framework covers the full waste lifecycle. You will need a permit if your activity involves:</p>
<ul>
  <li>Generating industrial, commercial, or hazardous waste beyond household quantities</li>
  <li>Transporting waste of any classification</li>
  <li>Operating treatment, recycling, or sorting facilities</li>
  <li>Storing waste on-site beyond short-term operational limits</li>
  <li>Handling medical or veterinary waste streams</li>
</ul>
<p>Even facilities that outsource waste handling to licensed contractors often still carry <strong>generator obligations</strong>, including waste characterisation, manifesting, and record-keeping.</p>

<h2>The documents that decide your application</h2>
<p>In our experience, the difference between a smooth approval and a rejection loop comes down to preparation of a few key documents:</p>
<ol>
  <li>A waste characterisation study that matches your actual waste streams</li>
  <li>An up-to-date environmental register for the facility</li>
  <li>Storage and handling procedures aligned with MWAN technical guidelines</li>
  <li>Contracts with licensed transporters and treatment facilities</li>
  <li>An emergency response plan proportionate to your waste classes</li>
</ol>
<blockquote>The single most common rejection reason we see is a mismatch between the declared waste classification and what the facility actually produces. Get the characterisation right first, everything else builds on it.</blockquote>

<h2>How long does it take?</h2>
<p>With complete documentation, straightforward applications typically clear review in a few weeks. Complex facilities, multiple waste classes, hazardous streams, or on-site treatment, should budget longer, plus time for any site inspection MWAN schedules.</p>

<h2>Renewals are not a formality</h2>
<p>Permits are time-limited, and renewal reviews increasingly examine your <strong>compliance history</strong>: late periodic reports, manifest gaps, or unresolved inspection findings will surface at renewal. Treat your reporting calendar as part of the permit itself.</p>

<h2>How BluePrint helps</h2>
<p>We prepare and file MWAN applications end-to-end: characterisation studies, register updates, procedure documentation, and direct coordination with the regulator until approval. If a permit is nearing renewal, we audit your compliance record first, so the renewal file goes in clean.</p>
""",
"environmental-permit-categories": """
<p class="lead">Before anything else in the permitting process, one question decides your cost, your timeline and the studies you will need to commission: which category does your activity fall into? Get it wrong and you either overspend on studies you never needed, or lose months when a reviewer reclassifies you upward.</p>

<h2>Why the category matters more than anything else</h2>
<p>Saudi environmental permitting is tiered by potential impact. The tier your activity sits in determines three things at once:</p>
<ul>
  <li><strong>What you must submit</strong>, a simple declaration, or a full impact assessment with field baseline data</li>
  <li><strong>How long review takes</strong>, weeks at the lower tier, months at the upper</li>
  <li><strong>What it costs</strong>, the studies, not the permit fee, are the real expense</li>
</ul>

<h2>The three tiers in practice</h2>
<h3>Category 1, lower impact</h3>
<p>Small commercial and service premises: retail units, offices, small workshops, clinics. The route is simplified, activity details, site information and basic supporting documents. Most facilities here are surprised there is any requirement at all, and only discover it when a municipal or commercial licence renewal is blocked.</p>

<h3>Category 2, moderate impact</h3>
<p>Medium manufacturing, food processing, larger workshops, construction projects above a threshold. This tier usually requires an environmental management plan and, depending on the activity, supporting measurement data. It is the tier most often <strong>misdeclared</strong>, operators classify themselves as Category 1 based on floor area or headcount, when the classification actually follows the <em>process</em> and its emissions.</p>

<h3>Category 3, higher impact</h3>
<p>Heavy industry, petrochemicals, cement, power generation, hazardous waste treatment, quarrying. A full Environmental Impact Assessment is required, with field baseline surveys, dispersion or hydrological modelling where relevant, and a detailed mitigation and monitoring programme.</p>

<blockquote>The most expensive mistake we see is not under-preparing. It is preparing thoroughly for the wrong category, then having to start again when the reviewer disagrees with the classification.</blockquote>

<h2>What actually determines your category</h2>
<p>Not your company size, and not your building. Classification follows the activity itself:</p>
<ol>
  <li>The nature of the process and what it emits, discharges or generates</li>
  <li>Production capacity, measured against defined thresholds</li>
  <li>The waste streams produced, and whether any are classified hazardous</li>
  <li>Site sensitivity, proximity to residential areas, coastline, protected habitat or groundwater</li>
  <li>Whether the activity appears on a scheduled list that fixes its category regardless of scale</li>
</ol>
<p>That last point catches people out. Some activities are assigned a category by name, so capacity arguments do not apply.</p>

<h2>Two failure modes, both costly</h2>
<p><strong>Declaring too low</strong> is the common one. The application is rejected or reclassified, you commission the studies you avoided, and you have lost a review cycle, often a quarter.</p>
<p><strong>Declaring too high</strong> is rarer and quieter. Nobody rejects it. You simply pay for baseline surveys and modelling your activity never required, and nobody tells you.</p>

<h2>How BluePrint approaches it</h2>
<p>We classify before we quote. A short scoping call covering your activity, capacity and site location is usually enough to place you accurately, and that determines the scope of everything after it. If your activity sits near a threshold, we will tell you, and tell you what the reviewer is likely to conclude, so there are no surprises at submission.</p>
""",

"environmental-permit-renewal": """
<p class="lead">Most operators treat permit renewal as an administrative formality, a form to submit shortly before expiry. It is not. Renewal review examines your compliance record across the entire permit term, and an expired permit puts you in violation from day one, with no grace period in practice.</p>

<h2>Start six months out. Here is why</h2>
<p>Six months sounds excessive until you map what has to happen:</p>
<ul>
  <li><strong>Months 6&ndash;5</strong>, internal compliance audit against your existing permit conditions</li>
  <li><strong>Months 5&ndash;4</strong>, close whatever gaps that audit finds, which is the part with no fixed duration</li>
  <li><strong>Months 4&ndash;3</strong>, carry out any measurements the renewal requires; some parameters need seasonal or repeated sampling</li>
  <li><strong>Months 3&ndash;2</strong>, compile the file, update the environmental register, prepare the submission</li>
  <li><strong>Months 2&ndash;0</strong>, submission, reviewer queries, and buffer</li>
</ul>
<p>Compress that into six weeks and something gives, usually the gap-closing, which is precisely what the reviewer looks at.</p>

<h2>What reviewers actually check</h2>
<p>A renewal is not a fresh application. The reviewer already has your file, and the questions are about the term you have just completed:</p>
<ol>
  <li>Were periodic environmental reports submitted on schedule, every cycle?</li>
  <li>Do measurement results show compliance, and where they do not, is there a documented corrective action?</li>
  <li>Is the environmental register current, complete and consistent with those reports?</li>
  <li>Were inspection findings from the term closed out, with evidence?</li>
  <li>Has the activity, capacity or site changed without notification?</li>
</ol>

<blockquote>The single most common renewal problem is a reporting gap from two years earlier that nobody noticed at the time. It surfaces at renewal, when there is no longer time to fix it quietly.</blockquote>

<h2>The change nobody declared</h2>
<p>Facilities evolve. A line is added, capacity increases, a new solvent enters the process, waste volume doubles. Each of those may require notification or a permit amendment at the time, not at renewal. Presenting a materially different facility from the one described in the original permit turns a renewal into a new application, with the timeline that implies.</p>

<h2>What an expired permit means</h2>
<p>Operating without a valid environmental permit is a violation from the day it lapses. Beyond any penalty, an expired permit can block the renewal of other licences that depend on it, commercial registration and municipal licensing among them. The operational consequence usually arrives before the environmental one.</p>

<h2>How BluePrint handles renewals</h2>
<p>We audit first and apply second. That means reviewing your compliance record before the file goes anywhere, so gaps are closed on your schedule rather than discovered on the reviewer's. For clients on ongoing reporting, renewal is largely a compilation exercise, because the record was maintained throughout the term rather than assembled at the end of it.</p>
""",

"environmental-compliance-violations": """
<p class="lead">Across the inspections we support, almost every finding falls into the same handful of categories. What is striking is how few are engineering failures. The overwhelming majority are documentation and record-keeping problems, which means they are avoidable at very little cost.</p>

<h2>1. Missing or late periodic reports</h2>
<p>The most frequent finding by a wide margin. Permit conditions set a reporting frequency, and it is easy for a cycle to slip when nobody owns the calendar. Inspectors check submission dates first because it is the fastest thing to verify.</p>
<p><strong>The fix:</strong> build the reporting calendar directly from your permit conditions, assign it to a named person, and schedule the measurements it depends on well in advance.</p>

<h2>2. An environmental register that is out of date</h2>
<p>The register is the first document requested in most inspections. Common problems are gaps in waste manifests, monitoring results filed in someone's inbox rather than the register, and chemical inventories that no longer match what is on site.</p>
<p><strong>The fix:</strong> treat the register as a live document with a review cadence, not an archive assembled when someone asks for it.</p>

<h2>3. Waste handling that does not match the declaration</h2>
<p>The permit describes certain waste streams, segregation and contracted disposal routes. The site does something slightly different, mixed storage, an uncontracted carrier, or a stream that appeared after the permit was issued and was never declared.</p>
<p><strong>The fix:</strong> reconcile actual waste streams against the declared inventory periodically, and verify that every carrier and treatment facility you use holds current authorisation.</p>

<blockquote>A licensed contractor collecting your waste does not transfer your obligation. Generator duties, characterisation, manifesting, record-keeping, stay with you.</blockquote>

<h2>4. Storage and containment gaps</h2>
<p>One of the few findings that is genuinely physical. Missing secondary containment under chemical or fuel storage, deteriorated bunding, drainage from a storage area running to a stormwater drain, or incompatible materials stored together.</p>
<p><strong>The fix:</strong> walk the site specifically against your permit's storage conditions. This is the category where a finding can become an incident.</p>

<h2>5. Monitoring that does not meet the specified method</h2>
<p>Measurements were taken, but not to the method, frequency or point the permit specifies, or by a party without the accreditation the results require. The data exists and is not accepted.</p>
<p><strong>The fix:</strong> check that every monitoring parameter names its method, location and frequency, and that whoever performs it is accredited for that work.</p>

<h2>6. An environmental management plan nobody follows</h2>
<p>The EMP exists because the permit required one. It sits in a folder. Site staff cannot describe the controls it specifies, and roles named in it belong to people who left.</p>
<p><strong>The fix:</strong> the EMP should be short enough to be usable, tied to named roles rather than individuals, and included in induction and refresher training.</p>

<h2>The pattern worth noticing</h2>
<p>Five of these six are administrative. They cost very little to prevent and a great deal to remediate under a deadline, with a finding already on record. An afternoon spent walking your permit conditions against your actual site and files will usually surface every one of them.</p>
""",

"quarry-studies-and-rehabilitation": """
<p class="lead">Extraction sites commit to a rehabilitation obligation years before it comes due, often at the point of licensing, when closure feels remote. That obligation does not expire because the quarry stopped producing, sat idle, or changed hands.</p>

<h2>The obligation begins on day one</h2>
<p>Rehabilitation is not something considered at closure. It is defined in the environmental approval that permitted extraction in the first place, and it usually specifies:</p>
<ul>
  <li>Final landform and slope stability requirements</li>
  <li>Topsoil stripping, storage and reinstatement, storage method matters, as poorly stored topsoil loses viability</li>
  <li>Revegetation with specified species and survival criteria</li>
  <li>Management of any water body left in the void</li>
  <li>Removal of infrastructure and remediation of contaminated ground</li>
  <li>Post-closure monitoring for a defined period</li>
</ul>
<p>Sites that plan for this progressively, rehabilitating worked-out areas while extraction continues elsewhere, spend a fraction of what sites face when the whole obligation lands at once.</p>

<h2>Studies required while operating</h2>
<p>Quarries and mining sites carry ongoing environmental obligations that are heavier than most operators anticipate:</p>
<ol>
  <li><strong>Dust monitoring</strong>, PM10 and TSP at site boundaries and nearby receptors</li>
  <li><strong>Noise and vibration</strong>, particularly where blasting occurs near communities or structures</li>
  <li><strong>Groundwater</strong>, monitoring where extraction approaches or intersects the water table</li>
  <li><strong>Surface water and runoff</strong>, sediment control and discharge quality</li>
  <li><strong>Slope and geotechnical stability</strong>, both a safety and an environmental requirement</li>
</ol>

<blockquote>Rehabilitation liability does not transfer cleanly with a site sale. Buyers who skip an environmental due diligence assessment routinely inherit an obligation far larger than the purchase discount they negotiated.</blockquote>

<h2>The idle-site trap</h2>
<p>A quarry that stops producing has not ceased to be a regulated site. Permits still require renewal, monitoring may still apply, and the rehabilitation commitment stands. Sites left dormant for years, with no monitoring record and no progressive rehabilitation, present the hardest cases we are asked to resolve, the obligation has accrued while the evidence of compliance has not.</p>

<h2>Progressive rehabilitation is cheaper</h2>
<p>Three reasons operators consistently underestimate:</p>
<ul>
  <li>Topsoil reinstated soon after stripping performs far better than topsoil stockpiled for a decade</li>
  <li>Equipment and crews are already mobilised on site, so the marginal cost is low</li>
  <li>It demonstrates good faith at every inspection and renewal in between</li>
</ul>

<h2>How BluePrint supports extraction sites</h2>
<p>We prepare the impact assessments and rehabilitation plans that extraction licensing requires, run the monitoring programmes that operations demand, and carry out closure and post-closure assessment. For sites already dormant with an unresolved obligation, we start with an assessment of what is actually owed, because in our experience that figure is rarely the one the operator has been assuming.</p>
""",

}


def article(a, page_header):
    body = ARTICLE_BODIES.get(a['slug'])
    if body is None:
        body = f"""
<p class="lead">{a['summary']}</p>
<div class="rounded-2xl p-6 my-8" style="background:var(--bp-blue-tint);border:1px solid var(--bp-border);">
  <p style="margin:0;"><strong>This article is being prepared.</strong> Our consultants are finalising it. In the meantime, if this topic affects your facility, get in touch, the initial consultation is free.</p>
</div>
"""
    import content as _C
    others = [x for x in _C.load_blog() if x['slug'] != a['slug']][:3]
    more = "".join(f"""
      <a href="blog-{o['slug']}.html" class="news-card block" style="text-decoration:none;">
        <div class="card-img-wrap"><img src="{o['img']}?w=600&h=340&fit=crop&q=80" alt="{o['title']}" loading="lazy" onerror="this.src='{o['fb']}?w=600&h=340&fit=crop'" /><div class="card-img-overlay"></div></div>
        <div class="card-body"><span class="card-time">{o['date']}</span><h3 class="card-title" style="margin-top:8px;">{o['title']}</h3></div>
      </a>""" for o in others)
    return f"""
<section class="page-header" style="padding-bottom:56px;">
  <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
    <div class="crumb"><a href="index.html">Home</a><i class="fas fa-chevron-right" style="font-size:.55rem;"></i><a href="blog.html">Blog</a></div>
    <h1 style="max-width:24ch;">{a['title']}</h1>
    <p style="margin-top:18px;font-size:.9rem;">{a['date']} &middot; {a['read']} &middot; BluePrint Environmental Services</p>
  </div>
</section>

<article class="py-16" style="background:var(--bp-page);">
  <div class="max-w-3xl mx-auto px-4 sm:px-6">
    <img src="{a['img']}?w=1000&h=520&fit=crop&q=80" alt="{a['title']}" class="w-full rounded-2xl shadow-lg mb-10" onerror="this.src='{a['fb']}?w=1000&h=520&fit=crop'" />
    <div class="article-body">{body}
      <div class="not-prose mt-10 rounded-2xl p-7 text-white" style="background:var(--bp-grad);">
        <h3 class="font-display text-xl font-bold mb-2">Not sure which permits apply to you?</h3>
        <p class="text-white/80 text-sm mb-5">Book a free consultation and we&rsquo;ll map exactly what your activity requires.</p>
        <a href="contact.html" class="inline-flex items-center gap-2 px-6 py-3 bg-white text-bp-ink rounded-full font-bold text-sm hover:bg-bp-sage transition-all">Book a free consultation <i class="fas fa-arrow-right" style="font-size:.7rem;"></i></a>
      </div>
    </div>

    <div class="flex flex-wrap items-center justify-between gap-4 mt-10 pt-8" style="border-top:1px solid var(--bp-border);">
      <a href="blog.html" class="btn-ghost"><i class="fas fa-arrow-left" style="font-size:.75rem;"></i> All articles</a>
      <div class="flex items-center gap-2">
        <span class="text-sm text-gray-400 mr-1">Share</span>
        <a href="https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblueprint-env.com%2Fblog%2F{a['slug']}" target="_blank" rel="noopener" class="w-9 h-9 rounded-lg bg-white border flex items-center justify-center text-bp-primary hover:bg-bp-light transition-all" style="border-color:var(--bp-border);" aria-label="Share on LinkedIn"><i class="fab fa-linkedin-in"></i></a>
        <a href="https://twitter.com/intent/tweet?url=https%3A%2F%2Fblueprint-env.com%2Fblog%2F{a['slug']}" target="_blank" rel="noopener" class="w-9 h-9 rounded-lg bg-white border flex items-center justify-center text-bp-primary hover:bg-bp-light transition-all" style="border-color:var(--bp-border);" aria-label="Share on X"><i class="fab fa-twitter"></i></a>
        <a data-wa="{a['title']}" class="w-9 h-9 rounded-lg bg-white border flex items-center justify-center hover:bg-bp-light transition-all" style="border-color:var(--bp-border);color:#25D366;" aria-label="Share on WhatsApp"><i class="fab fa-whatsapp"></i></a>
      </div>
    </div>
  </div>
</article>

<section class="py-16 bg-white">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="showcase-eyebrow">Keep reading</div>
    <h2 class="font-display text-3xl font-bold text-bp-ink mb-8">More from the briefing.</h2>
    <div class="grid grid-cols-1 md:grid-cols-3 gap-6">{more}
    </div>
  </div>
</section>
"""


LEGAL = {
"privacy": ("Privacy Policy", "How BluePrint Environmental Services collects, uses, and protects your personal information.", "July 1, 2026", """
<h2>Introduction</h2>
<p>BluePrint Environmental Services (&ldquo;BluePrint&rdquo;, &ldquo;we&rdquo;, &ldquo;us&rdquo;) respects your privacy. This policy explains what information we collect through our website, how we use it, and the choices you have.</p>

<h2>Information we collect</h2>
<ul>
  <li><strong>Contact details</strong> you provide through our enquiry form: name, email, phone, company, and the message you send.</li>
  <li><strong>Technical data</strong> such as your IP address and basic analytics about how you use the site.</li>
</ul>

<h2>How we use your information</h2>
<p>We use the information you provide to respond to your enquiry, prepare consultations and proposals, and improve our services. We do not sell your personal data to third parties.</p>

<h2>Data retention</h2>
<p>Enquiry records are retained only as long as necessary to serve you and to meet our legal and business obligations, after which they are securely deleted.</p>

<h2>Your rights</h2>
<p>You may request access to, correction of, or deletion of the personal information we hold about you by contacting us at the email address below.</p>

<h2>Cookies &amp; analytics</h2>
<p>We may use cookies and privacy-respecting analytics to understand site usage. You can control cookies through your browser settings.</p>

<h2>Contact</h2>
<p>For any privacy question, email us at <a data-mail data-text="email"></a> and we will respond promptly.</p>
"""),
"terms": ("Terms &amp; Conditions", "The terms and conditions governing use of the BluePrint Environmental Services website and services.", "July 1, 2026", """
<h2>Acceptance of terms</h2>
<p>By accessing and using the BluePrint Environmental Services website, you agree to these terms and conditions. If you do not agree, please do not use the site.</p>

<h2>Use of the website</h2>
<p>The content on this site is provided for general information about our environmental consulting services. It does not constitute regulatory, legal, or professional advice, and should not be relied upon as a substitute for a formal engagement with our consultants.</p>

<h2>Intellectual property</h2>
<p>All content, branding, text, and graphics on this website are the property of BluePrint Environmental Services unless otherwise stated, and may not be reproduced without permission.</p>

<h2>Service engagements</h2>
<p>Any environmental study, permit application, or compliance work is governed by a separate written agreement. The scope, deliverables, and fees for such work are defined in that agreement, not on this website.</p>

<h2>Limitation of liability</h2>
<p>While we strive to keep information accurate and current, BluePrint makes no warranties about the completeness or accuracy of website content and is not liable for decisions taken solely on that basis.</p>

<h2>Changes to these terms</h2>
<p>We may update these terms from time to time. Continued use of the site after changes constitutes acceptance of the revised terms.</p>

<h2>Governing law</h2>
<p>These terms are governed by the laws of the Kingdom of Saudi Arabia.</p>
"""),
}


def legal(key, page_header):
    title, desc, updated, body = LEGAL[key]
    return page_header(title, desc, "Legal") + f"""
<section class="py-16" style="background:var(--bp-page);">
  <div class="max-w-3xl mx-auto px-4 sm:px-6">
    <div class="bg-white rounded-3xl shadow-lg p-8 md:p-12">
      <p class="text-sm text-gray-400 mb-8 pb-6" style="border-bottom:1px solid var(--bp-border);">Last updated: {updated}</p>
      <div class="article-body">{body}</div>
    </div>
    <p class="text-center text-sm text-gray-500 mt-8">Questions about this page? <a href="contact.html" class="text-bp-primary font-semibold">Get in touch</a>.</p>
  </div>
</section>
"""
