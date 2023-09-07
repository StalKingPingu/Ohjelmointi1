kaupungit = []
määrä = 0

print("anna viiden kaupungin nimet")
kaupunki = input('Anna nimi')

while määrä < 5:
    kaupungit.append(kaupunki)
    määrä = määrä + 1
    if määrä < 5:
        kaupunki = input('seuraava nimi kiitos')

for kaupuki in kaupungit:
    print (kaupuki)
