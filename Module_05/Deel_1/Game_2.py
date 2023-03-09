import random

def play_game():
    print("Hallo, welkom bij Munch!")
    ans = input("Ben je klaar om te spelen (ja/nee)? :").lower()
    if ans.lower() == "ja":
        questions = {
            "Wie heeft Python ontworpen?": "Guido",
            "Wat is 8 * 8 - 8 + 5?": "61",
            "Wat is Pi?": "3.14",
            "Wie heeft basketbal uitgevonden?": "James Naismith",
            "Hoe wordt het genoemd als de scheidsrechter de bal in het spel brengt door hem op te gooien tussen twee tegenstanders die hem naar een teamgenoot proberen te tikken?": "Jump ball",
            "Bij basketbal, welke term verwijst naar het gooien, slaan of rollen van de bal naar een andere speler?": "Pass",
            "Welke basketballer ging met het hoogste scoringsgemiddelde in zijn carrière?": "Michael Jordan",
        }

        total_questions = len(questions)
        score = 0

        for question, answer in questions.items():
            user_answer = input(f"{question}: ").lower()
            if user_answer == answer.lower():
                score += 1
                print("Juist!")
            else:
                print("Onjuist!")

        user_choice_questions = input("Wie denk je dat een betere basketballer is tussen LeBron James en Michael Jordan? Typ = LJ of MJ?").lower()
        if user_choice_questions == "lj":
            user_answer = input("Hoeveel ringen heeft LeBron James? ").lower()
            if user_answer == "4":
                score += 1
                print("Juist!")
            else:
                print("Onjuist!")
        elif user_choice_questions == "mj":
            user_answer = input("Hoeveel ringen heeft Michael Jordan? ").lower()
            if user_answer == "6":
                score += 1
                print("Juist!")
            else:
                print("Onjuist!")

        percentage_correct = (score / total_questions) * 100
        print(f"Dank je wel voor het spelen! Je hebt {score} van de {total_questions} vragen correct beantwoord.")
        print(f"Je score is {percentage_correct}%.")

    print("GAME IS OVER. Tot ziens!")

play_game()
