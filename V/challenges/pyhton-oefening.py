# 1
tafel = 1
getal = 1
getal2 = 1
while tafel <= 13:
    print(f"Tafel van {tafel}")
    while getal2 <= 10:
        print(f"{getal} x {getal2} = {getal * getal2}")
        getal2 += 1
    getal2 = 1
    getal += 1
    tafel += 1

# 2
Lijst = [5,12,19,27,3]
print(Lijst)

#3
Lijst.insert(6,25)
print(Lijst)

#4
print(len(Lijst))

#5
del Lijst[1]
print(Lijst)

#6
del Lijst[0]
print(Lijst)

#6
Lijst.insert(0,36)
print(Lijst)

#7
print(sum(Lijst))

#8
Lijst.clear()
print(Lijst)

#9
Lijst.extend([1,2,3])
print(Lijst)

#10
Lijst.extend([1,2,3])
print(Lijst)


Lijst.clear()
print(Lijst)


#11
Lijst.extend(range(1,51))
print(Lijst)

#12
print(len(Lijst))

#13
del Lijst[0 and 50]
Lijst.insert(0,50)
Lijst.append(1)
print(Lijst)

Lijst.clear()
print(Lijst)

14
Lijst = [1,"aap",2,"apen",3,"watermeloen",15,27,15,"lekker bezig",6]
for u in Lijst :
    if str(type(u)) == "<class'int'>":
        print(f"{u} is een int.")

print("#13")
mijn_lijst2 = [1, "aap", 2, "apen", 3, "watermeloen", 15, 27]
print(mijn_lijst2)
aantal_getallen = 0
for i in mijn_lijst2:
    if str(type(i)) == "<class 'int'>":
        aantal_getallen += 1
        print(f"{i} is een int.")

print(aantal_getallen)    