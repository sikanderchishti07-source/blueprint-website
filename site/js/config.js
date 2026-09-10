/* ============================================================
   BluePrint — config.js
   Single source of truth for contact details and API endpoints.
   Edit the values here; every page and widget reads from this.
   ============================================================ */
window.BP_CONFIG = {
  COMPANY_NAME:   'BluePrint Environmental Services',
  COMPANY_SHORT:  'BluePrint',

  // Contact details taken from the client's live site (blueprint-env.com).
  // NOTE: their site shows two numbers — +966 54 347 0109 (about/services/blog)
  // and +966 59 000 0000 (home/contact, evidently a placeholder). Confirm which is correct.
  PHONE_DISPLAY:  '+966 54 347 0109',
  PHONE_TEL:      '+966543470109',
  WHATSAPP:       '966543470109',          // digits only, country code first
  EMAIL:          'info@blueprint-env.com',
  ADDRESS_LINE1:  'Riyadh, Saudi Arabia',
  ADDRESS_LINE2:  'Sunday &ndash; Thursday, 9:00&ndash;18:00 AST',
  WEBSITE:        'www.blueprint-env.com',

  // Backend endpoints (same services the previous single-file site used)
  API_BASE:       'https://aecon-backend.onrender.com',
  BOOKINGS_URL:   'https://aecon-backend.onrender.com/api/bookings',
  CLIENT_VALIDATE:'https://aecon-backend.onrender.com/api/clients/validate',
  REPORTS_URL:    'https://aecon-backend.onrender.com/api/reports/',
  AQI_URL:        '/api/aqi',
  CHAT_URL:       '/api/chat',

  // News bulletin
  GNEWS_API_KEY:  '',                      // optional; static fallback is used when empty
  NEWS_ARTICLE_COUNT: 6,
  NEWS_REFRESH_MS: 45 * 60 * 1000
};
