from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake-chan")

WALL_PADDING = 15
WALL = {
    "x" : screen.window_height()/2 - WALL_PADDING,
    "y" : screen.window_width()/2 - WALL_PADDING
}

screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

def crash_sequence():
    snake.reset_snake()
    scoreboard.reset_score()
    

game_continue = True
while game_continue:
    screen.update()
    if scoreboard.score<20:
        time.sleep(0.05 + 0.05*0.05*(20-scoreboard.score))
    else:
        time.sleep(0.05)

    
    snake.move()
    
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.score_up()
        snake.extend_snake()
    
    # Detect collision with the wall    
    if snake.head.xcor() > WALL["x"] or snake.head.ycor() > WALL["y"] or\
        snake.head.xcor() < -WALL["x"] or snake.head.ycor() < -WALL["y"]:
        crash_sequence()

    # Detect collision with the tail
    for part in snake.body[1:]:
        if snake.head.distance(part) <= 10:
            crash_sequence()

        
screen.exitonclick()