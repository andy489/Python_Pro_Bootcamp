from tkinter import *


def miles_to_km():
    try:
        miles = float(miles_input.get())
    except ValueError:
        miles = 0
    if miles > 0:
        km = round(1.609 * miles, 2)
        kilometer_result_label.config(text=f"{km}")
    else:
        kilometer_result_label.config(text="0")

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=120, height=150)
window.config(padx=30, pady=30)

miles_input = Entry(width=7)
miles_input.focus()
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

kilometer_result_label = Label(text="0")
kilometer_result_label.grid(column=1, row=1)

kilometer_label = Label(text="Km")
kilometer_label.grid(column=2, row=1)

calc_button = Button(text="Calculate", command=miles_to_km)
calc_button.grid(column=1, row=2)

window.mainloop()
