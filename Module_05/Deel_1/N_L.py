def namen_leeftijden():
    lijst = []
    while True:
        vraag1 = input("Voer hier je naam in: ")
        if vraag1 == "stop":
            break
        vraag2 = input("Voer hier je leeftijd in: ")
        if not vraag2.isdigit():
            print("Leeftijd moet een nummer zijn.")
            continue
        lijst.append({"name":vraag1, "age":int(vraag2)})
    
    for i in lijst:
        print(f"{i['name']} is {i['age']} jaar oud")

namen_leeftijden()
