def Papi_Gelato_1():
        
    print("Welkom bij Papi Gelato je mag alle smaken kiezen zolang het maar vanille ijs is")

    aantal_bolletjes = int(input("Hoeveel bolletjes wilt u? :"))
    aantal = ''
    if aantal_bolletjes <= 3 and aantal_bolletjes > 0:
        aantal = aantal_bolletjes
        c = True
        while c == True:
            vraag = input(f"Wilt u deze {aantal} bolletjes in een hoorntje of een bakje?: ")
            if vraag == "bakje" or vraag == "hoorntje":
                c = False
                print(f"Hier is uw {vraag} met {aantal} bolletjes")
            else:
                print("Sorry,dat snap ik niet...")
        
    elif aantal_bolletjes == 4 and aantal_bolletjes <= 8:
        print(f'Dan krijgt u van mij een bakje met {aantal} bolletjes')
    elif aantal_bolletjes > 8:
        print("Sorry, zulke grotebakken hebben we niet")
        Papi_Gelato_1()
    else:
        exit()
Papi_Gelato_1()

v = True
while v == True:
    bestelling_vraag = input("Wilt u nog meer bestellen?: ")
    if bestelling_vraag == "ja":
        Papi_Gelato_1()
        v = False
    elif bestelling_vraag == "nee":
        print("Bedankt en tot ziens!")
        v = False
    else:
        print("Sorry,dat snap ik niet...")
        
        


        