import random
M_en_Ms = ("oranje", "blauw", "groen", "bruin","paars")

vraag = int(input("Hoeveel M&Ms er aan de zak toegevoegd worden?: "))
zak = []
for u in range(vraag):
    randomcijfer = random.randint(0,4)
    zak.append(M_en_Ms[randomcijfer])

print(zak)

