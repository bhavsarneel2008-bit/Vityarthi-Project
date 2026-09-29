from games import coin_toss, number_guessing, rock_paper_scissors, tic_tac_toe, dice_roll
from quiz import python_quiz
from scores import save_score, show_scores

while True:
    print("\n==============================")
    print("       PYTHON GAME HUB")
    print("==============================")
    print("1. Tic Tac Toe")
    print("2. Rock Paper Scissors")
    print("3. Coin Toss")
    print("4. Number Guessing")
    print("5. Python Quiz")
    print("6. Dice Roll")
    print("7. View Scores")
    print("8. Exit")
    choice = input("\nEnter your choice: ")
    if choice == "1":
        result = tic_tac_toe()
        if result:
            save_score(result)
    elif choice == "2":
        result = rock_paper_scissors()
        if result:
            save_score(result)
    elif choice == "3":
        result = coin_toss()
        if result:
            save_score(result)
    elif choice == "4":
        result = number_guessing()
        if result:
            save_score(result)
    elif choice == "5":
        result = python_quiz()
        if result:
            save_score(result)
    elif choice == "6":
        result = dice_roll()
        if result:
            save_score(result)
    elif choice == "7":
        show_scores()
    elif choice == "8":
        print("\nThank you for playing!")
        break
    else:
        print("\nInvalid choice. Please try again.")


