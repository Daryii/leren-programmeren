zak = {}

while True:
    product = input("Voeg item toe ? :").lower
    if product in zak:
        zak
        #hoeveelheid= int(input(f"Hoeveel {product} wil je?: "))
    
    getal = 1
    if product and hoeveelheid not in zak:
        zak.update({hoeveelheid: product})
    elif product and hoeveelheid in zak:
        zak[product and hoeveelheid] +=1
        
    print(" -[ BOODSCHAPPENLIJST ]- ")
    for key,value in  zak.items():
        print(key,value)
        print(f"{value}x {key}")
    print("-----------------------")
   


