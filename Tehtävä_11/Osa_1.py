class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi
class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumäärä):
        super().__init__(nimi)
        self.kirjoittaja = kirjoittaja
        self.sivumäärä = sivumäärä

    def tulosta_tiedot(self):
        print(f" Kirjan tiedot: Nimi: {self.nimi}, Kirjailija: {self.kirjoittaja}, Sivumäärä: {self.sivumäärä}")

class Lehti(Julkaisu):
    def __init__(self, nimi, päätoimittaja):
        super().__init__(nimi)
        self.päätoimittaja = päätoimittaja

    def tulosta_tiedot(self):
        print(f" Kirjan tiedot: Nimi: {self.nimi}, Päätoimittaja: {self.päätoimittaja}")

Aku_Ankka = Lehti("Aku Ankka", "Aki Hyppää")
Hytti = Kirja("Hytti n:o 6", "Rosa Liksöm", 200)

Aku_Ankka.tulosta_tiedot()
Hytti.tulosta_tiedot()