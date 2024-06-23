from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
# The time module has a function to set a delay on the execution
# This can let us maintain a constant frame rate

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
# This makes it so that the screen needs to be updated manually

snake = Snake()
food = Food()
scorebaord = Scoreboard()

screen.listen()
# The onkey() method has positional arguments fun and key
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Next is to get the snake moving, I'll use a keypress to start the game later
# We can see that when we try to move the snake, each part moves individually,
# so it doesn't look visually pleasing, so to redraw the screen once it's done,
# we will need to use the tracer() and update() methods of the screen class
game_continue = True
while game_continue:
    screen.update()
    if scorebaord.score<20:
        time.sleep(0.05 + 0.05*0.05*(20-scorebaord.score))
    else:
        time.sleep(0.05)
    # After score of 20 the speed will be fixed at 0.05
    
    snake.move()
    
    # Now to detect collision with the food we will use the turtle method distance
    if snake.head.distance(food) < 15:
        # Since turtle is 20 and food is 10, detection might be optimal at middle
        food.refresh()
        scorebaord.score_up()
        snake.extend_snake()
    
    # Detect collision with the wall    
    if snake.head.xcor() > WALL["x"] or snake.head.ycor() > WALL["y"] or\
        snake.head.xcor() < -WALL["x"] or snake.head.ycor() < -WALL["y"]:
        scorebaord.game_over()
        game_continue = False
    
    # Detect collision with the tail
    for part in snake.body[1:]:
        # if part == snake.head:
        # # This allows us to skip comparing position of head with the head itself
        #     pass
        # The above code isn't needed since we have used slicing above
        if snake.head.distance(part) <= 10:
                scorebaord.game_over()
                game_continue = False
        
screen.exitonclick()