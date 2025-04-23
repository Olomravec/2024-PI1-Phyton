subor = open("subor.txt", "r")# "subor.txt" je relatívna cesta k súboru (musí byť v tom istom priečinku ako samostatný kód)
# open otvorí súbor.txt na čítanie, pre zápis sa používa "w", "r"- read, "w"- write. Ak súbor neexistuje vypíše chybu
# subor = open("c:/dokumenty/subor.txt","r")- toto je absolútna cesta "c:/dokumenty/subor.txt"
# subor = open("../16-list/subor.txt", "r") ..je o priečinok vyššie

# for i in range(4):
#     riadok = subor.readline()# readline prečíta celý riadok zo súboru a uloží do premennej
#     print(riadok)

# riadok = subor.readline()
# while riadok != "":# pokial riadok nieje prázdny
#     print(riadok)
#     riadok = subor.readline()

while True :
    riadok = subor.readline()
    if riadok =="":
        break # preruší cyklus a vyskočí z neho
    print(riadok.strip())# strip odstráni nečitateľné znaky napr. \n, \t (enter)
subor.close() # zatvorí súbor 