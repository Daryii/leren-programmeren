from functions import*

def get_ijs(soort_k) -> list:
    ijs_dict = {}


    
    aantal_bolletjes  = get_aantal_bolletjes(soort_k)
    ijs_dict["bolletjes"] = aantal_bolletjes
    ijs_dict['smaak'] = get_smaak(aantal_bolletjes,soort_k)
    if soort_k == 'zakelijke_klant':
        ijs_dict["keuzen"] = ''
    else:
        ijs_dict["keuzen"] = get_hoorntje_of_bakje(aantal_bolletjes)
    if soort_k == 'zakelijke_klant':
        ijs_dict['Toppings'] = {}
    else:
        ijs_dict['Toppings'] = Get_toppings()

    return ijs_dict
 

  
BESTELLINGEN = []

print("Welkom bij Papi Gelato\n")
soort_klant = get_soort_klant()

BESTELLINGEN.append(get_ijs(soort_klant))


while True:
    vraag = input("Wilt u nog meer bestellen? (ja/nee): ")

    if vraag == "nee":
        print("Hier is uw bestelling:")
        bon(BESTELLINGEN,soort_klant)
        break
    elif vraag == 'ja':
        BESTELLINGEN.append(get_ijs(soort_klant))
        print("------------------------------------")
       
    else:
        print("Sorry, dat begrijp ik niet.\n")

   