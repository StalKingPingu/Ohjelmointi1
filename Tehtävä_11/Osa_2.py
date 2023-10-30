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

class Sähköauto(Auto):
    def __init__(self, rekisteritunnuksen, huippunopeuden, akkukapasiteetti, nopeus):
        self.akku = akkukapasiteetti
        super().__init__(rekisteritunnuksen, huippunopeuden, nopeus)
class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnuksen, huippunopeuden, bensatankki, nopeus):
        self.tankki = bensatankki
        super().__init__(rekisteritunnuksen, huippunopeuden, nopeus)


sähköauto = Sähköauto("ABC-15", 180, 52.5, 90)
bensaauto = Polttomoottoriauto("ACD-123", 165, 32.3, 100)

sähköauto.kulje(3)
bensaauto.kulje(3)

print("sähköauto kulki:", sähköauto.matkakuljettu)
print("bensa-auto kulki:", bensaauto.matkakuljettu)