from turtle import Turtle, Screen

t = Turtle()

t.shape("turtle")
t.color("brown")

for i in range(20):
    if i & 1:
        t.penup()
    else:
        t.pendown()
    t.forward(10)

s = Screen()
s.exitonclick()