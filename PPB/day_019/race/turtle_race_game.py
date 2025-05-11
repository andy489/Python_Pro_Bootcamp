from turtle import Turtle, Screen
from random import randint, choice, choices

TRACE_TURTLES_COUNT = 6
RACE_START_X = -230
FINAL_X = 230
SQUARE_SIDE = 20


def create_turtle(color, y):
    t = Turtle(shape="turtle")
    t.color(color)
    t.penup()
    t.goto(RACE_START_X, y)
    return t


s = Screen()
s.setup(width=500, height=400)


def finish_line():
    s.tracer(0)

    for _ in range(20):
        t = Turtle(shape="square")
        t.color("black")
        t.penup()
        t.goto(x=FINAL_X + [0, -20][_ & 1], y=-180 + _ * 20)
    s.update()


finish_line()
s.tracer(1)

user_bet = s.textinput("Make your bet",
                       prompt="Which turtle will win the race? Enter a color \n"
                              "('red', 'orange', 'yellow', 'green', 'blue', 'purple'): ").lower()

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for i in range(TRACE_TURTLES_COUNT):
    all_turtles.append(create_turtle(colors[i], y_positions[i]))

is_race_on = False

if user_bet:
    is_race_on = True


def display_msg(text):
    msg = Turtle()
    msg.hideturtle()
    msg.penup()
    msg.goto(-233, 100)
    msg.write(text, font=("Arial", 18, "bold"))


while is_race_on:
    rand_distance = randint(0, 15)
    rand_turtle = choice(all_turtles)
    # rigged in favour of red turtle:
    # rand_turtle = choices(all_turtles, weights=[0.25, 0.15, 0.15, 0.15, 0.15, 0.15], k=1)[0]
    rand_turtle.forward(rand_distance)

    if rand_turtle.xcor() > FINAL_X - 2 * SQUARE_SIDE - 10:
        is_race_on = False
        winning_color = rand_turtle.pencolor()

        if winning_color == user_bet:
            display_msg(f"🏁 You've won! 🏆 The {winning_color} turtle is the winner!")
        else:
            display_msg(f"🏁 You've lost! 😞 The {winning_color} turtle is the winner!")

s.exitonclick()
