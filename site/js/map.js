/* ============================================================
   BluePrint - map.js
   Square Google map of the office in the footer.
   Google Maps sets its own cookies, so the live map loads only
   after the visitor accepts cookies (js/consent.js) or presses
   "Show map". Until then a light placeholder with the pin shows.
   The location comes from MAP_QUERY in js/config.js.
   ============================================================ */
(function () {
  var C = window.BP_CONFIG || {};
  var Q = C.MAP_QUERY || C.ADDRESS_LINE1 || '';
  var ar = (document.documentElement.lang || '').indexOf('ar') === 0;

  function granted() {
    if (window.BP_CONSENT) return true;
    try { return localStorage.getItem('bp_consent') === 'granted'; } catch (e) { return false; }
  }

  function load(box) {
    if (!box || box.classList.contains('is-live')) return;
    var f = document.createElement('iframe');
    f.src = 'https://www.google.com/maps?q=' + encodeURIComponent(Q) + '&z=16&hl=' + (ar ? 'ar' : 'en') + '&output=embed';
    f.title = box.getAttribute('data-title') || 'Map';
    f.loading = 'lazy';
    f.referrerPolicy = 'no-referrer-when-downgrade';
    f.onload = function () { box.classList.add('is-ready'); };
    box.insertBefore(f, box.firstChild);
    box.classList.add('is-live');
  }

  function dropWhenSeen(box) {
    if (!('IntersectionObserver' in window)) { box.classList.add('is-drop'); return; }
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) { if (e.isIntersecting) { box.classList.add('is-drop'); io.disconnect(); } });
    }, { threshold: 0.4 });
    io.observe(box);
  }

  function start() {
    var dir = 'https://www.google.com/maps/dir/?api=1&destination=' + encodeURIComponent(Q);
    document.querySelectorAll('[data-map-dir]').forEach(function (a) { a.href = dir; });
    document.querySelectorAll('[data-map]').forEach(function (box) {
      var btn = box.querySelector('.fc-map-load');
      if (btn) btn.onclick = function () { load(box); };
      if (granted()) load(box);
      dropWhenSeen(box);
    });
  }

  window.addEventListener('bp-consent', function () {
    document.querySelectorAll('[data-map]').forEach(load);
  });
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', start);
  else start();
})();
