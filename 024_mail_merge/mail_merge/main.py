# Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ready_to_send".

# w3schools.com/python/ref_file_readlines.asp
# w3schools.com/python/ref_string_replace.asp
# w3schools.com/python/ref_string_strip.asp

PLACEHOLDER = "[name]"

with open("./input/names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("./input/letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()

    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)

        with open(f"./output/ready_to_send/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)
