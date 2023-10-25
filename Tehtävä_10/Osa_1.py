
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

hissi1 = Hissi(1, 10)

hissi1.siirry_kerrokseen(6)

hissi1.siirry_kerrokseen(1)