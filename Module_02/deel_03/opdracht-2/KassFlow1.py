geel= input("Is de kaas geel?")
if geel == "ja":
    gaten = input("Zitten er gaten in?")
    if gaten == "ja":
        duur = input("Is de kaas belagelijk duur?")
        if duur == "ja":
                print ("Emmenthaler")
                
        elif duur == "nee":
                print ("Leerdammer")
                
    elif gaten == "nee": 
        hard = input("Is de kaas hard als steen?")
        if hard == "ja":
            print ("Parmigiano Reggiano")
        elif hard == "nee":
             print ("Goudse Kaas")

if geel == "nee":
    blauwe_schimmel = input("Heeft de kaas blauwe schimmel?")
    if blauwe_schimmel == "ja":
        korst1= input ("Heeft de kaas een korst1?")
        if korst1 == "ja":
            print ("Blue de Rochbaren")

        elif korst1 == "nee":
            print("foume d'Ambert")
            
    elif blauwe_schimmel == "nee":
        korst = input("Heeft de kaas een korst?")
        ruikt = input ("ruikt het kaas ?")
        if ruikt == "ja":
            print ("cemembert")
        else :
            print ("brie")

        if korst == "ja":
             print ("Camembert") 
        elif korst == "nee":
            print ("Mozzarella") 
       

                


    

