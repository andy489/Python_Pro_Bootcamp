from turtle import Turtle

ALIGNMENT = "center"
FONT_SCORE = ("Arial", 18, "normal")
FONT_GAME_OVER = ("Arial", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = 0
        with open("high_score_data.txt") as data:
            self.highscore = int(data.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 275)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} Highscore: {self.highscore}", align=ALIGNMENT, font=FONT_SCORE)

    def increment_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("high_score_data.txt", mode="w") as data:
                data.write(f"{self.highscore}")
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER", align=ALIGNMENT, font=FONT_GAME_OVER)
