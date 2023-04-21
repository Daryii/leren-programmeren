grootste = 0
kleinste = 1000
aantal = 0

for i in range(10):
    vraag = int(input("voer een getal in boven de 0 en onder 1000:"))

    if vraag > grootste:
        grootste = vraag
    if vraag < kleinste:
        kleinste = vraag
    
    if vraag % 3== 0:
       aantal = aantal +1

    print(f"het grootste getal{grootste}")
    print(f"het kleinste getal {kleinste}")
    print(f"het getallen dat deelbaar zijn door drie {aantal}")

