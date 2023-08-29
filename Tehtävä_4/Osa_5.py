käyttäjätunnus = "python"
salasana = "rules"

while True:
    käyttäjätunnus2 = input('Anna käyttäjätunnus')
    salasana2 = input('Anna salasana')
    if käyttäjätunnus2 == käyttäjätunnus:
        if salasana2 == salasana:
            print("Tervetuloa!")
            break
        else:
            print("Pääsy evätty")
    if käyttäjätunnus2 != käyttäjätunnus:
        print("Pääsy evätty")