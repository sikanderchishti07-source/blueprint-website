import io, os, re, glob

TARGETS = (glob.glob(os.path.join("build","*.py"))
           + glob.glob(os.path.join("content","blog","*.md"))
           + glob.glob(os.path.join("content","careers","*.md")))

PATTERNS = [(re.compile(r"\s*&mdash;\s*"), ", "),
            (re.compile(r"\s*\u2014\s*"), ", "),
            (re.compile(r"\s*&#8212;\s*"), ", ")]

TIDY = [(re.compile(r",\s*,"), ","),
        (re.compile(r"\s+,"), ","),
        (re.compile(r",\s*\."), ".")]

total = 0
for path in TARGETS:
    if os.path.basename(path) == "fix-dashes.py":
        continue
    src = io.open(path, encoding="utf-8").read()
    n = 0
    for rx, rep in PATTERNS:
        n += len(rx.findall(src))
        src = rx.sub(rep, src)
    if n:
        for rx, rep in TIDY:
            src = rx.sub(rep, src)
        io.open(path, "w", encoding="utf-8", newline="").write(src)
        print("%-44s %d" % (path, n))
        total += n
print()
print("Replaced %d em dashes." % total)
