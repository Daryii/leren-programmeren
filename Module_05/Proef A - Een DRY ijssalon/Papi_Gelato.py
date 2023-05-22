def get_aantal_bolletjes(vraag)-> int:
    aantal = None
    c = True
    while c:
        try:
            aantal = int(input(vraag))
            c = False
        except ValueError:
            print('Voer een getal in!')
    return aantal



def get_hoorntje_of_bakje(aantal_bolletjes):
    c = True
    while c:
        vraag = input(f"Wilt u deze {aantal_bolletjes} bolletjes in een hoorntje of een bakje?: ")
        if vraag == "hoorntje" or vraag == 'bakje':
            c = False
        else:
            print("Sorry,dat snap ik niet...")
    return vraag
    


def get_ijs() -> list:
    ijs_dict = {}
    vraag = ''
    
    aantal_bolletjes  = get_aantal_bolletjes('Hoeveel bolletje wilt uw hebben? :')

    if aantal_bolletjes <= 3 and aantal_bolletjes > 0:
        vraag = get_hoorntje_of_bakje(aantal_bolletjes)
        
    elif aantal_bolletjes >= 4 and aantal_bolletjes <= 8:
        print(f'Dan krijgt u van mij een bakje met {aantal_bolletjes} bolletjes')
    elif aantal_bolletjes > 8:
        print("Sorry, zulke grote bakken hebben we niet")
        return
    else:
        print("Sorry,dat snap ik niet...")
       

    ijs_dict["bolletjes"] = aantal_bolletjes
    ijs_dict["keuzen"] = vraag
    return ijs_dict     

    
            
orders = []

print("Welkom bij Papi Gelato je mag alle smaken kiezen zolang het maar vanille ijs is")
orders.append(get_ijs())


d = True
while d:
    bestelling_vraag = input("Wilt u nog meer bestellen?: ")

    if bestelling_vraag == "ja":
        orders.append(get_ijs())
    elif bestelling_vraag == "nee":
        print("Hier zijn uw bestellingen:")
        for i in orders:
            if i['keuzen'] == 'bakje' or i['keuzen'] == '':
                print(f"{i['bolletjes']} bolletjes in een bakje")
            else:
                print(f"{i['bolletjes']} bolletjes in een {i['keuzen']}")
        d = False
    else:
        print("Sorry,dat snap ik niet...")

