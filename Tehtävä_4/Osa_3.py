print("anna lukuja. tyhjä lopettaa ohjelman")

numero = input('anna luku')
alin = numero
ylin = numero

while numero != '':
    numero = input('anna luku')
    if numero != '':
        if numero < alin:
            alin = numero
    if numero > ylin:
        ylin = numero

    if numero == '':
        print("Ylin antama numero: ", ylin, "Alin antama numero: ", alin)
        break
