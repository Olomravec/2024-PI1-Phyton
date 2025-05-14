import random
class Auto:
    def __init__(self, znacka, rok,farba):
        self.farba = farba
        self.znacka = znacka
        self.rok = rok
    def info(self):
        print(f"farba auta je {self.farba} a bolo vyrobene v roku {self.rok} a značky {self.znacka}")
        
class elauto:
    def __init__(self):
        self.dojazd = random.randint(300,700) 
        potah = random.randint(1,8)
        self.potah = potah
        self.farba = random.choice(["modrá","červená","fialová","žltá","čierna","biela"])
        if self.farba == ("fialová"):
            self.vyber = "Taká bozzovská farba? To si pomaly taký bozzo ako Kubo "
        if self.farba == ("žltá"):
            self.vyber = "Taká bozzovská farba? To si pomaly taký bozzo ako Kubo "
        if self.farba == ("modrá"):
            self.vyber = "Taká bozzovská farba? To si pomaly taký bozzo ako Kubo "
        else:
            self.vyber = "Šumná farba"
        if self.potah ==1:
            self.sekunda = "sekundu" 
        elif self.potah > 1 and self.potah < 5:
            self.sekunda = "sekundy"
        else:
            self.sekunda = "sekúnd"
    def inf(self):
        print(f"farba auta je {self.farba} dojazd el.auta je {self.dojazd} km a potah auta je z 0 na 100 za {self.potah} {self.sekunda} {self.vyber}")

moje_auto = Auto("škoda",2019,"červená")
moje_elauto = elauto()
moje_auto.info()
moje_elauto.inf()