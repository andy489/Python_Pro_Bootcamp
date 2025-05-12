from turtle import Turtle, Screen

# Turtle Documentation: https://docs.python.org/3/library/turtle.html
# Turtle Colors: https://cs111.wellesley.edu/reference/colors

t = Turtle()
t.shape("turtle")

t.color("coral3")

t.width(3)
t.pencolor("bisque2")
t.fd(100)

s = Screen()
print(s.canvheight, s.canvwidth)

s.mainloop()