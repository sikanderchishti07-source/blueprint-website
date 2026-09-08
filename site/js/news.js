/* ============================================================
   BluePrint — news.js
   Environmental news bulletin: GNews API (optional) → static
   fallback. Auto-refresh countdown, topic filters, ticker.
   ============================================================ */
(function () {
  'use strict';
  if (!document.getElementById('news-grid')) return;
  var C = window.BP_CONFIG || {};

  /* Escape text before putting it into innerHTML. Article fields come
     from an external news API, so they are never trusted as markup. */
  function esc(s) {
    return String(s == null ? '' : s)
      .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;').replace(/'/g, '&#39;');
  }

  var TOPIC_IMAGES = {
    air:        ['https://images.unsplash.com/photo-1611273426858-450d8e3c9fce?w=800&q=80', 'https://images.unsplash.com/photo-1569952266837-07ce4f964a5e?w=800&q=80', 'https://images.unsplash.com/photo-1504711434969-e33886168f5c?w=800&q=80'],
    water:      ['https://images.unsplash.com/photo-1505118380757-91f5f5632de0?w=800&q=80', 'https://images.unsplash.com/photo-1583212292454-1fe6229603b7?w=800&q=80', 'https://images.unsplash.com/photo-1559825481-12a05cc00344?w=800&q=80'],
    climate:    ['https://images.unsplash.com/photo-1470071459604-3b5ec3a7fe05?w=800&q=80', 'https://images.unsplash.com/photo-1547683905-f686c993aae5?w=800&q=80', 'https://images.unsplash.com/photo-1504711434969-e33886168f5c?w=800&q=80'],
    energy:     ['https://images.unsplash.com/photo-1509391366360-2e959784a276?w=800&q=80', 'https://images.unsplash.com/photo-1466611653911-95081537e5b7?w=800&q=80', 'https://images.unsplash.com/photo-1548337138-e87d889cc369?w=800&q=80'],
    green:      ['https://images.unsplash.com/photo-1542601906990-b4d3fb778b09?w=800&q=80', 'https://images.unsplash.com/photo-1518531933037-91b2f5f229cc?w=800&q=80', 'https://images.unsplash.com/photo-1501854140801-50d01698950b?w=800&q=80'],
    regulation: ['https://images.unsplash.com/photo-1450101499163-c8848c66ca85?w=800&q=80', 'https://images.unsplash.com/photo-1568992687947-868a62a9f521?w=800&q=80', 'https://images.unsplash.com/photo-1521791136064-7986c2920216?w=800&q=80'],
    default:    ['https://images.unsplash.com/photo-1446776811953-b23d57bd21aa?w=800&q=80', 'https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?w=800&q=80', 'https://images.unsplash.com/photo-1500534314209-a25ddb2bd429?w=800&q=80']
  };
  var CATEGORIES = {
    air:        { label: '💨 Air Quality',    bg: 'rgba(0, 113, 129,.13)',  color: '#007181', imgKey: 'air' },
    water:      { label: '💧 Water',          bg: 'rgba(0, 113, 129,.11)',  color: '#005a66', imgKey: 'water' },
    climate:    { label: '🌡 Climate',        bg: 'rgba(160,80,20,.11)',  color: '#a05014', imgKey: 'climate' },
    energy:     { label: '⚡ Energy',         bg: 'rgba(100,117,66,.15)', color: '#4d5a33', imgKey: 'energy' },
    regulation: { label: '📋 Regulation',     bg: 'rgba(0, 113, 129,.11)',  color: '#007181', imgKey: 'regulation' },
    green:      { label: '🌱 Sustainability', bg: 'rgba(100,117,66,.15)', color: '#647542', imgKey: 'green' },
    default:    { label: '🌍 Environment',    bg: 'rgba(100,117,66,.12)', color: '#647542', imgKey: 'default' }
  };
  var FALLBACK_ARTICLES = [
    { title: 'Saudi Arabia Expands National Air Quality Monitoring Network Under Vision 2030', description: 'NCEC has commissioned 28 new ambient air quality stations across Jubail, Yanbu, Riyadh, and Dammam industrial zones.', url: 'https://ncec.gov.sa', source: { name: 'NCEC Saudi Arabia' }, publishedAt: new Date().toISOString(), image: null },
    { title: 'Saudi Green Initiative Surpasses 1 Billion Tree Planting Milestone Ahead of Schedule', description: "Saudi Arabia's afforestation programme has exceeded its first-year target across Tabuk, Al Qassim, and the Eastern Province.", url: 'https://www.greeninitiatives.gov.sa', source: { name: 'Saudi Green Initiative' }, publishedAt: new Date(Date.now() - 86400000).toISOString(), image: null },
    { title: 'Red Sea Global Secures Environmental Clearance for Phase Two Coastal Development', description: 'Red Sea Global secured EIA approvals incorporating marine protected area protocols and coral reef preservation.', url: 'https://www.redseaglobal.com', source: { name: 'Red Sea Global' }, publishedAt: new Date(Date.now() - 172800000).toISOString(), image: null },
    { title: 'WHO Air Quality Guidelines Prompt GCC Nations to Review Industrial Emission Standards', description: 'Environmental regulators across the GCC are aligning national emission thresholds with updated WHO parameters.', url: 'https://www.arabnews.com', source: { name: 'Arab News' }, publishedAt: new Date(Date.now() - 259200000).toISOString(), image: null },
    { title: 'NEOM Unveils Zero-Carbon Desalination Plant Powered by Solar and Wind', description: "NEOM unveiled plans for the world's largest renewable-powered desalination facility supplying 100 million litres daily.", url: 'https://www.neom.com', source: { name: 'NEOM' }, publishedAt: new Date(Date.now() - 345600000).toISOString(), image: null },
    { title: 'Aramco Reports 23% Reduction in Operational Carbon Intensity Ahead of 2030 Target', description: "Saudi Aramco's sustainability report documents methane intensity at a historic low with carbon capture at full capacity.", url: 'https://www.aramco.com/en/sustainability', source: { name: 'Saudi Aramco' }, publishedAt: new Date(Date.now() - 432000000).toISOString(), image: null }
  ];

  var allArticles = [], activeFilter = 'all', refreshTimer = null, countdownTimer = null, nextRefresh = null;

  function getCategory(a) {
    var t = ((a.title || '') + ' ' + (a.description || '')).toLowerCase();
    if (/air|pm2\.5|emission|smog/.test(t))          return CATEGORIES.air;
    if (/water|desalin|marine|sea/.test(t))          return CATEGORIES.water;
    if (/climate|carbon|co2|drought/.test(t))        return CATEGORIES.climate;
    if (/solar|renewable|wind|energy/.test(t))       return CATEGORIES.energy;
    if (/regulat|complia|policy|standard/.test(t))   return CATEGORIES.regulation;
    if (/green|sustainab|tree|forest/.test(t))       return CATEGORIES.green;
    return CATEGORIES.default;
  }
  /* Only allow http(s) links through to href — a feed should never
     be able to inject a javascript: URL. */
  function safeUrl(u) {
    var v = String(u || '');
    return /^https?:\/\//i.test(v) ? esc(v) : '#';
  }
  function getImage(a, i) { if (a.image && a.image.startsWith('http')) return a.image; var pool = TOPIC_IMAGES[getCategory(a).imgKey] || TOPIC_IMAGES.default; return pool[i % pool.length]; }
  function getFallbackImage(a, i) { var pool = TOPIC_IMAGES[getCategory(a).imgKey] || TOPIC_IMAGES.default; return pool[(i + 1) % pool.length]; }
  function timeAgo(d) {
    var s = Math.floor((Date.now() - new Date(d)) / 1000);
    if (s < 60) return s + 's ago'; if (s < 3600) return Math.floor(s / 60) + 'm ago';
    if (s < 86400) return Math.floor(s / 3600) + 'h ago'; return Math.floor(s / 86400) + 'd ago';
  }
  function fetchWithTimeout(url, ms) {
    var ctrl = new AbortController(); var t = setTimeout(function () { ctrl.abort(); }, ms || 8000);
    return fetch(url, { signal: ctrl.signal }).finally(function () { clearTimeout(t); });
  }

  async function fetchNews() {
    if (C.GNEWS_API_KEY) {
      try {
        var q = encodeURIComponent('Saudi Arabia environment OR "air quality" OR sustainability OR "green initiative" OR climate');
        var res = await fetchWithTimeout('https://gnews.io/api/v4/search?q=' + q + '&lang=en&max=' + C.NEWS_ARTICLE_COUNT + '&apikey=' + C.GNEWS_API_KEY);
        if (res.ok) { var data = await res.json(); if (data.articles && data.articles.length) return data.articles; }
      } catch (e) { /* fall through to static articles */ }
    }
    return FALLBACK_ARTICLES;
  }

  function renderTicker(articles) {
    var track = document.getElementById('ticker-track'); if (!track || !articles.length) return;
    var items = articles.concat(articles);
    track.innerHTML = items.map(function (a) {
      return '<span class="ticker-item"><span class="tk-arrow">▶</span><span>' + esc(a.title) + '</span><span class="tk-time">' + timeAgo(a.publishedAt) + '</span></span>';
    }).join('');
  }
  function filterArticles(a) {
    if (activeFilter === 'all') return a;
    return a.filter(function (x) { return ((x.title || '') + ' ' + (x.description || '')).toLowerCase().indexOf(activeFilter) !== -1; });
  }
  function renderCard(a, i) {
    var cat = getCategory(a), img = getImage(a, i), fb = getFallbackImage(a, i);
    return '<div class="news-card' + (i === 0 ? ' featured' : '') + '">' +
      '<div class="card-img-wrap"><img src="' + esc(img) + '" alt="' + esc(a.title) + '" loading="lazy" onerror="this.onerror=null;this.src=\'' + fb + '\'" /><div class="card-img-overlay"></div>' +
      '<span class="card-badge" style="background:' + cat.bg + ';color:' + cat.color + ';">' + cat.label + '</span><span class="card-source">' + esc((a.source && a.source.name) || 'News') + '</span></div>' +
      '<div class="card-body"><h3 class="card-title">' + esc(a.title) + '</h3><p class="card-desc">' + esc(a.description || 'Read the full article for details.') + '</p>' +
      '<div class="card-footer"><span class="card-time">' + timeAgo(a.publishedAt) + '</span><a href="' + safeUrl(a.url) + '" target="_blank" rel="noopener" class="read-more">Read More <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg></a></div></div></div>';
  }
  function renderGrid() {
    var grid = document.getElementById('news-grid'); if (!grid) return;
    var filtered = filterArticles(allArticles);
    grid.innerHTML = filtered.length ? filtered.map(renderCard).join('')
      : '<div style="grid-column:1/-1;text-align:center;padding:60px 20px;"><div style="font-size:2rem;margin-bottom:10px;">🔍</div><div class="font-display" style="font-size:1.1rem;color:var(--bp-text);">No articles match this filter</div></div>';
    var sources = []; filtered.forEach(function (a) { var n = a.source && a.source.name; if (n && sources.indexOf(n) === -1) sources.push(n); });
    document.getElementById('stat-count').textContent = filtered.length;
    document.getElementById('stat-sources').textContent = sources.length;
  }

  window.loadNews = async function () {
    var $sk = document.getElementById('skeleton-grid'), $gr = document.getElementById('news-grid'), $er = document.getElementById('news-error'), $ic = document.getElementById('refresh-icon'), $up = document.getElementById('last-updated');
    if ($ic) $ic.style.animation = 'spin 1s linear infinite';
    $sk.style.display = 'grid'; $gr.style.display = 'none'; $er.style.display = 'none';
    try {
      allArticles = await fetchNews();
      renderTicker(allArticles);
      $sk.style.display = 'none'; $gr.style.display = 'grid'; renderGrid();
      if ($up) $up.textContent = 'Updated ' + new Date().toLocaleTimeString('en-SA', { hour: '2-digit', minute: '2-digit' });
    } catch (err) {
      allArticles = FALLBACK_ARTICLES;
      $sk.style.display = 'none'; $gr.style.display = 'grid'; renderGrid(); $er.style.display = 'block';
    } finally { if ($ic) $ic.style.animation = ''; }
    clearInterval(refreshTimer); clearInterval(countdownTimer);
    nextRefresh = Date.now() + C.NEWS_REFRESH_MS;
    refreshTimer = setInterval(loadNews, C.NEWS_REFRESH_MS);
    countdownTimer = setInterval(function () {
      var rem = Math.max(0, nextRefresh - Date.now());
      var el = document.getElementById('next-refresh-label');
      if (el) el.textContent = 'Next refresh in: ' + Math.floor(rem / 60000) + 'm ' + String(Math.floor((rem % 60000) / 1000)).padStart(2, '0') + 's';
    }, 1000);
  };

  document.querySelectorAll('.filter-pill').forEach(function (btn) {
    btn.addEventListener('click', function () {
      document.querySelectorAll('.filter-pill').forEach(function (b) { b.classList.remove('active'); });
      btn.classList.add('active'); activeFilter = btn.dataset.topic; renderGrid();
    });
  });
  loadNews();
})();
