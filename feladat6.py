def hatodik():
    szam = int(input("Kérem adjon meg egy olyan számot ami 3-al osztható vagy négyzetszám"))
    while not (szam % 3 == 0):
        szam = int(input("Kérem adjon meg egy olyan számot ami 3-al osztható vagy négyzetszám"))
