import string
from json import JSONDecodeError
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
import io

# w3schools Python Writing to File Documentation: https://www.w3schools.com/python/python_file_write.asp
# w3schools Python join() method Documentation: https://www.w3schools.com/python/ref_string_join.asp
# Pyperclip Documentation on PyPi: https://pypi.org/project/pyperclip/
# Entry Widget Docs on tkdocs.com: https://tkdocs.com/tutorial/widgets.html#entry
# Python JSON Module Documentation: https://docs.python.org/3/library/json.html

MIN_UPPER = 1
MAX_UPPER = 3

MIN_LOWER = 5
MAX_LOWER = 8

MIN_SYM = 1
MAX_SYM = 3

MIN_PUN = 1
MAX_PUN = 3

MY_EMAIL = "stoev.andy@gmail.com"


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


def update_data(data, new_data):
    data.update(new_data)  # update JSON data

    with open("data.json", "w") as data_file:  # type: io.TextIOWrapper
        # Saving updated data
        json.dump(data, data_file, indent=4)


def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message="These are the details entered:\n"
                                               f"Email: {email}\nPassword: {password}\n"
                                               "Is it ok to save?")
        if is_ok:
            try:
                with open("data.json", "r") as data_file:  # type: io.TextIOWrapper
                    # Reading old data
                    data = json.load(data_file)
            except JSONDecodeError:
                with open("data.json", "w") as data_file:
                    data_file.write("{}")
                with open("data.json", "r") as data_file:
                    data = json.load(data_file)
                update_data(data, new_data)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                # Updating old data with new data
                update_data(data, new_data)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)


def find_password():
    website = website_entry.get()

    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    except JSONDecodeError:
        with open("data.json", "w") as data_file:
            data_file.write("{}")
        messagebox.showinfo(title="Error", message="No Data Yet.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")


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

password_entry = Entry(width=36)
password_entry.grid(column=1, row=3, columnspan=2)

# Buttons
search_button = Button(text="Search", width=12, command=find_password)
search_button.grid(row=1, column=2)

generate_password_button = Button(text="Generate Password", command=generate_pass, width=12)
generate_password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=34, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
