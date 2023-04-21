aantal_totaal = 0

def print_bestelling():
    print(f"U heeft in totaal {aantal_totaal} bolletjes besteld. Bedankt en tot ziens!")

def bestel_bolletjes():
    global aantal_totaal
    aantal_bolletjes = input("Hoeveel bolletjes wilt u? : ")
    if not aantal_bolletjes.isdigit():
        print("Sorry, dat is geen geldig aantal bolletjes.")
        bestel_bolletjes()
        return
    
    aantal_bolletjes = int(aantal_bolletjes)

    
    if aantal_bolletjes <= 3 and aantal_bolletjes > 0:
        aantal_totaal += aantal_bolletjes
        c = True
        while c == True:
            vraag = input(f"Wilt u deze {aantal_totaal} bolletjes in een hoorntje of een bakje?: ")
            if vraag == "bakje" or vraag == "hoorntje":
                c = False
                print(f"Hier is uw {vraag} met {aantal_totaal} bolletjes")
            else:
                print("Sorry,dat snap ik niet...")
        
    elif aantal_bolletjes >= 4 and aantal_bolletjes <= 8:
        aantal_totaal += aantal_bolletjes
        print(f'Dan krijgt u van mij een bakje met {aantal_totaal} bolletjes')
    elif aantal_bolletjes > 8:
        print("Sorry, zulke grotebakken hebben we niet")
        bestel_bolletjes()
    else:
        exit()



def bestel_meer():
    while True:
        bestelling_vraag = input("Wilt u nog meer bestellen?: ")
        if bestelling_vraag == "ja":
            bestel_bolletjes()
        elif bestelling_vraag == "nee":
            print_bestelling()
            break
        else:
            print("Sorry,dat snap ik niet...")

def start():
    print("Welkom bij Papi Gelato je mag alle smaken kiezen zolang het maar vanille ijs is")
    bestel_bolletjes()
    bestel_meer()

start()
            


