import colorgram
from random import choice
from turtle import Turtle, Screen, colormode

# https://pypi.org/project/colorgram.py/

DOT_SIZE = 30
DOTS_BY_ROW = 10
TOTAL_DOTS = DOTS_BY_ROW * DOTS_BY_ROW
DISTANCE = 50
OFFSET = -(DOTS_BY_ROW / 2) * DISTANCE
RIGHT_ANGLE = 90

# colors = colorgram.extract("../images/image1.jpg",50)
# rgb_colors = []
# for color in colors:
#     rgb_colors.append((color.rgb.r, color.rgb.g, color.rgb.b))
# print(rgb_colors)

color_list = [(169, 85, 27), (39, 19, 6), (212, 157, 87), (6, 32, 5), (234, 225, 206), (211, 129, 30), (78, 114, 73),
              (15, 1, 5), (140, 171, 137), (223, 197, 136), (146, 29, 8), (81, 74, 24), (2, 2, 6), (38, 84, 29),
              (106, 145, 98), (202, 222, 198), (222, 99, 40), (175, 207, 163), (247, 242, 244), (232, 179, 155),
              (141, 17, 21), (241, 242, 245), (99, 87, 89), (171, 162, 164), (96, 98, 100), (162, 164, 167),
              (134, 122, 124)]

t = Turtle()
t.hideturtle()
t.penup()
t.speed("fastest")
t.goto(OFFSET, OFFSET)
colormode(255)

for dots_count in range(1, TOTAL_DOTS + 1):

    t.dot(DOT_SIZE, choice(color_list))
    t.forward(DISTANCE)

    if dots_count % 10 == 0 and dots_count < TOTAL_DOTS:
        t.setheading(RIGHT_ANGLE)
        t.forward(DISTANCE)
        t.setheading(2 * RIGHT_ANGLE)
        t.forward(DISTANCE * DOTS_BY_ROW)
        t.setheading(0)

s = Screen()
s.exitonclick()
