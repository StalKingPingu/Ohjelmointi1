class Auto:
    def __init__(self, rekkari, huippunopeus, nopeus=0, matkakuljettu=0):
        self.rekkari = rekkari
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.matkakuljettu = matkakuljettu

    def kiihdytys(self, maara):
        self.nopeus = self.nopeus + maara


auto1 = Auto("ABC-123", 142)

while True:

    maara = int(input('anna muutoksen maara'))

    auto1.kiihdytys(maara)

    if auto1.nopeus > auto1.huippunopeus:
        auto1.nopeus = auto1.huippunopeus

    if auto1.nopeus < 0:
        auto1.nopeus = 0

    print(f"{auto1.nopeus}km/h")

    if auto1.nopeus == 0:
        break
