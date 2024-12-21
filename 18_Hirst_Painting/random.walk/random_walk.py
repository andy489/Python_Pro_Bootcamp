import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

tim.pensize(10)
tim.speed("fastest")

def rand_col():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    random_color = (r, g, b)

    return random_color

# colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]

for _ in range(200):
    tim.color(rand_col())
    tim.forward(30)
    tim.setheading(random.choice(directions))

t.mainloop()
