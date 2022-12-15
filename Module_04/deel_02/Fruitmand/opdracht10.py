from fruitmand import fruitmand
from operator import itemgetter

newlist = sorted(fruitmand,key=itemgetter("weight"))

for fruit in fruitmand:
    print("fruitsoort :",fruit["name"])
    print("fruitgewicht :",fruit["weight"]/1000,"kg")