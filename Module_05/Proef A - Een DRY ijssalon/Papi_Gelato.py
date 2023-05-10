def bestel_bolletjes():
    aantal_bolletjes = int(input("Hoeveel bolletjes wilt u? : "))
   
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
        bestel_meer()
    elif aantal_bolletjes > 8:
        print("Sorry, zulke grotebakken hebben we niet")
        bestel_bolletjes()
        return
    else:
        print("Sorry,dat snap ik niet...")
        return
        



def bestel_meer(aantal_bolletjes,vraag):
    while True:
        bestelling_vraag = input("Wilt u nog meer bestellen?: ")
        if bestelling_vraag == "ja":
            bestel_bolletjes()
        elif bestelling_vraag == "nee":
           
            print(f"Hier is uw {vraag} met {aantal_bolletjes} bolletjes")
            break
        else:
            print("Sorry,dat snap ik niet...")

def start():
    print("Welkom bij Papi Gelato je mag alle smaken kiezen zolang het maar vanille ijs is")
    bestel_bolletjes()
    bestel_meer()

start()
            


