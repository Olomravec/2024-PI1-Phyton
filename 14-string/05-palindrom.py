#palindrom je reťazec, ktorý je rovnaký pri čítaní od začiatku alebo od konca
ret = input(("Zadaj reťazec:"))
obrateny = ret[::-1]
if ret == obrateny:
    print("Reťazec",ret,"je palindrom")
else:
    print("Reťazec ",ret,"nieje palindrom")