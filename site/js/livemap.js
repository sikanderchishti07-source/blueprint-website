/* ============================================================
   BluePrint — livemap.js
   Live air quality across the Kingdom's industrial hubs, on a map.
   Data: Open-Meteo air-quality API (CAMS model estimates), hourly.
   Needs #lmList, #lmPins, #lmCard on the page.
   ============================================================ */
(function () {
  var list = document.getElementById('lmList'), pins = document.getElementById('lmPins'), card = document.getElementById('lmCard');
  if (!list || !pins || !card) return;
  var AR = document.documentElement.lang === 'ar';
  var P = { L0: 33.5, L1: 57.5, B0: 14.5, B1: 33.2, W: 1000, H: 853 };
  function xy(lat, lon) { return [(lon - P.L0) / (P.L1 - P.L0) * P.W, (P.B1 - lat) / (P.B1 - P.B0) * P.H]; }

  var T = AR ? {
    bands: ['جيد', 'معتدل', 'غير صحي للحساسين', 'غير صحي', 'غير صحي جداً', 'خطر'], short: ['جيد', 'معتدل', 'للحساسين', 'غير صحي', 'غير صحي جداً', 'خطر'],
    close: 'إغلاق', aqi: 'مؤشر جودة الهواء', pm: 'الجسيمات', last: 'PM2.5 خلال آخر 24 ساعة', applies: 'ما يهم منشآت هذه المنطقة',
    finder: 'أداة تحديد المتطلبات', wa: 'واتساب', loading: 'جارٍ التحميل…', na: 'غير متاح',
    waMsg: 'مرحباً بلوبرنت، أود الاستفسار عن خدماتكم في {c}.'
  } : {
    bands: ['Good', 'Moderate', 'Unhealthy for sensitive groups', 'Unhealthy', 'Very unhealthy', 'Hazardous'], short: ['Good', 'Moderate', 'Sensitive groups', 'Unhealthy', 'Very unhealthy', 'Hazardous'],
    close: 'Close', aqi: 'Air quality index', pm: 'Particulates', last: 'PM2.5 over the last 24 hours', applies: 'What matters for facilities here',
    finder: 'Compliance Finder', wa: 'WhatsApp', loading: 'Loading…', na: 'n/a',
    waMsg: 'Hello BluePrint, I would like to ask about your services in {c}.'
  };
  var COL = ['#1aa39a', '#d9b43a', '#e08a3c', '#d4583f', '#8e3b6b', '#6b2d3c'];
  function band(a) { return a <= 50 ? 0 : a <= 100 ? 1 : a <= 150 ? 2 : a <= 200 ? 3 : a <= 300 ? 4 : 5; }

  var S = {
    permit: ['service-environmental-permit.html', 'Environmental permit', 'الترخيص البيئي'],
    rcjy: ['service-environmental-permit.html', 'Royal Commission environmental approval', 'موافقة الهيئة الملكية البيئية'],
    air: ['service-air-quality-monitoring.html', 'Air quality and stack monitoring', 'رصد جودة الهواء والانبعاثات'],
    waste: ['service-waste-management-permit.html', 'MWAN waste management permit', 'ترخيص إدارة النفايات'],
    marine: ['service-marine-environment.html', 'Marine environmental studies', 'دراسات البيئة البحرية'],
    water: ['service-water-wastewater-testing.html', 'Water and wastewater testing', 'فحص المياه ومياه الصرف'],
    eia: ['service-environmental-impact-assessment.html', 'Environmental impact assessment', 'دراسة تقييم الأثر البيئي'],
    eco: ['service-ecological-surveys.html', 'Ecological surveys', 'المسوحات البيئية والأحيائية'],
    model: ['service-environmental-modelling.html', 'Dispersion modelling', 'نمذجة التشتت']
  };
  var C = [
    ['riyadh', 24.7136, 46.6753, 'Riyadh', 'الرياض', 'Capital · second and third industrial cities', 'العاصمة · المدن الصناعية الثانية والثالثة', ['permit', 'air', 'waste']],
    ['jubail', 27.0046, 49.6225, 'Jubail', 'الجبيل', 'Royal Commission industrial city', 'مدينة صناعية تابعة للهيئة الملكية', ['rcjy', 'air', 'marine']],
    ['dammam', 26.4207, 50.0888, 'Dammam', 'الدمام', 'Eastern Province industry and port', 'صناعة وميناء المنطقة الشرقية', ['permit', 'water', 'air']],
    ['yanbu', 24.0895, 38.0618, 'Yanbu', 'ينبع', 'Royal Commission industrial city', 'مدينة صناعية تابعة للهيئة الملكية', ['rcjy', 'marine', 'model']],
    ['rabigh', 22.7986, 39.0349, 'Rabigh', 'رابغ', 'Refining and petrochemicals', 'التكرير والبتروكيماويات', ['eia', 'air', 'marine']],
    ['jeddah', 21.4858, 39.1925, 'Jeddah', 'جدة', 'Red Sea coast and industrial city', 'ساحل البحر الأحمر والمدينة الصناعية', ['waste', 'marine', 'water']],
    ['neom', 27.95, 35.30, 'NEOM', 'نيوم', 'Giga-project on the Red Sea', 'مشروع عملاق على البحر الأحمر', ['eia', 'eco', 'marine']]
  ];
  var LABEL_LEFT = { jubail: 1, yanbu: 1, rabigh: 1, jeddah: 1 };  /* fixed sides so close cities never overlap */
  var LABEL_DY = { jubail: -12, dammam: 14 };
  var data = {}, cur = null;

  /* pins and list */
  var NS = 'http://www.w3.org/2000/svg';
  C.forEach(function (c) {
    var p = xy(c[1], c[2]), g = document.createElementNS(NS, 'g');
    g.setAttribute('class', 'lm-pin'); g.setAttribute('data-id', c[0]); g.setAttribute('tabindex', '0'); g.style.color = '#9fb3b8';
    var left = !!LABEL_LEFT[c[0]];
    g.innerHTML = '<circle class="lm-halo" cx="' + p[0] + '" cy="' + p[1] + '" r="14"/><circle class="lm-core" cx="' + p[0] + '" cy="' + p[1] + '" r="8"/>' +
      '<text x="' + (p[0] + (left ? -16 : 16)) + '" y="' + (p[1] + 6 + (LABEL_DY[c[0]] || 0)) + '" text-anchor="' + (left ? 'end' : 'start') + '">' + (AR ? c[4] : c[3]) + '</text>';
    pins.appendChild(g);
    var li = document.createElement('li');
    li.innerHTML = '<button type="button" data-id="' + c[0] + '"><span class="lm-dot"></span><span><b>' + (AR ? c[4] : c[3]) + '</b><small>' + (AR ? c[6] : c[5]) +
      '</small></span><span class="lm-v">…</span><span class="lm-t">' + T.loading + '</span></button>';
    list.appendChild(li);
  });

  function paint() {
    C.forEach(function (c) {
      var d = data[c[0]], btn = list.querySelector('button[data-id="' + c[0] + '"]'), pin = pins.querySelector('[data-id="' + c[0] + '"]');
      if (!d) { btn.querySelector('.lm-v').textContent = '—'; btn.querySelector('.lm-t').textContent = T.na; return; }
      var b = band(d.aqi), col = COL[b];
      pin.style.color = col; btn.querySelector('.lm-dot').style.background = col;
      btn.querySelector('.lm-v').textContent = d.aqi;
      var t = btn.querySelector('.lm-t'); t.textContent = T.short[b]; t.style.background = col + '1f'; t.style.color = col;
    });
  }

  function spark(vals) {
    var v = vals.filter(function (x) { return x != null; }); if (v.length < 2) return '';
    var mx = Math.max.apply(null, v), mn = Math.min.apply(null, v), W = 280, H = 40, r = (mx - mn) || 1;
    var pts = v.map(function (x, i) { return (i / (v.length - 1) * W).toFixed(1) + ',' + (H - 3 - (x - mn) / r * (H - 8)).toFixed(1); });
    return '<svg class="lm-spark" viewBox="0 0 ' + W + ' ' + H + '" preserveAspectRatio="none"><polyline points="0,' + H + ' ' + pts.join(' ') + ' ' + W + ',' + H +
      '" fill="rgba(14,147,168,.10)" stroke="none"/><polyline points="' + pts.join(' ') + '" fill="none" stroke="#0e93a8" stroke-width="2" stroke-linejoin="round" vector-effect="non-scaling-stroke"/></svg>';
  }

  function show(id, anchor) {
    var c = C.filter(function (x) { return x[0] === id; })[0]; if (!c) return; cur = id;
    [].forEach.call(document.querySelectorAll('.lm-pin, .lm-list button'), function (e) { e.classList.toggle('on', e.getAttribute('data-id') === id); });
    var d = data[id], name = AR ? c[4] : c[3], b = d ? band(d.aqi) : 0;
    var BP = window.BP_CONFIG || {}, wa = 'https://wa.me/' + (BP.WHATSAPP || '966543470109') + '?text=' + encodeURIComponent(T.waMsg.replace('{c}', name));
    card.innerHTML = '<button type="button" class="lm-x" aria-label="' + T.close + '">&times;</button><h3>' + name + '</h3><p class="lm-sub">' + (AR ? c[6] : c[5]) + '</p>' +
      (d ? '<div class="lm-row"><div class="lm-aqi" style="color:' + COL[b] + '">' + d.aqi + '<small>' + T.aqi + ' · ' + T.bands[b] + '</small></div>' +
        '<div class="lm-pm"><b>PM2.5</b> ' + d.pm25 + ' µg/m³<br><b>PM10</b> ' + d.pm10 + ' µg/m³</div></div>' + spark(d.hist) + '<div class="lm-spark-l">' + T.last + '</div>' : '<p class="lm-sub">' + T.na + '</p>') +
      '<h4>' + T.applies + '</h4><ul>' + c[7].map(function (k) { return '<li><a href="' + S[k][0] + '">' + (AR ? S[k][2] : S[k][1]) + ' <span>' + (AR ? '←' : '→') + '</span></a></li>'; }).join('') + '</ul>' +
      '<div class="lm-ctas"><a class="lm-c1" href="compliance-finder.html">' + T.finder + '</a><a class="lm-c2" href="' + wa + '" target="_blank" rel="noopener">' + T.wa + '</a></div>';
    if (window.innerWidth > 960) {
      var map = card.parentNode.getBoundingClientRect(), pin = pins.querySelector('[data-id="' + id + '"] .lm-core').getBoundingClientRect();
      var x = pin.left - map.left, y = pin.top - map.top, cw = card.offsetWidth || 330;
      var left = x > map.width / 2 ? x - cw - 24 : x + 30;
      card.style.left = Math.max(0, Math.min(map.width - cw, left)) + 'px';
      card.style.top = Math.max(0, Math.min(map.height - card.offsetHeight, y - 120)) + 'px';
    }
    card.classList.add('on');
  }

  card.addEventListener('click', function (e) { if (e.target.closest('.lm-x')) { card.classList.remove('on'); [].forEach.call(document.querySelectorAll('.lm-pin.on, .lm-list button.on'), function (x) { x.classList.remove('on'); }); cur = null; } });
  pins.addEventListener('click', function (e) { var g = e.target.closest('.lm-pin'); if (g) show(g.getAttribute('data-id')); });
  pins.addEventListener('mouseover', function (e) { var g = e.target.closest('.lm-pin'); if (g && window.innerWidth > 960) show(g.getAttribute('data-id')); });
  pins.addEventListener('keydown', function (e) { if (e.key === 'Enter') { var g = e.target.closest('.lm-pin'); if (g) show(g.getAttribute('data-id')); } });
  list.addEventListener('click', function (e) { var b = e.target.closest('button'); if (b) show(b.getAttribute('data-id')); });
  list.addEventListener('mouseover', function (e) { var b = e.target.closest('button'); if (b && window.innerWidth > 960) show(b.getAttribute('data-id')); });

  var url = 'https://air-quality-api.open-meteo.com/v1/air-quality?latitude=' + C.map(function (c) { return c[1]; }).join(',') +
    '&longitude=' + C.map(function (c) { return c[2]; }).join(',') + '&current=us_aqi,pm2_5,pm10&hourly=pm2_5&past_days=1&forecast_days=1&timezone=Asia%2FRiyadh';
  fetch(url).then(function (r) { return r.json(); }).then(function (res) {
    if (!Array.isArray(res)) res = [res];
    var now = Date.now();
    res.forEach(function (d, i) {
      var cu = d && d.current; if (!cu || cu.us_aqi == null) return;
      var h = (d.hourly && d.hourly.pm2_5) || [], t = (d.hourly && d.hourly.time) || [], hist = [];
      for (var k = 0; k < t.length; k++) { var ts = Date.parse(t[k] + ':00+03:00'); if (ts <= now && ts > now - 864e5) hist.push(h[k]); }
      data[C[i][0]] = { aqi: Math.min(500, Math.round(cu.us_aqi)), pm25: Math.round(cu.pm2_5), pm10: Math.round(cu.pm10), hist: hist };
    });
    paint(); show(cur || 'riyadh');
  }).catch(function () { paint(); show('riyadh'); });
})();
