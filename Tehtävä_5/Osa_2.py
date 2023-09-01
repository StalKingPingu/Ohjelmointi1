
numerot = []

while True:
    numero = input("anna numero. tyhä lopettaa")
    if numero == "":
        break
    try:
        luku = float(numero)
        numerot.append(luku)
    except ValueError:
        print("antamasi numero ei käy")

if len(numerot) < 5:
    print("anna ainakin 5 numeroa.")
else:
    numerot.sort(reverse=True)
    viisi_suurinta = numerot[:5]
    for luku in viisi_suurinta:
        print(luku)
