keuzen = ('a','b','c','d','e','f','g','h')

def getal_maal_dire(getal: int, max: int) -> int:
    if getal >= max:
        return getal
    else:
       return getal_maal_dire(3,1000)

print(getal_maal_dire)