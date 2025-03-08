# https://wrpsa.com/the-official-rules-of-rock-paper-scissors/

from art import rock, paper, scissors
from random import randint

game_images = [rock, paper, scissors]
outcome_names = ["rock", "paper", "scissors"]

user_choice = int(input("What do you choose? Type 0 for Rock, "
                        "1 for Paper or 2 for Scissors.\n"))
if 0 <= user_choice <= 2:
    print(f"You chose {outcome_names[user_choice]}: "
          f"{game_images[user_choice]}")

computer_choice = randint(0, 2)
print(f"Computer chose {outcome_names[computer_choice]}: "
      f"{game_images[computer_choice]}")

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number. You lose!")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif user_choice == 2 and computer_choice == 0:
    print("You lose!")
elif user_choice == computer_choice:
    print("It's a draw!")
elif computer_choice > user_choice:
    print("You lose!")
elif user_choice > computer_choice:
    print("You win!")
