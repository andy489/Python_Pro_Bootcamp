import pandas as pd

# 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
df = pd.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in df.iterrows()}
print(phonetic_dict)

# 2. Create a list of the phonetic code words from a word that the user inputs.
input_word = input("Enter a word: ").upper()
res = [phonetic_dict[sym] for sym in input_word]
print(res)