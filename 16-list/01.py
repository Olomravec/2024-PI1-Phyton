teplota = [10,13,15,20]
print(teplota)
print(teplota[0])


nakup = ["chlieb","maslo","mlieko"]
print(nakup)
print(nakup[1])

zviera = ["pes","dunčo",2020,"hnedá",10.7]# do listu môžeme vkladať hodnoty rôznych typov(int, str, bool...)
print(zviera)
print(zviera[2])

# v Pythone sú listy dynamické, to znamená, že nemusia mať definovanú veľkosť (počet prvkov)
# prvky pridávame pomocou fcie append()
prazdny = []
prazdny.append(25)
print(prazdny)
prazdny.append("ahoj")
print(prazdny)
prazdny.append("100")
print(prazdny[-1])
#listy vieme aj zreťaziť (spočítať)
nakupyazvierata = nakup + zviera
print(nakupyazvierata)
print(3*zviera)
print("dunčo"in zviera)
# narozdiel od string su listy vy pythone mutable (meniťeľné), tzn. môžem prepísať hodnotu prvku
