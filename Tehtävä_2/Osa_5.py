import math

leiviskät = int(input('Kuinka monta leiviskää: '))
naulat = int(input('Kuinka monta naulaa: '))
luodit = int(input('Kuinka monta Luotia: '))

naulat = naulat + leiviskät * 20
luodit = luodit + naulat * 32
paino = luodit * 13.3

paino = float(paino)
kilogrammat = math.floor(paino / 1000)
kilogrammat = kilogrammat * 1000
paino = paino - kilogrammat
kilogrammat = kilogrammat / 1000

print("Esineiden yhteismassa on: ", kilogrammat, " kilogrammaa ja ", paino, " grammaa")