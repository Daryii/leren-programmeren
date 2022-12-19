fruitmand = [{
    'name' : 'ananas',
    'weight' : 1590,
    'color' : 'yellow',
    'round' : False
},{
    'name' : 'appel',
    'weight' : 195,
    'color' : 'green',
    'round' : True
},{
    'name' : 'sinaasappel',
    'weight' : 130,
    'color' : 'orange',
    'round' : True
},{
    'name' : 'banaan',
    'weight' : 120,
    'color' : 'yellow',
    'round' : False
},{
    'name' : 'druif',
    'weight' : 5,
    'color' : 'red',
    'round' : True
},{
    'name' : 'kiwi',
    'weight' : 75,
    'color' : 'brown',
    'round' : False
},{
    'name' : 'citroen',
    'weight' : 100,
    'color' : 'yellow',
    'round' : True
}]


abc = ("a","b","c")
mijn_string = "Daryi"

for i in mijn_string:
    print(i)

for e in abc:
    print(e)

for fruit in fruitmand:
    print("Sleutels:")
    for sleutel in fruit.keys():
        print(sleutel)
    print("WaARDES:")
    for waarde in fruit.values():
        print(waarde)
