from turtle import Turtle, Screen

timmy = Turtle()
print(timmy)

my_screen = Screen()
print(f"Screen height {my_screen.canvheight}")
print(f"Screen width {my_screen.canvwidth}")

# https://docs.python.org/3/library/turtle.html
timmy.shape("turtle")
timmy.color("brown")
timmy.forward(100)

# Allow our program to continue running until we click on screen
my_screen.exitonclick()