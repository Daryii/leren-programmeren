
# land_1 = input("Voer land 1 in? : ")
# land_2 = input("Voer land 2 in? :")
# land_3 = input("Voer land 3 in? :")

landen_lijst = []
punten_lijst = []
doelsaldo_lijst = []
aantal_wedstrijden_lijst = []
wedstrijden_lijst = []


# score_land1 = 0
# score_land2 = 0

# doelsaldo_1 = 0
# doelsaldo_2 = 0
# doelsaldo_3 = 0

# voor_land1 = 0
# voor_land2 = 0
# voor_land3 = 0

# tegen_land1 =0
# tegen_land2 = 0
# tegen_land3 = 0


AANTAL_LANDEN = 4 # minimaal 3 landen.

# vraag 1
for x in range(1, AANTAL_LANDEN ):
    landen_lijst.append(input(f"Voer land {x} in:"))




for y in range(AANTAL_LANDEN):
    for z in range(y + 1, AANTAL_LANDEN):
        wedstrijden_lijst.append((landen_lijst[y],[landen_lijst[z]]))
        print("")
        
        doelpunten_land1nd1 = int(input(f"doelpunten: {landen_lijst}: "))
        doelpunten_land1nd2 = int(input(f"doelpunten: {landen_lijst}: "))
        
        if doelpunten_land1nd1 > doelpunten_land1nd2:

                punten_lijst += 3
                doelsaldo_lijst += doelpunten_land1nd1 - doelpunten_land1nd2
                doelsaldo_lijst += doelpunten_land1nd2 - doelpunten_land1nd1

        elif doelpunten_land1nd1 == doelpunten_land1nd2:

                punten_lijst += 1
                punten_lijst += 1
                # doelsaldo niet relevant want evenveel voor als tegen
        else:
                punten_lijst += 3
                doelsaldo_lijst += doelpunten_land1nd1 - doelpunten_land1nd2
                doelsaldo_lijst += doelpunten_land1nd2 - doelpunten_land1nd1

# # print("Wedstijd 2")


# # doelpuntwen_land1 = int(input(f"doelpunten: {land_1}"))
# # doelpuntwen_land3 = int(input(f"doelpunten: {land_2}"))

# # voor_land1 += doelpuntwen_land1
# # tegen_land1 += doelpuntwen_land3
# # voor_land2 += doelpuntwen_land3
# # tegen_land2 += doelpuntwen_land1

# # if doelpuntwen_land1 > doelpuntwen_land2:
# #     score_land1 += 3
# # else:
# #     score_land1 += 3


# # print("Wedstijd 3")


# # doelpuntwen_land2 = int(input(f"doelpunten: {land_1}"))
# # doelpuntwen_land3 = int(input(f"doelpunten: {land_2}"))

# # voor_land1 += doelpuntwen_land2
# # tegen_land1 += doelpuntwen_land3
# # voor_land2 += doelpuntwen_land3
# # tegen_land2 += doelpuntwen_land2

# # if doelpuntwen_land1 > doelpuntwen_land2:
# #     score_land1 += 3
# # else:
#     # score_land1 += 3

    print(f"Wedstrijd {landen_lijst} - {landen_lijst} eindigde in: {doelpunten_land1nd1} - {doelpunten_land1nd2}")
    print("Overzicht groep A")
 















































