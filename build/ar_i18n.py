# Shared engine for the Arabic pages.
#
# Each Arabic page is built from its English page: the English HTML is
# rendered, then word maps swap the text. Layout stays in one place, so a
# layout change in English flows into Arabic automatically.
#
# Three kinds of map entry:
#   TEXT  text between two tags, matched as a whole text node
#   ATTR  alt, aria-label, title and placeholder values
#   RAW   exact markup, for the rare case a straight word swap is not enough
#
# After translating, any visible English left on the page is printed as
# "untranslated", so a sentence added in English later never slips through.

import re
import html as _html

# technical terms, standards, software and brand names that stay in Latin script
ALLOWED = {
    "NCEC", "MWAN", "IAS", "RCJY", "ISO", "AQI", "US", "EPA", "PM", "PM2", "PM10", "NO", "SO", "CO",
    "VOCs", "COD", "BOD", "L90", "eq", "EIA", "ESIA", "CEMP", "EMP", "ESG", "GHG", "UTC",
    "BluePrint", "LEED", "BREEAM", "AERMOD", "CALPUFF", "DHI", "MIKE", "CORMIX", "HEC", "RAS", "HMS",
    "WMS", "Civil", "3D", "ArcGIS", "MODFLOW", "SoundPlan", "RFYB3704", "GCC", "KSA", "Sikander", "Chishti",
    "info", "blueprint", "env", "com",
}


def _node_pattern(en):
    words = en.split()
    return re.compile(r">(\s*)" + r"\s+".join(re.escape(w) for w in words) + r"(\s*)<")


def translate(html, text=(), attr=(), raw=()):
    missing = []
    for en, ar in raw:
        if en in html:
            html = html.replace(en, ar)
        else:
            missing.append(("raw", en))
    for en, ar in sorted(text, key=lambda p: -len(p[0])):
        html, n = _node_pattern(en).subn(lambda m: ">" + m.group(1) + ar + m.group(2) + "<", html)
        if not n:
            missing.append(("text", en))
    for en, ar in attr:
        pat = re.compile(r'((?:alt|aria-label|title|placeholder)=")' + re.escape(en) + '"')
        html, n = pat.subn(lambda m: m.group(1) + ar + '"', html)
        if not n:
            missing.append(("attr", en))
    return html, missing


def untranslated(html, extra_allowed=()):
    allowed = ALLOWED | set(extra_allowed)
    body = re.sub(r"<script.*?</script>", "", html, flags=re.S)
    body = re.sub(r"<!--.*?-->", "", body, flags=re.S)
    left = []
    for m in re.finditer(r">([^<>]+)<", body):
        s = " ".join(_html.unescape(m.group(1)).split())
        words = [w.strip(".") for w in re.findall(r"[A-Za-z][A-Za-z0-9.]*", s)]
        if [w for w in words if w not in allowed and len(w) > 1]:
            left.append(s)
    return sorted(set(left))


def build(name, en_html, page, common=((), (), ()), extra_allowed=()):
    """page and common are (TEXT, ATTR, RAW). Page entries that no longer match
    the English page are reported; common entries are expected to be partial."""
    html, missing = translate(en_html, *page)
    for kind, s in missing:
        print("  [%s] no longer on the English page (%s): %s" % (name, kind, s[:70]))
    html, _ = translate(html, *common)
    html = fill_runtime_text(html)
    for s in untranslated(html, extra_allowed):
        print("  [%s] untranslated: %s" % (name, s[:90]))
    return html

# Text that config.js would otherwise fill in English at runtime. On Arabic
# pages it is written in directly and the hook removed, so the script leaves it.
AR_ADDRESS = ('3704 أبي جعفر المنصور، حي اليرموك، الرياض <span dir="ltr">13251-7669</span>، '
              'المملكة العربية السعودية<br>الأحد &ndash; الخميس &middot; 9:00 &ndash; 18:00')


def fill_runtime_text(html):
    return re.sub(r'(<(\w+)[^>]*?) data-text="address"([^>]*)></\2>',
                  lambda m: m.group(1) + m.group(3) + ">" + AR_ADDRESS + "</" + m.group(2) + ">", html)
