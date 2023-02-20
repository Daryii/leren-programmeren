def addition(n1, n2):
    return n1 + n2

def subtraction(n1, n2):
    return n1 - n2

def multiplication(n1, n2):
    return n1 * n2

def division(n1, n2):
    return n1 / n2


keuze = " "
while not keuze in ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'):
    keuze = input("Wat wilt u doen? A) getallen optellen, B) getallen aftrekken, C) getallen vermenigvuldigen, D) getallen delen, E) getal ophogen, F) getal verlagen, G) getal verdubbelen of H) getal halveren of I) Nee?: ").lower()
    if keuze == "i":
        exit()


aantal = -1
while True:
    if aantal > -1 and keuze != 'i' and keuze in ('a', 'b', 'c', 'd'):
        n1 = aantal
        n2 = int(input("Geef de 2e getal op: "))

    elif aantal > -1 and keuze != 'i' and keuze in ('e', 'f', 'g', 'h'):
        n1 = aantal

        
    elif keuze in ('a', 'b', 'c', 'd'):
        n1 = int(input("Geef een getal op: "))
        n2 = int(input("Geef nog een getal op: "))

    elif keuze in ('e', 'f', 'g', 'h'):
        n1 = int(input("Geef een getal op: "))

    else: 
        exit()

    if keuze == "a":
        aantal = addition(n1, n2)
        print(aantal)
    elif keuze == "b":
        aantal = subtraction(n1, n2)
        print(aantal)
    elif keuze == "c":
        aantal = multiplication(n1, n2)
        print(aantal)
    elif keuze == "d":
        aantal = division(n1, n2)
        print(aantal)
    elif keuze == "e":
        n2 = 1
        aantal = addition(n1, n2)
        print(aantal)
    elif keuze == "f":
        n2 = 1
        aantal = subtraction(n1, n2)
        print(aantal)
    elif keuze == "g":
        n2 = 2
        aantal = multiplication(n1, n2)
        print(aantal)
    else:
        n2 = 2
        aantal = division(n1, n2)
        print(aantal)

    keuze = input(f"Wil je wat met het antwoord ({aantal}) doen? A) iets optellen, B) iets aftrekken, C) met iets vermenigvuldigen, D) ergens door delen, E) ophogen, F) verlagen, G) verdubbelen, H) halveren of I) Nee?")
    




    






