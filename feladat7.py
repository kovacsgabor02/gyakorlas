def hetedik():
    a = float(input("Kérem adjon meg egy valós számot"))
    b = float(input("Kérem adjon meg egy másik valós számot"))
    c = float(input("Kérem adjon meg egy harmadik valós számot"))
    while not ((a > b + c) and (b > a + c) and (c > a + b)):
        print("A háromszög nem szereszthető.")
        a = float(input("Kérem adjon meg egy valós számot"))
        b = float(input("Kérem adjon meg egy másik valós számot"))
        c = float(input("Kérem adjon meg egy harmadik valós számot"))
    print("A háromszög szerkeszthető.")
