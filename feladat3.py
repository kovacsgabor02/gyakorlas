def harmadik():
    szam = 0
    while szam < 1:
        szam1 = int(input("Kérem adjon meg egy 10-el osztható számot:"))
        if szam1 % 10 == 0:
            print(str(szam1), "osztható 10-el")
            szam += 1
        else:
            szam1 = int(input("kérem adjon me egy 10-el osztható számot!"))
            szam = 0
