import random
import getpass

# Constants
EMOJIS = {"rock": "🪨", "paper": "📄", "scissors": "✂️"}
OPTIONS = ("rock", "paper", "scissors")
WIN_SCORE = 3

# Function to determine the winner of a round
def determine_winner(choice1, choice2):
    if choice1 == choice2:
        return "tie"
    elif (
        (choice1 == "rock" and choice2 == "scissors") or
        (choice1 == "scissors" and choice2 == "paper") or
        (choice1 == "paper" and choice2 == "rock")
    ):
        return "player1"
    else:
        return "player2"

# Function to play against the computer
def play_robot():
    while True:
        count_user, count_robot = 0, 0

        while count_user < WIN_SCORE and count_robot < WIN_SCORE:
            user_choice = input("Pick between Rock, Paper or Scissors: ").lower()
            if user_choice not in OPTIONS:
                print("Invalid choice. Try again!\n")
                continue

            computer_choice = random.choice(OPTIONS)
            print(f"You chose {EMOJIS[user_choice]}")
            print(f"Computer chose {EMOJIS[computer_choice]}")

            result = determine_winner(user_choice, computer_choice)
            if result == "tie":
                print("It's a tie!\n")
            elif result == "player1":
                print("You win this round!\n")
                count_user += 1
            else:
                print("You lose this round!\n")
                count_robot += 1

            print(f"Score: You {count_user} - {count_robot} Computer\n")

        if count_user == WIN_SCORE:
            print("🏆 You won the match!\n")
        else:
            print("💀 You lost the match!\n")

        if not play_again():
            break

# Function to play against another player
def play_player():
    player1 = input("Enter your name: ")
    player2 = input("Enter your name: ")

    while True:
        count_player1, count_player2 = 0, 0

        while count_player1 < WIN_SCORE and count_player2 < WIN_SCORE:
            print("Pick between Rock, Paper or Scissors")

            while True:
                player1_choice = getpass.getpass(f"{player1} choice: ").lower()
                player2_choice = getpass.getpass(f"{player2} choice: ").lower()
                if player1_choice not in OPTIONS or player2_choice not in OPTIONS:
                    print("Invalid choice! Please respect the rules.\n")
                    continue
                break

            print(f"{player1} chose {EMOJIS[player1_choice]} and {player2} chose {EMOJIS[player2_choice]}")

            result = determine_winner(player1_choice, player2_choice)
            if result == "tie":
                print("It's a tie!\n")
            elif result == "player1":
                print(f"🏆 {player1} wins this round!\n")
                count_player1 += 1
            else:
                print(f"🏆 {player2} wins this round!\n")
                count_player2 += 1

            print(f"Score: {player1} {count_player1} - {count_player2} {player2}\n")

        if count_player1 == WIN_SCORE:
            print(f"🏆 {player1} won the match!\n")
        else:
            print(f"🏆 {player2} won the match!\n")

        if not play_again():
            break

# Function to ask if players want to play again
def play_again():
    while True:
        should_continue = input("Start another match? (y/n): ").lower()
        if should_continue == 'y':
            print("\nStarting a new match...\n")
            return True
        elif should_continue == 'n':
            print("Thanks for playing! 👋")
            return False
        else:
            print("Error! Please type 'y' or 'n'.\n")

# Main function
def main():
    print("Welcome to Rock, Paper, Scissors Game!")
    choice = input("Do you want to play with a robot or with another person? (player/robot): ").lower()

    if choice == "robot":
        play_robot()
    elif choice == "player":
        play_player()
    else:
        print("Invalid choice! Please restart the game.")

if __name__ == "__main__":
    main()
