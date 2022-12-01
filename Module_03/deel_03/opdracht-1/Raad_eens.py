import random


vraag = input("Ben je ready om te getallen te raden?:")
if vraag == ("ja"):
    print("oke jij gaat getallen raden.")
else:
    print("GAME OVER!!")
    exit()
 
#aantal_ronde = 20
#aantal_pogingen = 10
poging = 0
score = 0
ronde = 0



# while aantal_ronde < aantal_pogingen:
for u in range(20):
    num = random.randint(1, 1000)
    print(num)

    # while aantal_pogingen < aantal_ronde:
    for e in range(10):
        raden = int(input("raad een getal 0 - 1000:"))
        if raden == num:
                print("Je hebt het goed !")
                score += 1
                break
        verschil = abs(raden - num)
        if verschil <= 20:
            print("je bent heel warm!")
        elif verschil <= 50:
            print("je bent warm!")
            poging += 1
    ja_of_nee = input("wil je nog een keer raden ja of nee?: ")
    if ja_of_nee == "nee":
        print("Game over !")
        exit()
    else:
        print(f"je hebt {score} van {ronde}")
        print(f"je score is {score} en je hebt {ronde} rondes gespeeld")

