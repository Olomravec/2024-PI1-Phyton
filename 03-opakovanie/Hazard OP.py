import math
import random
a = 10
b = 9
c = 8
d = 7
e = 6
f = 5
g = 4
h = 3
i = 2
j = 1
k = 0
prašky = round(int(input("Zadaj prachy: ")))
skit = print("Tvoj vklad je", prašky,"eur.  Prajem veľa šťasťia!")
def many(prašky):
        zacatek = int(input("Zadaj číslo od 1 do 5: "))
        from random import randint
        x = randint(1,5)
        if zacatek == x:
                prašky = prašky * 30  
                zostatok = print("Vyhral si!",prašky ,"eur. Gratulujem !")
        elif zacatek > 5:  
                print("Jak mozes byť tak retardovaný a napísať väčšie císlo ako 5")
        else: 
                zostatok = print("Smola Prehral si. Tvoj zostatok je", prašky/2,"eur :(")
                prašky = prašky / 2
        print(x,("bolo výherné číslo"))
        skibidi = input("Ak už nechceš hrať tak stlač Enter. Ale ak chceš pokračovať stlač hocičo a potom enter: ")
        if skibidi:
                print(many(prašky))
        else : 
                print("Koniec hry")
                print("Ďakujem za to, že si si zahral moju hru :) Tvoj finálny zostatok je",prašky,"eur." )
many(prašky)
sulko = int(input("Ako hodnotíš hru od 0 - 10 ? "))
if sulko == (a):
        print("10 Fúha! Ďakujem za hodnotenie ")
elif sulko == (b):
        print("9 Fúha! Ďakujem za hodnotenie ")
elif sulko == (c):
        print("8 Fúha! Ďakujem za hodnotenie ")
elif sulko == (d):
        print("7 Fúha! Ďakujem za hodnotenie ")
elif sulko == (e):
        print("6 Dobre ďakujeem")
elif sulko == (f):
        print("5 Dobre ďakujem")
elif sulko == (g):
        print("4 Dobre ďakujem")
elif sulko == (h):
        print("3 No ďakujem: :/")
elif sulko == (i):
        print("2 No čo už: :/")
elif sulko == (j):
        print("1 No to teda nič moc: :(")
elif sulko == (k):
        print("0 To je až tak zlé? :(")
else:
        print("Kamoško to čo si napísal")










