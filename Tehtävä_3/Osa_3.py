sukupuoli = input('Oletko mies vai nainen? ')
hemoglobiini = int(input('mikä on hemoglobiini arvosi?'))

if sukupuoli == "mies":
    if hemoglobiini < 134:
        print("Hemoglobiini on alhainen.")
    elif hemoglobiini > 195:
        print("hemoglobiini on korkea.")
    else:
        print("hemoglobiini on normaali.")

if sukupuoli == "nainen":
    if hemoglobiini < 117:
        print("Hemoglobiini on alhainen.")
    elif hemoglobiini > 175:
        print("hemoglobiini on korkea.")
    else:
        print("hemoglobiini on normaali.")

