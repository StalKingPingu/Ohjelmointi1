import random

tahkomaara = int(input('monta puolta nopassa?'))
noppaluku = 0
def noppa():
    return (random.randint(1,tahkomaara))


while noppaluku != tahkomaara:
    noppaluku = noppa()
    print(noppaluku)