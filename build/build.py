import os, partials as P, pages as G
OUT = os.path.join(os.path.dirname(__file__), '..', 'site')
PAGES = {
  'index.html':      ('BluePrint Environmental Services | Air Quality Monitoring & Environmental Consultancy, KSA', 'BluePrint Environmental Services - environmental consultancy in Saudi Arabia. Air quality monitoring, stack emission testing, EIA, and compliance services across KSA and the Middle East.', G.home(), ()),
  'services.html':   ('Services | BluePrint Environmental Services', 'Ambient air quality, stack emission testing, indoor air quality, EIA/ESIA, water & soil analysis and environmental management plans across Saudi Arabia.', G.services(), ('js/services.js',)),
  'technology.html': ('Technology & Equipment | BluePrint Environmental Services', 'AQMS instrumentation, accredited laboratory equipment and the compliance standards BluePrint works to: NCEC, WHO, US EPA, IFC and ISO.', G.technology(), ()),
  'resources.html':  ('Resources & Tools | BluePrint Environmental Services', 'Free compliance checker, carbon footprint calculator, live Riyadh AQI and a curated environmental news bulletin for Saudi Arabia.', G.resources(), ('js/news.js',)),
  'contact.html':    ('Contact | BluePrint Environmental Services', 'Contact BluePrint Environmental Services in Riyadh for environmental monitoring, compliance consulting and site inspections.', G.contact(), ()),
}
for fname, (title, desc, body, extra) in PAGES.items():
    html = P.head(title, desc) + P.nav() + '\n<main>' + body + '</main>\n' + P.footer() + P.modals() + P.widgets() + P.scripts(extra)
    with open(os.path.join(OUT, fname), 'w', encoding='utf-8') as f: f.write(html)
    print(fname, len(html))
