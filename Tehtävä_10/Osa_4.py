import random

class Auto:
    def __init__(self, rekkari, huippunopeus, nopeus=0, matkakuljettu=0):
        self.rekkari = rekkari
        self.huippunopeus = int(huippunopeus)
        self.nopeus = int(nopeus)
        self.matkakuljettu = float(matkakuljettu)

    def kiihdytys(self, uusi_nopeus):
        self.nopeus = self.nopeus + uusi_nopeus
        if self.nopeus < 0:
            self.nopeus = 0
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus

    def kulje(self, aika):
        self.matkakuljettu = self.matkakuljettu + (self.nopeus * aika)


class Kilpailu:

    def __init__(self, nimi, pituus, kilpailijat):
        self.nimi = nimi
        self.pituus = pituus
        self.kilpailijat = kilpailijat

    def tunti_kuluu(self):
        tunti = 0
        while not self.kilpailu_ohi():
            for auto in autot2:
                auto.kiihdytys(random.randint(-10, 15))
                auto.kulje(1)
            tunti += 1
            if tunti % 10 == 0:
                self.tulosta_tilanne()

    def tulosta_tilanne(self):
        for auto in self.kilpailijat:
            print(f"{auto.rekkari} {auto.huippunopeus} {auto.nopeus} {auto.matkakuljettu}")

    def kilpailu_ohi(self):
        for b in self.kilpailijat:
            if b.matkakuljettu > self.pituus:
                self.tulosta_tilanne()
                return True
        return False

autot2 = []
for i in range(10):
    auto = Auto(f"ABC-{i + 1}", random.randint(100, 200))
    autot2.append(auto)
k = Kilpailu("Mahtava kilpa", 20000, autot2)
k.tunti_kuluu()