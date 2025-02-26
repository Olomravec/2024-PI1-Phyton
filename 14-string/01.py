#string je reťazec znakov napr. "Ahoj"
#reťazec začíname a končíme buď "" alebo'',pravý alt P
#\n - nový riadok, \t - tabulátor, \" - "
# funkcia lenght() - vráti dĺžku reťazca(počet znakov) počíta sa aj medzera
# znaky v reťazci sú indexované - prvý má index 0
#          123456789
# index píšeme do hranatých zátvoriek[] pravý alt + f/g
   
retazec = "Ahoj svet"
print(retazec)
print(len(retazec))
# print(retazec[0])
# print(retazec[1])

# for i in range (len(retazec)):
#     print(retazec[i])

for znak in retazec: # postupne vyberá znaky z reťazca do premennej znak
    print(znak)