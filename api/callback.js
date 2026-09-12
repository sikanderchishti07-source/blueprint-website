// Exchanges the GitHub code for a token and hands it back to the Decap editor.
module.exports = async (req, res) => {
  const clientId = process.env.OAUTH_CLIENT_ID;
  const clientSecret = process.env.OAUTH_CLIENT_SECRET;
  const code = (req.query && req.query.code) || '';

  const reply = (status, payload) => {
    const message = 'authorization:github:' + status + ':' + JSON.stringify(payload);
    const body =
      '<!doctype html><html><body><p>Signing you in...</p><script>' +
      '(function(){' +
      'var msg=' + JSON.stringify(message) + ';' +
      'function receive(e){' +
      'window.removeEventListener("message",receive,false);' +
      'window.opener.postMessage(msg, e.origin || "*");' +
      'setTimeout(function(){window.close();},600);' +
      '}' +
      'window.addEventListener("message",receive,false);' +
      'window.opener.postMessage("authorizing:github","*");' +
      '})();' +
      '</script></body></html>';
    res.setHeader('Content-Type', 'text/html');
    res.status(200).send(body);
  };

  if (!clientId || !clientSecret) {
    reply('error', { message: 'OAuth environment variables are missing on Vercel.' });
    return;
  }
  if (!code) {
    reply('error', { message: 'GitHub did not return a code.' });
    return;
  }

  try {
    const r = await fetch('https://github.com/login/oauth/access_token', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', Accept: 'application/json' },
      body: JSON.stringify({ client_id: clientId, client_secret: clientSecret, code: code }),
    });
    const data = await r.json();
    if (data.error || !data.access_token) {
      reply('error', { message: data.error_description || 'GitHub refused the token request.' });
      return;
    }
    reply('success', { token: data.access_token, provider: 'github' });
  } catch (e) {
    reply('error', { message: String(e) });
  }
};
