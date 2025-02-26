# string v Pythone je immutable, tzn. nemeniteľný
ret = "Ahoj Svet"
#ret[0] = "a" # toto nieje možné, lebo to je immutable
ret = "a" + ret[1:]# ak chceme zmeniť nejaký znak, musíme to urobiť takto
print(ret)

# reťazce vieme porovnávať 

print("a"== "A")
print(ord("a")) # ord je funkcia, ktorá vráti ordinálnu (číselnú) hodnotu
print(ord("A"))
print("a">"A")
print(chr(64)) # charakter. chr() je funkcia, ktorá na základe ordinálnej hodnoty vráti znak