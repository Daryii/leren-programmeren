import random

from fruitmand import fruitmand

vraag = int(input("voeg een getal in: "))

ran = random.choice(fruitmand)

for i in range(vraag):
    if "name" in ran:
        print(ran["name"])


