# This file will have the whole scorebaord class

from turtle import Turtle
FONT_SIZE = 50

class Scoreboard(Turtle):
    def __init__(self, x_pos):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.up()
        self.score = 0
        self.goto(x_pos, 320)
        self.write(arg= f"{self.score}", align= "center",
                   font= ("Impact", FONT_SIZE, "normal"))
        # In the course, both side scores were included within same object
        # But I decided against it for whatever reason
        
    def score_up(self):
        self.score += 1
        self.clear()
        self.write(arg= f"{self.score}", align= "center",
                   font= ("Impact", FONT_SIZE, "normal"))