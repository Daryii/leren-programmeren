from fruitmand import fruitmand

fruitmand.pop(4)

colors = set()

for fruit in fruitmand:
    colors.add(fruit["color"])

for color in colors:
    print(color)