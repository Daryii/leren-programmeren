orders = []
Bestelling = {'Bolletjes':1.10 ,'Hoorntje':1.25,'Bakje':0.75 }


def get_aantal_bolletjes(vraag)-> int:
    while True:
        try:
            aantal = int(input(vraag))
            if aantal > 8:
                print("Sorry, zulke grote bakken hebben we niet\n")
            else:
                return aantal
        except ValueError:
            print('Voer een getal in!')  

def get_hoorntje_of_bakje(aantal_bolletjes):
    vraag = 'bakje'
    if aantal_bolletjes <= 3 and aantal_bolletjes > 0:
        c = True
        while c:
            vraag = input(f"Wilt u deze {aantal_bolletjes} bolletjes in een hoorntje of een bakje?: ")
            if vraag == "hoorntje" or vraag == 'bakje':
                c = False
            else:
                print("Sorry,dat snap ik niet...\n") 

    else:
        print(f'Dan krijgt u van mij een bakje met {aantal_bolletjes} bolletjes\n')
    return vraag
    

def get_ijs() -> list:
    ijs_dict = {}

    aantal_bolletjes  = get_aantal_bolletjes('Hoeveel bolletje wilt uw hebben? :')

    ijs_dict["bolletjes"] = aantal_bolletjes
    ijs_dict['smaak'] = get_smaak(aantal_bolletjes)
    ijs_dict["keuzen"] = get_hoorntje_of_bakje(aantal_bolletjes)
    
    return ijs_dict     

    
def bon():

    Totaal = 0
    bakjes = 0
    hoorntjes = 0
    aantal_bolletjes = 0

    for i in orders:
        aantal_bolletjes += i['bolletjes']
        if i['keuzen'] == 'hoorntje':
            hoorntjes += 1
        elif i['keuzen'] == 'bakje':
            bakjes += 1

        Bereking_bolletjes = round(aantal_bolletjes * Bestelling['Bolletjes'],2)
        Bereking_keuzen_b = round(bakjes * Bestelling['Bakje'],2)
        Bereking_keuzen_h = round(hoorntjes * Bestelling['Hoorntje'],2)
        
        Totaal += Bereking_bolletjes + Bereking_keuzen_h + Bereking_keuzen_b

        print('------["Papi Gelato"]--------\n')

        if aantal_bolletjes > 0:
            for smaak,waarde in i['smaak'].items():
                smaak_bereking = round(waarde * Bestelling['Bolletjes'],2)
                if smaak == 'Aardbei':
                    print("B.Aardbei        "+ str(waarde) +' * €'+ str(Bestelling['Bolletjes'])+' = €'+ str(smaak_bereking)) 
                elif smaak == 'Chocolade':
                    print("B.Chocolade      "+ str(waarde) +' * €'+ str(Bestelling['Bolletjes'])+' = €'+ str(smaak_bereking)) 
                elif smaak == 'Munt':
                    print("B.Munt           "+ str(waarde) +' * €'+ str(Bestelling['Bolletjes'])+' = €'+ str(smaak_bereking)) 
                elif smaak == 'Vanille':
                    print("B.Vanille        "+ str(waarde) +' * €'+ str(Bestelling['Bolletjes'])+' = €'+ str(smaak_bereking)) 
        if hoorntjes > 0:
            print("Hoorntjes        "+ str(hoorntjes) +' * €' + str(Bestelling['Hoorntje'])+' = €'+ str(Bereking_keuzen_h))
        if bakjes > 0:
            print("Bakjes           "+ str(bakjes) +' * €'+ str(Bestelling['Bakje'])+' = €'+ str(Bereking_keuzen_b))

        print('                        --------- +')
        print('Totaal                     ' + '= £'+ str(Totaal)+'\n')

        print('Bedankt en tot ziens!\n')
                
def get_smaak(aantal_bollejes)-> list:
    smaken_dict = {}

    Aardbei = 0
    Chocolade = 0
    Munt = 0
    Vanille = 0

    for i in range(aantal_bollejes):
        c = True
        while c:
            vraag = input(f'Welke smaak wilt u voor bolletje nummer {i+1}? A) Aardbei, C) Chocolade, M) Munt of V) Vanille?').lower()
            if vraag in ['a','c','m','v']:
                c = False
                if vraag == 'a':
                    Aardbei += 1
                    smaken_dict['Aardbei'] = Aardbei
                elif vraag == 'c':
                    Chocolade += 1
                    smaken_dict['Chocolade'] = Chocolade
                elif vraag == 'm':
                    Munt += 1
                    smaken_dict['Munt'] = Munt
                elif vraag == 'v':
                    Vanille += 1
                    smaken_dict['Vanille'] = Vanille
                else:
                    print("Sorry dat snap ik niet....")
                    i -= 1
            else:
                c = True

    return smaken_dict

print()
print("Welkom bij Papi Gelato\n")
orders.append(get_ijs())


d = True
while d:
    bestelling_vraag = input("Wilt u nog meer bestellen? (ja/nee) :")

    if bestelling_vraag == "ja":
        orders.append(get_ijs())
    elif bestelling_vraag == "nee":
        print(orders)
        print("Hier zijn uw bestellingen:\n")
        bon()
        d = False
    else:
        print("Sorry,dat snap ik niet...\n")
