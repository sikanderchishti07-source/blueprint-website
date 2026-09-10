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
  blog.html                 The compliance briefing — article listing
  blog-<slug>.html          Five article pages (one full, four awaiting copy)
  privacy.html              Privacy Policy
  terms.html                Terms & Conditions
  index_arabic.html         Arabic (RTL) home page
  assets/logo/              blueprint-logo.png, blueprint-logo-white.png, blueprint-mark.png, favicon.png
  css/
    tailwind.css            Compiled Tailwind utilities (generated — do not edit by hand)
    base.css                Design tokens (colours, fonts), resets, buttons, modals, page-header band
    layout.css              Navbar, dropdowns, mobile drawer, footer
    components.css          Calculator, chatbot, AQI widget, WhatsApp, expert CTA, logo ticker, cards
    pages.css               Interactive services, news bulletin, article copy, responsive tweaks
    rtl.css                 Right-to-left overrides — loaded only by index_arabic.html
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
  pages.py                  main page bodies
  pages_extra.py            blog listing, article template, privacy & terms
  home_new.py               home page content
  content_new.py            service, laboratory and accreditation data
  arabic.py                 the whole Arabic page (its own nav + footer)
  build.py                  assembles site/*.html
  tailwind.config.js        brand colours (bp-ink, bp-dark, bp-primary, bp-soft, bp-light, bp-olive, bp-sage, bp-green)
  build.sh                  python3 build.py + tailwind compile
```

## Brand palette

A teal family (client-approved), with the olive and green taken from the logo.

| Token            | Hex       | Use                                   |
|------------------|-----------|---------------------------------------|
| `--bp-blue`      | `#007181` | Primary — buttons, links, accents     |
| `--bp-blue-deep` | `#005a66` | Headings on light, dark sections      |
| `--bp-blue-ink`  | `#04333a` | Footer, top strip, deepest surfaces   |
| `--bp-blue-soft` | `#2a93a3` | Secondary accents                     |
| `--bp-olive`     | `#647542` | Secondary — olive buttons, checks     |
| `--bp-olive-light` | `#a3b56f` | Highlight on dark backgrounds (replaces old gold) |
| `--bp-green-ink` | `#102e20` | Body text                             |

## Before going live

1. **`js/config.js`** — replace the placeholders: `PHONE_DISPLAY`, `PHONE_TEL`, `WHATSAPP` (digits only), `EMAIL`, `ADDRESS_LINE1/2`, `WEBSITE`. Every phone/email/WhatsApp link on the site is populated from here.
2. **Backend** — `API_BASE`, `BOOKINGS_URL`, `CLIENT_VALIDATE`, `REPORTS_URL` still point at `aecon-backend.onrender.com`; `AQI_URL` and `CHAT_URL` are relative (`/api/aqi`, `/api/chat`) and need a proxy or absolute URL on the host.
3. **Company facts still unconfirmed** — the AECON template's claims (founded 2014, 1000+ projects, 50+ specialists, offices in Jeddah/Dammam/Cairo/Milan, ISO/IEC 17025, and the NEOM/Qiddiya/Red Sea client list) have all been **removed** because they do not appear on the client's own site. If the owner confirms any of them for BluePrint, they can be added back.
4. **Blog articles** — `blog-mwan-waste-permit-guide.html` carries full copy. The other four show a short "being prepared" note; drop their text into `ARTICLE_BODIES` in `build/pages_extra.py` and rebuild.
5. **Arabic** — `index_arabic.html` is a complete RTL home page. The inner pages (services, laboratory, blog, contact) are English only; the language switch on those pages points to the Arabic home.
5. **Optional** — `GNEWS_API_KEY` in config.js enables live news; otherwise the curated fallback articles show. Social links in the footer are `#`.

## Editing shared markup

**The five HTML files in `site/` are generated — do not edit them by hand.** Each one starts with a warning comment saying so. Nav, footer, modals and widgets appear on every page; edit them once in `build/partials.py`, then rebuild:

```bash
cd build
npm install            # first time only (installs Tailwind CLI)
./build.sh             # regenerates site/*.html and site/css/tailwind.css
```

The CSS and JS files in `site/css/` and `site/js/` are *not* generated and are safe to edit directly — except `site/css/tailwind.css`. After adding new Tailwind utility classes to any markup, re-run just the Tailwind step:

```bash
npx tailwindcss -c tailwind.config.js -i tailwind.input.css -o ../site/css/tailwind.css --minify
```

To change the palette later, edit the `--bp-*` tokens at the top of `site/css/base.css` **and** the matching `bp` colours in `build/tailwind.config.js`, then run `build/build.sh`.
