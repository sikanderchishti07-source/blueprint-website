/* ============================================================
   BluePrint — scroll.js
   Staggered reveals and a light parallax drift on section
   imagery. Plain JS, no dependencies. Respects reduced motion.
   ============================================================ */
(function () {
  'use strict';
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;

  var GRIDS = [
    '.svq-feats', '.svq-whos', '.acr-grid', '.sect-card',
    '.em-stats', '.blog-filters'
  ];

  document.querySelectorAll('.scroll-reveal').forEach(function (el) {
    var kids = el.children;
    if (kids.length >= 2 && kids.length <= 8) {
      var grid = window.getComputedStyle(el).display;
      if (grid === 'grid' || grid === 'flex') el.classList.add('stagger');
    }
  });

  GRIDS.forEach(function (sel) {
    document.querySelectorAll(sel).forEach(function (el) {
      if (!el.classList.contains('scroll-reveal') && el.children.length >= 2 && el.children.length <= 8) {
        el.classList.add('scroll-reveal', 'stagger');
      }
    });
  });

  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      if (e.isIntersecting) { e.target.classList.add('active'); io.unobserve(e.target); }
    });
  }, { rootMargin: '0px 0px -8% 0px', threshold: 0.05 });

  document.querySelectorAll('.scroll-reveal').forEach(function (el) { io.observe(el); });

  var drifters = [];
  ['.space-y-20 .rounded-2xl.overflow-hidden.shadow-lg img',
   '#overview .about-video',
   '.svq-band-img'].forEach(function (sel) {
    document.querySelectorAll(sel).forEach(function (el) {
      el.classList.add('px-drift');
      drifters.push(el);
    });
  });

  if (!drifters.length) return;

  var ticking = false;
  function frame() {
    var vh = window.innerHeight;
    drifters.forEach(function (el) {
      var r = el.getBoundingClientRect();
      if (r.bottom < -200 || r.top > vh + 200) return;
      var mid = r.top + r.height / 2;
      var off = ((mid - vh / 2) / vh) * -26;
      el.style.transform = 'translate3d(0,' + off.toFixed(1) + 'px,0) scale(1.06)';
    });
    ticking = false;
  }
  function onScroll() {
    if (!ticking) { ticking = true; requestAnimationFrame(frame); }
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  window.addEventListener('resize', onScroll, { passive: true });
  frame();
})();
