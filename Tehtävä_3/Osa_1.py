pituus = int(input('Anna kuhan pituus:  '))

puuttuva = 37 - pituus

if pituus < 37:
    print("Laske kuha takaisin järveen. Kuhan pitää olla ainakin", puuttuva, "CM pidempi")
