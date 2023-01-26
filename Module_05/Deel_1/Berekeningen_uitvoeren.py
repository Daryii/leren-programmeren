def addition(n1, n2):
    return n1 + n2

def subtraction(n1, n2):
    return n1 - n2

def multiplication(n1, n2):
    return n1 * n2

def division(n1, n2):
    return n1 / n2

while True:
    keuzen = input("Wat wilt u doen? a) getallen optellen, b) getallen aftrekken, c) getallen vermenigvuldigen, d) getallen delen, e) getal ophogen, f) getal verlagen, g) getal verdubbelen of h) getal halveren? of i)om helemaal te stoppen: ").lower()

    if keuzen == "a":
        n1 = float(input("Welke getal: "))
        n2 = float(input(f"Welke getal optellen bij {n1} : "))
        uitkomst = addition(n1, n2)
        print(f"{n1} + {n2} = {uitkomst}")
        print("______________________________________")

    elif keuzen == "b":
        n1 = float(input("Welke getal: "))
        n2 = float(input(f"Welke getal aftrekken bij {n1} : "))
        uitkomst = subtraction(n1, n2)
        print(f"{n1} - {n2} = {uitkomst}")
        print("______________________________________")

    elif keuzen == "c":
        n1 = float(input("Welke getal: "))
        n2 = float(input(f"Welke getal vermenigvuldigen bij {n1} : "))
        uitkomst = multiplication(n1, n2)
        print(f"{n1} * {n2} = {uitkomst}")
        print("______________________________________")


    elif keuzen == "d":
        n1 = float(input("Welke getal: "))
        n2 = float(input(f"Welke getal delen bij {n1} : "))
        uitkomst = division(n1, n2)
        print(f"{n1} / {n2} = {uitkomst}")
        print("______________________________________")

    elif keuzen == "e":
        n1 = float(input("Getal: "))
        n2 = 1
        uitkomst = addition(n1, n2)
        print(f"{n1} + {n2} = {uitkomst}")
        print("______________________________________")

    elif keuzen == "f":
        n1 = float(input("Getal: "))
        n2 = 1
        uitkomst = subtraction(n1, n2)
        print(f"{n1} - {n2} = {uitkomst}")
        print("______________________________________")

    elif keuzen == "g":
        n1 = float(input("Getal: "))
        n2 = 2
        uitkomst = multiplication(n1, n2)
        print(f"{n1} * {n2} = {uitkomst}")
        print("______________________________________")

    elif keuzen == "h":
        n1 = float(input("Getal: "))
        n2 = 2
        uitkomst = division(n1, n2)
        print(f"{n1} / {n2} = {uitkomst}")
        print("______________________________________")

    elif keuzen =='i':
        break

    uitkomst1 = uitkomst
    while True : 
        keuzen2 = input(f"Wil je wat met de uitkomst ({uitkomst1}) doen? a) iets optellen, b) iets aftrekken, c) met iets vermenigvuldigen, d) ergens door delen, e) ophogen, f) verlagen, g) verdubbelen, h) halveren of i) niets? ").lower()

        if keuzen2 == "a":
            n2a = float(input(f"Welke getal optellen bij {uitkomst1}? :"))
            uitkomst1 = uitkomst + n2a
            print(f"{uitkomst1}")
            print("______________________________________")

        elif keuzen2 == "b":
            n2a = float(input(f"Welke getal aftrekken van {uitkomst1}?:  "))
            if n2a > uitkomst1:
                print("Dat is geen geldig getal! ")
            
                uitkomst1 = uitkomst - n2a
                print(f"{uitkomst1}")
                print("______________________________________")

    
        elif keuzen2 == "c":
            n2a = float(input(f"Welke getal vermenigvuldigen met {uitkomst1}?:  "))
            uitkomst1 = uitkomst * n2a
            print(f"{uitkomst1}")
            print("______________________________________")

        elif keuzen2 == "d":
            n2b = float(input(f"Welke getal delen met {uitkomst1}?:  "))
            if n2b == 0:
                print("kan niet door 0 delen")
            else:
                uitkomst1 = uitkomst / n2b
                print(f"{uitkomst1}")
            print("______________________________________")

        elif keuzen2 == "e":
            print("getal ophogen: ")
            uitkomst1 = uitkomst + 1
            print(f"{uitkomst1}")
            print("______________________________________")

        elif keuzen2 == "f":
            print("getal verlagen: ")
            uitkomst1 = uitkomst - 1
            print(f"{uitkomst1}")
            print("______________________________________")

        elif keuzen2 == "g":
            print("getal verdubbelen: ")
            uitkomst1 = uitkomst * 2
            print(f"{uitkomst1}")
            print("______________________________________")


        elif keuzen2 == "h":
            print("getal halveren: ")
            uitkomst1 = uitkomst / 2
            print(f"{uitkomst1}")
            print("______________________________________")


            

        elif keuzen2 == "i":
            exit()