from turtle import Turtle

MOVE_DISTANCE = 20
STARTING_POSITIONS = [(0, 0), (-40, 0), (-20, 0)]
DIRECTIONS = {
    "Left": 180,
    "Up": 90,
    "Right": 0,
    "Down": 270,
}


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def _add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)

        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        self._add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DIRECTIONS["Down"]:
            self.head.setheading(DIRECTIONS["Up"])

    def down(self):
        if self.head.heading() != DIRECTIONS["Up"]:
            self.head.setheading(DIRECTIONS["Down"])

    def left(self):
        if self.head.heading() != DIRECTIONS["Right"]:
            self.head.setheading(DIRECTIONS["Left"])

    def right(self):
        if self.head.heading() != DIRECTIONS["Left"]:
            self.segments[0].setheading(DIRECTIONS["Right"])
