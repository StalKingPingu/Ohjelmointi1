num1 = int(input('anna 5 lukua'))
num2 = int(input())
num3 = int(input())
num4 = int(input())
num5 = int(input())
def pariton_postaja(lista):
    parilliset = [luku for luku in lista if luku % 2 == 0]
    return parilliset

numerot = [num1, num2, num3, num4, num5]

tulos = pariton_postaja(numerot)
print("Parilliset numerot ovat:", tulos)