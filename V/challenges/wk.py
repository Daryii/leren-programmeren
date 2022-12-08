
land_1 = input("Voer land 1 in? : ")
land_2 = input("Voer land 2 in? :")
land_3 = input("Voer land 3 in? :")


score_land1 = 0
score_land2 = 0
score_land3 = 0

doelsaldo_1 = 0
doelsaldo_2 = 0
doelsaldo_3 = 0

voor_land1 = 0
voor_land2 = 0
voor_land3 = 0

tegen_land1 =0
tegen_land2 = 0
tegen_land3 = 0



print("Wedstijd 1")


doelpuntwen_land1 = int(input(f"doelpunten: {land_1}"))
doelpuntwen_land2 = int(input(f"doelpunten: {land_2}"))

voor_land1 += doelpuntwen_land1
tegen_land1 += doelpuntwen_land2
voor_land2 += doelpuntwen_land2
tegen_land2 += doelpuntwen_land1

if doelpuntwen_land1 > doelpuntwen_land2:
    score_land1 += 3
else:
    score_land1 += 3

print("Wedstijd 2")


doelpuntwen_land1 = int(input(f"doelpunten: {land_1}"))
doelpuntwen_land3 = int(input(f"doelpunten: {land_2}"))

voor_land1 += doelpuntwen_land1
tegen_land1 += doelpuntwen_land3
voor_land2 += doelpuntwen_land3
tegen_land2 += doelpuntwen_land1

if doelpuntwen_land1 > doelpuntwen_land2:
    score_land1 += 3
else:
    score_land1 += 3


print("Wedstijd 3")


doelpuntwen_land2 = int(input(f"doelpunten: {land_1}"))
doelpuntwen_land3 = int(input(f"doelpunten: {land_2}"))

voor_land1 += doelpuntwen_land2
tegen_land1 += doelpuntwen_land3
voor_land2 += doelpuntwen_land3
tegen_land2 += doelpuntwen_land2

if doelpuntwen_land1 > doelpuntwen_land2:
    score_land1 += 3
else:
    score_land1 += 3

print(f"{land_1}: score uit alle wedstrijden : {score_land1} doelpunten voor: {voor_land1} doelpunten tegen: {tegen_land1}")
print(f"{land_2}: score uit alle wedstrijden : {score_land2} doelpunten voor: {voor_land2} doelpunten tegen: {tegen_land2}")
print(f"{land_3}: score uit alle wedstrijden : {score_land3} doelpunten voor: {voor_land3} doelpunten tegen: {tegen_land3}")



















































