/* ============================================================
   BluePrint — widgets.js
   AQI live widget, AI chatbot, WhatsApp button, expert CTA,
   client-logo ticker.
   ============================================================ */
(function () {
  'use strict';
  var C = window.BP_CONFIG || {};

  /* ── AQI widget ──────────────────────────────────────────── */
  (function () {
    var w = document.getElementById('aqiWidget'); if (!w) return;
    var expanded = false;
    function aqiColor(v) {
      if (v <= 50)  return { hex: '#22c55e', alpha: 'rgba(34,197,94,.55)',  label: 'Good 😊',      stat: '#4ade80' };
      if (v <= 100) return { hex: '#eab308', alpha: 'rgba(234,179,8,.55)',  label: 'Moderate 😐',  stat: '#facc15' };
      if (v <= 150) return { hex: '#f97316', alpha: 'rgba(249,115,22,.55)', label: 'Unhealthy*',   stat: '#fb923c' };
      return               { hex: '#ef4444', alpha: 'rgba(239,68,68,.55)',  label: 'Unhealthy ⚠️', stat: '#f87171' };
    }
    function applyColor(c) {
      w.style.setProperty('--aqi-color', c.hex); w.style.setProperty('--aqi-color-alpha', c.alpha);
      var circle = document.getElementById('aqiCircle');
      circle.style.background = c.hex; circle.style.boxShadow = '0 0 20px ' + c.alpha;
      document.getElementById('aqiPM25').style.color = c.stat;
      document.getElementById('aqiPM10').style.color = c.stat;
    }
    async function fetchAQI() {
      try {
        var res = await fetch(C.AQI_URL, { headers: { Accept: 'application/json' } });
        if (!res.ok) throw new Error();
        var data = await res.json();
        if (data.status === 'ok') {
          var aqi = data.data.aqi, iaqi = data.data.iaqi || {};
          var c = aqiColor(aqi);
          document.getElementById('dotAqiVal').textContent = aqi;
          document.getElementById('aqiValue').textContent = aqi;
          document.getElementById('aqiPM25').textContent = (iaqi.pm25 && iaqi.pm25.v != null) ? iaqi.pm25.v : 'N/A';
          document.getElementById('aqiPM10').textContent = (iaqi.pm10 && iaqi.pm10.v != null) ? iaqi.pm10.v : 'N/A';
          document.getElementById('aqiCardTime').textContent = new Date().toLocaleTimeString('en-US', { hour: '2-digit', minute: '2-digit' });
          document.getElementById('aqiLabel').textContent = c.label;
          applyColor(c);
        } else { document.getElementById('aqiLabel').textContent = 'No data'; }
      } catch (e) { document.getElementById('aqiLabel').textContent = 'Offline'; }
    }
    fetchAQI(); setInterval(fetchAQI, 60000);
    window.toggleAQI = function () {
      expanded = !expanded;
      document.getElementById('aqiCard').classList.toggle('open', expanded);
      w.classList.toggle('expanded', expanded);
    };
    window.dismissAQI = function (e) {
      e.stopPropagation();
      document.getElementById('aqiCard').classList.remove('open'); expanded = false; w.classList.remove('expanded');
      setTimeout(function () { w.style.display = 'none'; }, 350);
    };
  })();

  /* ── AI chatbot ──────────────────────────────────────────── */
  (function () {
    if (!document.getElementById('chatbotWidget')) return;
    var chatOpen = false, chatHistory = [];
    window.toggleChat = function () {
      chatOpen = !chatOpen;
      document.getElementById('chatWindow').classList.toggle('open', chatOpen);
    };
    function escapeHtml(s) { var d = document.createElement('div'); d.textContent = s; return d.innerHTML; }
    function renderMarkdown(text) {
      return escapeHtml(text)
        .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
        .replace(/^- (.+)/gm, '<li style="margin-left:12px;list-style:disc">$1</li>')
        .replace(/(<li.*<\/li>)/s, '<ul style="margin:4px 0">$1</ul>')
        .replace(/\n\n/g, '<br><br>').replace(/\n/g, '<br>');
    }
    function addMessage(text, role) {
      var container = document.getElementById('chatMessages');
      var isBot = role === 'assistant';
      var div = document.createElement('div');
      div.className = 'flex gap-2' + (isBot ? '' : ' justify-end');
      div.innerHTML = isBot
        ? '<div class="w-7 h-7 bg-bp-light rounded-full flex items-center justify-center flex-shrink-0 mt-1"><i class="fas fa-robot text-bp-primary text-xs"></i></div><div class="chat-msg bot">' + renderMarkdown(text) + '</div>'
        : '<div class="chat-msg user">' + escapeHtml(text) + '</div>';
      container.appendChild(div); container.scrollTop = container.scrollHeight;
    }
    function showTyping() {
      var c = document.getElementById('chatMessages');
      var div = document.createElement('div');
      div.id = 'typingIndicator'; div.className = 'flex gap-2';
      div.innerHTML = '<div class="w-7 h-7 bg-bp-light rounded-full flex items-center justify-center flex-shrink-0"><i class="fas fa-robot text-bp-primary text-xs"></i></div><div class="chat-msg bot typing-indicator"><span></span><span></span><span></span></div>';
      c.appendChild(div); c.scrollTop = c.scrollHeight;
    }
    function hideTyping() { var t = document.getElementById('typingIndicator'); if (t) t.remove(); }
    window.sendChat = async function () {
      var input = document.getElementById('chatInput');
      var text = input.value.trim(); if (!text) return;
      input.value = '';
      document.getElementById('quickReplies').style.display = 'none';
      addMessage(text, 'user'); chatHistory.push({ role: 'user', content: text });
      showTyping();
      try {
        var res = await fetch(C.CHAT_URL, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ message: text }) });
        var data = await res.json();
        hideTyping();
        var reply = data.reply || "I'm sorry, I couldn't process that. Please email " + C.EMAIL + '.';
        chatHistory.push({ role: 'assistant', content: reply });
        addMessage(reply, 'assistant');
      } catch (e) {
        hideTyping();
        addMessage("Sorry, I'm having trouble connecting. Please email " + C.EMAIL, 'assistant');
      }
    };
    window.sendQuick = function (msg) { document.getElementById('chatInput').value = msg; sendChat(); };
  })();

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

  /* ── Logo ticker ─────────────────────────────────────────── */
  (function () {
    var track = document.getElementById('logoTrack'); if (!track) return;
    var LOGOS = [
      { name: 'Saudi Aramco',       url: 'https://upload.wikimedia.org/wikipedia/en/a/af/Saudi_Aramco_logo.svg' },
      { name: 'SABIC',              url: 'https://upload.wikimedia.org/wikipedia/en/a/af/Sabic_logo.svg' },
      { name: 'NEOM',               url: 'https://upload.wikimedia.org/wikipedia/en/6/61/NEOM_logo.svg' },
      { name: 'ACWA Power',         url: 'https://upload.wikimedia.org/wikipedia/en/7/70/ACWA_Power_logo.svg' },
      { name: 'Siemens',            url: 'https://upload.wikimedia.org/wikipedia/commons/5/5f/Siemens_logo.svg' },
      { name: 'GE',                 url: 'https://upload.wikimedia.org/wikipedia/en/6/6f/General_Electric_logo.svg' },
      { name: 'Schneider Electric', url: 'https://upload.wikimedia.org/wikipedia/en/7/75/Schneider_Electric_logo.svg' },
      { name: 'Masdar',             url: 'https://upload.wikimedia.org/wikipedia/en/2/2a/Masdar_logo.svg' },
      { name: 'Veolia',             url: 'https://upload.wikimedia.org/wikipedia/commons/0/06/Veolia_logo.svg' },
      { name: 'SGS',                url: 'https://upload.wikimedia.org/wikipedia/en/9/92/SGS_logo.svg' },
      { name: 'Bureau Veritas',     url: 'https://upload.wikimedia.org/wikipedia/en/b/b3/Bureau_Veritas_logo.svg' },
      { name: 'Intertek',           url: 'https://upload.wikimedia.org/wikipedia/commons/4/48/Intertek_logo.svg' }
    ];
    var html = '';
    for (var cycle = 0; cycle < 2; cycle++) {
      LOGOS.forEach(function (l) {
        html += '<div class="logo-item" title="' + l.name + '"><img src="' + l.url + '" alt="' + l.name + '" loading="lazy" onerror="this.parentElement.innerHTML=\'<span>' + l.name + '</span>\'"></div>';
      });
    }
    track.innerHTML = html;
  })();
})();
