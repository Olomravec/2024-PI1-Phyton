polozky = 0
cena = 0
for cenka in 1.75, 2.20, 1.03, 4.00, 3.50, 2.90, 1.89:
    polozky = polozky + 1
    cena = cena + cenka
print("poloziek je:",polozky)
print("cena vsetkeho je:",cena)
print("priemerna cena nákupu sú",int(cena/polozky),"eurka")

