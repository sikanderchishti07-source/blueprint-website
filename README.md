# BluePrint Environmental Services — Website

Multi-page static site rebuilt from the AECON Premium v22.1 single-file template, rebranded for BluePrint with a colour scheme taken directly from the BluePrint logo.

## Structure

```
site/                       ← deploy this folder (Vercel / Netlify / any static host)
  index.html                Home: hero, stats, overview, services preview, methodology, clients, why choose
  services.html             Interactive split-panel services (6 service lines, deep-links #svc-0 … #svc-5)
  technology.html           Equipment cards + compliance standards (#equipment, #standards)
  resources.html            Free tools cards, live AQI card, news bulletin (#tools, #aqi, #env-news-section)
  contact.html              Contact details + consultation form
  assets/logo/              blueprint-logo.png, blueprint-logo-white.png, blueprint-mark.png, favicon.png
  css/
    tailwind.css            Compiled Tailwind utilities (generated — do not edit by hand)
    base.css                Design tokens (colours, fonts), resets, buttons, modals, page-header band
    layout.css              Navbar, dropdowns, mobile drawer, footer
    components.css          Calculator, chatbot, AQI widget, WhatsApp, expert CTA, logo ticker, cards
    pages.css               Interactive services, news bulletin, responsive widget tweaks
  js/
    config.js               ★ Contact details + API endpoints — edit this first
    main.js                 Navbar, drawer, scroll reveal, modals, particles, contact injection
    tools.js                Booking modal, compliance checker, carbon calculator
    portal.js               Client portal (Client-ID login → dashboard → reports)
    widgets.js              AQI widget, chatbot, WhatsApp, expert CTA, logo ticker
    services.js             Services page only
    news.js                 Resources page only

build/                      ← source of the shared markup; optional
  partials.py               head / nav / footer / modals / widgets (shared by every page)
  pages.py                  page bodies
  build.py                  assembles site/*.html
  tailwind.config.js        brand colours (bp-ink, bp-dark, bp-primary, bp-soft, bp-light, bp-olive, bp-sage, bp-green)
  build.sh                  python3 build.py + tailwind compile
```

## Brand palette (from the logo)

| Token            | Hex       | Use                                   |
|------------------|-----------|---------------------------------------|
| `--bp-blue`      | `#0f3db2` | Primary — buttons, links, accents     |
| `--bp-blue-deep` | `#0a2a7a` | Headings on light, dark sections      |
| `--bp-blue-ink`  | `#071d55` | Footer, top strip, deepest surfaces   |
| `--bp-olive`     | `#647542` | Secondary — olive buttons, checks     |
| `--bp-olive-light` | `#a3b56f` | Highlight on dark backgrounds (replaces old gold) |
| `--bp-green-ink` | `#102e20` | Body text                             |

## Before going live

1. **`js/config.js`** — replace the placeholders: `PHONE_DISPLAY`, `PHONE_TEL`, `WHATSAPP` (digits only), `EMAIL`, `ADDRESS_LINE1/2`, `WEBSITE`. Every phone/email/WhatsApp link on the site is populated from here.
2. **Backend** — `API_BASE`, `BOOKINGS_URL`, `CLIENT_VALIDATE`, `REPORTS_URL` still point at `aecon-backend.onrender.com`; `AQI_URL` and `CHAT_URL` are relative (`/api/aqi`, `/api/chat`) and need a proxy or absolute URL on the host.
3. **Company facts inherited from the AECON template** — verify or change: "since 2014", 10+ years, 1000+ projects, 50+ specialists, 5 offices (Riyadh · Jeddah · Dammam · Cairo · Milan), ISO/IEC 17025 & ISO 14001, NCEC certification, the client/project list, and the logo ticker brands.
4. **Arabic** — links to `index_arabic.html` are kept in the nav/footer but the page is not included.
5. **Optional** — `GNEWS_API_KEY` in config.js enables live news; otherwise the curated fallback articles show. Social links in the footer are `#`.

## Editing shared markup

Nav, footer, modals and widgets appear on every page. Edit them once in `build/partials.py`, then rebuild:

```bash
cd build
npm install            # first time only (installs Tailwind CLI)
./build.sh             # regenerates site/*.html and site/css/tailwind.css
```

If you edit HTML files directly instead, re-run only the Tailwind step after adding new utility classes:

```bash
npx tailwindcss -c tailwind.config.js -i tailwind.input.css -o ../site/css/tailwind.css --minify
```
