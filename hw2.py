
Copy code
import random

def start_game():
    player_name = input("Enter your name: ")

    if not player_name:
        print("Please enter your name before starting the game.")
        return

    user_score = 0
    computer_score = 0
    rounds = 5

    for _ in range(rounds):
        user_roll = random.randint(1, 6)
        computer_roll = random.randint(1, 6)

        print(f"{player_name}'s roll: {user_roll}")
        print("Computer's roll:", computer_roll)

        if user_roll > computer_roll:
            print(f"{player_name} wins this round!\n")
            user_score += 1
        elif user_roll < computer_roll:
            print("Computer wins this round!\n")
            computer_score += 1
        else:
            print("It's a tie!\n")

    display_result(player_name, user_score, computer_score)

def display_result(player_name, user_score, computer_score):
    print("Game Over!\n")
    print(f"{player_name}'s Score: {user_score}")
    print(f"Computer's Score: {computer_score}")

    if user_score > computer_score:
        print(f"{player_name} wins! 🎉")
    elif user_score < computer_score:
        print("Computer wins! 🤖")
    else:
        print("It's a tie! 🤝")

if __name__ == "__main__":
    start_game()