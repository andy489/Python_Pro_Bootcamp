from turtle import Turtle, Screen

MOVE_STEP = 10
HEADING_STEP = 10

t = Turtle()
s = Screen()


def move_forward():
    t.forward(MOVE_STEP)


def move_backwards():
    t.backward(MOVE_STEP)


def turn_left():
    t.setheading(t.heading() + HEADING_STEP)


def turn_right():
    t.setheading(t.heading() - HEADING_STEP)


def clear_screen():
    t.clear()
    t.penup()
    t.home()
    t.pendown()


s.listen()
s.onkey(move_forward, "w")
s.onkey(move_backwards, "s")
s.onkey(turn_left, "a")
s.onkey(turn_right, "d")

s.onkey(clear_screen, "c")

s.exitonclick()
