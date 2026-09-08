/* ============================================================
   BluePrint — portal.js
   Client portal: Client-ID login → dashboard with real reports.
   ============================================================ */
(function () {
  'use strict';
  var C = window.BP_CONFIG || {};

  /* Escape any value coming from the API or from user input before it
     goes into innerHTML. */
  function esc(s) {
    return String(s == null ? '' : s)
      .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;').replace(/'/g, '&#39;');
  }
  /* Only allow http(s) file links through to href/src. */
  function safeUrl(u) {
    var v = String(u || '');
    return /^https?:\/\//i.test(v) ? esc(v) : '';
  }

  function loginMarkup() {
    return '<div id="portalLogin" style="padding:40px; max-width:420px; margin:0 auto;">' +
      '<button onclick="closeModal(\'portalModal\')" class="modal-close-btn" style="position:absolute; top:20px; right:20px;" aria-label="Close"><i class="fas fa-times"></i></button>' +
      '<div style="text-align:center; margin-bottom:32px;">' +
        '<img src="assets/logo/blueprint-mark.png" alt="BluePrint" style="height:64px; width:auto; margin:0 auto 16px; display:block;" />' +
        '<h2 style="font-family:var(--font-display); font-size:24px; font-weight:800; color:var(--bp-blue-ink); margin-bottom:8px;">Client Portal</h2>' +
        '<p style="color:#6b7280; font-size:14px;">Access your environmental reports and compliance documents</p>' +
      '</div>' +
      '<div style="margin-bottom:24px;">' +
        '<label for="portalClientId" style="display:block; font-size:14px; font-weight:500; color:#374151; margin-bottom:8px;">Client ID</label>' +
        '<input type="text" id="portalClientId" placeholder="Enter your Client ID" style="width:100%; padding:12px 16px; border:1px solid #d1d5db; border-radius:12px; font-size:16px; box-sizing:border-box;" />' +
      '</div>' +
      '<button id="portalLoginBtn" onclick="doLogin()" style="width:100%; padding:14px; background:var(--bp-blue); color:white; border:none; border-radius:12px; font-size:16px; font-weight:600; cursor:pointer; font-family:var(--font-display);">Access Portal</button>' +
      '<p style="text-align:center; margin-top:16px; font-size:12px; color:#9ca3af;">Contact BluePrint to get your Client ID</p>' +
    '</div>';
  }

  window.openPortal = function () {
    openModal('portalModal');
    var box = document.querySelector('#portalModal .modal-box');
    box.innerHTML = loginMarkup();
    var input = document.getElementById('portalClientId');
    input.addEventListener('keydown', function (e) { if (e.key === 'Enter') doLogin(); });
    setTimeout(function () { input.focus(); }, 50);
  };

  window.doLogin = async function () {
    var clientId = document.getElementById('portalClientId').value.trim().toUpperCase();
    if (!clientId) { alert('Please enter your Client ID'); return; }
    var button = document.getElementById('portalLoginBtn');
    if (button) { button.textContent = 'Connecting...'; button.disabled = true; }
    try {
      var response = await fetch(C.CLIENT_VALIDATE, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ clientId: clientId }) });
      var result = await response.json();
      if (response.ok && result.valid && result.client) {
        showDashboardUI(result.client.companyName || clientId, clientId);
        setTimeout(function () { loadDashboardData(clientId); }, 100);
      } else {
        alert('Client ID not found: ' + clientId + '\n\nPlease check your Client ID and try again.');
      }
    } catch (error) {
      console.error('Login error:', error);
      alert('Connection error. Please try again later.');
    } finally {
      if (button) { button.textContent = 'Access Portal'; button.disabled = false; }
    }
  };

  function navItem(id, icon, label, active) {
    return '<div id="nav-' + id + '" onclick="switchSection(\'' + id + '\')" class="portal-nav' + (active ? ' active' : '') + '"><i class="fas ' + icon + '" style="font-size:15px; width:20px; text-align:center;"></i><span style="font-size:14px; font-weight:500;">' + label + '</span></div>';
  }

  window.showDashboardUI = function (companyName, clientId) {
    var box = document.querySelector('#portalModal .modal-box');
    box.innerHTML =
      '<style>' +
        '.portal-nav{padding:14px 16px;border-radius:12px;margin-bottom:6px;cursor:pointer;color:rgba(255,255,255,.6);display:flex;align-items:center;gap:14px;transition:all .2s;border:1px solid transparent;}' +
        '.portal-nav:hover{background:rgba(255,255,255,.08);color:#fff;}' +
        '.portal-nav.active{background:rgba(255,255,255,.12);color:#fff;border-color:rgba(255,255,255,.08);}' +
        '.portal-stat{background:#fff;padding:24px;border-radius:16px;box-shadow:0 1px 3px rgba(0,0,0,.08);border:1px solid #e2e8f0;position:relative;overflow:hidden;}' +
        '@media(max-width:820px){.portal-side{display:none!important;}.portal-stats{grid-template-columns:1fr!important;}}' +
      '</style>' +
      '<div style="display:flex; min-height:700px; max-height:85vh; background:#f0f4f8;">' +
        '<div class="portal-side" style="width:280px; background:linear-gradient(180deg, #007181 0%, #04333a 100%); display:flex; flex-direction:column; flex-shrink:0;">' +
          '<div style="padding:24px; border-bottom:1px solid rgba(255,255,255,.08);"><img src="assets/logo/blueprint-logo-white.png" alt="BluePrint" style="height:40px; width:auto;" /></div>' +
          '<div style="margin:20px 16px; padding:16px; background:rgba(255,255,255,.08); border-radius:14px; border:1px solid rgba(255,255,255,.06);">' +
            '<div style="display:flex; align-items:center; gap:12px;">' +
              '<div style="width:42px; height:42px; background:var(--bp-grad-olive); border-radius:50%; display:flex; align-items:center; justify-content:center; font-weight:700; font-size:16px; color:white;">' + esc(companyName.charAt(0).toUpperCase()) + '</div>' +
              '<div style="flex:1; min-width:0;"><div style="font-weight:600; font-size:14px; color:white; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;">' + esc(companyName) + '</div><div style="font-size:11px; color:rgba(255,255,255,.5); margin-top:2px;">' + esc(clientId) + '</div></div>' +
              '<div style="width:8px; height:8px; background:#10b981; border-radius:50%; box-shadow:0 0 8px rgba(16,185,129,.6);"></div>' +
            '</div>' +
          '</div>' +
          '<div style="padding:8px 16px; flex:1;">' +
            '<div style="font-size:10px; color:rgba(255,255,255,.35); text-transform:uppercase; letter-spacing:1.2px; font-weight:600; padding:0 12px; margin-bottom:12px;">Menu</div>' +
            navItem('overview', 'fa-th-large', 'Dashboard', true) +
            navItem('reports', 'fa-folder-open', 'My Reports', false) +
          '</div>' +
          '<div style="padding:16px; border-top:1px solid rgba(255,255,255,.08);">' +
            '<div onclick="logoutPortal()" class="portal-nav"><i class="fas fa-arrow-right-from-bracket" style="font-size:15px; width:20px; text-align:center;"></i><span style="font-size:14px; font-weight:500;">Sign Out</span></div>' +
          '</div>' +
        '</div>' +
        '<div style="flex:1; display:flex; flex-direction:column; overflow:hidden; min-width:0;">' +
          '<div style="padding:20px 32px; background:white; border-bottom:1px solid #e2e8f0; display:flex; justify-content:space-between; align-items:center; flex-shrink:0;">' +
            '<div><h1 id="page-title" style="font-family:var(--font-display); font-size:24px; font-weight:700; color:#1e293b; margin:0; letter-spacing:-.5px;">Dashboard</h1><p id="page-subtitle" style="font-size:13px; color:#64748b; margin:4px 0 0 0;">Overview of your environmental reports</p></div>' +
            '<div style="display:flex; align-items:center; gap:12px;">' +
              '<div style="padding:10px 16px; background:#f1f5f9; border-radius:10px; font-size:12px; color:#64748b;"><i class="fas fa-calendar" style="margin-right:8px;"></i>' + new Date().toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' }) + '</div>' +
              '<button onclick="closeModal(\'portalModal\')" class="modal-close-btn" aria-label="Close"><i class="fas fa-times"></i></button>' +
            '</div>' +
          '</div>' +
          '<div style="flex:1; padding:28px 32px; overflow-y:auto; background:#f0f4f8;">' +
            '<div id="dash-overview">' +
              '<div style="background:var(--bp-grad); border-radius:20px; padding:32px 36px; margin-bottom:28px; position:relative; overflow:hidden; box-shadow:0 10px 40px rgba(4, 51, 58,.3);">' +
                '<div style="position:absolute; top:-50px; right:-50px; width:200px; height:200px; background:rgba(255,255,255,.05); border-radius:50%;"></div>' +
                '<div style="position:relative; z-index:1;">' +
                  '<div style="display:flex; align-items:center; gap:8px; margin-bottom:12px;"><div style="width:8px; height:8px; background:#10b981; border-radius:50%;"></div><span style="font-size:12px; color:rgba(255,255,255,.7); text-transform:uppercase; letter-spacing:1px; font-weight:600;">Welcome Back</span></div>' +
                  '<h2 style="font-family:var(--font-display); font-size:28px; font-weight:700; color:white; margin:0 0 8px 0; letter-spacing:-.5px;">Hello, ' + esc(companyName) + '! 👋</h2>' +
                  '<p style="font-size:15px; color:rgba(255,255,255,.75); margin:0; max-width:500px; line-height:1.6;">Access your environmental monitoring reports, track compliance status, and download documentation all in one place.</p>' +
                '</div>' +
              '</div>' +
              '<div class="portal-stats" style="display:grid; grid-template-columns:repeat(3, 1fr); gap:20px; margin-bottom:28px;">' +
                statCard('Total Reports', '<span id="stat-reports">-</span>', 'var(--bp-blue)', 'fa-file-lines', 'var(--bp-grad-blue)', '<i class="fas fa-arrow-up" style="font-size:10px;"></i> Available', '#10b981') +
                statCard('Portal Status', 'Active', '#10b981', 'fa-shield-halved', 'linear-gradient(135deg,#10b981,#059669)', '<i class="fas fa-circle" style="font-size:6px;"></i> Online', '#10b981') +
                statCard('Support', '24/7', 'var(--bp-olive)', 'fa-headset', 'var(--bp-grad-olive)', '<i class="fas fa-headset" style="font-size:10px;"></i> Available', 'var(--bp-olive)') +
              '</div>' +
              '<div style="background:white; border-radius:16px; padding:24px; box-shadow:0 1px 3px rgba(0,0,0,.08); border:1px solid #e2e8f0;">' +
                '<div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:20px;">' +
                  '<div style="display:flex; align-items:center; gap:12px;"><div style="width:40px; height:40px; background:var(--bp-olive-tint); border-radius:10px; display:flex; align-items:center; justify-content:center;"><i class="fas fa-clock-rotate-left" style="color:var(--bp-olive); font-size:16px;"></i></div><div><h3 style="font-size:16px; font-weight:700; color:#1e293b; margin:0;">Recent Reports</h3><p style="font-size:12px; color:#64748b; margin:2px 0 0 0;">Your latest environmental reports</p></div></div>' +
                  '<button onclick="switchSection(\'reports\')" style="padding:10px 18px; background:#f1f5f9; border:none; border-radius:10px; font-size:13px; color:#475569; cursor:pointer; font-weight:600; display:flex; align-items:center; gap:6px;">View All <i class="fas fa-arrow-right" style="font-size:11px;"></i></button>' +
                '</div>' +
                '<div id="recent-activity" style="color:#64748b; font-size:14px;">' + spinner('Loading reports...') + '</div>' +
              '</div>' +
            '</div>' +
            '<div id="dash-reports" style="display:none;"><div id="reports-list" style="color:#64748b; font-size:14px;">' + spinner('Loading your reports...') + '</div></div>' +
          '</div>' +
        '</div>' +
      '</div>';
    window.currentClientId = clientId;
  };

  function statCard(label, value, color, icon, grad, sub, subColor) {
    return '<div class="portal-stat"><div style="display:flex; align-items:flex-start; justify-content:space-between;"><div>' +
      '<div style="font-size:13px; color:#64748b; font-weight:500; margin-bottom:8px;">' + label + '</div>' +
      '<div style="font-family:var(--font-display); font-size:36px; font-weight:800; color:' + color + '; letter-spacing:-1px; line-height:1;">' + value + '</div>' +
      '<div style="font-size:12px; color:' + subColor + '; margin-top:8px; display:flex; align-items:center; gap:4px;">' + sub + '</div></div>' +
      '<div style="width:52px; height:52px; background:' + grad + '; border-radius:14px; display:flex; align-items:center; justify-content:center;"><i class="fas ' + icon + '" style="color:white; font-size:22px;"></i></div></div></div>';
  }
  function spinner(text) {
    return '<div style="display:flex; align-items:center; justify-content:center; padding:40px;"><div style="text-align:center;"><div style="width:48px; height:48px; background:#f1f5f9; border-radius:50%; display:flex; align-items:center; justify-content:center; margin:0 auto 12px;"><i class="fas fa-spinner fa-spin" style="font-size:20px; color:var(--bp-blue);"></i></div><p style="margin:0; color:#64748b;">' + text + '</p></div></div>';
  }

  window.loadDashboardData = async function (clientId) {
    var backendUrl = C.API_BASE;
    function getFileUrl(path) { if (!path) return ''; if (path.startsWith('http')) return path; return backendUrl + path; }
    try {
      var res = await fetch(C.REPORTS_URL + clientId);
      var data = await res.json();
      var reports = data.reports || [];
      var statEl = document.getElementById('stat-reports'); if (statEl) statEl.textContent = reports.length;

      var recentEl = document.getElementById('recent-activity');
      if (recentEl) {
        if (!reports.length) {
          recentEl.innerHTML = '<div style="text-align:center; padding:40px 20px;"><div style="width:64px; height:64px; background:#f1f5f9; border-radius:50%; display:flex; align-items:center; justify-content:center; margin:0 auto 16px;"><i class="fas fa-inbox" style="font-size:24px; color:#94a3b8;"></i></div><p style="margin:0; color:#64748b; font-size:14px; font-weight:500;">No reports uploaded yet</p><p style="margin:8px 0 0 0; color:#94a3b8; font-size:12px;">Reports will appear here when available</p></div>';
        } else {
          var grads = ['var(--bp-grad-blue)', 'linear-gradient(135deg,#10b981,#059669)', 'var(--bp-grad-olive)'];
          recentEl.innerHTML = '<div style="display:flex; flex-direction:column; gap:10px;">' + reports.slice(0, 3).map(function (r, idx) {
            var title = r.reportTitle || r.title || 'Report', type = r.reportType || '', loc = r.location || '';
            var date = r.reportDate ? new Date(r.reportDate).toLocaleDateString('en-US', { month: 'short', day: 'numeric' }) : '';
            title = esc(title); type = esc(type); loc = esc(loc);
            return '<div onclick="switchSection(\'reports\')" style="background:#f8fafc; padding:16px 18px; border-radius:12px; display:flex; align-items:center; gap:14px; cursor:pointer; border:1px solid #e2e8f0;">' +
              '<div style="width:46px; height:46px; background:' + grads[idx % 3] + '; border-radius:12px; display:flex; align-items:center; justify-content:center; flex-shrink:0;"><i class="fas fa-file-lines" style="color:white; font-size:18px;"></i></div>' +
              '<div style="flex:1; min-width:0;"><p style="font-size:14px; font-weight:600; color:#1e293b; margin:0; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;">' + title + '</p><p style="font-size:12px; color:#64748b; margin:4px 0 0 0;"><span style="background:#e2e8f0; padding:2px 8px; border-radius:4px; font-size:11px; font-weight:500;">' + type + '</span> <span style="margin-left:8px;"><i class="fas fa-location-dot" style="margin-right:4px; font-size:10px;"></i>' + loc + '</span></p></div>' +
              '<div style="text-align:right; flex-shrink:0;"><div style="font-size:11px; color:#94a3b8; font-weight:500;">' + date + '</div><i class="fas fa-chevron-right" style="color:#cbd5e1; font-size:12px; margin-top:6px;"></i></div></div>';
          }).join('') + '</div>';
        }
      }

      var reportsEl = document.getElementById('reports-list');
      if (reportsEl) {
        if (!reports.length) {
          reportsEl.innerHTML = '<div style="text-align:center; padding:80px 40px; background:white; border-radius:20px; border:1px solid #e2e8f0;"><div style="width:88px; height:88px; background:linear-gradient(135deg,#f1f5f9,#e2e8f0); border-radius:50%; display:flex; align-items:center; justify-content:center; margin:0 auto 24px;"><i class="fas fa-folder-open" style="font-size:36px; color:#94a3b8;"></i></div><h3 style="color:#1e293b; margin:0 0 8px 0; font-size:20px; font-weight:700;">No Reports Yet</h3><p style="color:#64748b; font-size:14px; max-width:300px; margin:0 auto;">Your environmental reports will appear here once they are uploaded by the BluePrint team.</p></div>';
        } else {
          reportsEl.innerHTML = '<div style="display:flex; flex-direction:column; gap:20px;">' + reports.map(function (r, idx) {
            var title = esc(r.reportTitle || r.title || 'Untitled Report'), type = esc(r.reportType || 'Report'), loc = esc(r.location || '');
            var raw = r.issueDate || r.reportDate || '';
            var date = raw ? new Date(raw).toLocaleDateString('en-US', { year: 'numeric', month: 'short', day: 'numeric' }) : '';
            var pdfUrl = (r.files && r.files.pdfReport) ? safeUrl(getFileUrl(r.files.pdfReport)) : '';
            var images = [];
            if (r.files) ['stationImages', 'noiseImages', 'coordinateImages'].forEach(function (k) { if (r.files[k]) images = images.concat(r.files[k].map(getFileUrl).map(safeUrl).filter(Boolean)); });
            var downloadBtn = pdfUrl
              ? '<a href="' + pdfUrl + '" target="_blank" rel="noopener" style="background:var(--bp-grad-blue); color:white; padding:12px 24px; border-radius:12px; font-size:13px; text-decoration:none; display:inline-flex; align-items:center; gap:10px; font-weight:600; box-shadow:0 4px 14px rgba(0, 113, 129,.35);"><i class="fas fa-download"></i> Download PDF</a>'
              : '<span style="color:#94a3b8; font-size:13px; background:#f1f5f9; padding:12px 24px; border-radius:12px; font-weight:500;">No PDF available</span>';
            var html = '<div style="background:white; border-radius:20px; overflow:hidden; box-shadow:0 1px 3px rgba(0,0,0,.08); border:1px solid #e2e8f0;">' +
              '<div style="background:var(--bp-grad-blue); padding:24px 28px; color:white; position:relative; overflow:hidden;">' +
                '<div style="display:flex; align-items:center; gap:10px; margin-bottom:10px;"><span style="background:rgba(255,255,255,.2); padding:4px 12px; border-radius:6px; font-size:11px; font-weight:600; text-transform:uppercase; letter-spacing:.5px;">Report #' + (idx + 1) + '</span><span style="background:rgba(16,185,129,.3); color:#a7f3d0; padding:4px 10px; border-radius:6px; font-size:10px; font-weight:600;"><i class="fas fa-check" style="margin-right:4px;"></i>Published</span></div>' +
                '<h3 style="font-family:var(--font-display); font-size:20px; font-weight:700; margin:0 0 12px 0; letter-spacing:-.3px;">' + title + '</h3>' +
                '<div style="display:flex; flex-wrap:wrap; gap:16px; font-size:13px; color:rgba(255,255,255,.85);"><span><i class="fas fa-tag" style="font-size:11px; opacity:.7; margin-right:6px;"></i>' + type + '</span><span><i class="fas fa-location-dot" style="font-size:11px; opacity:.7; margin-right:6px;"></i>' + loc + '</span><span><i class="fas fa-calendar" style="font-size:11px; opacity:.7; margin-right:6px;"></i>' + date + '</span></div>' +
              '</div><div style="padding:24px 28px;">';
            if (images.length) {
              html += '<div style="margin-bottom:24px;"><div style="display:flex; align-items:center; gap:10px; margin-bottom:14px;"><div style="width:32px; height:32px; background:#f1f5f9; border-radius:8px; display:flex; align-items:center; justify-content:center;"><i class="fas fa-images" style="font-size:14px; color:#64748b;"></i></div><span style="font-size:13px; color:#475569; font-weight:600;">Attached Images</span><span style="background:#e2e8f0; padding:2px 8px; border-radius:4px; font-size:11px; color:#64748b; font-weight:600;">' + images.length + '</span></div><div style="display:grid; grid-template-columns:repeat(auto-fill, minmax(110px, 1fr)); gap:10px;">';
              images.forEach(function (imgUrl) { html += '<a href="' + imgUrl + '" target="_blank" rel="noopener" style="display:block; aspect-ratio:4/3; border-radius:12px; overflow:hidden; border:2px solid #e2e8f0;"><img src="' + imgUrl + '" alt="" style="width:100%; height:100%; object-fit:cover;" onerror="this.parentElement.style.display=\'none\'" /></a>'; });
              html += '</div></div>';
            }
            html += '<div style="display:flex; justify-content:space-between; align-items:center; padding-top:16px; border-top:1px solid #e2e8f0; flex-wrap:wrap; gap:12px;"><div style="font-size:12px; color:#94a3b8;"><i class="fas fa-info-circle" style="margin-right:6px;"></i>Click to download the full report</div>' + downloadBtn + '</div></div></div>';
            return html;
          }).join('') + '</div>';
        }
      }
    } catch (err) {
      console.error('Failed to load dashboard data:', err);
      var msg = '<div style="text-align:center; padding:40px; color:#ef4444;"><i class="fas fa-exclamation-circle" style="font-size:32px; margin-bottom:12px; display:block;"></i><p style="margin:0;">Failed to load reports. Please try again.</p></div>';
      var a = document.getElementById('recent-activity'); if (a) a.innerHTML = msg;
      var b = document.getElementById('reports-list');    if (b) b.innerHTML = msg;
    }
  };

  window.switchSection = function (section) {
    ['overview', 'reports'].forEach(function (s) {
      var sec = document.getElementById('dash-' + s); if (sec) sec.style.display = s === section ? 'block' : 'none';
      var nav = document.getElementById('nav-' + s);  if (nav) nav.classList.toggle('active', s === section);
    });
    var t = document.getElementById('page-title'), st = document.getElementById('page-subtitle');
    if (section === 'overview') { t.textContent = 'Dashboard'; st.textContent = 'Overview of your environmental reports'; }
    else { t.textContent = 'My Reports'; st.textContent = 'View and download your environmental monitoring reports'; }
  };

  window.logoutPortal = function () { closeModal('portalModal'); };
})();
