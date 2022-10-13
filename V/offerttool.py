
hoogte = int(input("Voe r hier de hoogte in:"))
breedte = int(input("Voer hier de breedte in:"))
diepte = float(input("Voer hier de diepte in:"))
km = int(input("Voer hier de km's in:"))

inhoudzwembad = {hoogte*breedte*diepte} 
afvoeren_g = {hoogte*breedte*diepte*32.50}
uitgraven = {hoogte*breedte*diepte*25}
voorrijkosten = {km*1.15+100}
totaal = (hoogte*breedte*diepte*32.50 + hoogte*breedte*diepte*25 )


if km < 50 and inhoudzwembad < 20 :
    print (100 +1.25)
    if km >= 50 and inhoudzwembad < 20 :
       print (100 +1.15)
elif km < 50 and inhoudzwembad > 20 :
    print (250+2.15)
else:
    print( 250+2.03)

print (f"Offerte als volgt uit :",inhoudzwembad,"m3")
print ("Uitgraven: €",uitgraven,"")
print ("Afvoeren grond: €",afvoeren_g,"")
print ("Voorrijkosten: €",voorrijkosten,"")
print ("Totaal: €",totaal,"")


