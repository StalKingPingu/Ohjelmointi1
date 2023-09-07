num1 = int(input('anna 5 lukua'))
num2 = int(input())
num3 = int(input())
num4 = int(input())
num5 = int(input())
def summan_laskija(lista):
    summa = 0
    for luku in lista:
        summa = summa + luku
    return summa

numerot = [num1, num2, num3, num4, num5]

tulos = summan_laskija(numerot)
print("Numeroiden summa on:", tulos)