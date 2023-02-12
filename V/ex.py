mijn_zin = "apple is het beste merk \n windows 2"

print(mijn_zin)    



def multiplier():
    lijst = []
    getal = float(input ("vul een getal in: "))
    for i in range (1,11):
        sum = i * getal
        lijst.append(f" {i} * {getal} = {sum}")
    return lijst

for e in multiplier():
    print(e)
   