zak = {}

getal = 1

while True:
    product = input("Voeg item toe ? :")
    if product in zak:
        zak[product] += 1
    else:
        zak.update({product : getal})
    voeg_product = input("wil je nog een product toe: ")
    if voeg_product == "ja":
        continue
    else:
        break
print(" -[ BOODSCHAPPENLIJST ]- ")
for key,value in  zak.items():
    print(f"{value} x {key}")
    print("-----------------------")
   


