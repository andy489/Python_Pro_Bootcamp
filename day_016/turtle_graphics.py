from turtle import Turtle, Screen

# Turtle Documentation: https://docs.python.org/3/library/turtle.html
# Turtle Colors: https://cs111.wellesley.edu/reference/colors

timmy = Turtle()

timmy.shape("turtle")
timmy.color("coral3")
timmy.width(3)
timmy.pencolor("bisque2")
timmy.fd(100)

screen = Screen()
screen.setup(600, 600)
screen.mainloop()
