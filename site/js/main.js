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

  /* the nav goes transparent over dark sections and solid over light ones.
     a section counts as dark if it carries .bp-dark or is one of the known
     dark blocks below. */
  var DARK = '.bp-dark, .wrap, .carsec-head ~ *, .abt-hero, .abt-mdl-sec, .abt-cta, ' +
             /* .svcd-hero is left out: only its photo side is dark, and the menu
                sits over the light side, so white menu text would vanish there */
             '.eqp-hero, .cmp-hero, .svq-hero, .svq-cta, .svq-band, ' +
             '.svcd-band, .page-header, .site-footer, .footer-cta-strip';

  /* the element list is fixed for the page, so query it once */
  var darkEls = [];
  var navH = 84;
  function cacheDark() {
    darkEls = Array.prototype.slice.call(document.querySelectorAll(DARK));
    if (nav) navH = nav.getBoundingClientRect().height * 0.55;
  }

  function overDark() {
    for (var i = 0; i < darkEls.length; i++) {
      var r = darkEls[i].getBoundingClientRect();
      if (r.top <= navH && r.bottom >= navH) return true;
    }
    return false;
  }

  var ticking = false;
  function syncNav() {
    if (!nav || ticking) return;
    ticking = true;
    requestAnimationFrame(function () {
      nav.classList.toggle('scrolled', window.scrollY > 20);
      nav.classList.toggle('on-dark', overDark());
      ticking = false;
    });
  }

  cacheDark();
  window.addEventListener('scroll', syncNav, { passive: true });
  window.addEventListener('resize', function () { cacheDark(); syncNav(); });
  syncNav();

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
  window.sendContactMessage = function () { /* lang-aware */ alert(document.documentElement.lang === 'ar' ? 'شكراً لك! سيتواصل معك فريقنا قريباً.' : 'Thank you! Our team will contact you shortly.'); };
})();


/* Logo unfurl runs on the home page only */
(function () {
  var p = (location.pathname.split('/').pop() || 'index.html').toLowerCase();
  if (p === '' || p === 'index.html') {
    document.documentElement.classList.add('bp-home');
  }


  /* videos below the fold only start downloading when they come near */
  (function () {
    var vids = document.querySelectorAll('video[data-lazy], .about-video video, .abt-story-video');
    if (!vids.length || !('IntersectionObserver' in window)) return;
    vids.forEach(function (v) {
      var srcs = Array.prototype.slice.call(v.querySelectorAll('source'));
      srcs.forEach(function (s) {
        if (s.src) { s.setAttribute('data-src', s.src); s.removeAttribute('src'); }
      });
      v.removeAttribute('autoplay');
      v.preload = 'none';
      v.load();
    });
    var io2 = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (!e.isIntersecting) return;
        var v = e.target;
        v.querySelectorAll('source[data-src]').forEach(function (s) {
          s.src = s.getAttribute('data-src'); s.removeAttribute('data-src');
        });
        v.preload = 'auto';
        v.load();
        v.play().catch(function () {});
        io2.unobserve(v);
      });
    }, { rootMargin: '300px' });
    vids.forEach(function (v) { io2.observe(v); });
  })();

})();
