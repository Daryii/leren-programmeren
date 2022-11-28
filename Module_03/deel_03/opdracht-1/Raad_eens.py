import random

ronden1 = 20
ronden2 = 10
score = 0
total_P = 20
vraag2 = ""


vraag = input("Ben je ready om te getallen te raden?:")
num = random.randint(1, 1000)
if vraag == "ja":
    vraag2 = input("raad een getal 0 - 1000:")
    if vraag2 == "":
        score += 1
else:
    print("end")
if ronden2 == True:
    if vraag2 >= 20:
        print("je bent heel warm!")
    elif vraag2 >= 50:
        print("je bent warm!")
if ronden1 == True:
    print ('Dankjewel voor spelen jij hebt' ,score,"van de 20 vragen goed. ")
    mark = (score/total_P) * 100

    print("Mark:",str(mark) +'%' )

