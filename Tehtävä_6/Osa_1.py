import random

noppaluku = 0
def noppa():
    return (random.randint(1,6))

while noppaluku != 6:
    noppaluku = noppa()
    print(noppaluku)
