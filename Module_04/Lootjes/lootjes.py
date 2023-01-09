import random 


namen_lijst_1 = []
namen_lijst_2 = []

Vraag = input("Wil uw lootjes trekken?: ")
if Vraag == "ja":
    while True:
        namen = input("Voer hier de namen van de deelnamers, en type ( klaar ) als je klaar bent: ")

        if namen == "klaar":
            break
        namen_lijst_1.append(namen)
        namen_lijst_2 = list(set(namen_lijst_1))

        print(namen_lijst_1)
else:   
    exit()
   
if len(namen_lijst_1) < 3:
    print("Opgegeven namen zijn minder dan drie of al ingevoerd")

elif len(namen_lijst_1) > len(set(namen_lijst_1)):
    print("Opgegeven namen zijn minder dan drie of al ingevoerd")   
else:
    random.shuffle(namen_lijst_1)
    for j in range(len(namen_lijst_1)):
        print(f"{namen_lijst_1[j]} heeft {namen_lijst_2[j]} getrokken")
            

            




