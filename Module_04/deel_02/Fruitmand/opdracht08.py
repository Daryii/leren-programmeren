from fruitmand import fruitmand

fruitmand.append({
    'name' : 'watermeloen',
    'weight' : 3500,
    'color' : 'green',
    'round' : True
})

total_weight = 0

for fruit in fruitmand:
    total_weight += fruit["weight"]
    print((total_weight))
