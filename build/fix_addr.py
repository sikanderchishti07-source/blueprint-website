import io
p = r"C:\Users\ACER\Downloads\blueprint-website\site\js\config.js"
old = "ADDRESS_LINE1:  'Riyadh, Saudi Arabia',"
new = "ADDRESS_LINE1:  '3704 Abi Jafar Al Mansur, Al Yarmouk District, Riyadh 13251-7669, Saudi Arabia',"
with io.open(p, encoding="utf-8") as f:
    t = f.read()
print("matches:", t.count(old))
if t.count(old) == 1:
    with io.open(p, "w", encoding="utf-8", newline="") as f:
        f.write(t.replace(old, new))
    print("updated")
