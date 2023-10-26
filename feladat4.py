def negyedik():
    szam = int(input("Kérem adjon meg egy olyan számot ami kétjegyű és páros! "))
    while not ((((szam >= 10) and (szam <= 99)) or (szam >= -99) and (szam <= -10)) and szam % 2 == 0):
        szam = int(input("Kérem adjon meg egy olyan számot ami kétjegyű és páros: "))
