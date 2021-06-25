from turtle import Turtle


class Scorecard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("scores.txt","r") as f:
            self.high_score = int(f.read())
        self.color("white")
        self.penup()
        self.goto(0,260)
        self.hideturtle()
        self.update_scorecard()

    def write_score(self):
        with open("scores.txt","w") as f:
            f.write(str(self.high_score))

    def update_scorecard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}",align="center",font=("Courier", 24, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.write_score()
        self.update_scorecard()

    def increase_score(self):
        self.score += 1
        self.update_scorecard()