import random
import turtle as t

t.colormode(255)

tim = t.Turtle()
tim.speed("fastest")

def rand_col():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    random_color = (r, g, b)

    return random_color

def draw_circle(heading):
    tim.setheading(heading)
    tim.color(rand_col())
    tim.circle(100)

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(rand_col())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()



