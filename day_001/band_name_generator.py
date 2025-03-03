print("Welcome to the Band Name generator.")

last_meal = input("What's the last thing you ate?\n").title()
pet_name = input("What is your pet's name?\n").capitalize()

band_name = pet_name + "'s " + last_meal

print("Your band name could be \"" + band_name + "\"!")
