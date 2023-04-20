EASY_TEXT = """Ik hou van programmeren. Programmeren is leuk. 
Ik kan veel dingen maken met programmeren. Ik kan een website maken. 
Ik kan een spel maken. Ik kan een chatbot maken. 
Programmeren is niet moeilijk. Ik moet alleen de juiste code schrijven. 
De code moet logisch zijn. De code moet foutloos zijn. Werkende code maakt mij blij. 
Niet-werkende code chagerijnig. Programmeren is een avontuur. Ik leer elke dag iets nieuws met programmeren."""

DIFFICULT_TEXT = """Programmeren is een geweldige activiteit, die je in staat stelt om je creativiteit, 
logica en probleemoplossend vermogen te gebruiken, om allerlei soorten applicaties te maken, 
die nuttig, vermakelijk of zelfs levensveranderend kunnen zijn, afhankelijk van je doel en publiek. 
Het is ook een uitdagende bezigheid, die je voortdurend leert om nieuwe talen, technieken en concepten te leren, 
die je helpen om je code efficiënter, eleganter en robuuster te maken, zonder dat je je ooit hoeft te vervelen of te herhalen. 
Bovendien is het een leuke hobby, die je veel voldoening en plezier kan geven, als je ziet hoe je ideeën tot leven komen op het scherm, als je de interactie met je gebruikers ziet of 
als je de reacties van je vrienden en familie ziet, als je ze verrast met je eigen creaties.
"""

TEST_TEKST = '''Maecenas commodo velit a mi fermentum, sit amet varius ipsum fringilla. Aliquam eget erat gravida, sollicitudin urna sit amet, feugiat urna. Aliquam feugiat urna non est consequat, in tincidunt nulla fringilla. Suspendisse lacinia, tortor a bibendum facilisis, lacus justo malesuada eros, et efficitur nulla purus et libero. Nam vehicula felis et tristique blandit. Vestibulum nec turpis id turpis rutrum fermentum. Cras vitae suscipit urna, id venenatis velit. Integer venenatis odio in turpis varius, a facilisis odio feugiat. Vestibulum sagittis vestibulum sapien, vitae aliquet libero lacinia eu. Vestibulum pulvinar sem vel dolor finibus bibendum. Praesent nec nisi ac nunc aliquam efficitur. Praesent non fringilla lacus, ut bibendum neque. Nam at lacinia massa, et feugiat tellus. Sed vestibulum dapibus arcu id iaculis. Aenean a interdum ipsum, at suscipit purus.
'''

EASY_TEXT_2 = '''Python is een populaire programmeertaal die bekend staat om zijn eenvoud en kracht. Het werd in 1991 ontwikkeld door Guido van Rossum en is sindsdien uitgegroeid tot een van de meest gebruikte talen in de wereld van de softwareontwikkeling.Python is een objectgeoriënteerde taal, wat betekent dat alles in Python een object is, inclusief getallen, tekst en zelfs functies. Het heeft ook een uitgebreide standaardbibliotheek, waardoor het gemakkelijk is om complexe taken uit te voeren, zoals het manipuleren van gegevens, het werken met netwerken en het maken van grafische interfaces.Een van de grootste voordelen van Python is de leesbaarheid van de code. De syntax is eenvoudig en duidelijk, waardoor het gemakkelijk is om te begrijpen wat er in de code gebeurt. Dit maakt Python een geweldige keuze voor beginners en ervaren programmeurs.
'''

DIFFICULT_TEXT_2 = '''Het was een heldere ochtend en de zon scheen fel door het raam van mijn slaapkamer. Ik stapte uit bed en rekte me uit, waarna ik naar de badkamer liep om een douche te nemen. Terwijl het warme water over me heen stroomde, dacht ik na over de plannen voor de dag. Ik had een belangrijke vergadering op mijn werk en moest me voorbereiden op een presentatie. Na het douchen en aankleden liep ik naar de keuken om koffie te zetten. Ik keek uit het raam en zag dat de bladeren aan de bomen begonnen te verkleuren en te vallen, wat betekende dat de herfst was begonnen. Ik nam een slok van mijn koffie en dacht na over hoe snel de tijd voorbij was gegaan.Ik reed naar mijn werk en arriveerde net op tijd voor de vergadering. Ik gaf de presentatie en beantwoordde vragen van mijn collega's. Na de vergadering ging ik terug naar mijn kantoor en begon ik aan mijn volgende project.Maecenas commodo velit a mi fermentum, sit amet varius ipsum fringilla. Aliquam eget erat gravida, sollicitudin urna sit amet, feugiat urna. Aliquam feugiat urna non est consequat, in tincidunt nulla fringilla. Suspendisse lacinia, tortor a bibendum facilisis, lacus justo malesuada eros, et efficitur nulla purus et libero. Nam vehicula felis et tristique blandit. Vestibulum nec turpis id turpis rutrum fermentum. Cras vitae suscipit urna, id venenatis velit. Integer venenatis odio in turpis varius, a facilisis odio feugiat. Vestibulum sagittis vestibulum sapien, vitae aliquet libero lacinia eu. Vestibulum pulvinar sem vel dolor finibus bibendum. Praesent nec nisi ac nunc aliquam efficitur. Praesent non fringilla lacus, ut bibendum neque. Nam at lacinia massa, et feugiat tellus. Sed vestibulum dapibus arcu id iaculis. Aenean a interdum ipsum, at suscipit purus.
'''

ALLOWED_IN_WORD = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_-"

# depending on the type of text you wish you get an easy, difficult or text from file.
def getText(choice: str) -> str:
    if choice == 'easy':
        return EASY_TEXT
    elif choice == 'difficult':
        return DIFFICULT_TEXT
    elif choice == 'test_1':
        return TEST_TEKST
    elif choice == 'easy_1':
        return EASY_TEXT_2
    elif choice == 'difficult_1':
        return DIFFICULT_TEXT_2
    else:
        return getFileContentAsString(choice)

def getFileContentAsString(textFile: str) -> str:
    with open(textFile, 'r') as file:
        content = file.read()
    return content

# opdracht 1
def getNumberOfCharacters(text: str) -> int:
    teller = 0
    for i in text:
        if i in ALLOWED_IN_WORD:
            teller += 1
    return teller


# opdracht 2
def getNumberOfSentences(text: str) -> int:
    woord = ""
    teller = 0
    for x in text:
        if x in "?!." and len(woord.strip()) >= 2:
            teller += 1
            woord = ""
        else:
            if x not in "?!." :
            
                woord += x
    return teller

# opdracht 3
def getNumberOfWords(text: str) -> int:
    teller = text.split()
    return len(teller)
 

# opdracht 5
def getAVIscore(text: str) -> int:
    teller = 0
    aantal_woord = getNumberOfWords(text)
    aantal_zin = getNumberOfSentences(text)

    gemiddeld_aantaal =  aantal_woord / aantal_zin

    print(aantal_zin)
    print(aantal_woord)
    print(gemiddeld_aantaal)

    if  gemiddeld_aantaal <= 7:
        teller = 5
    elif  gemiddeld_aantaal <= 8:
        teller = 6
    elif  gemiddeld_aantaal <=  9:
        teller =  7
    elif  gemiddeld_aantaal <=  10:
        teller = 8
    elif  gemiddeld_aantaal <= 11:
        teller = 11
    elif  gemiddeld_aantaal > 11:
        teller= 12
    return teller
   
