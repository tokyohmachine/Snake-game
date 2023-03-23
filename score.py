from turtle import Turtle

FONT = ("Courier", 18, "normal")  # Use uppercase for constants, and adjust font name to uppercase.

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)  # Use named arguments for clarity, and remove unnecessary x=0.
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()  # Clear the score before writing it to avoid overwriting old scores.
        self.write(f"Score: {self.score}", align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()  # Clear the score in update_score instead of increase_score.
