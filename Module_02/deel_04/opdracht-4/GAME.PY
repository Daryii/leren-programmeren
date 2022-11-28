print("Hallo,Welkom bij Munch!")

ans =input ("Ben je ready om te spelen (ja/nee)? :")
score = 0
total_P = 9
vraag_1_goed = False

if ans.lower () == "ja":
    Vraag1 = input ("1.Wie hebt python ontwerpen?")
    if Vraag1.lower () == "guido":
        vraag_1_goed = True
        score += 1
        print ("juist")
    else:
        print ('onjuist')

           
    vraag_2 = input ("2.Wat is 8 * 8 - 8 + 5?")
    if vraag_2.lower () == "61":
        score += 1
        print ("juist")
    else:
        print ('onjuist')

    vraag_3 = input ("3.Wat is Pi?")
    if vraag_3.lower () == "3.14" or ans.lower () == "22/7" :
        score += 1
        print ("juist")
    else:
        print ('onjuist')

    vraag_4 = input ("4.Wie heeft basketbal uitgevonden?")
    if  vraag_4.lower () == "j.n":
        score += 1
        print ("juist")
    else:
        print ('onjuist')


    vraag_5 = input ("5.Hoe wordt het bij basketbal genoemd als de scheidsrechter de bal in het spel brengt door hem op te gooien tussen twee tegenstanders die hem naar een teamgenoot proberen te tikken?")
    if  vraag_5.lower () == "jumpball":
        score += 1
        print ("juist")
    else:
        print ('onjuist')

    if vraag_1_goed:
        ans_s = input ("Wilt uw een hint?")
        if ans_s == "ja":
            print ("Zijn achternaam is naismith")


    vraag_6 = input ("6.Wie heeft basketbal uitgevonden?")
    if  vraag_6.lower () == "james naismith":
        score += 1
        print ("juist")
    else:
        print ('onjuist')


    vraag_7= input ("7.Bij basketbal, welke term verwijst naar het gooien, slaan of rollen van de bal naar een andere speler?")
    if vraag_7.lower () == "pass":
        score += 1
        print ("juist")
    else:
        print ('onjuist')


    vraag_8 = input ("8.Welke van deze basketballers ging met pensioen met het hoogste scoringsgemiddelde in zijn carrière?")
    if vraag_8.lower () == "michael jordan":
        score += 1
        print ("juist")
    else:
        print ('onjuist')


    vraag_9 = input ("9. Wie denk je dat een betere basketballer is tussen lerbron james en Michael Jordan typ = LJ of MJ?").lower()
    if vraag_9 == "lj":
        LJ = input ("Hoeveel rings heeft Lebron james?")
        if LJ == "4":
            score += 1
            print("juist")
        else:
            print("jij bent een ezel")

    elif vraag_9 == "mj":
        MJ = input ("Hoeveel rings heeft Michael Jordan?")
        if MJ == "6":
            score += 1
            print("juist")
        else:
            print("jij bent een ezel")


    print ('Dankjewel voor spelen jij hebt' ,score,"van de 9 vragen goed. ")
    mark = (score/total_P) * 100

    print("Mark:",str(mark) +'%' )

print('GAME IS OVER GANGY GOODBYE')
        