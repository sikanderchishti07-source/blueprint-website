import io

p = r"C:\Users\ACER\Downloads\blueprint-website\build\partials.py"
with io.open(p, encoding="utf-8") as f:
    t = f.read()

# 1. new top-level nav item, inserted before Services
anchor = (
    '          <div class="nav-item">\n'
    '            <a href="services.html" class="nav-link" data-page="services.html">Services'
)
item = (
    '          <div class="nav-item">\n'
    '            <a href="about.html" class="nav-link" data-page="about.html">About</a>\n'
    '          </div>\n'
    '\n'
)
print("nav anchor matches:", t.count(anchor))

# 2. repoint the dropdown link at the real page
old_dd = '{dd_link("index.html#overview", "fa-building", "About BluePrint", "Mission, vision &amp; Vision 2030")}'
new_dd = '{dd_link("about.html", "fa-building", "About BluePrint", "Who we are &amp; how we work")}'
print("dropdown matches:", t.count(old_dd))

if t.count(anchor) == 1 and t.count(old_dd) == 1 and 'data-page="about.html"' not in t:
    t = t.replace(anchor, item + anchor, 1).replace(old_dd, new_dd, 1)
    with io.open(p, "w", encoding="utf-8", newline="") as f:
        f.write(t)
    print("patched")
else:
    print("NOT patched, check the counts above")
