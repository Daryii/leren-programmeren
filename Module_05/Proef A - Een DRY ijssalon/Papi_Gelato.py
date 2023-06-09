from functions import*

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
        print("Sorry, dat begrijp ik niet.\n")
        bon()
        break

    print("Hier is uw laatste bestelling:")
    bon()
    print("------------------------------------")
    BESTELLINGEN = []
