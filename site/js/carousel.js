/* ============================================================
   BluePrint — carousel.js
   Fanned "Our services" carousel. Bails out if not on the page.
   ============================================================ */
(function () {
  'use strict';
  const track = document.getElementById('carTrack');
  if (!track) return;

  const S = [
    {t:'Environmental Studies', i:'fa-seedling',
     d:'In-depth impact assessments and baseline studies that support informed decisions and regulatory approval.',
     href:'service-environmental-studies.html', img:'assets/img/svc-card-1.webp'},
    {t:'Marine Environment', i:'fa-water',
     d:'Water quality, sediment, benthic habitat and oceanographic survey for coastal development and discharge.',
     href:'service-marine-environment-services.html', img:'assets/img/svc-card-2.webp'},
    {t:'Terrestrial Environment', i:'fa-leaf',
     d:'Habitat mapping, baseline ecology and protected species assessment across desert and coastal terrain.',
     href:'service-terrestrial-environment.html', img:'assets/img/svc-card-3.webp'},
    {t:'Veterinary Consultations &amp; Biosecurity', i:'fa-paw',
     d:'Biosecurity planning and veterinary advisory for operations where animal health and the environment meet.',
     href:'service-veterinary-biosecurity.html', img:'assets/img/svc-card-4.webp'},
    {t:'Test Boreholes', i:'fa-ruler-vertical',
     d:'Borehole drilling and sampling to establish ground conditions, groundwater and the extent of contamination.',
     href:'service-test-boreholes.html', img:'assets/img/svc-card-5.webp'},
    {t:'Hydrogeology &amp; Geotechnics', i:'fa-tint',
     d:'Groundwater assessment and geotechnical investigation for development, extraction and remediation.',
     href:'service-hydrogeology-geotechnics.html', img:'assets/img/svc-card-6.webp'},
    {t:'Treatment &amp; Rehabilitation', i:'fa-recycle',
     d:'Remediation design and rehabilitation of contaminated and disturbed land, validated through to closure.',
     href:'service-treatment-rehabilitation.html', img:'assets/img/svc-card-7.webp'},
    {t:'Environmental Training', i:'fa-graduation-cap',
     d:'Practical training for site teams on monitoring, permit conditions and environmental record-keeping.',
     href:'service-environmental-training.html', img:'assets/img/svc-card-8.webp'}
  ];

  const dots = document.getElementById('carDots');
  let cur = 0, hov = null;

  S.forEach((s, n) => {
    const a = document.createElement('a');
    a.className = 'car-card';
    a.href = s.href;
    a.innerHTML =
      '<img src="' + s.img + '" alt="" loading="lazy"><span class="car-veil"></span>' +
      '<span class="car-idx">' + String(n + 1).padStart(2, '0') + ' / 08</span>' +
      '<span class="car-body"><span class="car-ic"><i class="fas ' + s.i + '"></i></span>' +
      '<h3>' + s.t + '</h3><p>' + s.d + '</p>' +
      '<span class="car-go"><i class="fas fa-arrow-right"></i></span></span>';
    a.addEventListener('click', e => { if (n !== cur) { e.preventDefault(); go(n); } });
    a.addEventListener('mouseenter', () => { hov = n; layout(); pause(); });
    a.addEventListener('mouseleave', () => { hov = null; layout(); resume(); });
    a.addEventListener('focus',      () => { hov = n; layout(); pause(); });
    a.addEventListener('blur',       () => { hov = null; layout(); resume(); });
    track.appendChild(a); s.el = a;

    const d = document.createElement('button');
    d.className = 'car-dot'; d.type = 'button';
    d.setAttribute('aria-label', 'Go to service ' + (n + 1));
    d.addEventListener('click', () => { go(n); pause(); resume(); });
    dots.appendChild(d); s.dot = d;
  });

  function layout() {
    const N = S.length;
    S.forEach((s, n) => {
      let o = n - cur; if (o > N / 2) o -= N; if (o < -N / 2) o += N;
      const a = Math.abs(o);
      
      const x = o * 224 + Math.sign(o) * Math.min(a, 1) * 44;
      const rot = Math.max(-26, Math.min(26, -o * 8));
      const z = -a * 95;
      const sc = a === 0 ? 1 : Math.max(.84, 1 - a * .045);
      const lift = (n === hov && a !== 0);
      s.el.style.transform =
        'translateX(' + x + 'px) translateZ(' + (lift ? z + 90 : z) + 'px) ' +
        'rotateY(' + (lift ? rot * 0.45 : rot) + 'deg) scale(' + (lift ? Math.min(1, sc + .09) : sc) + ')';
      s.el.style.opacity = a > 3.5 ? 0 : (lift ? 1 : Math.max(.88, 1 - a * .045));
      s.el.style.zIndex = String(lift ? 25 : 30 - Math.round(a));
      s.el.style.pointerEvents = a > 3.5 ? 'none' : 'auto';
      s.el.classList.toggle('hov', lift);
      s.el.classList.toggle('act', a === 0);
      /* cards left of centre are covered on their right edge and vice versa,
         so the label hugs whichever edge is still visible */
      s.el.classList.toggle('sideL', o < 0);
      s.el.classList.toggle('sideR', o > 0);
      s.dot.classList.toggle('on', a === 0);
    });
  }
  function go(n) { cur = (n + S.length) % S.length; layout(); }

  /* autorotation — pauses on hover, on focus and when the tab is hidden */
  const REDUCED = matchMedia('(prefers-reduced-motion: reduce)').matches;
  let timer = null;
  function resume() { if (REDUCED || timer || hov !== null) return; timer = setInterval(() => go(cur + 1), 5000); }
  function pause() { clearInterval(timer); timer = null; }
  document.addEventListener('visibilitychange', () => document.hidden ? pause() : resume());

  document.getElementById('carPrev').onclick = () => { go(cur - 1); pause(); resume(); };
  document.getElementById('carNext').onclick = () => { go(cur + 1); pause(); resume(); };
  const stage = document.querySelector('.car-stage');
  stage.addEventListener('mouseenter', pause);
  stage.addEventListener('mouseleave', resume);

  layout(); resume();
})();
