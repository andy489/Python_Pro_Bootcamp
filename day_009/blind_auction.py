from art import logo

print(logo)


def clear_screen():
    print("\n" * 100)


def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0

    for bidder, bid in bidding_dictionary.items():
        if bid > highest_bid:
            highest_bid = bid
            winner = bidder

    print(f"The winner is {winner} with a bid of ${highest_bid}.")


bids = {}
continue_bidding = True

while continue_bidding:
    name = input("What is your name?: ")
    price = float(input("What is your bid?: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()

    clear_screen()

    if should_continue == "no":
        continue_bidding = False
        find_highest_bidder(bids)
