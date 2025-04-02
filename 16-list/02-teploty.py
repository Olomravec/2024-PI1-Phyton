import random

teplota = []

pocet_dní = 30
# naplní list teploty náhodnými teplotami v rozsahu od 10 do 30
for i in range(30):
    #teplota[i] = random.randint(10,30)# vráti chybu,mlebo prvky ešte neexistujú
    teplota.append(random.randint(10,30))
for i in range(pocet_dní):
    print(f"{i+1}.deň - {teplota[i]}°C")

    # vypočíta avypíše priemernú fciu
# priemerna_teplota = sum(teplota)/pocet_dní
# print(priemerna_teplota)
suma = 0
for i in range(pocet_dní):
    suma += teplota[i]
priemerna_tep = suma/pocet_dní
print(f"priemerná teplota v mesiaci je {priemerna_tep}°C")

print("dni s podpriemernou teplotou:")
for i in range(pocet_dní):
    if teplota < priemerna_tep:
        print("podpriemerná teplota je",teplota) 
