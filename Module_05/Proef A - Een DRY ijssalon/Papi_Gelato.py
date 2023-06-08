PRIJZEN = {'Bolletjes':1.10 ,'Hoorntje':1.25,'Bakje':0.75 ,'Slagroom': 0.50 ,'Sprinkels':0.30 , "Caramel_Saus":0.90 , "L":9.80}
BTW = 9

def get_aantal_bolletjes(klant)-> int:
    while True:
        try:
            if klant == 'zakelijke_klant':
                aantal = int(input('Hoeveel liter wilt uw hebben? :'))
            elif klant == 'particuliere_klant':
                aantal = int(input('Hoeveel bolletjes wilt uw hebben? :'))
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


    soort_k = ijs_dict['soort_k'] = get_soort_klant() 
    aantal_bolletjes  = get_aantal_bolletjes(soort_k)
    ijs_dict["bolletjes"] = aantal_bolletjes
    ijs_dict['smaak'] = get_smaak(aantal_bolletjes,soort_k)
    if soort_k == 'zakelijke_klant':
        pass
        ijs_dict["keuzen"] = ''
    else:
        ijs_dict["keuzen"] = get_hoorntje_of_bakje(aantal_bolletjes)
    if soort_k == 'zakelijke_klant':
        pass
        ijs_dict['Toppings'] = {}
    else:
        ijs_dict['Toppings'] = Toppings()

    return ijs_dict
    
def bon():
    Totaal_bedrag = 0
    bakjes = 0
    hoorntjes = 0
    aantal_bolletjes = 0
    smaken_dict = {}
    Topping_dict = {}

    # Totaal berekenen.
    for i in BESTELLINGEN:
        aantal_bolletjes += i['bolletjes']

        if i['keuzen'] == 'hoorntje':
            hoorntjes += 1 
        elif i['keuzen'] == 'bakje':
            bakjes += 1

        Toppings_v = i['Toppings']
        for key, value in Toppings_v.items():
            if key in Topping_dict:
                Topping_dict[key] += value
            else:
                Topping_dict.update({key: value})

        smaken = i['smaak'] 
        for k, v in smaken.items():
            if k in smaken_dict:
                smaken_dict[k] += v
            else:
                smaken_dict.update({k: v})

        Bereking_bolletjes = round(i['bolletjes'] * PRIJZEN['Bolletjes'], 3)
        Bereking_keuzen_b = round(bakjes * PRIJZEN['Bakje'], 3)
        Bereking_keuzen_h = round(hoorntjes * PRIJZEN['Hoorntje'], 3)

        Totaal_bedrag += Bereking_bolletjes + Bereking_keuzen_h + Bereking_keuzen_b

    # Totaal printen
    print('------["Papi Gelato"]--------\n')

    if aantal_bolletjes > 0:
        for smaak, waarde in smaken_dict.items():           
            for u in BESTELLINGEN:
                if u['soort_k'] == 'zakelijke_klant':
                    print(f"L.{smaak}        {waarde} * € {PRIJZEN['L']} = € {round(waarde * PRIJZEN['L'], 2)}")
                else:
                    print(f"B.{smaak}        {waarde} * € {PRIJZEN['Bolletjes']} = € {round(waarde * PRIJZEN['Bolletjes'], 2)}")

    if hoorntjes > 0:
        print(f"Hoorntjes        {hoorntjes} * € {PRIJZEN['Hoorntje']} = € {Bereking_keuzen_h}")
    if bakjes > 0:
        print(f"Bakjes           {bakjes} * €{PRIJZEN['Bakje']} = € {Bereking_keuzen_b}")

    topping_b = 0
    if Topping_dict:
        for k, v in Topping_dict.items():
            topping_b += PRIJZEN[k] * v
            if k == 'Caramel_Saus' and hoorntjes > 0:
                print(f"T.{k}           = € {topping_b - 0.30:.2f}")
            else:
                print(f"T.{k}                = € {topping_b}")

    print('                        --------- +')

    berekening = sum(waarde * PRIJZEN['L'] for waarde in smaken_dict.values())
    if Topping_dict == {}:
        print(f'Totaal_bedrag                = € {berekening}')
        print(f"BTW:                         = € {berekening/100 * BTW:.2f}")
    else:
        print(f'Totaal_bedrag                = € {Totaal_bedrag + topping_b:.2f}\n')

    print('Bedankt en tot ziens!\n')
    
def get_smaak(aantal_bollejes,klant)-> list:
    smaken_dict = {}

    Aardbei = 0
    Chocolade = 0
    Munt = 0
    Vanille = 0

    for i in range(aantal_bollejes):
        c = True
        while c:
            if klant == 'zakelijke_klant':
                soort_ijs = 'liter'
            elif klant == 'particuliere_klant':
                soort_ijs = 'bolletje'
            smaak_v = input(f'Welke smaak wilt u voor {soort_ijs} nummer {i+1}? A) Aardbei, C) Chocolade, M) Munt of V) Vanille?').lower()
            c = False
            
            if smaak_v in ['a','c','m','v']:
                c = False
                if smaak_v == 'a':
                    Aardbei += 1
                    smaken_dict['Aardbei'] = Aardbei
                elif smaak_v == 'c':
                    Chocolade += 1
                    smaken_dict['Chocolade'] = Chocolade
                elif smaak_v == 'm':
                    Munt += 1
                    smaken_dict['Munt'] = Munt
                elif smaak_v == 'v':
                    Vanille += 1
                    smaken_dict['Vanille'] = Vanille
                else:
                    print("Sorry dat snap ik niet....")
                    i -= 1
            else:
                c = True

    return smaken_dict

def Toppings():

    Toppings_dict = {}
    Slagroom = 0
    Sprinkels = 0
    Caramel_Saus = 0


    T = True
    while T:
        vraag = input('Wat voor topping wilt u:\n A) Geen \n B) Slagroom \n C) Sprinkels \n D) Caramel Saus : ').lower()
        if vraag in ['a','b','c','d']:
            T = False
            if vraag == 'a':
                print('Geen extra kosten')
            elif vraag == 'b':
                Slagroom += 1
                Toppings_dict['Slagroom'] = Slagroom
            elif vraag == 'c':
                Sprinkels += 1
                Toppings_dict['Sprinkels'] = Sprinkels
            elif vraag == 'd':
                Caramel_Saus += 1
                Toppings_dict['Caramel_Saus'] = Caramel_Saus
            else:
                print("Sorry dat snap ik niet....")

        else:
            T = True
    return Toppings_dict

def get_soort_klant():
    c = True
    while c:
        vraag = input("Bent u a) een particuliere klant of b) een zakelijke klant? (a of b): ").lower()
        if vraag == 'a':
            c = False
            return 'particuliere_klant'
        elif vraag == 'b':
            c = False
            return 'zakelijke_klant'
        else:
            print("Sorry,dat snap ik niet...\n") 

  
BESTELLINGEN = []
laatste_bestelling = None


print("Welkom bij Papi Gelato\n")

while True:
    BESTELLINGEN.append(get_ijs())
    laatste_bestelling = BESTELLINGEN[-1]

    vraag = input("Wilt u nog meer bestellen? (ja/nee): ")

    if vraag == "nee":
        print("Hier zijn uw bestelling(en):\n")
        bon()
        break
    elif vraag != "ja":
        print("Sorry, dat begrijp ik niet. Uw bestelling(en) worden afgedrukt:\n")
        bon()
        break

    print("Hier is uw laatste bestelling:")
    bon()
    print("------------------------------------")
    BESTELLINGEN = []
