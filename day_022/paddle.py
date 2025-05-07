from turtle import Turtle


class Paddle(Turtle):
    UPPER_PADDLE_LIMIT = 270
    LOWER_PADDLE_LIMIT = -255

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 20
        if new_y > self.UPPER_PADDLE_LIMIT:
            return
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        if new_y < self.LOWER_PADDLE_LIMIT:
            return
        self.goto(self.xcor(), new_y)
