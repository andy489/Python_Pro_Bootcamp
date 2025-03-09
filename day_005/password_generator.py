# Check which services you sign up to have been compromised
# https://haveibeenpwned.com/
import string
import random as rand

FIRST_PUNCTUATION_SYMBOLS = 11

letters = list(string.ascii_lowercase)
symbols = list(string.punctuation[:FIRST_PUNCTUATION_SYMBOLS])
symbols.remove("'")
digits = list(string.digits)

print("Welcome to the PyPassword Generator!")

nr_letters = int(input("How many letter would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_digits = int(input("How many numbers would you like?\n"))

password_list = []

for char in range(nr_letters):
    password_list.append(rand.choice(letters))

for char in range(nr_symbols):
    password_list.append(rand.choice(symbols))

for char in range(nr_digits):
    password_list.append(rand.choice(digits))

rand.shuffle(password_list)
password = "".join(password_list)

print(f"Your password is: {password}")
