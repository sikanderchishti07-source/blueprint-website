// Starts the GitHub OAuth flow for the Decap CMS editor at /admin.
module.exports = (req, res) => {
  const clientId = process.env.OAUTH_CLIENT_ID;
  if (!clientId) {
    res.status(500).send('OAUTH_CLIENT_ID is not set in the Vercel environment variables.');
    return;
  }
  const host = req.headers['x-forwarded-host'] || req.headers.host;
  const proto = req.headers['x-forwarded-proto'] || 'https';
  const url =
    'https://github.com/login/oauth/authorize' +
    '?client_id=' + encodeURIComponent(clientId) +
    '&scope=repo' +
    '&redirect_uri=' + encodeURIComponent(proto + '://' + host + '/api/callback');
  res.writeHead(301, { Location: url });
  res.end();
};
