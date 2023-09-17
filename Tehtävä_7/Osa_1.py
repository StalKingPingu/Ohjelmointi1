vuodenajat = ("Talvi", "Kevät", "Kesä", "Syksy")

kuukausi = int(input('anna kuukausen numero (1-12)'))

vuodenaika = 0

if 3 <= kuukausi <= 5:
    vuodenaika = 1
elif 6 <= kuukausi <= 8:
    vuodenaika = 2
elif 9 <= kuukausi <=11:
    vuodenaika = 3
else:
    vuodenaika = 0

vastaus = vuodenajat[vuodenaika]
print(f"{kuukausi} on {vastaus}")