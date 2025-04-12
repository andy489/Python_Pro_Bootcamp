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
        return "Hold 🙃\n"
    elif c_score == 0:
        "You lose. Dealer has Blackjack 😱\n"
    elif u_score > 21:
        return "You lose. You Bust. 😭\n"
    elif c_score > 21:
        return "You win. Dealer Bust. 😁\n"
    elif u_score > c_score:
        return "You win 😏\n"
    else:
        return "You lose 😤\n"


def play_game():
    player_cards = []
    player_score = 0

    dealer_cards = []
    dealer_score = 0

    is_game_over = False

    for _ in range(2):
        player_cards.append(deal_card())
        dealer_cards.append(deal_card())

    while not is_game_over:
        player_score = calculate_score(player_cards)

        print(f"Your cards: {player_cards}, current score: {player_score}")
        print(f"Dealer's first card is: {dealer_cards[0]}")

        if player_score > 21:
            is_game_over = True
        else:
            player_hit = input("Type 'y' to hit, type 'n' to stand:\n")
            if player_hit == "y":
                player_cards.append(deal_card())
            else:
                is_game_over = True

    dealer_score = calculate_score(dealer_cards)

    if player_score <= 21:
        while dealer_score < 17:
            dealer_cards.append(deal_card())
            dealer_score = calculate_score(dealer_cards)

        print(f"Your final hand: {player_cards}, final score: {player_score}")
        print(f"Dealer's final hand: {dealer_cards}, final score: {dealer_score}")
    else:
        print(f"Your final hand: {player_cards}, final score: {player_score}")

    print(compare(player_score, dealer_score))

    continue_playing = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

    if continue_playing == "y":
        clear_console()
        print(logo)
        play_game()


def clear_console():
    print("\n" * 20)


print(logo)
play_game()
