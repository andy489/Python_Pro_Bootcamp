# Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ready_to_send".

# w3schools.com/python/ref_file_readlines.asp
# w3schools.com/python/ref_string_replace.asp
# w3schools.com/python/ref_string_strip.asp

from os import path, makedirs

PLACEHOLDER = "[name]"
DESTINATION_FOLDER = "ready_to_send"

with open("./input/names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("./input/letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()

    res_path = f"./output/{DESTINATION_FOLDER}/"
    path_exists = path.exists(res_path)
    if not path_exists:
        makedirs(res_path)

    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)

        with open(f"{res_path}/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)
