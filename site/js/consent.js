/* ============================================================
   BluePrint - consent.js
   Cookie banner (English / Arabic) and Google Analytics 4.
   Analytics is loaded ONLY after the visitor clicks Accept.
   The choice is remembered in this browser; the "Cookie settings"
   link in the footer opens the banner again.
   The GA ID lives in js/config.js (GA_ID).
   ============================================================ */
(function () {
  var KEY = 'bp_consent';
  var C = window.BP_CONFIG || {};
  var GA = C.GA_ID;
  var ar = (document.documentElement.lang || '').indexOf('ar') === 0;
  var T = ar ? {
    text: 'نستخدم ملفات تعريف الارتباط للإحصاءات ولخريطة موقع المكتب، بهدف تحسين موقعنا، ولا تُفعَّل إلا بموافقتك.',
    more: 'سياسة الخصوصية', accept: 'قبول', decline: 'رفض',
    label: 'ملفات تعريف الارتباط', settings: 'إعدادات ملفات تعريف الارتباط'
  } : {
    text: 'We use cookies for website analytics and for the office map, so we can improve our website. They are only set if you accept.',
    more: 'Privacy Policy', accept: 'Accept', decline: 'Decline',
    label: 'Cookies', settings: 'Cookie settings'
  };

  function get() { try { return localStorage.getItem(KEY); } catch (e) { return null; } }
  function set(v) { try { localStorage.setItem(KEY, v); } catch (e) {} }

  var loaded = false;
  function loadGA() {
    if (loaded || !GA) return;
    loaded = true;
    window.dataLayer = window.dataLayer || [];
    window.gtag = function () { window.dataLayer.push(arguments); };
    window.gtag('js', new Date());
    window.gtag('config', GA);
    var s = document.createElement('script');
    s.async = true;
    s.src = 'https://www.googletagmanager.com/gtag/js?id=' + encodeURIComponent(GA);
    document.head.appendChild(s);
  }

  function clearGACookies() {
    var host = location.hostname.replace(/^www\./, '');
    document.cookie.split(';').forEach(function (c) {
      var name = c.split('=')[0].trim();
      if (name.indexOf('_ga') !== 0) return;
      ['', '; domain=' + host, '; domain=.' + host].forEach(function (d) {
        document.cookie = name + '=; expires=Thu, 01 Jan 1970 00:00:00 GMT; path=/' + d;
      });
    });
  }

  function css() {
    if (document.getElementById('bp-cc-css')) return;
    var st = document.createElement('style');
    st.id = 'bp-cc-css';
    st.textContent =
      '#bp-cc{position:fixed;left:50%;bottom:20px;transform:translateX(-50%);z-index:9999;width:min(620px,calc(100% - 24px));' +
      'background:#0b2f38;color:#fff;border-radius:16px;box-shadow:0 12px 40px rgba(0,0,0,.28);padding:18px 20px;' +
      'display:flex;gap:16px;align-items:center;flex-wrap:wrap;font-size:14px;line-height:1.55}' +
      '#bp-cc p{margin:0;flex:1 1 300px;color:rgba(255,255,255,.88)}' +
      '#bp-cc a{color:#45bbce;text-decoration:underline}' +
      '#bp-cc .bp-cc-btns{display:flex;gap:8px;flex:0 0 auto}' +
      '#bp-cc button{border:0;border-radius:999px;padding:10px 20px;font:inherit;font-weight:700;cursor:pointer}' +
      '#bp-cc .bp-cc-yes{background:#fff;color:#0b2f38}' +
      '#bp-cc .bp-cc-no{background:transparent;color:#fff;box-shadow:inset 0 0 0 1px rgba(255,255,255,.45)}' +
      '#bp-cc button:focus-visible{outline:2px solid #45bbce;outline-offset:2px}' +
      '@media (max-width:640px){#bp-cc{bottom:12px;padding:16px}#bp-cc .bp-cc-btns{width:100%}#bp-cc button{flex:1}}';
    document.head.appendChild(st);
  }

  function fire() { try { window.dispatchEvent(new Event('bp-consent')); } catch (e) {} window.BP_CONSENT = true; }

  function hide() { var b = document.getElementById('bp-cc'); if (b) b.remove(); }

  function show() {
    if (document.getElementById('bp-cc')) return;
    css();
    var b = document.createElement('div');
    b.id = 'bp-cc';
    b.setAttribute('role', 'region');
    b.setAttribute('aria-label', T.label);
    b.dir = ar ? 'rtl' : 'ltr';
    b.innerHTML = '<p>' + T.text + ' <a href="privacy.html">' + T.more + '</a></p>' +
      '<div class="bp-cc-btns"><button type="button" class="bp-cc-yes">' + T.accept + '</button>' +
      '<button type="button" class="bp-cc-no">' + T.decline + '</button></div>';
    b.querySelector('.bp-cc-yes').onclick = function () { set('granted'); hide(); loadGA(); fire(); };
    b.querySelector('.bp-cc-no').onclick = function () {
      var was = get() === 'granted';
      set('denied'); hide(); clearGACookies();
      if (was && loaded) location.reload();   // stop analytics that already started on this page
    };
    document.body.appendChild(b);
  }

  // "Cookie settings" link next to the footer's privacy link
  function footerLink() {
    var p = document.querySelector('.footer-legal-btn[href$="privacy.html"]');
    if (!p || document.getElementById('bp-cc-open')) return;
    var sep = document.createElement('span');
    sep.className = 'footer-legal-sep';
    var a = document.createElement('a');
    a.id = 'bp-cc-open';
    a.href = '#';
    a.className = 'footer-legal-btn';
    a.textContent = T.settings;
    a.onclick = function (e) { e.preventDefault(); show(); };
    p.parentNode.insertBefore(sep, p.nextSibling);
    p.parentNode.insertBefore(a, sep.nextSibling);
  }

  function start() {
    footerLink();
    var v = get();
    if (v === 'granted') { loadGA(); fire(); }
    else if (v !== 'denied') show();
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', start);
  else start();
})();
