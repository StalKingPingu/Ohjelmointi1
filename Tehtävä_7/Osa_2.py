nimet = set()

syöte = input('Syötä nimi: ')
nimet.add(syöte)

while syöte != '':
    syöte = input('Syötä nimi: ')
    if syöte != '':
        nimet.add(syöte)

for i in nimet:
    print(i)