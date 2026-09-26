"""Join the hand-written stylesheets into site/css/site.css and minify it safely.
Order matters (later files win), so it follows the order the pages used to load them.
The minifier only removes comments and extra spaces; it never touches text inside quotes.
"""
import os, re

FILES = ["base.css", "layout.css", "components.css", "pages.css", "cover.css", "carousel.css", "insights.css"]


def _minify(css):
    out, i, n = [], 0, len(css)
    while i < n:
        c = css[i]
        if c in "\"'":                       # keep quoted text exactly
            j = i + 1
            while j < n and css[j] != c:
                j += 2 if css[j] == "\\" else 1
            out.append(css[i:j + 1]); i = j + 1
        elif css.startswith("/*", i):        # drop comments
            j = css.find("*/", i + 2); i = n if j < 0 else j + 2
        elif c.isspace():                    # squeeze whitespace to one space
            j = i
            while j < n and css[j].isspace(): j += 1
            out.append(" "); i = j
        else:
            out.append(c); i += 1
    s = "".join(out)
    # tidy spaces next to braces and semicolons only (safe for selectors and values)
    parts = re.split(r'("(?:[^"\\]|\\.)*"|\'(?:[^\'\\]|\\.)*\')', s)
    for k in range(0, len(parts), 2):
        t = re.sub(r"\s*([{};])\s*", r"\1", parts[k])
        parts[k] = t.replace(";}", "}")
    return "".join(parts).strip() + "\n"


def make(css_dir):
    chunks = []
    for f in FILES:
        with open(os.path.join(css_dir, f), encoding="utf-8") as fh:
            chunks.append(_minify(fh.read()))
    data = "/* built by build/css_bundle.py from: " + ", ".join(FILES) + " */\n" + "".join(chunks)
    path = os.path.join(css_dir, "site.css")
    old = open(path, encoding="utf-8").read() if os.path.exists(path) else None
    if old != data:
        with open(path, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(data)
