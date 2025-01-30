from turtle import Turtle, Screen

MOVE_STEP = 20


def move_forward():
    t.forward(MOVE_STEP)


t = Turtle()
s = Screen()

s.listen()

s.onkey(key="space", fun=move_forward)

s.exitonclick()
