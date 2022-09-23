# Naam= Daryi Wolderghiorghis 
# opdracht =  Pizza calculator

small_p=  7.99
medium_p = 9.99
large_p = 12.99

#Voorbeeld een klant bestelde 1 small , 2 medium en 2 large!

Besteling1 = int(input( " Hoeveel small pizza wilt u hebben?:"))
bestelding2= int(input( " Hoeveel medium pizza wilt u hebben?:"))
bestelding3 = int(input( " Hoeveel large pizza wilt u hebben?:"))

ant_1= int(small_p * Besteling1)
ant_2= int (medium_p * bestelding2)
ant_3= int (large_p * bestelding3)

totaal= ant_1 + ant_2 + ant_3

print("------------------------------------------")
print(F"|          Daryi's Pizza                 ")  

print(F"|{Besteling1}  small pizza {ant_1}:Euros")
print(F"|{bestelding2}  medium pizza {ant_2}:Euros")
print(F"|{bestelding3}  large pizza {ant_3}:Euros")
print(f"|Het totaal bedrag is = {totaal} :Euros")

print("|Dankjewel voor het bestellen")
print("|------------------------------------------")
