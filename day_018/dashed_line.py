from turtle import Turtle, Screen

t = Turtle(shape="turtle")
t.color("brown")

for _ in range(20):
    [t.penup, t.pendown][_ & 1]()
    t.fd(10)

s = Screen()
s.exitonclick()
