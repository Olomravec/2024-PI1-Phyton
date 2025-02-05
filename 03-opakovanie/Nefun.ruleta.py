import math 
import random
prachy = int(input("Zadaj sumu, ktorú chceš staviť: "))
def skamp(x):
    stavka = input("Zadaj, či chceš staviť na červenú, alebo čiernu,alebo na číslo od 1 do 7: ") 
    číslo = input("Zadaj číslo na ktoré chceš staviť :")
    from random import choice
    x = random.choice("červená""čierna")
    j = random.randint(1,7)
    if stavka == x:
        print(int("Trafil si!!!. Tvoj zostatok je", prachy * 1,5))
    if číslo == j:
        print(int("Gratulujem!!! Trafil si. Tvoj zostatok je", prachy * 50))
    else:
        print("Konec")

    


skamp(prachy)
