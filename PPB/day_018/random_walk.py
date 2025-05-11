from turtle import Turtle, Screen, colormode
from random import choice, randint

# What is a Random Walk?: https://en.wikipedia.org/wiki/Random_walk
DIRECTIONS = [0, 1, 2, 3]
STEP = 50
PEN_SIZE = 10
RIGHT_ANGLE = 90


def get_rand_color():
    """
    Returns a 3-tuple of random numbers in the range 0 - 255
    eg : (89, 103, 108)
    """
    return (randint(0, 255) for _ in range(3))


def random_walk(t: Turtle):
    """Draws endlessly in random directions"""
    while True:
        t.right(choice(DIRECTIONS) * RIGHT_ANGLE)
        t.color(*get_rand_color())
        t.forward(STEP)


tim = Turtle()
tim.hideturtle()
tim.speed("fast")
tim.pensize(PEN_SIZE)
screen = Screen()
colormode(255)

random_walk(tim)

screen.exitonclick()
