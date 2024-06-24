from turtle import Turtle
import time

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.up()
        self.hideturtle()
        self.goto(-280,260)
        self.level = 0
        self.show_score()
        
    def show_score(self):
        self.clear()
        self.write(arg= f"Level: {self.level}", align= "left",
                   font= FONT)
        
    def level_up(self):
        self.level += 1
        self.show_score()
        
    def game_over(self):
        g_over = Scoreboard()
        self.clear()
        self.home()
        self.write(arg= "GAME OVER", align= "center",
                   font= FONT)
        