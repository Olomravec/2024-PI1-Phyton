n = int (input("zadaj n:"))
faktorial = 1
for i in range(n):
    faktorial = faktorial * (i+1) # sucet + (i+1) je vyraz, najskor sa vypocita vyraz a vysledna hodnota sa priradi do premennej suce
print(i, i+1, faktorial)
    # print(i, i+1, sucet)
print(n, "!=", faktorial)
print(f"{n}! = {faktorial}") # napiseme pravy alt+b, pravy alt+n
