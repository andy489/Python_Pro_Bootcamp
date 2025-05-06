from turtle import Turtle, Screen

t = Turtle()
s = Screen()


def move_forward():
    t.fd(10)

# Turtle listen method: https://docs.python.org/3/library/turtle.html#turtle.listen
s.listen()
s.onkey(key="space", fun=move_forward)

s.exitonclick()
