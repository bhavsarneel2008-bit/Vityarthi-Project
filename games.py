import random

def coin_toss():
    print("\n===== COIN TOSS =====")
    choice = input("Choose heads or tails: ").lower()
    if choice != "heads" and choice != "tails":
        print("Invalid choice,kindly check your choice again!")
        return
    result = random.choice(["heads", "tails"])
    print("Coin result:", result)
    if choice == result:
        print("You won!")
        return "Coin Toss Won"
    else:
        print("You lost!")
        return "Coin Toss Lost"

def number_guessing():
    print("\n===== NUMBER GUESSING =====")
    print("I have selected a number between 1 and 20.")
    number = random.randint(1, 20)
    while True:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Enter a number.")
            continue
        if guess < 1 or guess > 20:
            print("Enter a number between 1 and 20.")
            continue
        if guess == number:
            print("Correct! You have won!")
            return "Number Guessing - Won"
        elif guess < number:
            print("Try a bigger number.")
        else:
            print("Try a smaller number.")


def rock_paper_scissors():
    print("\n===== ROCK PAPER SCISSORS =====")
    choices = ["rock", "paper", "scissors"]
    computer = random.choice(choices)
    player = input("Choose rock, paper or scissors: ").lower()
    if player not in choices:
        print("Invalid choice!")
        return
    print("Computer chose:", computer)
    if player == computer:
        print("It's a tie!")
        return "Rock Paper Scissors - Tie"
    elif player == "rock" and computer == "scissors":
        print("You won!")
        return "Rock Paper Scissors - Won"
    elif player == "paper" and computer == "rock":
        print("You won!")
        return "Rock Paper Scissors - Won"
    elif player == "scissors" and computer == "paper":
        print("You won!")
        return "Rock Paper Scissors - Won"
    else:
        print("You lost!")
        return "Rock Paper Scissors - Lost"

def tic_tac_toe():
    print("\n===== TIC TAC TOE =====")
    board = [" ", " ", " ",
             " ", " ", " ",
             " ", " ", " "]
    player = "X"
    while True:
        print("\n")
        print(board[0], "|", board[1], "|", board[2])
        print("--+---+--")
        print(board[3], "|", board[4], "|", board[5])
        print("--+---+--")
        print(board[6], "|", board[7], "|", board[8])
        print("\nPlayer", player)
        try:
            position = int(input("Enter position (1-9): "))
        except ValueError:
            print("Please enter a number from 1 to 9.")
            continue
        if position < 1 or position > 9:
            print("Please enter a number from 1 to 9.")
            continue
        if board[position - 1] != " ":
            print("That position is already taken.")
            continue
        board[position - 1] = player
        if (board[0] == board[1] == board[2] != " " or
            board[3] == board[4] == board[5] != " " or
            board[6] == board[7] == board[8] != " "):
            print("\nPlayer", player, "wins!")
            return "Tic Tac Toe - Player " + player + " Won"
        if (board[0] == board[3] == board[6] != " " or
            board[1] == board[4] == board[7] != " " or
            board[2] == board[5] == board[8] != " "):
            print("\nPlayer", player, "wins!")
            return "Tic Tac Toe - Player " + player + " Won"
        if (board[0] == board[4] == board[8] != " " or
            board[2] == board[4] == board[6] != " "):
            print("\nPlayer", player, "wins!")
            return "Tic Tac Toe - Player " + player + " Won"
        if " " not in board:
            print("\nIt's a draw!")
            return "Tic Tac Toe - Draw"
        if player == "X":
            player = "O"
        else:
            player = "X"


def dice_roll():
    print("\n===== DICE ROLL =====")
    input("Press Enter to roll the dice...") 
    number = random.randint(1, 6)
    print("You rolled:", number)
    if number == 6:
        print("Lucky! You got a 6.")
    return "Dice Roll - " + str(number)

