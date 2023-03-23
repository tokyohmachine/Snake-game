from turtle import Turtle
import random

COLORS = ["purple", "yellow", "red"]  # Define a list of colors as a constant.

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color(random.choice(COLORS))  # Use the constant COLORS instead of the "colors" list.
        self.speed("fastest")  # Use the "fastest" constant instead of 20.
        self.refresh()

    def refresh(self):
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.goto(x, y)
