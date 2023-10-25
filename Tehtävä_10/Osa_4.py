import random

autot = ["auto1", "auto2", "auto3", "auto4", "auto5", "auto6", "auto7", "auto8", "auto9", "auto10"]

autot2 = []
class Auto:
    def __init__(self, rekkari, huippunopeus, nopeus=0, matkakuljettu=0):
        self.rekkari = rekkari
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.matkakuljettu = matkakuljettu

    def kiihdytys(self):
        nopeus = random.randint(-10, 15)
        self.nopeus = self.nopeus + nopeus
        if self.nopeus < 0:
            self.nopeus = 0
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus

    def kulje(self):
        self.matkakuljettu = self.matkakuljettu + self.nopeus

class Kilpailu:
    def __init__(self, nimi, pituus, kilpailijat):
        self.nimi = nimi
        self.pituus = pituus
        self.kilpailijat = []

    def tunti_kuluu(self):
        self.kilpailijat

for i, name in enumerate(autot):
    auto = Auto(f"ABC-{i + 1}", random.randint(100, 200))
    autot2.append(auto)

while all(auto.matkakuljettu < 10000 for auto in autot2):

    for auto in autot2:
        auto.kiihdytys()
        auto.kulje()
        print(auto.rekkari, auto.matkakuljettu)

print("Tulokset!")

for auto in autot2:
    print(f"Rekisterikilpi: {auto.rekkari}, Huippunopeus: {auto.huippunopeus}, nopeus lopussa: {auto.nopeus}, kuljettu matka: {auto.matkakuljettu}")
