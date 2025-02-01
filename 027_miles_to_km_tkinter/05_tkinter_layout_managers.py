import tkinter
from tkinter import *


def button_clicked():
    print("I got clicked")
    my_label.config(text=input_txt.get())


window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label
my_label = Label(text="I am a Label", font=("Arial", 18, "bold"))
my_label.config(text="New Text")
# my_label.pack(side="left")
# my_label.place(x=0, y=0)
my_label.grid(column=0, row=0)
my_label.config(padx=30, pady=30)

# Button
button = Button(text="Click Me", command=button_clicked)
# button.pack(side="left")
# button.place(x=100, y=100)
button.grid(column=1, row=1)

# New Button
new_button = Button(text="Click Me", command=button_clicked)
# button.pack(side="left")
# button.place(x=100, y=100)
new_button.grid(column=2, row=0)

# Entry
input_txt = Entry(width=10)
print(input_txt.get())
# input_txt.pack(side="left")
# input_txt.place(x=200, y=200)
input_txt.grid(column=3, row=2)

tkinter.mainloop()
