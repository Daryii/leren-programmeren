 ################################################################################################################################################################

# commentaar schrij je met #
 # Data types
 # string = woord of zin
 #Int = geheel getal

################################################################################################################################################################

 # het boeites als '' of "" gebruikt

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

 ################################################################################################################################################################
