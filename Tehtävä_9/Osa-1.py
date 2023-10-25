class Auto:
    def __init__(self, rekkari, huippunopeus, nopeus=0, matkakuljettu=0):
        self.rekkari = rekkari
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.matkakuljettu = matkakuljettu

auto1 = Auto("ABC-123", 142)

print(f"Rekisterikilpi: {auto1.rekkari} Huippunopeus:{auto1.huippunopeus}km/h Tämänhektinen nopeus: {auto1.nopeusnyt}km/h kuljettu matka: {auto1.matkakuljettu}km")