/* ============================================================
   BluePrint - config.js
   Single source of truth for the company's contact details.
   Edit the values here; every page and widget reads from this.
   ============================================================ */
window.BP_CONFIG = {
  COMPANY_NAME:   'BluePrint Environmental Services',
  COMPANY_SHORT:  'BluePrint',

  // Contact details taken from the client's live site (blueprint-env.com).
  // NOTE: their site shows two numbers - +966 54 347 0109 (about/services/blog)
  // and +966 59 000 0000 (home/contact, evidently a placeholder). Confirm which is correct.
  PHONE_DISPLAY:  '+966 54 347 0109',
  PHONE_TEL:      '+966543470109',
  WHATSAPP:       '966543470109',          // digits only, country code first
  EMAIL:          'info@blueprint-env.com',
  ADDRESS_LINE1:  '3704 Abi Jafar Al Mansur, Al Yarmouk District, Riyadh 13251-7669, Saudi Arabia',
  ADDRESS_LINE2:  'Sunday &ndash; Thursday, 9:00&ndash;18:00 AST',
  WEBSITE:        'www.blueprint-env.com',

  // Google Analytics 4. Loaded only after the visitor accepts the cookie banner (js/consent.js).
  GA_ID:          'G-YB0RQ9K2S1',

  // Footer map. Use the office's exact coordinates ('24.7,46.7') or an address.
  MAP_QUERY:      '3704 Abi Jafar Al Mansur, Al Yarmouk, Riyadh 13251, Saudi Arabia'

};
