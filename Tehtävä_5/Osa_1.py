import random
random.seed()

noppamäärä = int(input('anna noppien määrä'))
summa = 0

for i in range(noppamäärä):
    noppaluku = (random.randint(1,6))
    print(noppaluku)
    summa += noppaluku

print(summa)