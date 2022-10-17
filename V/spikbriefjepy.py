 ################################################################################################################################################################

# commentaar schrij je met #
 # Data types
 # string = woord of zin
 #Int = geheel getal

################################################################################################################################################################

 # variabele = slime gehogen
 # conditie = voorwaarde if
 # Expresseie = * / + - 
 # x is opereters
 # // for bereken van eind getal , en %  
 # true ,false = is boolean

################################################################################################################################################################

# Varebielen v.B
# aantal type 2 =  

################################################################################################################################################################

# Waarom gebruik we '' ?
# voor spacie

################################################################################################################################################################

# print is het laten zien in het computer 
# print kan ook in een keer veel laten zien.
# als je wil printen moet je verschilled () gebruiken
# als je een tekst met de order wilt doorgeven moet het in "" of '' gebruiken

################################################################################################################################################################

from random import Random


aantal= 5 #edit is integer, integer is een geheel getal (Int)
omschrijving = 'milk 2 liter' # edit is een string (str)
stukjeprijs = 0.89 # edit is een float, float is een getal met een komma

#Voorbeeld van print =
aantal = 3
stuksprijs = 0.98
omschrrijving =' Crocky narutal 300gr '

print(f"{aantal} {omschrrijving} {stuksprijs}")
print(str (aantal) + ' ' + omschrrijving+ ' ' + str(stuksprijs))

 ################################################################################################################################################################
# Waarom gebruik we '' ?
# voor spacie
# built in funcie = print , str
# str(input) gebruik je voor zinnen of woorden te vragen 
# Int(input) gebruik je om een vraag te stellen met een geheel getaal
# float,str gebruik je als b.v 0.39 euro te printen

 ################################################################################################################################################################
# Random V.B van Int
# De ( / 100 )  gebruik je om het string naar een Int te veranderen.
prijs = int(crossaintjes * crossaintjes_prijs / 100 + stokbroden * stokbroden_prijs / 100 - korting * korting_C / 100)


##################################################################################################################################################################

# = voer uit en == vergrijken
# VB van Iets vragen 

naam = input('wat is uw naam?')
print(f"ja mij naam is:{naam}")

 ################################################################################################################################################################

# IF = als
# V.B van "IF" 
MEMBER_KORTING= 15
CONSOLE_PRIJS = 55
PC_PRIJS = 45 

platform = input ('Ben je pc of console gamer?')
prijs = CONSOLE_PRIJS # dit is de prijs van een consolegame

if platform == 'console':
    prijs == CONSOLE_PRIJS
    if input('Bent u member?') == 'ja':
        prijs -= MEMBER_KORTING

print (f'U bent {platform}gamer , dan kost de game: {prijs} euro')

# extra if V.B
if prijs_Iphone_13 > Prijs_Samssung_22:
    print ("Iphone is duurder")
elif Prijs_Samssung_22 > prijs_Iphone_13:
    print("Samsung is duurder")
 # > betekenit = groter
 ################################################################################################################################################################
# == is vergelijken
# v.b van 
Duur = input ("is de kaas belachelijke duur?")
if Duur == "ja":
    kosrt = input('zit er kor')

#################################################################################################################################################################

import random
print (random.randrange(1,15))

 #################################################################################################################################################################

x = 1
y= -112.2682
w= 9j

print (type(x))
print (type(y))
print (type(w))

#################################################################################################################################################################

hoeveelheid = 9
artikel = 5
prijs=2
mijn_besteling= ("ik wil {} stukken van artikel {} voor {} euro" )

print(mijn_besteling.format(hoeveelheid,artikel,prijs))

hoeveelheid = 9
artikel = 5
prijs=2
mijn_besteling= ("ik wil {} stukken van artikel {} voor {} euro" )

print(mijn_besteling.format(hoeveelheid,artikel,prijs))

#################################################################################################################################################################

txt= "komt er een hond achter je aan?"
c = "je aan?"in txt
print(c)

#################################################################################################################################################################

a = "hallo, mami"
print(len(a))

a = "hallo, mami"
print (a[-11:-3])

a = "hallo, mami"
print (a[0:11])

naam = input("wat is je naam ? ")

print ("jouw naam is "+ naam +".")

#################################################################################################################################################################
tel = 0


while tel <= 10:
    tel += 1
    print (tel)

for  y in range(11):
    print (y)


from time import sleep

delay = 1
 #sleep(delay)