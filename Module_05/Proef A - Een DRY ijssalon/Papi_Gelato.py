orders = []
Bestelling = {'Bolletjes':1.10 ,'Hoorntje':1.25,'Bakje':0.75 }


def get_aantal_bolletjes(vraag)-> int:
    aantal = None
    c = True
    while c:
        try:
            aantal = int(input(vraag))
            c = False
        except ValueError:
            print('Voer een getal in!')
        if aantal > 8:
            print("Sorry, zulke grote bakken hebben we niet")
    return aantal



def get_hoorntje_of_bakje(aantal_bolletjes):
    vraag = 'bakje'
    if aantal_bolletjes <= 3 and aantal_bolletjes > 0:
        c = True
        while c:
            vraag = input(f"Wilt u deze {aantal_bolletjes} bolletjes in een hoorntje of een bakje?: ")
            if vraag == "hoorntje" or vraag == 'bakje':
                c = False
            else:
                print("Sorry,dat snap ik niet...") 

    else:
        print(f'Dan krijgt u van mij een bakje met {aantal_bolletjes} bolletjes')
    return vraag
    

def get_ijs() -> list:
    ijs_dict = {}

    aantal_bolletjes  = get_aantal_bolletjes('Hoeveel bolletje wilt uw hebben? :')

    ijs_dict["bolletjes"] = aantal_bolletjes
    ijs_dict["keuzen"] = get_hoorntje_of_bakje(aantal_bolletjes)
    return ijs_dict     

    
def bon():

    Totaal = 0
    bakjes = 0
    hoorntjes = 0
    aantal_bolletjes = 0

    for i in orders:
        aantal_bolletjes += i['bolletjes']
        if i['keuzen'] == 'hoorntjes':
            hoorntjes += 1
        elif i['keuzen'] == 'bakje':
            bakjes += 1

        Bereking_bolletjes = round(i['bolletjes'] * Bestelling['Bolletjes'],2)
        Bereking_keuzen_b = round(bakjes * Bestelling['Bakje'],2)
        Bereking_keuzen_h = round(hoorntjes * Bestelling['Hoorntje'],2)
        # print(Bereking_bolletjes)
        # print(Bereking_keuzen_h)
        Totaal += Bereking_bolletjes + Bereking_keuzen_h + Bereking_keuzen_b

        print('------["Papi Gelato"]--------')
        
        print("Bolletjes   "+ str(i['bolletjes']) +' * €'+ str(Bestelling['Bolletjes'])+' = €'+ str(Bereking_bolletjes))
        print("Hoorntjes   "+ str(hoorntjes) +' * €' + str(Bestelling['Hoorntje'])+' = €'+ str(Bereking_keuzen_h))
        print("Bakjes      "+ str(bakjes) +' * €'+ str(Bestelling['Bakje'])+' = €'+ str(Bereking_keuzen_b))
        print('                  --------- +')
        print('Totaal               ' + '= £'+ str(Totaal)+'\n')

        print('Bedankt en tot ziens!')
                

print("Welkom bij Papi Gelato je mag alle smaken kiezen zolang het maar vanille ijs is")
orders.append(get_ijs())


d = True
while d:
    bestelling_vraag = input("Wilt u nog meer bestellen? (ja/nee) :")

    if bestelling_vraag == "ja":
        orders.append(get_ijs())
    elif bestelling_vraag == "nee":
        print("Hier zijn uw bestellingen:")
        for i in orders:
            print(f"{i['bolletjes']} bolletjes in een {i['keuzen']}")
        bon()
        d = False
    else:
        print("Sorry,dat snap ik niet...")

