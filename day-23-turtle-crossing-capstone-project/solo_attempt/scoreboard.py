from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.up()
        self.hideturtle()
        self.goto(-200,260)
        self.level = 0
        self.show_score()
        
    def show_score(self):
        self.clear()
        self.write(arg= f"Level: {self.level}", align= "center",
                   font= FONT)
        
    def level_up(self):
        self.level += 1
        self.show(self.score)
        