# Je wilt 17 croissantjes van elk 39 eurocent en 2 stokbroden van elk 2,78 euro kopen. Je hebt 3 kortingsbonnen van 50 eurocent. Hoeveel geld moet je betalen?
# 17*0.39+2.78*2 = 12.19 - 1.50 = €10.69

crossaintjes = int(input("vul hier de aantal crossaintjes ="))
crossaintjes_prijs = int(input("vul hier de prijs in centen ="))
stokbroden =  int(input("vul hier de aantal stokbroden = "))
stokbroden_prijs = int(input("vul hier de prijs van de stokbroden in centen ="))
korting = int(input ("vul hier de aantal kortingsbonen ="))
korting_C = int(input ("Vul hier de prijs van de kortingbonnen ="))

prijs = (crossaintjes * crossaintjes_prijs / 100 + stokbroden * stokbroden_prijs / 100 - korting * korting_C / 100)

print (f"De feestlunch kost je {prijs} euro voor de  croissantjes en de {stokbroden} stokbroden als de 3 kortingsbonnen nog geldig zijn")

