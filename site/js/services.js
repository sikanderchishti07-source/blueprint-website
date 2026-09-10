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
      page: "environmental-permit", title: "Environmental Permit", subtitle: "NCEC \u00b7 required before you build and before you operate", icon: "fas fa-file-signature",
      desc: "Every regulated facility in the Kingdom needs a valid environmental permit before it builds and before it operates. BluePrint prepares the whole file \u2014 classification, supporting studies, and supporting documents \u2014 and carries it through to issuance, coordinating directly with the reviewing authority.",
      features: ["Commercial registration and municipal licence", "Site plan, coordinates, and land-use approval", "Process description and production capacity", "Activity classification against permit categories", "Supporting studies where the category requires them", "Submission handling and reviewer correspondence"],
      stats: [{ val: "NCEC", lbl: "Aligned" }, { val: "Cat 1\u20133", lbl: "All categories" }, { val: "End-to-end", lbl: "To issuance" }]
    },
    {
      page: "environmental-impact-assessment", title: "Environmental Impact Assessment", subtitle: "The study that stands between a project and its licence", icon: "fas fa-clipboard-check",
      desc: "The EIA is the study that stands between a high-impact project and its licence. BluePrint produces assessments that reviewers accept \u2014 because they answer the questions reviewers actually ask, with a stated methodology and a field baseline behind every prediction.",
      features: ["Scoping report and terms of reference", "Field baseline survey and measurement campaign", "Impact prediction with stated methodology", "Mitigation hierarchy and residual impact assessment", "Environmental management and monitoring plan", "Submission support through reviewer queries"],
      stats: [{ val: "EIA", lbl: "&amp; ESIA" }, { val: "Baseline", lbl: "Field surveys" }, { val: "Reviewer", lbl: "Accepted" }]
    },
    {
      page: "waste-management-permit", title: "Waste Management Permit (MWAN)", subtitle: "For anyone who generates, transports, treats or disposes", icon: "fas fa-recycle",
      desc: "Anyone who generates, transports, treats, or disposes of regulated waste in the Kingdom needs a MWAN permit. BluePrint takes facilities from unqualified to permitted \u2014 characterising the waste streams, closing the containment gaps, and preparing the file the National Center for Waste Management expects.",
      features: ["Waste stream inventory and characterisation", "Hazard classification with lab analysis where needed", "Storage, segregation, and containment gap closure", "Contracted-carrier and disposal-route verification", "Manifest and record-keeping system setup", "Permit application preparation and submission"],
      stats: [{ val: "MWAN", lbl: "Registered" }, { val: "Hazardous", lbl: "&amp; industrial" }, { val: "Gap-to-permit", lbl: "Full service" }]
    },
    {
      page: "environmental-management-plan", title: "Environmental Management Plan", subtitle: "The document inspectors ask for first", icon: "fas fa-tasks",
      desc: "The EMP turns permit conditions into daily practice \u2014 and it is the document inspectors ask for first. BluePrint writes plans that a site team can actually follow, tying every obligation to a named control, a monitoring parameter, and a responsible role.",
      features: ["Legal and permit-condition register", "Impact-by-impact mitigation measures", "Monitoring programme with parameters and frequencies", "Roles, responsibilities, and reporting lines", "Incident and emergency response procedures", "Training and awareness requirements"],
      stats: [{ val: "EMP", lbl: "&amp; EMMP" }, { val: "Site-ready", lbl: "Practical" }, { val: "Audit", lbl: "Defensible" }]
    },
    {
      page: "environmental-register", title: "Environmental Register", subtitle: "Proof you have been compliant every day since", icon: "fas fa-folder-open",
      desc: "A permit proves you were compliant on the day it was issued. The environmental register proves you have been compliant every day since. BluePrint establishes the register, populates it from your existing records, and keeps it current so an inspection never becomes a document hunt.",
      features: ["Permits, licences, and their conditions", "Waste inventory, manifests, and disposal receipts", "Emission, effluent, and noise monitoring results", "Chemical and hazardous material inventories", "Incident, complaint, and corrective action log", "Ongoing upkeep and periodic review"],
      stats: [{ val: "Live", lbl: "Maintained" }, { val: "Inspection", lbl: "Ready" }, { val: "All records", lbl: "One place" }]
    },
    {
      page: "periodic-environmental-report", title: "Periodic Environmental Report", subtitle: "The obligation most facilities let slip", icon: "fas fa-calendar-check",
      desc: "Permits are kept, not just won. Periodic reporting is the obligation most facilities let slip \u2014 and the easiest violation for a regulator to spot. BluePrint builds the reporting calendar from your permit conditions, schedules the measurements it calls for, and files on time, every cycle.",
      features: ["Reporting calendar built from permit conditions", "Scheduling and supervision of required measurements", "Data compilation and limit comparison", "Exceedance investigation and corrective actions", "Report drafting in the regulator&rsquo;s format", "Submission and follow-up on queries"],
      stats: [{ val: "On time", lbl: "Every cycle" }, { val: "Permit-driven", lbl: "Calendar" }, { val: "Filed", lbl: "&amp; followed up" }]
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
      + '<a href="service-' + (svc.page || '') + '.html" class="isvc-btn-ghost">Full service detail <i class="fas fa-arrow-right" style="font-size:.7rem;"></i></a>'
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
