import io, re

files = [
    r"C:\Users\ACER\Downloads\blueprint-website\build\partials.py",
    r"C:\Users\ACER\Downloads\blueprint-website\build\arabic.py",
]

# matches the whole <svg class="whatsapp-icon" ...>...</svg> block
pat = re.compile(r'<svg class="whatsapp-icon".*?</svg>', re.S)
new = '<i class="fab fa-whatsapp whatsapp-icon"></i>'

for p in files:
    with io.open(p, encoding="utf-8") as f:
        t = f.read()
    n = len(pat.findall(t))
    print(p.split("\\")[-1], "->", n, "replaced")
    if n:
        t = pat.sub(new, t)
        with io.open(p, "w", encoding="utf-8", newline="") as f:
            f.write(t)
