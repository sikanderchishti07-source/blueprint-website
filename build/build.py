import os, partials as P, pages as G, pages_extra as X, arabic as AR
OUT = os.path.join(os.path.dirname(__file__), '..', 'site')
PAGES = {
  'index.html':      ('Environmental Consultancy in Saudi Arabia | BluePrint', 'Accredited Saudi environmental consultancy delivering environmental studies, MWAN permitting, impact assessments, and compliance solutions aligned with KSA regulations.', G.home(), ('js/cards.js',)),
  'services.html':   ('Environmental Services in Saudi Arabia | BluePrint', 'Environmental services across KSA: impact assessments, MWAN waste permits, environmental registers, management plans, rehabilitation, and reporting.', G.services(), ('js/services.js',)),
  'technology.html': ('Laboratory & Accreditations | BluePrint', 'Environmental sampling, testing and monitoring services, and the licences BluePrint holds: NCEC, MWAN, Royal Commission for Jubail & Yanbu, IAS and ISO.', G.technology(), ()),
  'blog.html':       ('Environmental Compliance Blog | BluePrint KSA', 'Guides and insights on Saudi environmental regulation: MWAN permits, impact assessments, environmental registers, waste management, and compliance best practice.', X.blog(G.page_header), ()),
  'privacy.html':    ('Privacy Policy | BluePrint Environmental Services', 'How BluePrint Environmental Services collects, uses, and protects your personal information.', X.legal('privacy', G.page_header), ()),
  'terms.html':      ('Terms & Conditions | BluePrint Environmental Services', 'The terms and conditions governing use of the BluePrint Environmental Services website and services.', X.legal('terms', G.page_header), ()),
  'contact.html':    ('Contact BluePrint — Free Compliance Consultation', 'Talk to BluePrint accredited environmental consultants in Riyadh. Free initial consultation to map the studies and permits your facility needs in Saudi Arabia.', G.contact(), ()),
}
for a in X.ARTICLES:
    PAGES['blog-%s.html' % a['slug']] = (a['title'] + ' | BluePrint', a['summary'], X.article(a, G.page_header), ())

with open(os.path.join(OUT, 'index_arabic.html'), 'w', encoding='utf-8') as f:
    f.write(AR.arabic())
print('index_arabic.html')

for fname, (title, desc, body, extra) in PAGES.items():
    html = P.head(title, desc) + P.nav() + '\n<main>' + body + '</main>\n' + P.footer() + P.modals() + P.widgets() + P.scripts(extra)
    with open(os.path.join(OUT, fname), 'w', encoding='utf-8') as f: f.write(html)
    print(fname, len(html))
