lista = [1, 6, 4, 9, 3, 6]

numero = 0
for i in lista:
    numero = i + lista.index(i)
    print(numero)

lause = "python on todella hauskaa ja kivaa"

sanamäärä = len(lause.split())
print("sanamäärä on ", sanamäärä)