def namen_leeftijden():
    lijst = []
       
    while True:
        vraag1 = input("voer hier je naam in: ")
        if vraag1 == "stop":
            break
        vraag2 = input("voer hier je leeftijd in: ")
        if vraag2 == "stop":
            break
        lijst.append([{"name":vraag1},
    {"age":vraag2}])

    for i in lijst:
        print(f"{i[0]['name']} is {i[1]['age']} jaar")


namen_leeftijden()