def otodik():
    szam = int(input("kérem adjon meg egy számot:"))

    while not (szam > 0) and (szam % 2 == 1):
        szam = int(input("Kérem adjon meg egy olyan számot ami pozitív páratlan szám!"))

    if (szam % 2 == 1) and (szam > 0):
        print("A(z) " + str(szam) + " páratlan szám")
