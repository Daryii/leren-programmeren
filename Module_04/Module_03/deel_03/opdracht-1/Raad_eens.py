import random


score = 0
ronde = 0

vraag = input("Ben je ready om te getallen te raden?:")
if vraag == ("ja"):
    print("oke jij gaat getallen raden.")


    while ronde < 20:
        num = random.randint(1, 1000)
        print(num)

        poging = 0
        while poging < 10:
            raden = int(input("raad een getal 0 - 1000:"))
            if raden == num:
                    print("Je hebt het goed !")
                    score += 1
                    poging = 10
            else:
                verschil = abs(raden - num)
                poging += 1
                if raden > num:
                    print("Lager")
                elif raden < num:
                    print("Hoger")
                if verschil <= 20:
                    print("je bent heel warm!")
                elif verschil <= 50:
                    print("je bent warm!")
        ronde += 1
        if ronde < 20:
            ja_of_nee = input("wil je nog een keer raden ja of nee?: ")
            if ja_of_nee == "nee":
                ronde = 20
            
        print(f"je hebt {score} van {ronde}")
        print(f"je score is {score} en je hebt {ronde} rondes gespeeld")
            
else:
    print("GAME OVER!!")
