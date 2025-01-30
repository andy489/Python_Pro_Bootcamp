from turtle import Turtle, Screen, colormode
from random import randint, choice

FULL_ROTATION = 360


def get_rand_color():
    """
    Returns a 3-tuple of random numbers in the range 0 - 255
    eg : (89, 103, 108)
    """
    return (randint(0, 255) for _ in range(3))


colormode(255)
t = Turtle()

t.hideturtle()
t.speed("fastest")


def draw_spirograph(size_of_gap):
    for _ in range(int(FULL_ROTATION / size_of_gap)):
        t.color(*get_rand_color())
        t.circle(100)
        t.setheading(t.heading() + size_of_gap)


draw_spirograph(5)

s = Screen()
s.exitonclick()
