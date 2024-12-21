import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")

# colors = colorgram.extract('image1.jpg', 30)
#
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

color_list1 = [
    (169, 85, 27), (39, 19, 6), (212, 157, 87), (6, 32, 5), (234, 225, 206), (211, 129, 30), (78, 114, 73), (15, 1, 5),
    (140, 171, 137), (223, 197, 136), (146, 29, 8), (81, 74, 24), (2, 2, 6), (38, 84, 29), (106, 145, 98),
    (202, 222, 198), (222, 99, 40), (175, 207, 163), (247, 242, 244), (232, 179, 155), (141, 17, 21), (241, 242, 245),
    (99, 87, 89), (171, 162, 164), (96, 98, 100), (162, 164, 167), (134, 122, 124)
]

color_list2 = [
    (96, 81, 70), (75, 95, 112), (24, 39, 53), (56, 33, 22), (131, 157, 170), (39, 25, 31), (92, 80, 87),
    (173, 154, 131), (76, 98, 90), (49, 62, 84), (198, 230, 238), (235, 230, 215), (131, 165, 156),
    (33, 52, 47), (83, 55, 49), (89, 144, 156), (93, 63, 28), (114, 125, 147), (74, 57, 66), (218, 243, 239),
    (157, 143, 149), (48, 72, 67), (100, 143, 134), (37, 75, 81), (141, 214, 224), (164, 129, 81),
    (211, 202, 155), (126, 230, 218), (241, 238, 240), (163, 113, 99)
]

tim.hideturtle()
tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.pendown()
    tim.dot(20, random.choice(color_list1))
    tim.penup()
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()
