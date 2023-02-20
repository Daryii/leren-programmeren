def addition(n1, n2):
    return n1 + n2

def subtraction(n1, n2):
    return n1 - n2

def multiplication(n1, n2):
    return n1 * n2

def division(n1, n2):
    return n1 / n2


keuzen = input("Wat wilt u doen? a) getallen optellen, b) getallen aftrekken, c) getallen vermenigvuldigen, d) getallen delen, e) getal ophogen, f) getal verlagen, g) getal verdubbelen of h) getal halveren? of i)om helemaal te stoppen: ").lower()

n1 = float(input("Welke getal: "))

while True:
    if keuzen == "a":
        n2 = float(input(f"Welke getal optellen bij {n1} : "))
        uitkomst = addition(n1, n2)
        print(f"{n1} + {n2} = {uitkomst}")
        print("______________________________________")

    n1 = uitkomst
    keuzen_uitkomst = input(f"Wat wil je wat met de uitkomst ({uitkomst}) doen? a) iets optellen, b) iets aftrekken, c) met iets vermenigvuldigen, d) ergens door delen, e) ophogen, f) verlagen, g) verdubbelen, h) halveren of i) niets? ").lower()

    while keuzen_uitkomst != "i":
        if keuzen_uitkomst == "a":
            vraag = float(input(f"Welke getal optellen bij {uitkomst}?:  "))
            brekening = uitkomst + vraag
            print(f"{uitkomst} + {vraag} = {brekening}")
            print("______________________________________")
        elif keuzen_uitkomst == "b":
            vraag = float(input(f"Welke getal aftrekken van {uitkomst}?:  "))
            brekening = uitkomst - vraag
            print(f"{uitkomst} - {vraag} = {break}")
