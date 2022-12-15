from fruitmand import fruitmand

fruitmand.append({
    'name' : 'watermeloen',
    'weight' : 3500,
    'color' : 'green',
    'round' : True
})
fruit =""

gewicht = [(fruit["weight"])
for fruit in fruitmand 
    if 'weight'in fruit]
print(sum(gewicht))