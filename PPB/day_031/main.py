from tkinter import *
import pandas as pd
from random import choice

# Wiktionary Frequency Lists: https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists
# 2018 Frequency Lists from Hermit Dave: https://github.com/hermitdave/FrequencyWords/tree/master/content/2018
# Open Subtitles: https://www.opensubtitles.org/en/search/subs
# Google Sheets: https://workspace.google.com/products/sheets/
# Google Translate for Google Sheets: https://support.google.com/docs/answer/3093331?hl=en-GB
# Google Translate Language Codes: https://cloud.google.com/translate/docs/languages?hl=en

BACKGROUND_COLOR = "#B1DDC6"
FLIP_CARD_AFTER = 3000
current_card = {}
to_learn = {}

try:
    df = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = df.to_dict(orient="records")


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(FLIP_CARD_AFTER, func=flip_card)  # type: ignore


def is_known():
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)

card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")

card_background = canvas.create_image(400, 253, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))

canvas.config(bg=BACKGROUND_COLOR, highlightbackground=BACKGROUND_COLOR)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightbackground=BACKGROUND_COLOR, command=next_card)
unknown_button.grid(column=0, row=1)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightbackground=BACKGROUND_COLOR, command=is_known)
known_button.grid(column=1, row=1)

flip_timer = window.after(FLIP_CARD_AFTER, func=flip_card)  # type: ignore
next_card()

window.mainloop()
