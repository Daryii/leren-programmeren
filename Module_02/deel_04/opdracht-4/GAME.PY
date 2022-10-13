print("Hallo ,JAelkom bij Munch!")

ans =input ("Ben je ready om te spelen (ja/nee)? :")
score = 0
total_P = 9

if ans.lower () == "ja":
    ans = input ("1.Wie hebt python ontwerpen?")
    if ans.lower () == "guido":
        score += 1
        print ("juist")
    else:
        print ('onjuist')
        
    ans = input ("2.Wat is 8 * 8 - 8 + 5?")
    if ans.lower () == "61":
        score += 1
        print ("juist")
    else:
        print ('onjuist')

    ans = input ("3.Wat is Pi?")
    if ans.lower () == "3.14" or ans.lower () == "22/7" :
        score += 1
        print ("juist")
    else:
        print ('onjuist')

    ans = input ("4.Wie heeft basketbal uitgevonden?")
    if ans.lower () == "j.n":
        score += 1
        print ("juist")
else:
       

    ans = input ("5.Hoe wordt het bij basketbal genoemd als de scheidsrechter de bal in het spel brengt door hem op te gooien tussen twee tegenstanders die hem naar een teamgenoot proberen te tikken?")
    if ans.lower () == "jumpball":
        score += 1
        print ("juist")
    else:
        print ('onjuist')

    ans = input ("6.Wie heeft basketbal uitgevonden?")
    if ans.lower () == "james naismith":
        score += 1
        print ("juist")
    else:
        print ('onjuist')


    ans = input ("7.Bij basketbal, welke term verwijst naar het gooien, slaan of rollen van de bal naar een andere speler?")
    if ans.lower () == "pass":
        score += 1
        print ("juist")
    else:
        print ('onjuist')


    ans = input ("8.Welke van deze basketballers ging met pensioen met het hoogste scoringsgemiddelde in zijn carrière?")
    if ans.lower () == "michael jordan":
        score += 1
        print ("juist")
    else:
        print ('onjuist')


    ans = input ("9. Wie denk je dat een betere basketballer is tussen lerbron james en Michael Jordan typ = LJ of MJ?").lower()
    if ans == "lj":
        LJ = input ("Hoeveel rings heeft Lebron james?")
        if LJ == "4":
            score += 1
            print("juist")
        else:
            print("jij bent een ezel")

    elif ans == "mj":
        MJ = input ("Hoeveel rings heeft Michael Jordan?")
        if MJ == "6":
            score += 1
            print("juist")
        else:
            print("jij bent een ezel")


    print ('Dankjewel voor spelen jij hebt' ,score,"vragen goed. ")
    mark = (score/total_P) * 100

    print("Mark:",str(mark) +'%' )

print('GAME IS OVER GANGY GOODBYE')
        