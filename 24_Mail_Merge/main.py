INVITED_NAMES_PATH = "./Input/Names/invited_names.txt"
STARTING_LETTER_PATH = "./Input/Letters/starting_letter.txt"
READY_TO_SEND_PATH = "./Output/ReadyToSend/"

PLACEHOLDER = "[name]"

with open(INVITED_NAMES_PATH) as names_file:
    names = names_file.readlines()

with open(STARTING_LETTER_PATH) as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)

        with open(f"{READY_TO_SEND_PATH}/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)
