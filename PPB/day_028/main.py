from tkinter import *

# Use Color Hunt to Choose a Nice Color: https://colorhunt.co/
# TCL tk Docs (after): https://www.tcl-lang.org/man/tcl8.6/TclCmd/after.htm
# CONSTANTS
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
SECONDS_IN_MIN = 60
MILLISECONDS_IN_SEC = 1000
DEFAULT_WORK_REPS = 4
SESSION_TYPES = 2

reps = 0
timer = ""


# TIMER RESET
def reset_timer():
    if timer != "":
        window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps = 0


# TIMER MECHANISM
def start_timer():
    global reps

    if reps > 0:
        return

    reps += 1

    work_sec = WORK_MIN * SECONDS_IN_MIN
    short_break_sec = SHORT_BREAK_MIN * SECONDS_IN_MIN
    long_break_sec = LONG_BREAK_MIN * SECONDS_IN_MIN

    if reps % (DEFAULT_WORK_REPS * SESSION_TYPES) == 0:
        count_down(long_break_sec)
        title_label.config(text="Break", fg=RED)
    elif reps % SESSION_TYPES == 0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)


# COUNTDOWN MECHANISM
def count_down(count):
    min_cnt = count // SECONDS_IN_MIN
    sec_cnt = count % SECONDS_IN_MIN

    # # dynamic typing
    if sec_cnt < 10:
        sec_cnt = f"0{sec_cnt}"

    canvas.itemconfig(timer_text, text=f"{min_cnt}:{sec_cnt}")

    if count > 0:
        global timer
        timer = window.after(MILLISECONDS_IN_SEC, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = reps // SESSION_TYPES

        for _ in range(work_sessions):
            marks += "✔"

        check_marks.config(text=marks)


# UI SETUP
window = Tk()
window.title("Pomodoro")
window.config(padx=30, pady=30, bg=YELLOW)

title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "normal"))
title_label.grid(column=1, row=0)

canvas = Canvas(width=208, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(106, 112, image=tomato_img)
timer_text = canvas.create_text(104, 132, text="00:00", fill="white", font=(FONT_NAME, 32, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", highlightbackground=YELLOW, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightbackground=YELLOW, command=reset_timer)
reset_button.grid(column=2, row=2)

check_marks = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 42, "bold"))
check_marks.grid(column=1, row=3)

window.mainloop()
