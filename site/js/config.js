/* ============================================================
   BluePrint — config.js
   Single source of truth for contact details and API endpoints.
   Edit the values here; every page and widget reads from this.
   ============================================================ */
window.BP_CONFIG = {
  COMPANY_NAME:   'BluePrint Environmental Services',
  COMPANY_SHORT:  'BluePrint',

  // TODO: replace placeholders with the real BluePrint details
  PHONE_DISPLAY:  '+966 5X XXX XXXX',
  PHONE_TEL:      '+9665XXXXXXXX',
  WHATSAPP:       '9665XXXXXXXX',          // digits only, country code first
  EMAIL:          'info@blueprint-es.com',
  ADDRESS_LINE1:  'Office address line 1',
  ADDRESS_LINE2:  'Riyadh, Kingdom of Saudi Arabia',
  WEBSITE:        'www.blueprint-es.com',

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
