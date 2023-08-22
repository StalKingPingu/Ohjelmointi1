leiviskät = int(input('Kuinka monta leiviskää: '))
naulat = int(input('Kuinka monta naulaa: '))
luodit = int(input('Kuinka monta Luotia: '))

naulat = naulat + leiviskät * 20
luodit = luodit + naulat * 32
paino = luodit * 13.3

print("Esineiden yhteismassa on: ", paino, " grammaa")