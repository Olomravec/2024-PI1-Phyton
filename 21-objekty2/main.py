import datetime
class Osoba:# triedy vždy píšeme veľkým písmenom
    def __init__(self,meno,priezvisko,rok): # konštruktor, zavlá sa pri vzniku objektu
        self.meno = meno # atribút objektu (vlastnosť)
        self.priezvisko = priezvisko
        self.rok = rok
        self.vek = datetime.date.today().year - self.rok

    def pozdrav(self):# metóda (čo vie objekt robiť)
        print(f"Ahoj, ja som {self.meno} {self.priezvisko} a mám {self.vek}")
    
    def vypis_meno(self):
        print(self.meno, self.priezvisko)
    def vypis_vek(self):
        print(self.vek)
    def vypis_rok(self):
        print(self.rok)
class Student(Osoba):# trieda Student zdedí atribúty a metódy od triedy Osoba
    def __init__(self, meno, priezvisko, rok):
        super().__init__(meno, priezvisko, rok)# super - znamená, že použije atribúty z rodičovskej triedy(Osoba)
    Osoba.__init__0
olo = Osoba("Oliver","Mravec",2009)# vznikne objekt olo, vytvorený pomocou triedy osoba
olo.pozdrav()# voláme metódu objektu pozdrav
fero = Osoba("František","Mikloško",1990)
fero.pozdrav()

olo.vypis_meno()
olo.vypis_rok()
olo.vypis_vek()