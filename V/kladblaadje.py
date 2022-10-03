def get_bool(karakter: str) -> bool:
    print(f"ik ben nu bezig met: {karakter}")
    reactie = False
    if karakter == "a":
        reactie = True
    elif karakter == "b":
        reactie = False
    print(reactie)
    return reactie

if get_bool("a") or get_bool("b"):
    print("Het is waar")



    
x = 3
y = 4
aap = x == 4 or y == 4
noot = x == 3 and y == 5
if x == 4 or y == 4:
    print("aap lust noot")
print(aap)
print(noot)






zin = "ayoo"
x = 0
for c in (0,1,2):
    for d in (0,1,2):
        for x in (0,1,2):
            x += 1                        # x = x + 1
            print (zin,c,d,x)


hoeveel_pizza =0

prijs = 6,99
while True:
    try:
        hoeveel_pizza = int (input ("hoeveel pizza's wil je hebben"))
    except ValueError:
        print ("je moet wel een getal invullen !!!!!!!!!!")


    bedrag = hoeveel_pizza * prijs

