from fruitmand import fruitmand  #importing  fruitmand from some module 
lengte = 0
longest_fruit = {}

kleuren_dict = {"yellow" : "geel" ,"green":"groen","orange":"oranje","red":"rood","brown":"bruin",}

for fruit in fruitmand:
    if len(fruit["name"]) > lengte:
        lengte = len(fruit["name"])
        longest_fruit = fruit

print(f"De",longest_fruit['name'],(lengte),"heeft een",kleuren_dict[longest_fruit['color']],"kleur","en een","gewicht","van",longest_fruit["weight"]/1000,"kg.")
