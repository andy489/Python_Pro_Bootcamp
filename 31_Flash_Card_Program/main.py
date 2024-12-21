# https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists
# https://github.com/hermitdave/FrequencyWords/tree/master/content/2018

from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

to_learn = {}
curr_card = {}

try:
    df = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_df = pandas.read_csv("data/french_words.csv")
    to_learn = original_df.to_dict(orient="records")
else:
    to_learn = df.to_dict(orient="records")


def next_card():
    global curr_card, flip_timer
    window.after_cancel(flip_timer)

    curr_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=curr_card["French"], fill="black")
    canvas.itemconfig(card_back, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=curr_card["English"], fill="white")
    canvas.itemconfig(card_back, image=card_back_img)


def is_known():
    to_learn.remove(curr_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_back = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, bd=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, bd=0, command=is_known)
known_button.grid(row=1, column=1)

next_card()

window.mainloop()
