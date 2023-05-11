def get_ijs(bestellingen) -> list:
    ijs_dict = {}
    vraag = ""
    aantal_bolletjes = int(input("Hoeveel bolletjes wilt u? : "))

    a = True
    while a == True:
        if aantal_bolletjes != int:
            a = False
        else:
            print("voer een getal in!")
            a = True

    if aantal_bolletjes <= 3 and aantal_bolletjes > 0:
        c = True
        while c == True:
            vraag = input(f"Wilt u deze {aantal_bolletjes} bolletjes in een hoorntje of een bakje?: ")
            if vraag == "bakje" or vraag == "hoorntje":
                c = False
            else:
                print("Sorry,dat snap ik niet...")

    elif aantal_bolletjes >= 4 and aantal_bolletjes <= 8:
        print(f'Dan krijgt u van mij een bakje met {aantal_bolletjes} bolletjes')

    elif aantal_bolletjes > 8:
        print("Sorry, zulke grote bakken hebben we niet")
        return bestellingen
    else:
        print("Sorry,dat snap ik niet...")
        return bestellingen

    ijs_dict["bolletjes"] = aantal_bolletjes
    ijs_dict["keuzen"] = vraag
    bestellingen.append(ijs_dict)

    while True:
        bestelling_vraag = input("Wilt u nog meer bestellen?: ")
        if bestelling_vraag == "ja":
            get_ijs(bestellingen)
        elif bestelling_vraag == "nee":
            print("Hier zijn uw bestellingen:")
            for i in bestellingen:
                if i in ijs_dict["keuzen"]:
                    print(f"{i['bolletjes']} bolletjes in een {i['keuzen']}")
            else:
                print(f"{i['bolletjes']} bolletjes in een bakje")
            return bestellingen
        else:
            print("Sorry,dat snap ik niet...")
            
orders = []
get_ijs(orders)