import string
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# w3schools Python Writing to File Documentation: https://www.w3schools.com/python/python_file_write.asp
# w3schools Python join() method Documentation: https://www.w3schools.com/python/ref_string_join.asp
# Pyperclip Documentation on PyPi: https://pypi.org/project/pyperclip/
# Entry Widget Docs on tkdocs.com: https://tkdocs.com/tutorial/widgets.html#entry

MIN_UPPER = 1
MAX_UPPER = 3

MIN_LOWER = 5
MAX_LOWER = 8

MIN_SYM = 1
MAX_SYM = 3

MIN_PUN = 1
MAX_PUN = 3

MY_EMAIL = "stoev.andy@gmail.com"

# Password Generator

def start_with_alpha(input_list):
    """Accepts a list of characters and returns it without modification if it's first element is alphabetic ASCII
    char.
    Otherwise, traverses the list in reverse order until it finds an alphabetic ASCII char and swaps it with
    the first char of the list."""

    n = len(input_list) - 1

    while not input_list[0].isalpha():
        temp = input_list[0]
        input_list[0] = input_list[n]
        input_list[n] = temp
        n -= 1

    return input_list

def generate_pass():
    password_entry.delete(0, END)

    lower_letters = string.ascii_lowercase
    upper_letters = string.ascii_uppercase
    numbers = string.digits
    symbols = string.punctuation

    password_list = ([choice(lower_letters) for _ in range(randint(MIN_LOWER, MAX_LOWER))] +
                     [choice(upper_letters) for _ in range(randint(MIN_UPPER, MAX_UPPER))] +
                     [choice(symbols) for _ in range(randint(MIN_SYM, MAX_SYM))] +
                     [choice(numbers) for _ in range(randint(MIN_PUN, MAX_PUN))])

    shuffle(password_list)
    password_list = start_with_alpha(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)

    pyperclip.copy(password)


# Save Password
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left"
                                                  "any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message="These are the details entered:\n"
                                               f"Email: {email}\nPassword: {password}\n"
                                               "Is it ok to save?")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# UI SETUP
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=180, height=180)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(130, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1, sticky="e")

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2, sticky="e")

password_label = Label(text="Password:")
password_label.grid(column=0, row=3, sticky="e")

# Entries
website_entry = Entry(width=36)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=36)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, MY_EMAIL)

password_entry = Entry(width=20)
password_entry.grid(column=1, row=3)

# Buttons
generate_password_button = Button(text="Generate Password", command=generate_pass, width=12)
generate_password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=34, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
