import random

# Začiatky s počiatočným zostatkom
zostatok = 0  # Počiatočný zostatok

# Získaj od používateľa vklad a číslo na hádanie
vklad = int(input("Vlož vklad: "))
zacatek = int(input("Zadaj číslo od 1 do 8: "))

# Nastavíme počiatočný zostatok ako hodnotu vkladu
zostatok += vklad

# Generujeme náhodné číslo
from random import randint
x = randint(1, 8)

# Porovnáme zadané číslo s náhodným číslom
if zacatek == x:
    vyhra = vklad * 20  # Ak vyhráš, vklad sa násobí 20
    zostatok += vyhra  # Pridáme výhru k zostatku
    print(f"Vyhral si {vyhra} EUR. Gratulujem! Tvoj nový zostatok je {zostatok} EUR.")
elif zacatek > 8 or zacatek < 1:
    print("Jak mozes byť tak retardovaný a napísať číslo mimo rozsah (1-8)! Tvoj zostatok je stále", zostatok, "EUR.")
else:
    prehral = vklad / 2  # Ak prehráš, zostatok sa zníži o polovicu vkladu
    zostatok -= prehral  # Odpočítame polovicu vkladu
    print(f"Smola. Prehral si {prehral} EUR. Tvoj nový zostatok je {zostatok} EUR. :(")

# Zobrazenie výherného čísla
print(f"{x} bolo výherné číslo.")
