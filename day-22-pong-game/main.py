# In today's lesson we'll be creating another game: Pong
# Atari's machine-breaking popular game

from turtle import Screen
# Let's first start with the screen setup
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

PADDLE_POS = [(-550, 0), (550, 0)]
SCORE_POS = [-80, 80]

screen = Screen()
screen.setup(width= 1200, height= 800)
screen.title("Pong-chan")
screen.bgcolor("black")
screen.tracer(0)

screen.listen()

r_paddle = Paddle(PADDLE_POS[1])
# I originally had a method to set position but this looks neater
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")


l_paddle = Paddle(PADDLE_POS[0])
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

ball = Ball()

left_score = Scoreboard(SCORE_POS[0])
right_score = Scoreboard(SCORE_POS[1])

game_on = True

while game_on:
    screen.update()
    time.sleep(0.05)
    # I knew in order to speed up the game, the course would use
    # less sleep time, which is what I did with snake game before
    # but this time I experimented with the speed of the ball instead
    # I imported time when creating paddle, but it wasn't used
    # until I got the ball part. I'm still not sure though
    if ball.collide_with_wall():
        ball.deflect("vertical")
    if ball.hit_paddle(l_paddle) or ball.hit_paddle(r_paddle):
        ball.deflect("horizontal")
    if ball.miss():
       if ball.miss_side == "left":
           right_score.score_up()
       elif ball.miss_side == "right":
           left_score.score_up()
       ball.regen()
        
    ball.move()
      
screen.exitonclick()