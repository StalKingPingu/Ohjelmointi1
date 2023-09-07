
gallonat = int(input('monta gallonaa bensiiniä?'))


def muunnin():
    litrat = gallonat * 3.785
    return litrat


while gallonat >= 0:
    gallonat = int(input('monta gallonaa bensiiniä?'))
    print(gallonat, "gallonaa on ", muunnin(), "litraa")
