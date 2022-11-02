dagen = ["maandag", "dinsdag", "woensdag", "donderdag", "vrijdag", "zaterdag", "zondag"]

dag = int(input("kies een dag van de week ?")) #maar dan met een cijfer b.v maandag = 1 en donderdag = 4 etc ... 
d = 0

while d < dag:
    print(dagen[d])
    d = d + 1
    