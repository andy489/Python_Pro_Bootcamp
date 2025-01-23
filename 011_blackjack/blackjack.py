from art import logo
from random import choice


def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = choice(cards)
    return card


def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    total = 0
    soft_aces = 0
    for card in cards:
        if card == 11:
            soft_aces += 1
            total += 11
        else:
            total += card
    while total > 21 and soft_aces > 0:
        total -= 10
        soft_aces -= 1
    return total


def compare(u_score, c_score):
    if u_score == c_score:
        return "Hold 🙃"
    elif c_score == 0:
        "You lose. Opponent has Blackjack 😱"
    elif u_score > 21:
        return "You went over - Bust. You lose. 😭"
    elif c_score > 21:
        return "You win. Opponent went over. 😁"
    elif u_score > c_score:
        return "You win 😏"
    else:
        return "You lose 😤"


def clear_console():
    print("\n" * 20)


def play_game():
    print(logo)

    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first cards: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to hit, type 'n' to stand: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    clear_console()
    play_game()
