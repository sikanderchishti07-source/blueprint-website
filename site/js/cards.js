/* ============================================================
   BluePrint — cards.js
   Three-card service showcase. Click a card to expand its
   service list, staggered in. Home page only.
   ============================================================ */
(function () {
  'use strict';
  var stage = document.getElementById('svcStage');
  if (!stage) return;

  var GROUPS = [
    {
      key: 'Compliance &amp; Permitting', num: '01', icon: 'fa-stamp',
      img: 'assets/img/card-1.jpg', pos: '20% 30%',
      blurb: 'Getting your facility licensed &mdash; and keeping it licensed.',
      href: 'services.html#permitting',
      items: [
        ['Environmental Permit', 'NCEC permit file, start to issuance', 'services.html#svc-0'],
        ['Environmental Impact Assessment', 'EIA/ESIA for high-impact projects', 'services.html#svc-1'],
        ['Waste Management Permit', 'MWAN permit for regulated waste', 'services.html#svc-2'],
        ['Environmental Management Plan', 'Permit conditions into daily practice', 'services.html#svc-3'],
        ['Environmental Register', 'Continuous proof of compliance', 'services.html#svc-4'],
        ['Periodic Environmental Report', 'Keeping the permit you won', 'services.html#svc-5']
      ]
    },
    {
      key: 'Monitoring, Testing &amp; Measurement', num: '02', icon: 'fa-flask',
      img: 'assets/img/card-2.jpg', pos: '75% 60%',
      blurb: 'The numbers behind every compliance claim.',
      href: 'services.html#monitoring',
      items: [
        ['Air Quality Monitoring &amp; Testing', 'Measurement against KSA standards', 'technology.html#equipment'],
        ['Water &amp; Wastewater Testing', 'Accredited analysis', 'technology.html#equipment'],
        ['Noise Monitoring &amp; Assessment', 'Against regulated limits', 'technology.html#equipment'],
        ['Soil &amp; Sediment Testing', 'Characteristics and contaminants', 'technology.html#equipment'],
        ['Field Monitoring &amp; Measurement', 'Precise on-site parameters', 'technology.html#equipment'],
        ['Environmental Sampling', 'Chain-of-custody protocols', 'technology.html#equipment'],
        ['Monitoring Programmes', 'Scheduled, tracked, reported', 'technology.html#equipment'],
        ['Laboratory Analysis', 'With technical interpretation', 'technology.html#equipment'],
        ['Pollution Control Equipment', 'Supply and operation', 'technology.html#equipment'],
        ['Reporting &amp; Compliance', 'Periodic regulatory reports', 'technology.html#equipment']
      ]
    },
    {
      key: 'Specialist Disciplines', num: '03', icon: 'fa-layer-group',
      img: 'assets/img/card-3.jpg', pos: '50% 75%',
      blurb: 'Deeper technical work across six disciplines.',
      href: 'services.html',
      items: [
        ['Climate Change &amp; Sustainability', 'ESG, carbon footprint, net zero &mdash; 17 services', 'services.html'],
        ['Ecological &amp; Biological Surveys', 'Baseline, habitat, protected species &mdash; 6', 'services.html'],
        ['Marine Environment', 'Sampling, mapping, modelling &mdash; 6', 'services.html'],
        ['Remediation &amp; Rehabilitation', 'Investigation to in-situ works &mdash; 5', 'services.html'],
        ['Environmental Modelling', 'Dispersion, hydrology, noise &mdash; 5', 'services.html'],
        ['Laboratory Services', 'Sampling through interpretation &mdash; 10', 'services.html']
      ]
    }
  ];

  var overlay = document.getElementById('svcOverlay');
  var lastFocus = null;

  GROUPS.forEach(function (g, i) {
    var c = document.createElement('button');
    c.type = 'button';
    c.className = 'svc-card';
    c.setAttribute('aria-label', 'View ' + g.key.replace(/&amp;/g, 'and') + ' services');
    c.addEventListener('click', function () { openOverlay(i, c); });
    var teaser = g.items.slice(0, 4).map(function (it) { return '<li>' + it[0] + '</li>'; }).join('');
    c.innerHTML =
      '<span class="svc-flip">' +
        '<span class="svc-face svc-front">' +
          '<span class="svc-card-bg" style="background-image:url(\'' + g.img + '\');background-position:' + g.pos + '"></span>' +
          '<span class="svc-card-veil"></span>' +
          '<span class="svc-card-num">' + g.num + '</span>' +
          '<span class="svc-card-icon"><i class="fas ' + g.icon + '"></i></span>' +
          '<span class="svc-card-glass">' +
            '<span class="svc-card-count">' + g.items.length + ' services</span>' +
            '<span class="svc-card-title">' + g.key + '</span>' +
            '<span class="svc-card-blurb">' + g.blurb + '</span>' +
          '</span>' +
        '</span>' +
        '<span class="svc-face svc-back">' +
          '<span class="svc-back-num">' + g.num + '</span>' +
          '<span class="svc-back-title">' + g.key + '</span>' +
          '<ul class="svc-back-list">' + teaser + '</ul>' +
          '<span class="svc-back-more">+ ' + (g.items.length - 4) + ' more</span>' +
          '<span class="svc-back-cta">Open full list <i class="fas fa-arrow-right"></i></span>' +
        '</span>' +
      '</span>';
    stage.appendChild(c);
  });

  function openOverlay(i, trigger) {
    var g = GROUPS[i];
    lastFocus = trigger || null;
    document.getElementById('svcOvBg').style.backgroundImage = "url('" + g.img + "')";
    document.getElementById('svcOvBg').style.backgroundPosition = g.pos;
    document.getElementById('svcOvKicker').innerHTML = g.num + ' &mdash; ' + g.items.length + ' services';
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
    document.body.style.overflow = 'hidden';
    setTimeout(function () { document.getElementById('svcOvClose').focus(); }, 380);
  }

  window.closeSvcOverlay = function () {
    overlay.classList.remove('is-open');
    overlay.setAttribute('aria-hidden', 'true');
    document.body.style.overflow = '';
    if (lastFocus) lastFocus.focus();
  };

  overlay.addEventListener('click', function (e) {
    if (e.target === overlay) closeSvcOverlay();
  });

  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && overlay.classList.contains('is-open')) closeSvcOverlay();
  });
})();
