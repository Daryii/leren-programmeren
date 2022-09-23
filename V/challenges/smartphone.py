IPHONE = "iphone"
GALAXY= "galaxy"

prijs_Iphone_13=  int(input("Hoe duur is de Iphone ?"))
Prijs_Samssung_22= int(input( "Hoe duur is de Samsung ?"))

print (prijs_Iphone_13)
print (Prijs_Samssung_22)

if prijs_Iphone_13 > Prijs_Samssung_22:
        duurste_tele = "iphone"
        goedkoopste_tele = "galaxy"
        prijs_duurste = prijs_Iphone_13
        prijs_goedkoopste = Prijs_Samssung_22
else:
    duurste_tele = "galaxy"
    goedkoopste_tele = "iphone"
    prijs_duurste = Prijs_Samssung_22   
    prijs_goedkoopste = prijs_Iphone_13

print=  (f"De  {duurste_tele} is het duurste, de telefoon kost: {prijs_duurste}euro")
print=  (f"De  {goedkoopste_tele} is het duurste, de telefoon kost: {prijs_goedkoopste}euro")

# hier het advies
verschil = prijs_Iphone_13 - Prijs_Samssung_22
if verschil > 50:
    advies_telefoon = prijs_Iphone_13 

    print (f"advies is dus de {advies_telefoon} te koop . verschil: {verschil}")