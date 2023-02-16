

def namen_leeftijd():
    naam = input("voer je naam in: ")
    leeftijd = int(input("voer je leeftijd in: "))
    return {"naam":naam,"leeftijd" : leeftijd}

mijn_lijst = []

while True:
    x = namen_leeftijd()
    mijn_lijst.append(x)

    vraag_3 = input("voer stop als uw wilt stoppen: ")
    if vraag_3 == "stop":
        break

for i in mijn_lijst:
    print(f"{i['naam']} is {i['leeftijd']} jaar")


