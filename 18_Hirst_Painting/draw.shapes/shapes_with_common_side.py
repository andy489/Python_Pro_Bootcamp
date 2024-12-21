import random
from turtle import Turtle, Screen
import matplotlib.colors as mcolors

t = Turtle()
t.shape("turtle")
t.color("DarkOrange")

# for _ in range (4):
#     t.forward(100)
#     t.right(90)

# for _ in range (20):
#     if _ % 2 == 0:
#         t.pendown()
#         t.forward(10)
#     else:
#         t.penup()
#         t.forward(10)

FIRST_SHAPE_SIDES_COUNT = 3
LAST_SHAPE_SIDES_COUNT = 10
FULL_ROTATION = 360
SIDE_LEN = 100

def draw_shape(num_sides):
    angle = FULL_ROTATION/ num_sides
    for _ in range(num_sides):
        t.forward(SIDE_LEN)
        t.right(angle)

def random_color_generator():
    color = random.choice(list(mcolors.CSS4_COLORS.keys()))
    return color

for sides in range(FIRST_SHAPE_SIDES_COUNT, LAST_SHAPE_SIDES_COUNT):
    t.color(random_color_generator())
    draw_shape(sides)

screen = Screen()
screen.colormode(255)
screen.exitonclick()