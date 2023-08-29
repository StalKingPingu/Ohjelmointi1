käyttäjätunnus = "python"
salasana = "rules"
yritykset = 0

while True:
    if yritykset < 5:
        käyttäjätunnus2 = input('Anna käyttäjätunnus')
        salasana2 = input('Anna salasana')
        if käyttäjätunnus2 == käyttäjätunnus:
            if salasana2 == salasana:
                print("Tervetuloa!")
                break
            else:
                print("Pääsy evätty")
                yritykset = yritykset + 1
        if käyttäjätunnus2 != käyttäjätunnus:
            print("Pääsy evätty")
            yritykset = yritykset + 1
    else:
        print("Yritit liian monta kertaa")
        break