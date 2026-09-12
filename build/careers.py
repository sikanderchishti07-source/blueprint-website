# Careers pages, built from content/careers/*.md


def _hero_facts(roles):
    locs = []
    for r in roles:
        loc = (r.get('location') or '').strip()
        if loc and loc not in locs:
            locs.append(loc)
    rows = [("Open roles", str(len(roles)) if roles else "None right now")]
    if locs:
        rows.append(("Based in", locs[0] if len(locs) == 1 else "Multiple locations"))
    rows.append(("Work", "Field and office"))
    return "".join(
        f"""
        <div class="flex items-center justify-between gap-4 py-3.5 border-b border-white/10 last:border-0">
          <span class="text-sm text-gray-400">{k}</span>
          <span class="text-sm font-medium text-white">{v}</span>
        </div>""" for k, v in rows)


def _hero(eyebrow, title, lede, crumb, facts=None):
    side = f"""
      <div class="lg:border-l lg:border-white/15 lg:pl-10">{facts}
      </div>""" if facts else ""
    return f"""
<section class="pt-32 pb-20 text-white relative" style="background:var(--bp-blue-ink);">
  <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="crumb crumb-dark mb-6">{crumb}</div>
    <div class="grid lg:grid-cols-3 gap-10 lg:gap-14 items-center">
      <div class="lg:col-span-2">
        <div class="text-xs uppercase font-semibold mb-4 text-bp-sage" style="letter-spacing:.22em;">{eyebrow}</div>
        <h1 class="text-3xl lg:text-5xl font-bold tracking-tight leading-tight">{title}</h1>
        <p class="text-gray-300 text-base leading-relaxed mt-5 max-w-xl">{lede}</p>
      </div>
{side}
    </div>
  </div>
</section>"""


def careers_index(page_header, roles):
    if roles:
        cards = "".join(f"""
      <a href="career-{r['slug']}.html" class="crole scroll-reveal">
        <div class="crole-main">
          <div class="crole-dept">{r.get('department') or 'BluePrint'}</div>
          <h3>{r['title']}</h3>
          <p>{r.get('summary','')}</p>
          <div class="crole-meta">
            <span><i class="fas fa-location-dot"></i> {r.get('location','')}</span>
            <span><i class="fas fa-clock"></i> {r.get('type','')}</span>
            {f"<span><i class='fas fa-calendar'></i> Closes {r['closing']}</span>" if r.get('closing') else ""}
          </div>
        </div>
        <span class="crole-go"><i class="fas fa-arrow-right"></i></span>
      </a>""" for r in roles)
        body = f'<div class="croles">{cards}</div>'
    else:
        body = """
      <div class="cempty scroll-reveal">
        <i class="fas fa-inbox"></i>
        <h3>No open vacancies at the moment</h3>
        <p>We are not advertising a role right now, but we are always glad to hear
           from environmental scientists, field technicians and laboratory staff.
           Send your CV and we will keep it on file.</p>
        <a data-mail class="btn-primary">Send your CV</a>
      </div>"""

    crumb = ('<a href="index.html">Home</a>'
             '<i class="fas fa-chevron-right" style="font-size:.55rem;"></i>'
             '<span>Careers</span>')

    hero = _hero(
        "Careers",
        "Work in Saudi environmental compliance",
        "The work is varied, field monitoring one week, permit files the next.",
        crumb,
        _hero_facts(roles),
    )

    return f"""
{hero}

<section class="py-20 bg-white">
  <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
    {body}
  </div>
</section>

<section class="py-20" style="background:var(--bp-page);">
  <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="text-center mb-12 scroll-reveal">
      <div class="showcase-eyebrow">What it is like</div>
      <h2 class="text-3xl font-bold text-bp-ink tracking-tight">Working here</h2>
    </div>
    <div class="cwhy scroll-reveal">
      <div><b>Varied work</b><span>Field campaigns, laboratory analysis, permit files and reporting, most people touch several of these rather than one.</span></div>
      <div><b>Accredited practice</b><span>Work is carried out to referenced methods under accreditation,
        which is a good discipline to learn early in a career.</span></div>
      <div><b>Across the Kingdom</b><span>Sites range from coastal and marine to desert industrial,
        so field work is genuinely different from month to month.</span></div>
      <div><b>Regulatory depth</b><span>You will learn the Saudi environmental framework properly,
        which is a scarce and portable skill.</span></div>
    </div>
  </div>
</section>
"""


def career_page(page_header, r, others):
    rel = "".join(f"""
      <a href="career-{o['slug']}.html" class="crel">
        <span class="crel-t">{o['title']}</span>
        <i class="fas fa-arrow-right"></i>
      </a>""" for o in others)

    meta = "".join(
        f"""
        <div class="flex items-center justify-between gap-4 py-3.5 border-b border-white/10 last:border-0">
          <span class="text-sm text-gray-400">{k}</span>
          <span class="text-sm font-medium text-white">{v}</span>
        </div>""" for k, v in [
            ("Location", r.get('location', '')),
            ("Type", r.get('type', '')),
            ("Closes", r.get('closing', '')),
        ] if v)

    crumb = ('<a href="index.html">Home</a>'
             '<i class="fas fa-chevron-right" style="font-size:.55rem;"></i>'
             '<a href="careers.html">Careers</a>')

    hero = _hero(
        r.get('department') or 'Vacancy',
        r['title'],
        r.get('summary', ''),
        crumb,
        meta,
    )

    return f"""
{hero}

<section class="py-20 bg-white">
  <div class="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="article-body scroll-reveal">{r['html']}</div>

    <div class="capply scroll-reveal">
      <h3>How to apply</h3>
      <p>Send your CV and a short note about why this role interests you. We read
         every application and reply either way.</p>
      <div class="flex flex-wrap gap-3 mt-5">
        <a data-mail class="btn-primary">Apply by email</a>
        <a data-wa="Hello BluePrint, I would like to apply for the {r['title']} role." class="btn-ghost"><i class="fab fa-whatsapp"></i> Ask a question</a>
      </div>
    </div>

    {f'<div class="mt-14"><h3 class="font-display text-lg font-bold text-bp-ink mb-4">Other open roles</h3><div class="crels">{rel}</div></div>' if others else ''}
  </div>
</section>
"""
