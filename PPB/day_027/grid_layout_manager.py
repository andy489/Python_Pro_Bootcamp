from tkinter import *

window = Tk()
window.title("Grid Layout Playground")
window.minsize(width=500, height=300)
window.config(padx=40, pady=80)

# Label
my_label = Label(text="I'm a Label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)
my_label.config(padx=10, pady=10)

# Button
button = Button(text="Click Me")
button.grid(column=1, row=1)

new_button = Button(text="New Button")
new_button.grid(column=2, row=0)

# Entry
my_input = Entry(width=10)
my_input.grid(column=3, row=2)

window.mainloop()
