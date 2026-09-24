# Link-preview images and favicon set for the BluePrint site.
#
#   python make_og.py
#
# Writes, under site/:
#   assets/og/<page>.jpg      1200x630 preview image per page (page photo + logo)
#   assets/og/default.jpg     branded card, used by any page without its own
#   favicon.ico               16/32/48 px, the file browsers ask for first
#   assets/icons/*.png        32px tab icon, Apple home-screen icon, Android icons
#
# The images carry no text: WhatsApp, LinkedIn and X print the page title and
# description under the image, so one image serves both languages.
#
# Run it again after adding a page or changing a hero photo. Needs Pillow
# (pip install pillow). Not part of the normal build.

import os
import re
import io
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.normpath(os.path.join(HERE, "..", "site"))
OG = os.path.join(SITE, "assets", "og")
ICONS = os.path.join(SITE, "assets", "icons")
LOGO_WHITE = os.path.join(SITE, "assets", "logo", "blueprint-logo-white.png")
MARK = os.path.join(SITE, "assets", "logo", "blueprint-mark.png")

W, H = 1200, 630
INK, DEEP = (11, 47, 56), (10, 111, 128)

# pages whose content has no photo, or where another photo suits better
CHOSEN = {
    "index": "cover-1-1920.webp",
    "services": "cover-2-1920.webp",
    "contact": "cover-4-1920.webp",
    "compliance": "feature-2.jpg",
    "equipment": "feature-3.jpg",
    "careers": "svc-field-monitoring-hero.webp",
}
BRAND_CARD = {"privacy", "terms"}


def cover(im, w, h):
    """Scale and centre-crop to exactly w x h."""
    im = im.convert("RGB")
    s = max(w / im.width, h / im.height)
    im = im.resize((round(im.width * s), round(im.height * s)), Image.LANCZOS)
    x, y = (im.width - w) // 2, (im.height - h) // 2
    return im.crop((x, y, x + w, y + h))


def shade(im):
    """Darken the lower left so the white logo reads on any photo."""
    grad = Image.new("L", (W, H), 0)
    d = ImageDraw.Draw(grad)
    for y in range(H):
        t = max(0.0, (y - H * 0.45) / (H * 0.55))
        d.line([(0, y), (W, y)], fill=int(170 * t ** 1.3))
    dark = Image.new("RGB", (W, H), INK)
    return Image.composite(dark, im, grad)


def put_logo(im, width, pos):
    logo = Image.open(LOGO_WHITE).convert("RGBA")
    logo = logo.resize((width, round(logo.height * width / logo.width)), Image.LANCZOS)
    base = im.convert("RGBA")
    x = pos[0] if pos[0] >= 0 else (W - logo.width) // 2
    y = pos[1] if pos[1] >= 0 else H - logo.height + pos[1]
    base.alpha_composite(logo, (x, y))
    return base.convert("RGB")


def brand_card():
    im = Image.new("RGB", (W, H), INK)
    d = ImageDraw.Draw(im)
    for x in range(W):
        t = x / W
        d.line([(x, 0), (x, H)], fill=tuple(round(INK[i] + (DEEP[i] - INK[i]) * t * 0.9) for i in range(3)))
    logo = Image.open(LOGO_WHITE).convert("RGBA")
    lw = 560
    logo = logo.resize((lw, round(logo.height * lw / logo.width)), Image.LANCZOS)
    base = im.convert("RGBA")
    base.alpha_composite(logo, ((W - lw) // 2, (H - logo.height) // 2))
    return base.convert("RGB")


def first_photo(html):
    main = html[html.find("<main>"):html.find("</main>")]
    m = re.search(r"""(?:url\(['"]?|<img[^>]+src=")(?:\.\./)?assets/img/([^'")\s]+\.(?:webp|jpg|jpeg|png))""", main)
    return m.group(1) if m else None


def save_jpg(im, path):
    im.save(path, "JPEG", quality=80, optimize=True, progressive=True)


def make_previews():
    os.makedirs(OG, exist_ok=True)
    save_jpg(brand_card(), os.path.join(OG, "default.jpg"))
    made = 0
    for f in sorted(os.listdir(SITE)):
        if not f.endswith(".html"):
            continue
        stem = f[:-5]
        if stem in BRAND_CARD:
            continue                     # these use default.jpg
        src = CHOSEN.get(stem)
        if not src:
            with io.open(os.path.join(SITE, f), encoding="utf-8") as fh:
                src = first_photo(fh.read())
        path = os.path.join(SITE, "assets", "img", src) if src else None
        if not path or not os.path.exists(path):
            continue                     # falls back to default.jpg
        im = shade(cover(Image.open(path), W, H))
        save_jpg(put_logo(im, 300, (56, -44)), os.path.join(OG, stem + ".jpg"))
        made += 1
    print("preview images:", made, "+ default.jpg in", OG)


def square_mark(size, pad, bg=None):
    mark = Image.open(MARK).convert("RGBA")
    inner = round(size * (1 - 2 * pad))
    s = inner / max(mark.width, mark.height)
    mark = mark.resize((max(1, round(mark.width * s)), max(1, round(mark.height * s))), Image.LANCZOS)
    canvas = Image.new("RGBA", (size, size), bg or (0, 0, 0, 0))
    canvas.alpha_composite(mark, ((size - mark.width) // 2, (size - mark.height) // 2))
    return canvas


def make_icons():
    os.makedirs(ICONS, exist_ok=True)
    square_mark(32, 0.04).save(os.path.join(ICONS, "favicon-32.png"))
    square_mark(180, 0.12, (255, 255, 255, 255)).convert("RGB").save(os.path.join(ICONS, "apple-touch-icon.png"))
    square_mark(192, 0.12, (255, 255, 255, 255)).save(os.path.join(ICONS, "icon-192.png"))
    square_mark(512, 0.12, (255, 255, 255, 255)).save(os.path.join(ICONS, "icon-512.png"))
    big = square_mark(256, 0.04)
    big.save(os.path.join(SITE, "favicon.ico"), sizes=[(16, 16), (32, 32), (48, 48)])
    print("favicon.ico and icons written")


if __name__ == "__main__":
    make_previews()
    make_icons()
