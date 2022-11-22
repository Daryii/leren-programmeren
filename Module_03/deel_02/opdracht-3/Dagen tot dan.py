dagen = ["maandag","dinsdag","woensdag","donderdag","vrijdag","zaterdag","zondag"]

dag = input("kies een dag van de week ?") # maar dan met een cijfer b.v maandag = 1 en donderdag = 4 etc ... 

s =7
w =0

while w < s:
    daz = dagen[w]
    if dag == daz:
        break
    print(daz)
    w = w + 1

