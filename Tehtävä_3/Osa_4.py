vuosiluku = int(input("anna vuosiluku"))

if vuosiluku % 100 == 0:
    if vuosiluku % 400 == 0:
        print(vuosiluku, "on karkausvuosi.")
    else:
        print(vuosiluku, "ei ole karkausvuosi.")
elif vuosiluku % 4 == 0:
    print(vuosiluku, "on karkausvuosi.")
else:
    print(vuosiluku, "ei ole karkausvuosi.")