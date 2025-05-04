# https://higherlowergame.com/

from art import logo, vs
from game_data import data
from random import choice
from os import linesep


def format_data(account):
    """Take the account data and returns the printable format."""
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_description}, from {account_country}."


def check_answer(user_guess, a_followers, b_followers):
    """Take a user's guess and the follower counts and returns if they got it right"""
    if a_followers > b_followers:
        return user_guess == 'a'
    else:
        return user_guess == 'b'

def clear_screen():
    print(linesep * 20)
    print(logo)

print(logo)
score = 0
game_should_continue = True
account_b = choice(data)

while game_should_continue:
    account_a = account_b
    account_b = choice(data)

    while account_a == account_b:
        account_b = choice(data)

    print(f"Compare A: {format_data(account_a)}", vs, f"Compare B: {format_data(account_b)}", sep=linesep)

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    clear_screen()

    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    if is_correct:
        score += 1
        print(f"You're right! Current score {score}.")
    else:
        print(f"Sorry, that's wrong. Final score: {score}.")
        game_should_continue = False
