# BluePrint, Compliance Hub.
#
# Regulation entries carried over from the AECON portal build. Each is a plain
# summary, not the legal text. The reference, year, authority and status fields
# are reproduced as supplied and have NOT been verified against the official
# instruments, which is why the page states that the official text governs.
#
# To add an entry, append to REGS. Fields:
#   (ref, authority, category, year, severity, status, title_en, title_ar, summary)
# severity: high | medium | low
# category must match one of CATEGORIES below.

CATEGORIES = [
    ("all", "fa-layer-group", "All regulations"),
    ("air", "fa-wind", "Air quality"),
    ("water", "fa-droplet", "Water"),
    ("waste", "fa-trash-can", "Waste management"),
    ("noise", "fa-volume-high", "Noise"),
    ("eia", "fa-clipboard-check", "EIA / ESIA"),
    ("marine", "fa-water", "Marine &amp; coastal"),
    ("climate", "fa-earth-americas", "Climate &amp; Vision 2030"),
]

REGS = [
    ("GAMEP Article 12", "GAMEP", "air", "2021", "high", "Ongoing",
     "Ambient Air Quality Standards for Industrial Zones",
     "معايير جودة الهواء المحيط للمناطق الصناعية",
     "Industrial facilities must not exceed the established ambient air quality limits for PM2.5, "
     "PM10, NO&#8322;, SO&#8322;, CO and O&#8323;. Continuous monitoring is required at major emission points."),

    ("GAMEP Article 18", "GAMEP", "air", "2022", "high", "Compliance deadline set",
     "Stack Emission Limits for Power Generation Facilities",
     "حدود انبعاثات المداخن لمنشآت توليد الكهرباء",
     "Power plants and cogeneration facilities must install certified stack emission monitoring "
     "systems and comply with the NO&#8339;, SO&#8322; and particulate limits defined by GAMEP."),

    ("Royal Decree M/165", "GAMEP", "air", "2020", "medium", "Ongoing",
     "Vehicle Emission Standards and Inspection Requirements",
     "معايير انبعاثات المركبات ومتطلبات الفحص",
     "Vehicles operating in Saudi Arabia must comply with Euro 5 emission standards. Commercial "
     "fleet operators are required to maintain emission inspection records."),

    ("GAMEP Article 34", "GAMEP", "water", "2021", "high", "Ongoing",
     "Industrial Wastewater Discharge Standards",
     "معايير تصريف مياه الصرف الصناعي",
     "Facilities discharging wastewater to municipal networks or water bodies must comply with the "
     "maximum permissible limits for BOD, COD, TSS, heavy metals and pH."),

    ("GAMEP Article 41", "MEWA", "water", "2022", "medium", "Before commissioning",
     "Treated Sewage Effluent Reuse Standards",
     "معايير إعادة استخدام مياه الصرف الصحي المعالجة",
     "Reuse of treated sewage effluent is tied to the intended application, with quality "
     "requirements and monitoring set before a new scheme is commissioned."),

    ("GAMEP Article 112", "GAMEP", "marine", "2021", "high", "Permit required before works",
     "Coastal Development Setback and Buffer Zone Requirements",
     "متطلبات حظر البناء الساحلي ومناطق الحماية",
     "No permanent structures may be built within 200 m of the mean high-water mark along Red Sea "
     "and Arabian Gulf coastlines without a coastal zone permit."),

    ("MARPOL / Royal Decree", "GAMEP", "marine", "2020", "high", "Ongoing",
     "Ship and Port Discharge Regulations",
     "لوائح التصريف من السفن والموانئ",
     "Vessels in Saudi territorial waters must comply with MARPOL. Ports must provide waste "
     "reception facilities, and bilge and ballast water discharge is strictly regulated."),

    ("GAMEP Article 118", "GAMEP", "marine", "2023", "high", "Survey required pre-works",
     "Coral Reef and Seagrass Protection in Development Zones",
     "حماية الشعاب المرجانية والأعشاب البحرية",
     "Development or dredging near coral reef or seagrass habitat requires a marine biological "
     "survey, a compensation plan and ongoing ecological monitoring."),

    ("Saudi Green Initiative", "GAMEP", "climate", "2023", "high", "Annual reporting",
     "Carbon Emission Reporting for Large Industrial Emitters",
     "متطلبات الإبلاغ عن انبعاثات الكربون",
     "Large industrial emitters are required to report carbon emissions annually under the Saudi "
     "Green Initiative framework."),
]

SEV_LABEL = {"high": "High", "medium": "Medium", "low": "Low"}


def _counts():
    out = {}
    for _r, _a, cat, _y, _s, _st, _t, _ta, _d in REGS:
        out[cat] = out.get(cat, 0) + 1
    out["all"] = len(REGS)
    return out


def _chips():
    c = _counts()
    out = []
    for key, icon, name in CATEGORIES:
        n = c.get(key, 0)
        if n == 0 and key != "all":
            continue
        active = " active" if key == "all" else ""
        out.append(
            '<button class="cmp-chip' + active + '" data-cat="' + key + '" type="button">'
            '<i class="fas ' + icon + '"></i><span>' + name + '</span>'
            '<em>' + str(n) + '</em></button>')
    return "\n".join(out)


def _cards():
    out = []
    for ref, auth, cat, year, sev, status, t_en, t_ar, desc in REGS:
        out.append(
            '<article class="cmp-card" data-cat="' + cat + '" data-sev="' + sev + '" '
            'data-text="' + (ref + " " + t_en + " " + t_ar + " " + desc).lower().replace('"', "") + '">'
            '<div class="cmp-meta">'
            '<span class="cmp-ref">' + ref + '</span>'
            '<span class="cmp-tag">' + auth + '</span>'
            '<span class="cmp-tag">' + year + '</span>'
            '<span class="cmp-sev cmp-sev-' + sev + '">' + SEV_LABEL[sev] + '</span>'
            '<span class="cmp-status">' + status + '</span>'
            '</div>'
            '<h3>' + t_en + '</h3>'
            '<p class="cmp-ar" dir="rtl" lang="ar">' + t_ar + '</p>'
            '<p class="cmp-desc">' + desc + '</p>'
            '</article>')
    return "\n".join(out)


def _stats():
    c = _counts()
    sev = {}
    for _r, _a, _c, _y, s, _st, _t, _ta, _d in REGS:
        sev[s] = sev.get(s, 0) + 1
    cats = len([k for k in c if k != "all"])
    auths = len(set(r[1] for r in REGS))
    return [
        (str(c["all"]), "Regulations listed"),
        (str(cats), "Categories"),
        (str(auths), "Issuing authorities"),
        (str(sev.get("high", 0)), "High severity"),
    ]


def _statblock():
    return "\n".join(
        '<div><strong>' + v + '</strong><span>' + l + '</span></div>'
        for v, l in _stats())


_TPL = """
<section class="cmp-hero">
  <div class="cmp-wrap">
    <nav class="cmp-crumb" aria-label="Breadcrumb">
      <a href="index.html">Home</a><span>/</span><span>Compliance Hub</span>
    </nav>
    <p class="cmp-eyebrow">Saudi Arabia &middot; GAMEP &middot; MEWA &middot; NCEC &middot; MWAN</p>
    <h1>Compliance hub</h1>
    <p class="cmp-lede">The environmental obligations that apply to regulated facilities in the
       Kingdom, in one place. Search by keyword, reference or Arabic title, or filter by category.</p>
    <div class="cmp-stats">{stats}</div>
  </div>
</section>

<div class="cmp-body">
  <div class="cmp-wrap">

    <div class="cmp-tools">
      <div class="cmp-search">
        <i class="fas fa-magnifying-glass"></i>
        <input type="search" id="cmpSearch" placeholder="Search by keyword, reference or Arabic text"
               aria-label="Search regulations" autocomplete="off" />
      </div>
      <div class="cmp-sevfilter">
        <button class="cmp-sev-btn active" data-sev="all" type="button">All severities</button>
        <button class="cmp-sev-btn" data-sev="high" type="button">High</button>
        <button class="cmp-sev-btn" data-sev="medium" type="button">Medium</button>
      </div>
    </div>

    <div class="cmp-chips">{chips}</div>

    <p class="cmp-count" id="cmpCount"></p>

    <div class="cmp-list" id="cmpList">{cards}</div>

    <p class="cmp-empty" id="cmpEmpty" hidden>No regulation matches that search.</p>

    <aside class="cmp-disclaimer">
      <h3>How to use this list</h3>
      <p>Each entry is a plain summary prepared for orientation. The official instrument governs in
         every case, and the obligations that apply to a particular facility depend on its activity,
         capacity and location. Where a specific reference matters to a submission, confirm it
         against the published text before relying on it.</p>
      <a href="contact.html" class="cmp-cta">Ask which of these apply to your facility
         <i class="fas fa-arrow-right" style="font-size:.7rem;"></i></a>
    </aside>

  </div>
</div>

<script>
(function () {
  var search = document.getElementById('cmpSearch');
  var list   = document.getElementById('cmpList');
  var count  = document.getElementById('cmpCount');
  var empty  = document.getElementById('cmpEmpty');
  if (!list) return;

  var cards = Array.prototype.slice.call(list.querySelectorAll('.cmp-card'));
  var cat = 'all', sev = 'all';

  function apply() {
    var q = (search && search.value ? search.value : '').toLowerCase().trim();
    var shown = 0;
    cards.forEach(function (c) {
      var okCat = (cat === 'all') || (c.getAttribute('data-cat') === cat);
      var okSev = (sev === 'all') || (c.getAttribute('data-sev') === sev);
      var okTxt = !q || c.getAttribute('data-text').indexOf(q) !== -1;
      var show = okCat && okSev && okTxt;
      c.hidden = !show;
      if (show) shown++;
    });
    count.textContent = shown + (shown === 1 ? ' regulation' : ' regulations');
    empty.hidden = shown !== 0;
  }

  if (search) search.addEventListener('input', apply);

  document.querySelectorAll('.cmp-chip').forEach(function (b) {
    b.addEventListener('click', function () {
      document.querySelectorAll('.cmp-chip').forEach(function (x) { x.classList.remove('active'); });
      b.classList.add('active');
      cat = b.getAttribute('data-cat');
      apply();
    });
  });

  document.querySelectorAll('.cmp-sev-btn').forEach(function (b) {
    b.addEventListener('click', function () {
      document.querySelectorAll('.cmp-sev-btn').forEach(function (x) { x.classList.remove('active'); });
      b.classList.add('active');
      sev = b.getAttribute('data-sev');
      apply();
    });
  });

  apply();
})();
</script>
"""


def compliance():
    return (_TPL
            .replace("{stats}", _statblock())
            .replace("{chips}", _chips())
            .replace("{cards}", _cards()))
