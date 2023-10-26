def masodik():
    osztharom = 0
    sorszam = 0
    while sorszam < 10:
        szam = int(input(f"Kérem add meg az a(z) {sorszam + 1}. számot!"))
        if szam % 3 == 0:
            osztharom += 1
        sorszam += 1
        print(f"Az osztható 3mal számok száma:" +str(osztharom))
