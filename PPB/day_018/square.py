# Turtle Graphics Documentation: https://docs.python.org/3/library/turtle.html
# Trinket Turtle Colors: https://trinket.io/docs/colors
# Turtle Colors: https://cs111.wellesley.edu/reference/colors

from turtle import Turtle, Screen

def square(turtle, n):
    for _ in range(4):
        turtle.fd(n)
        turtle.left(90)

t = Turtle()
t.shape('turtle')
t.shapesize(stretch_wid=3)
t.color("coral")
t.width(4)
t.pencolor('blue')

square(t, 100)












s = Screen()
s.exitonclick()
