/* ============================================================
   BluePrint — cards.js
   Three-card service showcase. Click a card to expand its
   service list, staggered in. Home page only.
   ============================================================ */
(function () {
  'use strict';
  var stage = document.getElementById('svcStage');
  if (!stage) return;

  // Arabic pages supply their own dataset
  var GROUPS = (typeof window !== 'undefined' && window.SVC_DATA_AR)
    ? window.SVC_DATA_AR.map(function (g) {
        return { key: g.key, short: g.short, num: g.num, icon: g.icon, img: g.img,
                 pos: g.pos, blurb: g.blurb, href: g.href, items: g.items };
      })
    : [
    {
      key: 'Compliance &amp; Permitting', short: 'Permitting', num: '01', icon: 'fa-stamp',
      img: 'assets/img/card-1.jpg', pos: '20% 30%',
      blurb: 'Getting your facility licensed &mdash; and keeping it licensed.',
      href: 'service-environmental-permit.html',
      items: [
        ['Environmental Permit', 'NCEC permit file, start to issuance', 'service-environmental-permit.html'],
        ['Environmental Impact Assessment', 'EIA/ESIA for high-impact projects', 'service-environmental-impact-assessment.html'],
        ['Waste Management Permit', 'MWAN permit for regulated waste', 'service-waste-management-permit.html'],
        ['Environmental Management Plan', 'Permit conditions into daily practice', 'service-environmental-management-plan.html'],
        ['Environmental Register', 'Continuous proof of compliance', 'service-environmental-register.html'],
        ['Periodic Environmental Report', 'Keeping the permit you won', 'service-periodic-environmental-report.html']
      ]
    },
    {
      key: 'Monitoring, Testing &amp; Measurement', short: 'Monitoring', num: '02', icon: 'fa-flask',
      img: 'assets/img/card-2.jpg', pos: '75% 60%',
      blurb: 'The numbers behind every compliance claim.',
      href: 'service-air-quality-monitoring.html',
      items: [
        ['Air Quality Monitoring &amp; Testing', 'Measurement against KSA standards', 'service-air-quality-monitoring.html'],
        ['Water &amp; Wastewater Testing', 'Accredited analysis', 'service-water-wastewater-testing.html'],
        ['Noise Monitoring &amp; Assessment', 'Against regulated limits', 'service-noise-monitoring.html'],
        ['Soil &amp; Sediment Testing', 'Characteristics and contaminants', 'service-soil-sediment-testing.html'],
        ['Field Monitoring &amp; Measurement', 'Precise on-site parameters', 'service-field-monitoring.html'],
        ['Environmental Sampling', 'Chain-of-custody protocols', 'service-environmental-sampling.html'],
        ['Monitoring Programmes', 'Scheduled, tracked, reported', 'service-monitoring-programmes.html'],
        ['Laboratory Analysis', 'With technical interpretation', 'service-laboratory-analysis.html'],
        ['Pollution Control Equipment', 'Supply and operation', 'service-pollution-control-equipment.html'],
        ['Reporting &amp; Compliance', 'Periodic regulatory reports', 'service-reporting-compliance.html']
      ]
    },
    {
      key: 'Specialist Disciplines', short: 'Specialist', num: '03', icon: 'fa-layer-group',
      img: 'assets/img/card-3.jpg', pos: '50% 75%',
      blurb: 'Deeper technical work across six disciplines.',
      href: 'services.html',
      items: [
        ['Climate Change &amp; Sustainability', 'ESG, carbon footprint, net zero &mdash; 17 services', 'service-climate-sustainability.html'],
        ['Ecological &amp; Biological Surveys', 'Baseline, habitat, protected species &mdash; 6', 'service-ecological-surveys.html'],
        ['Marine Environment', 'Sampling, mapping, modelling &mdash; 6', 'service-marine-environment.html'],
        ['Remediation &amp; Rehabilitation', 'Investigation to in-situ works &mdash; 5', 'service-remediation-rehabilitation.html'],
        ['Environmental Modelling', 'Dispersion, hydrology, noise &mdash; 5', 'service-environmental-modelling.html'],
        ['Laboratory Services', 'Sampling through interpretation &mdash; 10', 'service-laboratory-services.html']
      ]
    }
  ];

  var T = (typeof window !== 'undefined' && window.SVC_T) || {
    services: 'services', openList: 'Open full list', more: 'more',
    hint: 'Hover a card to preview · click to open the full list'
  };
  var overlay = document.getElementById('svcOverlay');
  var lastFocus = null;

  GROUPS.forEach(function (g, i) {
    var c = document.createElement('button');
    c.type = 'button';
    c.className = 'svc-card';
    c.setAttribute('aria-label', 'View ' + g.key.replace(/&amp;/g, 'and') + ' services');
    c.addEventListener('click', function () { openOverlay(i, c); });
    var teaser = g.items.map(function (it) {
      return '<li><span class="svc-bl-t">' + it[0] + '</span>' +
             '<span class="svc-bl-d">' + it[1] + '</span></li>'; }).join('');
    c.innerHTML =
      '<span class="svc-flip">' +
        '<span class="svc-face svc-front">' +
          '<span class="svc-card-bg" style="background-image:url(\'' + g.img + '\');background-position:' + g.pos + '"></span>' +
          '<span class="svc-card-veil"></span>' +
          '<span class="svc-card-num">' + g.num + '</span>' +
          '<span class="svc-card-icon"><i class="fas ' + g.icon + '"></i></span>' +
          '<span class="svc-card-glass">' +
            '<span class="svc-card-kick">' + (T.kicker || 'OUR SERVICES') + '</span>' +
            '<span class="svc-card-short">' + g.short + '</span>' +
            '<span class="svc-card-rule"></span>' +
            '<span class="svc-card-count">' + g.items.length + ' ' + T.services + '</span>' +
            '<span class="svc-card-title">' + g.key + '</span>' +
            '<span class="svc-card-blurb">' + g.blurb + '</span>' +
            '<span class="svc-card-cta">View ' + g.items.length + ' services <i class="fas fa-arrow-right"></i></span>' +
          '</span>' +
        '</span>' +
        '<span class="svc-face svc-back">' +
          '<span class="svc-back-num">' + g.num + '</span>' +
          '<span class="svc-back-title">' + g.key + '</span>' +
          '<span class="svc-back-sub">' + g.blurb + '</span>' +
          '<ul class="svc-back-list">' + teaser + '</ul>' +
          
          '<span class="svc-back-cta">' + T.openList + ' <i class="fas fa-arrow-right"></i></span>' +
        '</span>' +
      '</span>';
    stage.appendChild(c);
  });

  function openOverlay(i, trigger) {
    var g = GROUPS[i];
    lastFocus = trigger || null;
    document.getElementById('svcOvBg').style.backgroundImage = "url('" + g.img + "')";
    document.getElementById('svcOvBg').style.backgroundPosition = g.pos;
    document.getElementById('svcOvKicker').innerHTML = g.num + ' &mdash; ' + g.items.length + ' ' + T.services;
    document.getElementById('svcOvTitle').innerHTML = g.key;
    document.getElementById('svcOvBlurb').innerHTML = g.blurb;
    var link = document.getElementById('svcOvLink');
    link.setAttribute('href', g.href);

    var grid = document.getElementById('svcOvGrid');
    grid.innerHTML = '';
    g.items.forEach(function (it, n) {
      var a = document.createElement('a');
      a.className = 'svc-ov-item';
      a.setAttribute('href', it[2]);
      a.style.animationDelay = (0.045 * n + 0.22) + 's';
      a.innerHTML = '<span class="svc-ov-n">' + String(n + 1).replace(/^(\d)$/, '0$1') + '</span>' +
                    '<span class="svc-ov-text"><span class="svc-ov-t">' + it[0] + '</span>' +
                    '<span class="svc-ov-d">' + it[1] + '</span></span>' +
                    '<i class="fas fa-arrow-right svc-ov-go"></i>';
      grid.appendChild(a);
    });

    overlay.classList.add('is-open');
    overlay.setAttribute('aria-hidden', 'false');
    // lock the page behind the overlay — html as well as body, or the
    // page scrollbar stays visible down the right edge
    var sbw = window.innerWidth - document.documentElement.clientWidth;
    document.documentElement.style.overflow = 'hidden';
    document.body.style.overflow = 'hidden';
    if (sbw > 0) document.body.style.paddingRight = sbw + 'px';
    setTimeout(function () { document.getElementById('svcOvClose').focus(); }, 380);
  }

  window.closeSvcOverlay = function () {
    overlay.classList.remove('is-open');
    overlay.setAttribute('aria-hidden', 'true');
    document.documentElement.style.overflow = '';
    document.body.style.overflow = '';
    document.body.style.paddingRight = '';
    if (lastFocus) lastFocus.focus();
  };

  overlay.addEventListener('click', function (e) {
    if (e.target === overlay) closeSvcOverlay();
  });

  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && overlay.classList.contains('is-open')) closeSvcOverlay();
  });
})();
