/* ============================================================
   BluePrint — services.js
   Interactive split-panel services showcase (desktop tabs /
   mobile accordion) with auto-rotate.
   ============================================================ */
(function () {
  'use strict';
  if (!document.getElementById('isvcTabs')) return;

  var SERVICES = [
    {
      title: 'Ambient Air Quality Monitoring', subtitle: '24/7 real-time environmental surveillance', icon: 'fas fa-wind',
      desc: 'BluePrint deploys state-of-the-art Beta Attenuation Monitors (BAM) and reference-grade gas analysers to continuously measure criteria pollutants across industrial, urban, and sensitive receptor zones. All data streams are telemetrically transmitted to our monitoring centre for immediate regulatory reporting and public health protection.',
      features: ['PM2.5, PM10 & TSP via BAM/gravimetric samplers', 'NO₂, SO₂, CO & ozone — continuous gas analysers', 'Real-time telemetric data acquisition & dashboards', '24/7 alarm management & exceedance notifications', 'NCEC SAAQS & WHO AQG 2021 compliance reporting', 'Meteorological station integration (wind, temp, RH)'],
      stats: [{ val: '300+', lbl: 'Monitoring Sites' }, { val: '24/7', lbl: 'Live Data Feed' }, { val: 'SAAQS', lbl: 'Compliant' }]
    },
    {
      title: 'Stack Emission Testing', subtitle: 'EPA-certified isokinetic source testing', icon: 'fas fa-smog',
      desc: 'Our qualified stack-testing teams conduct isokinetic sampling on industrial flue gas stacks using US EPA Methods 1–17, NCEC emission protocols, and EN ISO procedures. We serve cement, power generation, oil & gas, chemicals and waste-to-energy facilities, delivering LDAR programmes, CEMS installation, and complete compliance documentation.',
      features: ['US EPA Methods 1, 4, 5, 9, 17 & NCEC equivalent', 'Particulate matter, opacity & opacity audit (Method 9)', 'HCl, HF, SO₃, NOx, CO, CO₂, O₂ flue-gas analysis', 'CEMS calibration, validation & RATA testing', 'Mercury speciation & heavy metals (Methods 29/30B)', 'Full permit-ready reports with QA/QC documentation'],
      stats: [{ val: '500+', lbl: 'Stack Tests Done' }, { val: 'EPA', lbl: 'Certified Methods' }, { val: 'CEMS', lbl: 'Validation' }]
    },
    {
      title: 'Indoor Air Quality Assessment', subtitle: 'TVOC, microbial & comfort parameter profiling', icon: 'fas fa-building',
      desc: 'BluePrint conducts comprehensive IAQ surveys for offices, hospitals, schools, hotels, and residential developments. We quantify TVOC, formaldehyde, CO₂, CO, temperature, humidity, particulates and biological contaminants, benchmarking against ASHRAE 62.1, WHO and NCEC IAQ guidelines to protect occupant health and productivity.',
      features: ['TVOC & formaldehyde (ISO 16000 methods)', 'CO₂, CO, temperature, relative humidity profiling', 'PM2.5, PM10 & bioaerosol (mould/bacteria) sampling', 'Radon and volatile organic compound speciation', 'Ventilation system assessment & HVAC auditing', 'Health-risk assessment & remediation recommendations'],
      stats: [{ val: '150+', lbl: 'IAQ Surveys' }, { val: 'ASHRAE', lbl: '62.1 Compliant' }, { val: 'WHO', lbl: 'Benchmarked' }]
    },
    {
      title: 'Environmental Impact Assessment', subtitle: 'EIA/ESIA — NCEC, IFC & Equator Principles', icon: 'fas fa-mountain',
      desc: 'BluePrint prepares statutory Environmental Impact Assessments (EIA) and Environmental & Social Impact Assessments (ESIA) for industrial plants, infrastructure corridors, coastal developments, and mega-projects aligned with Saudi Vision 2030. Our multi-disciplinary team covers air, noise, water, ecology, socio-economics and cumulative impacts through to regulatory submission.',
      features: ['Scoping, baseline characterisation & data collection', 'Air dispersion modelling (AERMOD, CALPUFF)', 'Noise impact assessment & prediction modelling', 'Marine & freshwater ecology surveys', 'Social impact assessment & stakeholder engagement', 'Environmental Management & Monitoring Plans (EMMP)'],
      stats: [{ val: '80+', lbl: 'EIA Projects' }, { val: 'NCEC', lbl: 'Approved' }, { val: 'IFC', lbl: 'Aligned' }]
    },
    {
      title: 'Water & Soil Analysis', subtitle: 'Accredited laboratory — ISO/IEC 17025', icon: 'fas fa-tint',
      desc: 'Our ISO/IEC 17025-accredited laboratory analyses groundwater, surface water, marine water, wastewater, drinking water, and soil/sediment samples using internationally validated methods. We determine physical, chemical, and microbiological parameters from sub-ppb trace metals to full organic panels, supporting regulatory compliance, due diligence, and remediation projects.',
      features: ['Heavy metals by ICP-MS (sub-ppb detection limits)', 'VOC, SVOC, PAHs & TPH by GC-MS/FID', 'Physicochemical: pH, EC, TDS, BOD, COD, nutrients', 'Microbiological: E. coli, TCC, Legionella, coliforms', 'Soil contamination & remediation baseline surveys', 'Chain-of-custody documentation & LIMS reporting'],
      stats: [{ val: '17025', lbl: 'ISO Accredited' }, { val: '200+', lbl: 'Parameters Tested' }, { val: 'ppt', lbl: 'Detection Limits' }]
    },
    {
      title: 'Environmental Management Plans', subtitle: 'ISO 14001 · EMP design · Emergency response', icon: 'fas fa-leaf',
      desc: 'BluePrint develops bespoke Environmental Management Plans (EMP), Environmental Monitoring & Management Plans (EMMP), and ISO 14001 Environmental Management Systems (EMS) for clients across construction, operation, and decommissioning phases. We also prepare Emergency Response Plans (ERP), spill contingency plans, and support clients through NCEC and third-party audits.',
      features: ['Site-specific EMP/EMMP development & implementation', 'ISO 14001:2015 gap analysis, design & certification support', 'Emergency Response Plans & spill contingency procedures', 'Environmental compliance auditing & gap reporting', 'Waste management plans & hazardous materials protocols', 'Staff environmental training & awareness programmes'],
      stats: [{ val: '120+', lbl: 'EMP Projects' }, { val: 'ISO', lbl: '14001 Certified' }, { val: 'KSA', lbl: 'NCEC Approved' }]
    }
  ];

  function buildBody(svc) {
    var feat = svc.features.map(function (f) { return '<div class="isvc-feature-item"><div class="isvc-feature-check"><i class="fas fa-check"></i></div><span class="isvc-feature-text">' + f + '</span></div>'; }).join('');
    var stats = svc.stats.map(function (s) { return '<div class="isvc-stat-chip"><div class="sc-val">' + s.val + '</div><div class="sc-lbl">' + s.lbl + '</div></div>'; }).join('');
    return '<div class="isvc-panel-title-row"><div class="isvc-panel-icon-large"><i class="' + svc.icon + '"></i></div><div><div class="isvc-panel-title">' + svc.title + '</div><div class="isvc-panel-subtitle">' + svc.subtitle + '</div></div></div>'
      + '<p class="isvc-panel-desc">' + svc.desc + '</p>'
      + '<div class="isvc-features">' + feat + '</div>'
      + '<div class="isvc-stats-row">' + stats + '</div>'
      + '<div class="isvc-cta-row">'
      + '<a href="contact.html" class="isvc-btn-primary"><i class="fas fa-paper-plane" style="font-size:.76rem;"></i> Get a Quote</a>'
      + '<button type="button" class="isvc-btn-ghost" onclick="openBookingModal()">Request Inspection <i class="fas fa-arrow-right" style="font-size:.7rem;"></i></button>'
      + '</div>';
  }

  SERVICES.forEach(function (svc, i) {
    var pb = document.getElementById('isvc-panel-body-' + i); if (pb) pb.innerHTML = buildBody(svc);
    var ab = document.getElementById('isvc-acc-body-' + i);   if (ab) ab.innerHTML = buildBody(svc);
  });

  var cur = 0, busy = false, timer = null;
  var tabs = document.querySelectorAll('.isvc-tab');
  var bar = document.getElementById('isvcProgressBar');

  window.selectService = function (idx) {
    if (idx === cur || busy) return;
    busy = true;
    tabs.forEach(function (t) { t.classList.remove('active'); });
    if (tabs[idx]) tabs[idx].classList.add('active');
    if (bar) bar.style.width = ((idx + 1) / SERVICES.length * 100) + '%';
    var out = document.getElementById('isvc-panel-' + cur);
    var inn = document.getElementById('isvc-panel-' + idx);
    if (out) { out.classList.remove('active'); out.classList.add('exit'); }
    if (inn) { void inn.offsetWidth; inn.classList.remove('exit'); inn.classList.add('active'); }
    var prev = cur; cur = idx;
    setTimeout(function () { var old = document.getElementById('isvc-panel-' + prev); if (old) old.classList.remove('exit'); busy = false; }, 450);
    startAuto();
  };

  function startAuto() {
    clearInterval(timer);
    timer = setInterval(function () { selectService((cur + 1) % SERVICES.length); }, 6000);
  }
  ['isvcPanelWrap', 'isvcTabs'].forEach(function (id) {
    var el = document.getElementById(id); if (!el) return;
    el.addEventListener('mouseenter', function () { clearInterval(timer); });
    el.addEventListener('mouseleave', startAuto);
  });
  startAuto();

  // Deep link: services.html#svc-3 opens tab 3
  var m = location.hash.match(/^#svc-(\d)$/);
  if (m) setTimeout(function () { selectService(+m[1]); }, 300);

  var obs = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('visible'); obs.unobserve(e.target); } });
  }, { threshold: 0.08 });
  document.querySelectorAll('.isvc-reveal').forEach(function (el) { obs.observe(el); });
})();
