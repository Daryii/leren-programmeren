import random

from fruitmand import fruitmand

vraag = int(input("voeg een getal in: "))

for i in range(vraag):
    ran = random.choice(fruitmand)
    print(ran["name"])


