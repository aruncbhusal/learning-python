from turtle import Turtle
import time
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
ALIGNMENT = "center"
FONT_SIZE = 15
FONT = ("Arial", FONT_SIZE, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.up()
        self.goto(0, SCREEN_HEIGHT/2 - 20)
        self.score = 0
        # Adding a high score attribute here
        # The challenge is to extract the high score from a text file called data.txt
        with open("day-24-files-directories-paths\snake-improved\data.txt") as data:
            self.high_score = int(data.read())
        self.show_score()
        
    def show_score(self):
        self.clear()
        self.write(arg = f"Score: {self.score}\tHighscore: {self.high_score}", move = False
                   , align = ALIGNMENT, font = FONT)
    
    def score_up(self):
        self.score += 1
        self.show_score()
                
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(arg = f"GAME OVER", move = False
    #                , align = ALIGNMENT, font = FONT)
        
    def reset_score(self):
        if self.score > self.high_score:
            with open("day-24-files-directories-paths\snake-improved\data.txt", mode = "w") as data:
                self.high_score = self.score
                data.write(f"self.high_score")
        self.score = 0
        self.show_score()
    