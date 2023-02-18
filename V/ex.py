def addition(n1, n2):
    return n1 + n2


def vraag_2(uitkomst):
    keuzen_uitkomst = input(f"Wil je wat met de uitkomst ({uitkomst}) doen? a) iets optellen, b) iets aftrekken, c) met iets vermenigvuldigen, d) ergens door delen, e) ophogen, f) verlagen, g) verdubbelen, h) halveren of i) niets? ").lower()
    return keuzen_uitkomst


keuzen = input("Wat wilt u doen? a) getallen optellen, b) getallen aftrekken, c) getallen vermenigvuldigen, d) getallen delen, e) getal ophogen, f) getal verlagen, g) getal verdubbelen of h) getal halveren? of i) om helemaal te stoppen: ").lower()

test = False
uitkomst = 0

while True:
    if not test:
        n1 = float(input("Welk getal: "))
        test = True
    if keuzen == "a":
        n2 = float(input(f"Welk getal wilt u optellen bij {n1}: "))
        uitkomst = addition(n1, n2)
        print(f"{n1} + {n2} = {uitkomst}")