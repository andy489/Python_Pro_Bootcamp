from turtle import Turtle, Screen
# from turtle import Turtle as Tur, Screen as Scr
# from turtle import *

# https://docs.python.org/3/library/turtle.html

tim = Turtle("turtle")
tim.shape("turtle")

# https://www.tcl.tk/man/tcl8.4/TkCmd/colors.htm
# https://cs111.wellesley.edu/archive/cs111_fall14/public_html/labs/lab12/tkintercolor.html
screen = Screen()
tim.color("coral")

for _ in range(4):
    tim.forward(100)
    tim.left(90)

screen.exitonclick()
