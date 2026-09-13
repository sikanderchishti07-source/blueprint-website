/* ============================================================
   BluePrint â€” main.js
   Navbar, mobile drawer, scroll reveal, modals, particles,
   contact-detail injection from BP_CONFIG.
   ============================================================ */
(function () {
  'use strict';
  var C = window.BP_CONFIG || {};

  /* â”€â”€ Inject contact details from config â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€ */
  function waLink(text) {
    return 'https://wa.me/' + C.WHATSAPP + (text ? '?text=' + encodeURIComponent(text) : '');
  }
  document.querySelectorAll('[data-wa]').forEach(function (a) {
    a.href = waLink(a.getAttribute('data-wa') || '');
    a.target = '_blank'; a.rel = 'noopener';
  });
  document.querySelectorAll('[data-tel]').forEach(function (a) { a.href = 'tel:' + C.PHONE_TEL; });
  document.querySelectorAll('[data-mail]').forEach(function (a) { a.href = 'mailto:' + C.EMAIL; });
  document.querySelectorAll('[data-text=phone]').forEach(function (el) { el.textContent = C.PHONE_DISPLAY; });
  document.querySelectorAll('[data-text=email]').forEach(function (el) { el.textContent = C.EMAIL; });
  document.querySelectorAll('[data-text=website]').forEach(function (el) { el.textContent = C.WEBSITE; });
  document.querySelectorAll('[data-text=address]').forEach(function (el) { el.innerHTML = C.ADDRESS_LINE1 + '<br>' + C.ADDRESS_LINE2; });
  document.querySelectorAll('[data-text=year]').forEach(function (el) { el.textContent = new Date().getFullYear(); });
  window.bpWaLink = waLink;

  /* â”€â”€ Navbar scrolled state â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€ */
  var nav = document.getElementById('navbar');
  window.addEventListener('scroll', function () {
    if (nav) nav.classList.toggle('scrolled', window.scrollY > 20);
  }, { passive: true });

  /* â”€â”€ Active nav link for current page â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€ */
  var page = (location.pathname.split('/').pop() || 'index.html').toLowerCase();
  document.querySelectorAll('.nav-link[data-page]').forEach(function (l) {
    if (l.getAttribute('data-page') === page) l.classList.add('active');
  });

  /* â”€â”€ Mobile drawer â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€ */
  window.toggleNavDrawer = function () {
    var drawer = document.getElementById('navMobileDrawer');
    var overlay = document.getElementById('navDrawerOverlay');
    var ham = document.getElementById('navHamburger');
    var isOpen = drawer.classList.contains('open');
    drawer.classList.toggle('open'); overlay.classList.toggle('open'); ham.classList.toggle('open');
    document.body.style.overflow = isOpen ? '' : 'hidden';
  };
  window.closeNavDrawer = function () {
    ['navMobileDrawer', 'navDrawerOverlay', 'navHamburger'].forEach(function (id) {
      var el = document.getElementById(id); if (el) el.classList.remove('open');
    });
    document.body.style.overflow = '';
  };

  /* â”€â”€ Scroll-reveal observer â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€ */
  var revealObserver = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) { if (e.isIntersecting) e.target.classList.add('active'); });
  }, { threshold: 0.1, rootMargin: '0px 0px -50px 0px' });
  document.querySelectorAll('.scroll-reveal').forEach(function (el) { revealObserver.observe(el); });

  /* â”€â”€ Smooth same-page anchor scrolling â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€ */
  document.querySelectorAll('a[href^="#"]').forEach(function (a) {
    a.addEventListener('click', function (e) {
      var href = a.getAttribute('href');
      if (href === '#') { e.preventDefault(); return; }
      var target = document.querySelector(href);
      if (target) { e.preventDefault(); target.scrollIntoView({ behavior: 'smooth' }); closeNavDrawer(); }
    });
  });

  /* â”€â”€ Hero particles â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€ */
  var container = document.getElementById('particles');
  if (container) {
    for (var i = 0; i < 20; i++) {
      var p = document.createElement('div');
      p.className = 'particle';
      p.style.cssText = 'width:' + (Math.random() * 10 + 5) + 'px;height:' + (Math.random() * 10 + 5) + 'px;left:' + (Math.random() * 100) + '%;top:' + (Math.random() * 100) + '%;animation-delay:' + (Math.random() * 5) + 's;animation-duration:' + (Math.random() * 10 + 10) + 's';
      container.appendChild(p);
    }
  }

  /* â”€â”€ Logo click â†’ home / top â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€ */
  document.querySelectorAll('.js-home-link').forEach(function (el) {
    el.addEventListener('click', function (e) {
      if (page === 'index.html' || page === '') { e.preventDefault(); window.scrollTo({ top: 0, behavior: 'smooth' }); }
    });
  });

  /* â”€â”€ Contact form (front-end only, as in the original) â”€â”€â”€â”€â”€ */
  window.sendContactMessage = function () { alert('Thank you! Our team will contact you shortly.'); };
})();

/* Client logo strip - logos grow as they cross the centre of the band */
(function () {
  var band = document.querySelector('.logo-marquee');
  if (!band) return;
  var track = band.querySelector('.logo-track');
  if (!track) return;
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    Array.prototype.forEach.call(track.children, function (c) { c.style.opacity = 1; });
    return;
  }
  var cells = track.children, RANGE = 300, MAX = 0.25, running = false;
  function frame() {
    var b = band.getBoundingClientRect();
    if (b.bottom < 0 || b.top > window.innerHeight) { requestAnimationFrame(frame); return; }
    var mid = b.left + b.width / 2;
    for (var i = 0; i < cells.length; i++) {
      var r = cells[i].getBoundingClientRect();
      var d = Math.abs((r.left + r.width / 2) - mid);
      var t = Math.max(0, 1 - d / RANGE);
      var e = t * t * (3 - 2 * t);
      cells[i].style.transform = 'scale(' + (1 + MAX * e).toFixed(3) + ')';
      cells[i].style.zIndex = e > 0.5 ? 2 : 1;
      
    }
    requestAnimationFrame(frame);
  }
  if (!running) { running = true; requestAnimationFrame(frame); }
})();


