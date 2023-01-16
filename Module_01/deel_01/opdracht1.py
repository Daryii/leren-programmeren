MEMBER_KORTING= 15
CONSOLE_PRIJS = 55
PC_PRIJS = 45 

platform = input ('Ben je pc of console gamer?')
prijs = CONSOLE_PRIJS # dit is de prijs van een consolegame

if platform == 'console':
    prijs == CONSOLE_PRIJS
    if input('Bent u member?') == 'ja':
        prijs -= MEMBER_KORTING
else:

    print (f'U bent {platform}gamer , dan kost de game: {prijs} euro')
print(prijs)