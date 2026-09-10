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

  var panel = document.getElementById('svcPanel');
  var lastFocus = null;

  GROUPS.forEach(function (g, i) {
    var c = document.createElement('button');
    c.type = 'button';
    c.className = 'svc-card';
    c.setAttribute('aria-label', 'View ' + g.key.replace(/&amp;/g, 'and') + ' services');
    c.addEventListener('click', function () { openPanel(i, c); });
    c.innerHTML =
      '<span class="svc-card-bg" style="background-image:url(\'' + g.img + '\');background-position:' + g.pos + '"></span>' +
      '<span class="svc-card-veil"></span>' +
      '<span class="svc-card-num">' + g.num + '</span>' +
      '<span class="svc-card-icon"><i class="fas ' + g.icon + '"></i></span>' +
      '<span class="svc-card-glass">' +
        '<span class="svc-card-count">' + g.items.length + ' services</span>' +
        '<span class="svc-card-title">' + g.key + '</span>' +
        '<span class="svc-card-blurb">' + g.blurb + '</span>' +
        '<span class="svc-card-cta">Explore <i class="fas fa-arrow-right"></i></span>' +
      '</span>';
    stage.appendChild(c);
  });

  function openPanel(i, trigger) {
    var g = GROUPS[i];
    lastFocus = trigger || null;
    document.getElementById('svcPanelHero').style.backgroundImage = "url('" + g.img + "')";
    document.getElementById('svcPanelHero').style.backgroundPosition = g.pos;
    document.getElementById('svcPanelKicker').innerHTML = g.num + ' &mdash; ' + g.items.length + ' services';
    document.getElementById('svcPanelTitle').innerHTML = g.key;
    document.getElementById('svcPanelBlurb').innerHTML = g.blurb;
    var link = document.getElementById('svcPanelLink');
    link.setAttribute('href', g.href);

    var grid = document.getElementById('svcPanelGrid');
    grid.innerHTML = '';
    g.items.forEach(function (it, n) {
      var a = document.createElement('a');
      a.className = 'svc-item';
      a.setAttribute('href', it[2]);
      a.style.animationDelay = (0.055 * n + 0.14) + 's';
      a.innerHTML = '<span class="svc-item-n">' + String(n + 1).replace(/^(\d)$/, '0$1') + '</span>' +
                    '<span><span class="svc-item-t">' + it[0] + '</span>' +
                    '<span class="svc-item-d">' + it[1] + '</span></span>';
      grid.appendChild(a);
    });

    stage.classList.add('is-open');
    panel.classList.add('is-open');
    panel.setAttribute('aria-hidden', 'false');
    setTimeout(function () { document.getElementById('svcPanelClose').focus(); }, 380);
  }

  window.closeSvcPanel = function () {
    stage.classList.remove('is-open');
    panel.classList.remove('is-open');
    panel.setAttribute('aria-hidden', 'true');
    if (lastFocus) lastFocus.focus();
  };

  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && panel.classList.contains('is-open')) closeSvcPanel();
  });
})();
