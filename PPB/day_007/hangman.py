import random as rand
from art import *
from hangman_words import word_list

print(logo)

lives = 6
chosen_word = rand.choice(word_list)
word_len = len(chosen_word)
curr_state = ["_"] * word_len
chosen_symbols = []

# print("Psst... " + chosen_word)

while True:
    print("Word to guess: " + "".join(curr_state))
    print(lives_info.format(lives))

    guess = input("Guess a letter: ").lower()

    if guess in chosen_symbols:
        print(f"You've already guessed {guess}")
    else:
        chosen_symbols.append(guess)

    right_guess = False
    for i in range(word_len):
        if chosen_word[i] == guess:
            right_guess = True
            curr_state[i] = guess

    if not right_guess:
        lives -= 1

    if "_" not in curr_state:
        print(f"Congratulations! The word is: {chosen_word}")
        print(win_msg)
        break

    print(stages[lives])

    if lives == 0:
        print(lose_msg)
        print(f"The word you were trying to guess was: {chosen_word}")
        break
