import about as AB
import equipment as EQ
import compliance as CP
import finder as FD
import os, partials as P, pages as G, pages_extra as X, arabic as AR, content as C, careers as CR, service_pages as SP, svc_cards as SVQ, svc_permitting as SPP, svc_monitoring as SPM, svc_specialist as SPS, svc_caps as SPC
OUT = os.path.join(os.path.dirname(__file__), '..', 'site')
PAGES = {
  'index.html':      ('Environmental Consultancy in Saudi Arabia | BluePrint', 'Accredited Saudi environmental consultancy delivering environmental studies, MWAN permitting, impact assessments, and compliance solutions aligned with KSA regulations.', G.home(), ('js/cards.js', 'js/cover.js', 'js/carousel.js', 'js/livemap.js')),
  'about.html':      ('About BluePrint | Environmental Consultancy in Saudi Arabia', 'BluePrint Environmental Services, a registered Saudi environmental consultancy in Riyadh delivering permitting, monitoring, modelling and laboratory services across the Kingdom and the GCC.', AB.about(), ()),
  'equipment.html':  ('Equipment Catalogue | BluePrint Environmental Services', 'The instrument types BluePrint uses across air quality, noise, water, soil, marine, laboratory analysis and environmental modelling, with what each measures.', EQ.equipment(), ('js/eqp-lightbox.js',)),
  'compliance.html': ('Compliance Hub | Saudi Environmental Regulations | BluePrint', 'Searchable summaries of the Saudi environmental obligations that apply to regulated facilities, by category, authority and severity.', CP.compliance(), ()),
  'compliance-finder.html': ('Compliance Finder | Which Permits Apply? | BluePrint', 'Answer three questions to see the environmental permits, studies and monitoring a facility like yours is normally asked for in Saudi Arabia.', FD.page(G.page_header), ('js/finder.js',)),
  'services.html':   ('Environmental Services in Saudi Arabia | BluePrint', 'Environmental services across KSA: impact assessments, MWAN waste permits, environmental registers, management plans, rehabilitation, and reporting.', G.services(), ('js/services.js',)),
  'technology.html': ('Laboratory & Accreditations | BluePrint', 'Environmental sampling, testing and monitoring services, and the licences BluePrint holds: NCEC, MWAN, Royal Commission for Jubail & Yanbu, IAS and ISO.', G.technology(), ()),
  'blog.html':       ('Environmental Compliance Blog | BluePrint KSA', 'Guides and insights on Saudi environmental regulation: MWAN permits, impact assessments, environmental registers, waste management, and compliance best practice.', X.blog(G.page_header), ()),
  'privacy.html':    ('Privacy Policy | BluePrint Environmental Services', 'How BluePrint Environmental Services collects, uses, and protects your personal information.', X.legal('privacy', G.page_header), ()),
  'terms.html':      ('Terms & Conditions | BluePrint Environmental Services', 'The terms and conditions governing use of the BluePrint Environmental Services website and services.', X.legal('terms', G.page_header), ()),
  'contact.html':    ('Contact BluePrint, Free Compliance Consultation', 'Talk to BluePrint accredited environmental consultants in Riyadh. Free initial consultation to map the studies and permits your facility needs in Saudi Arabia.', G.contact(), ()),
}
_GROUP_LABEL = {'permitting': 'Compliance &amp; Permitting',
                'monitoring': 'Monitoring, Testing &amp; Measurement',
                'specialist': 'Specialist Disciplines'}

ALL_SERVICES = {}
ALL_SERVICES.update(SPP.PERMITTING)
ALL_SERVICES.update(SP.SERVICES)
ALL_SERVICES.update(SPM.MONITORING)
ALL_SERVICES.update(SPS.SPECIALIST)

_CAP_IMGS = ['assets/img/cap-scoped.webp', 'assets/img/cap-accredited.webp',
             'assets/img/cap-schedule.webp', 'assets/img/cap-interpreted.webp']
for _slug, _s in ALL_SERVICES.items():
    # service-specific capability items replace the shared block
    if _slug in SPC.CAPS:
        _s['caps'] = [(t, d, _CAP_IMGS[i], b, bs)
                      for i, (t, d, b, bs) in enumerate(SPC.CAPS[_slug])]
    _s.setdefault('group_label', _GROUP_LABEL.get(_s.get('group'), 'Services'))
    _s.setdefault('detail_img', _s['hero_img'])
    _s.setdefault('band_img', 'assets/img/svc-air-lab.jpg')
    _s.setdefault('faq_title', 'Common questions')
    # related = the other services in the same group, first three
    _rel = [(o['slug'], o['title'], o['num']) for k, o in ALL_SERVICES.items()
            if o.get('group') == _s.get('group') and k != _slug][:3]
    PAGES['service-%s.html' % _slug] = (
        _s['title'].replace('&amp;', '&') + ' | BluePrint Environmental Services',
        _s['meta'], SP.service_page(_s, G.page_header, _rel), ())


# carousel service pages
for _k, _c in SVQ.CARDS.items():
    _rel = [o for kk, o in SVQ.CARDS.items() if kk != _k][:4]
    PAGES['service-%s.html' % _c['slug']] = (
        _c['title'].replace('&amp;', '&') + ' | BluePrint Environmental Services',
        _c['meta'], SVQ.card_page(_c, _rel), ())

_roles = C.load_careers()
PAGES['careers.html'] = ('Careers | BluePrint Environmental Services',
  'Environmental consultancy careers in Saudi Arabia, field monitoring, laboratory analysis, permitting and reporting roles at BluePrint.',
  CR.careers_index(G.page_header, _roles), ())
for _r in _roles:
    PAGES['career-%s.html' % _r['slug']] = (
        _r['title'] + ' | Careers | BluePrint',
        _r.get('summary','') or ('Vacancy: ' + _r['title'] + ' at BluePrint Environmental Services, Riyadh.'),
        CR.career_page(G.page_header, _r, [o for o in _roles if o['slug'] != _r['slug']][:3]), ())

for a in C.load_blog():
    PAGES['blog-%s.html' % a['slug']] = (a['title'] + ' | BluePrint', a['summary'], X.article(a, G.page_header), ())

import ar_pages as ARP
ARP.setup(PAGES)
P.AR_AVAILABLE = set(ARP.AR_PAGES)

for fname, (title, desc, body, extra) in PAGES.items():
    html = P.head(title, desc, page=fname) + P.nav(page=fname) + '\n<main>' + body + '</main>\n' + P.footer(page=fname) + P.modals() + P.widgets() + P.scripts(extra)
    with open(os.path.join(OUT, fname), 'w', encoding='utf-8') as f: f.write(html)
    print(fname, len(html))


# ---- Arabic pages, written to site/ar/ -------------------------------------
AR_OUT = os.path.join(OUT, 'ar')
os.makedirs(AR_OUT, exist_ok=True)
for fname, (title, desc, body, extra) in ARP.AR_PAGES.items():
    html = (P.head(title, desc, lang='ar', page=fname) + P.nav('ar', fname)
            + '\n<main>' + body + '</main>\n' + P.footer('ar', fname) + P.modals()
            + P.widgets('ar') + P.scripts(extra, 'ar'))
    html = P.ar_paths(html, P.AR_AVAILABLE)
    with open(os.path.join(AR_OUT, fname), 'w', encoding='utf-8') as f: f.write(html)
    print('ar/' + fname, len(html))
