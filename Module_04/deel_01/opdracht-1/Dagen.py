Alle_dagen = ("maandag", "dinsdag", "woensdag", "donderdag", "vrijdag", "zaterdag", "zondag")

print("Alle dagen van de week zijn:")
for u in Alle_dagen:
    print(u)   

print("De werkdagen zijn:")
for e in Alle_dagen[0:5]:
    print(e)

print("De weekenddagen zijn:")
for d in Alle_dagen[5:]:
    print(d)

print("Alle dagen van de week in omgekeerde volgorde zijn:")
for f in reversed(Alle_dagen):
    print(f)

print("De werkdagen in omgekeerde volgorde zijn:")
for s in reversed (Alle_dagen[0:5]):
    print(s)

print("De weekenddagen in omgekeerde volgorde zijn:")
for e in reversed (Alle_dagen[5:]):
    print(e)
