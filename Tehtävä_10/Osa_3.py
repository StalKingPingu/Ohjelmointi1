class Hissi:
    def __init__(self, alinkerros, ylinkerros):
        self.ylinkerros = ylinkerros
        self.alinkerros = alinkerros
        self.kerros = alinkerros

    def kerros_ylös(self):
        if self.kerros < self.ylinkerros:
            self.kerros = self.kerros + 1

    def kerros_alas(self):
        if self.kerros > self.alinkerros:
            self.kerros = self.kerros - 1

    def siirry_kerrokseen(self, uusikerros):
        while self.kerros != uusikerros:
            print(self.kerros)
            if self.kerros < uusikerros:
                self.kerros_ylös()
            elif self.kerros > uusikerros:
                self.kerros_alas()
        print(self.kerros)

class Talo:
    def __init__(self, alinkerros, ylinkerros, hissimaara):
        self.hissit = [Hissi(alinkerros,ylinkerros) for i in range(hissimaara)]
        self.alinkerros = alinkerros
        self.ylinkerros = ylinkerros
        self.hissimaara = hissimaara

    def aja_hissiä(self, hissinumero, kerros):
        if hissinumero < len(self.hissit):
            hissi = self.hissit[hissinumero]
            while hissi.kerros < kerros:
                print("hissi", hissinumero,"on kerroksessa", hissi.kerros)
                hissi.kerros_ylös()
            while hissi.kerros > kerros:
                print("hissi", hissinumero,"on kerroksessa", hissi.kerros)
                hissi.kerros_alas()
        print("hissi", hissinumero,"on kerroksessa", hissi.kerros)

    def palohalytys(self):
        for hissi in self.hissit:
            hissi.kerros = self.hissit[0].alinkerros
            print("hissi on palohälytyksen vuoksi alimmassa kerroksessa", hissi.kerros)


talo = Talo(1, 10, 3)

talo.aja_hissiä(0, 5)
talo.aja_hissiä(1, 7)
talo.aja_hissiä(2, 3)

talo.palohalytys()