# https://ascii.co.uk/art

from art import treasure_box

print(treasure_box)

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

first_choice = input('You\'re at a crossroad, where do you want to go? '
                     'Type "left" or "right".\n').lower()

if first_choice == "left":
    second_choice = input('You\'ve come to a lake. '
                          'There is an island in the middle of the lake. '
                          'Type "wait" to wait for a boat. '
                          'Type "swim" to swim across.\n').lower()

    if second_choice == "wait":
        third_choice = input("You arrive at the island unharmed. "
                             "There is house with 3 doors. "
                             "One red, one yellow and one blue. "
                             "Which colour do you choose?\n").lower()

        if third_choice == "red":
            print("It's a room full of fire. Game Over.")
        elif third_choice == "yellow":
            print("You found the treasure. You Win!")
        elif third_choice == "blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You got attacked by an angry trout. Game Over.")

else:
    print("You fell in to a hole. Game Over.")
