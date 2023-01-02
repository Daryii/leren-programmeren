import random 
import copy

namen_lijst_1 = []
namen_lijst_2 = []

Vraag = input("Wil uw lootjes trekken?: ")
if Vraag == "ja":
    while True:
        namen = input("Voer hier de namen van de deelnamers, en type ( klaar ) als je klaar bent: ")

        if namen == "klaar":
            break
        namen_lijst_1.append(namen)
        namen_lijst_2 = copy.copy(namen_lijst_1)
        print(namen_lijst_1)
else:   
    exit()
   
if len(namen_lijst_1) < 3:
    print("Alle opgegeven namen zijn minder dan drie ")

elif len(namen_lijst_1) > len(set(namen_lijst_1)):
    print("Uw hebt deze naam al ingevoerd ")   
else:
    for i in range(len(namen_lijst_1)):
        random.shuffle(namen_lijst_1)
        if namen_lijst_1 == namen_lijst_2:
            break
        else:
            print(f"{namen_lijst_1[i]} heeft {namen_lijst_2[i]} getrokken")
            

            

            




