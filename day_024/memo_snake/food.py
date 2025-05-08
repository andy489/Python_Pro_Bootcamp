from turtle import Turtle
from random import randint as ri


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("coral")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.goto(ri(-280, 280), ri(-280, 280))
