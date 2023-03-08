from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        self.score_1 = 0
        self.score_2 = 0
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 230)
        self.write(f"{self.score_1}:{self.score_2}", align="center", font=("Courier", 40, "normal"))

    def update_score(self):
        self.clear()
        self.write(f"{self.score_1}:{self.score_2}", align="center", font=("Courier", 40, "normal"))

    def score1_increment(self):
        self.score_1 += 1
        self.update_score()

    def score2_increment(self):
        self.score_2 += 1
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        if self.score_1==5:
            self.write(f" Game Over\nPlayer 1 Won", align="center", font=("Ariel", 30, "normal"))
        else:
            self.write(f" Game Over\nPlayer 2 Won", align="center", font=("Ariel", 30, "normal"))