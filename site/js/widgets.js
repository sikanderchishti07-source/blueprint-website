/* ============================================================
   BluePrint — widgets.js
   WhatsApp button, expert CTA,
   client-logo ticker.
   ============================================================ */
(function () {
  'use strict';
  var C = window.BP_CONFIG || {};

  /* ── WhatsApp floating button ────────────────────────────── */
  var wa = document.getElementById('whatsappBtn');
  if (wa) wa.addEventListener('click', function (e) {
    e.preventDefault();
    window.open(bpWaLink("Hi BluePrint, I'm interested in your environmental services."), '_blank');
  });

  /* ── Expert CTA ──────────────────────────────────────────── */
  var expertEl = document.getElementById('expertCTA');
  if (expertEl) {
    window.toggleExpert = function () { expertEl.classList.toggle('open'); };
    window.closeExpert  = function () { expertEl.classList.remove('open'); };
    document.getElementById('expertTab').addEventListener('keydown', function (e) {
      if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); toggleExpert(); }
    });
    document.addEventListener('click', function (e) {
      if (expertEl.classList.contains('open') && !expertEl.contains(e.target)) closeExpert();
    });
    window.sendExpertMsg = function () {
      var input = document.getElementById('expertMsgInput');
      var msg = input.value.trim(); if (!msg) return;
      window.open(bpWaLink('Hi BluePrint, I have a question: ' + msg), '_blank');
      input.value = '';
    };
    document.getElementById('expertMsgInput').addEventListener('keydown', function (e) { if (e.key === 'Enter') sendExpertMsg(); });
    window.addEventListener('scroll', function () {
      var show = window.scrollY > 200;
      expertEl.style.opacity = show ? '1' : '0';
      expertEl.style.pointerEvents = show ? 'all' : 'none';
    }, { passive: true });
  }

})();
