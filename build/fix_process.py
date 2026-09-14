import io
p = r"C:\Users\ACER\Downloads\blueprint-website\build\home_new.py"
with io.open(p, encoding="utf-8") as f:
    t = f.read()

swaps = [
    ("assets/img/svc-permit.jpg",   "assets/img/process-scoping.webp"),
    ("assets/img/svc-field.jpg",    "assets/img/process-assessment.webp"),
    ("assets/img/svc-sampling.jpg", "assets/img/process-measurement.webp"),
    ("assets/img/svc-report.jpg",   "assets/img/process-lab.webp"),
    ("assets/img/svc-register.jpg", "assets/img/process-reporting.webp"),
]

i = t.index("PROCESS = [")
j = t.index("]", i) + 1
block = t[i:j]

for old, new in swaps:
    n = block.count(old)
    print(n, old, "->", new)
    block = block.replace(old, new)

with io.open(p, "w", encoding="utf-8", newline="") as f:
    f.write(t[:i] + block + t[j:])

print()
print(block)
