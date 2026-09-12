// Exchanges the GitHub code for a token and hands it back to the Decap editor.
module.exports = async (req, res) => {
  const clientId = process.env.OAUTH_CLIENT_ID;
  const clientSecret = process.env.OAUTH_CLIENT_SECRET;
  const code = (req.query && req.query.code) || '';

  const finish = (status, payload) => {
    const body =
      '<!doctype html><html><body><script>' +
      '(function(){' +
      'function post(){window.opener&&window.opener.postMessage(' +
      JSON.stringify('authorization:github:' + status + ':' + JSON.stringify(payload)) +
      ',"*");}' +
      'window.addEventListener("message",post,{once:true});' +
      'post();' +
      '})();' +
      '</script><p>You can close this window.</p></body></html>';
    res.setHeader('Content-Type', 'text/html');
    res.status(200).send(body);
  };

  if (!clientId || !clientSecret) {
    finish('error', { message: 'OAuth environment variables are missing on Vercel.' });
    return;
  }
  if (!code) {
    finish('error', { message: 'GitHub did not return a code.' });
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
      finish('error', { message: data.error_description || 'GitHub refused the token request.' });
      return;
    }
    finish('success', { token: data.access_token, provider: 'github' });
  } catch (e) {
    finish('error', { message: String(e) });
  }
};
