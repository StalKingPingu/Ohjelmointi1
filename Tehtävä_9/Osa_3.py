class Auto:
    def __init__(self, rekkari, huippunopeus, nopeus=0, matkakuljettu=0):
        self.rekkari = rekkari
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.matkakuljettu = matkakuljettu

    def kiihdytys(self, maara):
        self.nopeus = self.nopeus + maara

    def kulje(self, aika):
        self.matkakuljettu = self.matkakuljettu + self.nopeus * aika


auto1 = Auto("ABC-123", 142, 0, 2000)

while True:

    maara = int(input('anna muutoksen maara'))

    aika = float(input('anna matkan aika'))

    auto1.kiihdytys(maara)

    if auto1.nopeus > auto1.huippunopeus:
        auto1.nopeus = auto1.huippunopeus

    if auto1.nopeus < 0:
        auto1.nopeus = 0

    auto1.kulje(aika)

    print(f"nopeus: {auto1.nopeus}km/h")
    print(f"matka: {auto1.matkakuljettu}")

    if auto1.nopeus == 0:
        break
