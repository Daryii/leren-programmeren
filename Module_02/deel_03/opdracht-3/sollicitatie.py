print ("Solicitatieformulier Circusdirecteur voor Circus HotelDeBotel")
print ("Er wordt u een aantal relevante vragen gesteld...")
print ("Gelieve die naar eer en geweten in te vullen. ")
print ("Als blijkt dat u aan de criteria voldoet dan komt u in")
print ("aanmerking voor een serieus sollicitatiegesprek!")
print ("Ontspan maar blijf wakker hier komen de vragen." )

naam = input ('wat is je naam ?')
diploma = input('Ben je bezit van een Diploma MBO-4 ondernemen ja/of ?')
vrachtwagen_R = input('ben je bezit van een geldig Vrachtwagen rijbewijs ja/of ?')               
hoge_hoed = input('ben je  bezit van een hoge hoed ja/of ?')
geslacht = input('wat is uw geslacht ?')

if geslacht == 'man':
    snor =input('heeft uw een snor ja/nee ?')
    if snor == 'ja':
       size_snor= int(input('Hoelang is uw snor lengte is cm ?'))

elif geslacht == 'vrouw':
    krullen = input ('Heeft u rood krullend haar? ja/nee ?')
    if krullen == "ja":
        krullen_lengte = int(input('Wat is krullend haar lengte in cm'))

lengte = int(input('Wat is uw lengte in cm ?') )
gewicht = int(input ('Wat is uw gewicht in kg ?'))
Certificaat = input('Heeft uw een Certificaat van Overleven met gevaarlijk personeel (ja 0f nee)?')
praktijk = int(input ('Hoeveel jaar ervaring heeft u met dieren-dressuur? ')) 
jongleren = int(input('Hoeveel jaar ervaring heeft u met jongleren ?')) 
acrobatiek = int(input ('Hoeveel jaar ervaring heeft u met acrobatiek ?')) 
 
ervaring = praktijk > 4 and jongleren > 5 and acrobatiek > 3 

if ((geslacht == 'man' and snor == "ja" and size_snor >= 10) or (geslacht == 'vrouw' and krullen == 'ja' and krullen_lengte >= 20)) and diploma == "ja" and vrachtwagen_R == "ja" and hoge_hoed == "ja" and lengte > 150 and gewicht > 90  and Certificaat == 'ja'and ervaring :
    print ("Proficiat! U komt in aanmerking voor een sollicitatiegesprek, stuur snel uw CV!")
else :
    print ("Helaas u voldoet niet aan onze strenge eisen voor de functie van Circusdirecteur")