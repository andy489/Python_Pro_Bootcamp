import turtle
from turtle import Turtle, Screen
from random import randint, choice

TRACE_TURTLES_COUNT = 6
RACE_START_X = -230
FINAL_X = 230


def create_turtle(color, y):
    t = Turtle(shape="turtle")
    t.color(color)
    t.penup()
    t.goto(RACE_START_X, y)
    return t


s = Screen()
s.setup(width=500, height=400)
user_bet = s.textinput("Make your bet", prompt="Which turtle will win the race? Enter a color: ")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for i in range(TRACE_TURTLES_COUNT):
    all_turtles.append(create_turtle(colors[i], y_positions[i]))

is_race_on = False

if user_bet:
    is_race_on = True

while is_race_on:
    rand_distance = randint(0, 15)
    rand_turtle = choice(all_turtles)
    rand_turtle.forward(rand_distance)

    if rand_turtle.xcor() > FINAL_X:
        is_race_on = False
        winning_color = rand_turtle.pencolor()
        if winning_color == user_bet:
            print(f"You've won! The {winning_color} turtle is the winner!")
        else:
            print(f"You've lost! The {winning_color} turtle is the winner!")

s.exitonclick()
