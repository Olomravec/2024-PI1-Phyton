vstup  = input("Zadaj slovo:")
retazec1 = retazec2 =""
for znak in vstup:
    retazec1 = retazec1 + znak
    retazec2 = znak + retazec2
print(retazec1,retazec2)