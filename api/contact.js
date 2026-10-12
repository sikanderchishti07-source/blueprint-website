/* BluePrint website: contact form endpoint (Vercel serverless function).
   POST /api/contact  ->  emails the enquiry to the company and (optionally) creates an Odoo CRM lead.

   Settings live in Vercel (Project > Settings > Environment Variables), never in the code:
     SMTP_USER       mailbox that sends the email, e.g. website@blueprint-env.com
     SMTP_PASS       that mailbox's password
     SMTP_HOST       default smtp.hostinger.com
     SMTP_PORT       default 465 (SSL)
     MAIL_TO         who receives enquiries, default info@blueprint-env.com (comma-separate for several)
   Odoo (optional, either way):
     ODOO_LEAD_EMAIL  an Odoo email alias that turns emails into leads, added as an extra recipient
     or the API: ODOO_URL (https://x.odoo.com), ODOO_DB, ODOO_USER (login email), ODOO_API_KEY
   Until SMTP_USER/SMTP_PASS are set the endpoint answers 503 and the page falls back to WhatsApp. */

const tls = require('tls');

const LIMITS = { name: 120, company: 160, email: 160, phone: 40, service: 120, message: 4000, page: 200, lang: 4 };
const hits = new Map();   // simple per-instance rate limit: 5 per IP per 10 minutes

function clean(v, n) { return String(v == null ? '' : v).replace(/[\u0000-\u0008\u000b\u000c\u000e-\u001f]/g, '').trim().slice(0, n); }
function esc(s) { return s.replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c])); }
function hdr(s) { return '=?UTF-8?B?' + Buffer.from(s, 'utf8').toString('base64') + '?='; }

function smtpSend({ host, port, user, pass, from, to, replyTo, subject, text, html }) {
  return new Promise((resolve, reject) => {
    const boundary = 'bp' + Date.now().toString(36);
    const body = [
      'From: ' + hdr('BluePrint Website') + ' <' + from + '>',
      'To: ' + to.join(', '),
      replyTo ? 'Reply-To: ' + replyTo : null,
      'Subject: ' + hdr(subject),
      'Date: ' + new Date().toUTCString(),
      'MIME-Version: 1.0',
      'Content-Type: multipart/alternative; boundary="' + boundary + '"',
      '', '--' + boundary, 'Content-Type: text/plain; charset=UTF-8', 'Content-Transfer-Encoding: base64', '',
      Buffer.from(text, 'utf8').toString('base64').replace(/.{76}/g, '$&\r\n'),
      '--' + boundary, 'Content-Type: text/html; charset=UTF-8', 'Content-Transfer-Encoding: base64', '',
      Buffer.from(html, 'utf8').toString('base64').replace(/.{76}/g, '$&\r\n'),
      '--' + boundary + '--', ''
    ].filter(l => l !== null).join('\r\n');

    const steps = [
      [null, 220],
      ['EHLO blueprint-env.com', 250],
      ['AUTH LOGIN', 334],
      [Buffer.from(user).toString('base64'), 334],
      [Buffer.from(pass).toString('base64'), 235],
      ['MAIL FROM:<' + from + '>', 250],
      ...to.map(r => ['RCPT TO:<' + r + '>', 250]),
      ['DATA', 354],
      [body.replace(/\r\n\./g, '\r\n..') + '\r\n.', 250],
      ['QUIT', 221]
    ];
    let i = 0, buf = '', done = false;
    const sock = tls.connect({ host, port, servername: host }, () => {});
    const fail = e => { if (!done) { done = true; sock.destroy(); reject(e); } };
    sock.setTimeout(15000, () => fail(new Error('SMTP timeout')));
    sock.on('error', fail);
    sock.on('data', d => {
      buf += d.toString('utf8');
      if (!/(^|\r\n)\d{3} [^\r\n]*\r\n$/.test(buf)) return;   // wait for the last line of a reply
      const last = buf.trim().split('\r\n').pop(); buf = '';
      const want = steps[i][1];
      if (parseInt(last.slice(0, 3), 10) !== want) return fail(new Error('SMTP ' + last));
      i++;
      if (i >= steps.length) { done = true; sock.end(); return resolve(); }
      sock.write(steps[i][0] + '\r\n');
    });
  });
}

async function odooLead(f, env) {
  const url = env.ODOO_URL.replace(/\/$/, '') + '/jsonrpc';
  const call = async (service, method, args) => {
    const r = await fetch(url, { method: 'POST', headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ jsonrpc: '2.0', method: 'call', params: { service, method, args }, id: Date.now() }) });
    const j = await r.json();
    if (j.error) throw new Error('Odoo: ' + (j.error.data && j.error.data.message || j.error.message));
    return j.result;
  };
  const uid = await call('common', 'login', [env.ODOO_DB, env.ODOO_USER, env.ODOO_API_KEY]);
  if (!uid) throw new Error('Odoo login failed');
  const desc = [f.message, '', 'Service: ' + (f.service || '-'), 'Page: ' + (f.page || '-'), 'Language: ' + f.lang].join('\n');
  return call('object', 'execute_kw', [env.ODOO_DB, uid, env.ODOO_API_KEY, 'crm.lead', 'create', [{
    name: 'Website: ' + (f.service || 'Enquiry') + ' - ' + (f.company || f.name),
    contact_name: f.name, partner_name: f.company || false, email_from: f.email || false, phone: f.phone || false,
    description: desc, type: 'lead'
  }]]);
}

module.exports = async (req, res) => {
  res.setHeader('Cache-Control', 'no-store');
  if (req.method !== 'POST') { res.statusCode = 405; return res.end(JSON.stringify({ ok: false })); }
  const env = process.env;
  const json = (code, obj) => { res.statusCode = code; res.setHeader('Content-Type', 'application/json'); res.end(JSON.stringify(obj)); };

  const origin = req.headers.origin || '';
  if (origin && !/^https:\/\/(www\.)?blueprint-env\.com$|\.vercel\.app$|^http:\/\/localhost(:\d+)?$/.test(origin)) return json(403, { ok: false });

  const ip = String(req.headers['x-forwarded-for'] || '').split(',')[0].trim() || 'x';
  const now = Date.now(), list = (hits.get(ip) || []).filter(t => now - t < 600000);
  if (list.length >= 5) return json(429, { ok: false, error: 'rate' });
  list.push(now); hits.set(ip, list);

  let b = req.body;
  if (typeof b === 'string') { try { b = JSON.parse(b); } catch (e) { b = {}; } }
  b = b || {};
  if (b.website) return json(200, { ok: true });            // honeypot filled: a bot, pretend success
  if (b.t && now - Number(b.t) < 3000) return json(200, { ok: true });   // sent faster than a human can type

  const f = {}; for (const k in LIMITS) f[k] = clean(b[k], LIMITS[k]);
  if (!f.name || (!f.email && !f.phone)) return json(400, { ok: false, error: 'missing' });
  if (f.email && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(f.email)) return json(400, { ok: false, error: 'email' });

  if (!env.SMTP_USER || !env.SMTP_PASS) return json(503, { ok: false, error: 'not-configured' });

  const to = (env.MAIL_TO || 'info@blueprint-env.com').split(',').map(s => s.trim()).filter(Boolean);
  if (env.ODOO_LEAD_EMAIL) to.push(env.ODOO_LEAD_EMAIL.trim());
  const rows = [['Name', f.name], ['Company', f.company], ['Email', f.email], ['Phone', f.phone], ['Service', f.service],
    ['Language', f.lang === 'ar' ? 'Arabic' : 'English'], ['Page', f.page]].filter(r => r[1]);
  const subject = 'Website enquiry: ' + (f.service || 'General') + ' - ' + (f.company || f.name);
  const text = rows.map(r => r[0] + ': ' + r[1]).join('\n') + '\n\nMessage:\n' + (f.message || '-');
  const html = '<div style="font-family:Arial,sans-serif;font-size:14px;color:#0b2f38">' +
    '<h2 style="color:#078f88;margin:0 0 12px">New website enquiry</h2><table cellpadding="6" style="border-collapse:collapse">' +
    rows.map(r => '<tr><td style="color:#5a6b72;padding-right:16px">' + r[0] + '</td><td><b>' + esc(r[1]) + '</b></td></tr>').join('') +
    '</table><p style="margin:16px 0 4px;color:#5a6b72">Message</p><div style="white-space:pre-wrap;background:#f3f6f7;padding:12px;border-radius:8px">' +
    esc(f.message || '-') + '</div></div>';

  let mailed = false, odoo = false;
  try {
    await smtpSend({ host: env.SMTP_HOST || 'smtp.hostinger.com', port: +(env.SMTP_PORT || 465), user: env.SMTP_USER, pass: env.SMTP_PASS,
      from: env.SMTP_USER, to, replyTo: f.email || null, subject, text, html });
    mailed = true;
  } catch (e) { console.error('mail', e.message); }
  if (env.ODOO_URL && env.ODOO_DB && env.ODOO_USER && env.ODOO_API_KEY) {
    try { await odooLead(f, env); odoo = true; } catch (e) { console.error('odoo', e.message); }
  }
  if (!mailed && !odoo) return json(502, { ok: false, error: 'send' });
  return json(200, { ok: true });
};
