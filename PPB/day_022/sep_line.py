from turtle import Turtle


class SepLine(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.draw_sep_line()

    def draw_sep_line(self):
        self.penup()
        self.setheading(270)
        self.goto(0, 300)
        self.hideturtle()

        for pen in range(1, 600):
            if pen % 2 == 0:
                self.penup()
            else:
                self.pendown()

            self.forward(10)
