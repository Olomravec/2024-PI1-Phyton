r = float(input("Zadaj polomer:" )) # float je funkcia na prevodtextu do desatinneho čísla
# údajove typy: 
# string - reťazec znakov ( text)
# int - celé čísla
# float - desatinné čísla
O = 2 * 3.14 * r # desatinne čísla vždy uvádzané s bodkou !!!
S = 3.14 * (r * r)
print("Obvod kruhu je", round(O, 2))# round zaokruhli cislo resp. premennú, O je premenná a 2 je počet desatinných miest
print("Obsah kruhu je", round(S, 2))