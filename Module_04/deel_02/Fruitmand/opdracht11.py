from fruitmand import fruitmand

RONDE = 0
NIET_RONDE = 0

beschikbaar_kleuren = [fruit["color"] for fruit in fruitmand]

while True:
    vraag = input("kies een kleur uit deze kleuren,(yellow)(brown)(red)(orange)(green): ")
    if vraag not in beschikbaar_kleuren:
        print(f"De kleur {vraag} zit er niet in de fruitmand")
        continue
    for fruit in fruitmand:
        if fruit["color"] == vraag:
            if fruit["round"] == True:
                RONDE +=1
            else:
                NIET_RONDE +=1

    if RONDE > NIET_RONDE:
        print(f"Er zijn {RONDE-NIET_RONDE} meer RONDE vruchten dan niet RONDE vruchten in de kleur {vraag}")
    elif RONDE < NIET_RONDE:
        print(f"Er zijn {NIET_RONDE-RONDE} minder RONDE vruchten dan niet RONDE vruchten in de kleur {vraag}")
    else:
        print(f"Er zijn {RONDE} RONDE vruchten en {NIET_RONDE} niet RONDE vruchten in de kleur {vraag}")        

