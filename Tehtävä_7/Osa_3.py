lentoasemat = {"EFHK" : "Helsinki-Vantaan lentoasema"}

valinta = "hi"

while valinta != "3":
    print("Mitä haluat tehdä?")
    print("1. Lisää lentoasema")
    print("2. Etsi lentoasema")
    print("3. Lopeta")

    valinta = input('')

    if valinta == "1":
        ICAO = input("Anna lentoaseman ICAO koodi")
        nimi = input("Anna lentoaseman nimi")
        lentoasemat[ICAO] = nimi

    elif valinta == "2":
        ICAO = input("Syötä etsittävän lentoaseman ICAO-koodi: ")
        if ICAO in lentoasemat:
            print(f"Lentoaseman nimi on: {lentoasemat[ICAO]}.")
        else:
            print(f"{ICAO} ei löydy listasta.")

    else:
        print("Virheellinen valinta. Valitse 1, 2 tai 3.")