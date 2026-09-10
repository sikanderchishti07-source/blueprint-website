# Blog and legal pages — content mirrored from the client's own site.

ARTICLES = [
    dict(slug="mwan-waste-permit-guide",
         title="The Complete Guide to MWAN Waste Management Permits in Saudi Arabia",
         date="July 20, 2026", read="2 min read",
         img="https://images.unsplash.com/photo-1532996122724-e3c354a0b15b",
         fb="https://images.unsplash.com/photo-1581094794329-c8112a89af12",
         cat="Waste Permits",
         summary="Everything facility owners need to know about National Waste Management Center permits — who needs one, the documents required, and how to avoid the delays that catch most applicants."),
    dict(slug="environmental-permit-categories",
         title="Environmental Permit Categories in Saudi Arabia: Which One Applies to You",
         date="July 22, 2026", read="2 min read",
         img="https://images.unsplash.com/photo-1450101499163-c8848c66ca85",
         fb="https://images.unsplash.com/photo-1521791136064-7986c2920216",
         cat="Permitting",
         summary="Category 1, 2, or 3 determines the studies you need, what you will pay, and how long licensing takes. Misclassifying your activity is the most expensive mistake we see."),
    dict(slug="environmental-permit-renewal",
         title="Renewing Your Environmental Permit: Start Six Months Early",
         date="July 24, 2026", read="2 min read",
         img="https://images.unsplash.com/photo-1509391366360-2e959784a276",
         fb="https://images.unsplash.com/photo-1466611653911-95081537e5b7",
         cat="Renewals",
         summary="Renewal is not a formality. Reviewers examine your compliance history, and an expired permit puts you in violation immediately — with no grace period in practice."),
    dict(slug="environmental-compliance-violations",
         title="The Six Environmental Violations Saudi Inspectors Find Most Often",
         date="July 26, 2026", read="2 min read",
         img="https://images.unsplash.com/photo-1565008447742-97f6f38c985c",
         fb="https://images.unsplash.com/photo-1473341304170-971dccb5ac1e",
         cat="Inspections",
         summary="Almost every finding we see falls into the same handful of categories — and nearly all of them are documentation problems rather than engineering failures."),
    dict(slug="quarry-studies-and-rehabilitation",
         title="Quarry Studies and Rehabilitation: The Obligation That Outlives the Site",
         date="July 27, 2026", read="2 min read",
         img="https://images.unsplash.com/photo-1578319439584-104c94d37305",
         fb="https://images.unsplash.com/photo-1441986300917-64674bd600d8",
         cat="Quarries & Mining",
         summary="Extraction sites commit to a rehabilitation obligation years before it comes due. It does not expire because the quarry closed, sat idle, or changed hands."),
]


def blog(page_header):
    feat = ARTICLES[-1]
    rest = list(reversed(ARTICLES[:-1]))
    cards = "".join(f"""
      <article class="news-card">
        <a href="blog-{a['slug']}.html" class="card-img-wrap block">
          <img src="{a['img']}?w=800&h=450&fit=crop&q=80" alt="{a['title']}" loading="lazy" onerror="this.onerror=null;this.src='{a['fb']}?w=800&h=450&fit=crop'" />
          <div class="card-img-overlay"></div>
          <span class="card-badge" style="background:rgba(0,113,129,.14);color:var(--bp-blue-deep);">{a['cat']}</span>
        </a>
        <div class="card-body">
          <h3 class="card-title"><a href="blog-{a['slug']}.html" style="color:inherit;text-decoration:none;">{a['title']}</a></h3>
          <p class="card-desc">{a['summary']}</p>
          <div class="card-footer">
            <span class="card-time">{a['date']} &middot; {a['read']}</span>
            <a href="blog-{a['slug']}.html" class="read-more">Read article <i class="fas fa-arrow-right" style="font-size:.65rem;"></i></a>
          </div>
        </div>
      </article>""" for a in rest)
    return page_header("The compliance briefing",
                       "Practical guides and regulatory insights from our consultants &mdash; everything you need to keep your facility ahead of Saudi environmental requirements.",
                       "Blog") + f"""
<section class="py-20" style="background:var(--bp-page);">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">

    <a href="blog-{feat['slug']}.html" class="block bg-white rounded-3xl overflow-hidden shadow-lg hover:shadow-2xl transition-all mb-14 scroll-reveal group" style="text-decoration:none;">
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

    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 scroll-reveal">{cards}
    </div>
  </div>
</section>

<section class="py-20 text-white" style="background:var(--bp-grad);">
  <div class="max-w-3xl mx-auto px-4 text-center">
    <h2 class="font-display text-3xl md:text-4xl font-bold mb-4">Ask our consultants directly.</h2>
    <p class="text-white/80 mb-8 text-lg">Reading up is a great start &mdash; but every facility is different. Get advice specific to yours.</p>
    <div class="flex flex-wrap justify-center gap-3">
      <a data-wa="Hello BluePrint, I would like to ask about your environmental services." class="px-7 py-3.5 bg-white text-bp-ink rounded-full font-bold hover:bg-bp-sage transition-all inline-flex items-center gap-2"><i class="fab fa-whatsapp"></i> Chat on WhatsApp</a>
      <a data-tel class="px-7 py-3.5 border-2 border-white/60 text-white rounded-full font-bold hover:bg-white hover:text-bp-ink transition-all inline-flex items-center gap-2"><i class="fas fa-phone" style="font-size:.85rem;"></i> <span data-text="phone"></span></a>
    </div>
  </div>
</section>
"""


ARTICLE_BODIES = {
"mwan-waste-permit-guide": """
<p class="lead">If your facility generates, transports, treats, or stores waste in Saudi Arabia, the National Waste Management Center (MWAN) almost certainly requires you to hold a valid permit. Yet most first-time applicants underestimate the preparation involved &mdash; and pay for it in weeks of avoidable delays.</p>

<h2>Who needs an MWAN permit?</h2>
<p>MWAN&rsquo;s licensing framework covers the full waste lifecycle. You will need a permit if your activity involves:</p>
<ul>
  <li>Generating industrial, commercial, or hazardous waste beyond household quantities</li>
  <li>Transporting waste of any classification</li>
  <li>Operating treatment, recycling, or sorting facilities</li>
  <li>Storing waste on-site beyond short-term operational limits</li>
  <li>Handling medical or veterinary waste streams</li>
</ul>
<p>Even facilities that outsource waste handling to licensed contractors often still carry <strong>generator obligations</strong> &mdash; including waste characterisation, manifesting, and record-keeping.</p>

<h2>The documents that decide your application</h2>
<p>In our experience, the difference between a smooth approval and a rejection loop comes down to preparation of a few key documents:</p>
<ol>
  <li>A waste characterisation study that matches your actual waste streams</li>
  <li>An up-to-date environmental register for the facility</li>
  <li>Storage and handling procedures aligned with MWAN technical guidelines</li>
  <li>Contracts with licensed transporters and treatment facilities</li>
  <li>An emergency response plan proportionate to your waste classes</li>
</ol>
<blockquote>The single most common rejection reason we see is a mismatch between the declared waste classification and what the facility actually produces. Get the characterisation right first &mdash; everything else builds on it.</blockquote>

<h2>How long does it take?</h2>
<p>With complete documentation, straightforward applications typically clear review in a few weeks. Complex facilities &mdash; multiple waste classes, hazardous streams, or on-site treatment &mdash; should budget longer, plus time for any site inspection MWAN schedules.</p>

<h2>Renewals are not a formality</h2>
<p>Permits are time-limited, and renewal reviews increasingly examine your <strong>compliance history</strong>: late periodic reports, manifest gaps, or unresolved inspection findings will surface at renewal. Treat your reporting calendar as part of the permit itself.</p>

<h2>How BluePrint helps</h2>
<p>We prepare and file MWAN applications end-to-end: characterisation studies, register updates, procedure documentation, and direct coordination with the regulator until approval. If a permit is nearing renewal, we audit your compliance record first &mdash; so the renewal file goes in clean.</p>
""",
}


def article(a, page_header):
    body = ARTICLE_BODIES.get(a['slug'])
    if body is None:
        body = f"""
<p class="lead">{a['summary']}</p>
<div class="rounded-2xl p-6 my-8" style="background:var(--bp-blue-tint);border:1px solid var(--bp-border);">
  <p style="margin:0;"><strong>This article is being prepared.</strong> Our consultants are finalising it. In the meantime, if this topic affects your facility, get in touch &mdash; the initial consultation is free.</p>
</div>
"""
    others = [x for x in ARTICLES if x['slug'] != a['slug']][:3]
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
