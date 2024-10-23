cislo = int(input("Zadaj číslo"))
# výpis párnych čísel 
print(f"Párne čísla do{cislo}:")
for i in range(2, cislo + 1, 2):
    print(i)
#výpis nepárnych čísiel
cislo = int(input("Zadaj číslo"))
print(f"Nepárne čísla do{cislo}:")
for i in range(1, cislo + 1, 2):
    print(i)
if cislo%2 == 0 :
    print("Číslo je Párne ")
else: print("Číslo je nepárne")