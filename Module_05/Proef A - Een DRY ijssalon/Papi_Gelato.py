
#om het aantal bolletjes op te vragen
def get_aantal_bolletjes(vraag :str)-> int:

    aantal = int(input(vraag))
    a = True
    while a == True:
        if aantal != int:
            a = False
        else:
            print("voer een getal in!")
            a = True
    return aantal


def get_hoorntje_of_bakje(aantal_bolletjes):
    c = True
    while c == True:
        vraag = input(f"Wilt u deze {aantal_bolletjes} bolletjes in een hoorntje of een bakje?: ")
        if vraag == "bakje" or vraag == "hoorntje":
            c = False
        else:
            print("Sorry,dat snap ik niet...")
        return aantal_bolletjes
    
#maakt een ijsje een geeft het terug
def get_ijs() -> list:
    
    ijs_dict = {}
    vraag = ""
    

    aantal_bolletjes  = get_aantal_bolletjes("Hoeveel bolletjes wilt u? : ")

    if aantal_bolletjes <= 3 and aantal_bolletjes > 0:
        
            
    elif aantal_bolletjes >= 4 and aantal_bolletjes <= 8:
        print(f'Dan krijgt u van mij een bakje met {aantal_bolletjes} bolletjes')
   
    elif aantal_bolletjes > 8:
        print("Sorry, zulke grote bakken hebben we niet")
        
    else:
        print("Sorry,dat snap ik niet...")
       

    ijs_dict["bolletjes"] = aantal_bolletjes
    ijs_dict["keuzen"] = vraag
    return ijs_dict     

    
            
orders = []

print("Welkom bij Papi Gelato je mag alle smaken kiezen zolang het maar vanille ijs is")
orders.append(get_ijs())


d = True
while d == True:
    bestelling_vraag = input("Wilt u nog meer bestellen?: ")
    if bestelling_vraag == "ja":
        orders.append(get_ijs())
        print(orders)
    elif bestelling_vraag == "nee":
        print("Hier zijn uw bestellingen:")
        for i in orders:
            print(f"{i['bolletjes']} bolletjes in een {i['keuzen']}")
        d = False
    else:
        print("Sorry,dat snap ik niet...")

