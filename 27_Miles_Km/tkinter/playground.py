# tkinter
# Graphical User Interfaces (GUI)

from tkinter import *

def button_clicked():
    # print("I got clicked")
    # my_label.config(text="Button Got Clicked")
    new_text = e_input.get()
    my_label.config(text=new_text)

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=40, pady=40)

# Label

my_label = Label(text="I'm a Label", font=("Arial", 24, "bold"))
# my_label.pack(side="left")
# my_label.place(x=100, y=200)
my_label.grid(column=0, row=0)
my_label.config(padx=15, pady=15)

# my_label["text"] = "New Text"
# my_label.config(text="Another New Text")

# Button
button = Button(text="Click me", command=button_clicked)
# button.pack(side="left")
button.grid(column=1,row=1)

new_button = Button(text="New Button")
new_button.grid(column=2, row=0)

# Entry component
e_input = Entry(width=10)
# e_input.pack(side="left")
e_input.grid(column=3, row=2)

window.mainloop()
