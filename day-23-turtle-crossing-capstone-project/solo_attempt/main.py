# Today is a Capstone day, where we graduate from Turtle academy
# Jokes aside, this is probably the final turtle project for a while
# In this project, we will recreate the "Crossing Road" game
# to an extent. I don't have to start from total scratch since
# the import, screen setup and class definition is taken care of
# I will be adding on this barebones starting code to make the game

# There were 3 difficulty levels: normal hard and expert, and since
# I like challenging myself, I'll go the expert route with only 1 hint
# Thankfully the 2 hints were in a separate file so I closed the 2nd one
# Looks like the hint 1 is basically game rules. Let me write them here:

# 1. The turtle can only move forward(i.e. up), not left/right/down
# 2. Cars will be generated randomly along Y axis and move in RTL direction
# 3. If turtle reaches top of screen, level up and reset, car speed increase
# 4. If turtle hit by car, game over and reset to level 1

import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

screen.listen()

player = Player()
screen.onkey(player.move,"w")

car_manager = CarManager()

scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    car_manager.new_car()
    car_manager.move()
    screen.update()
    
    for car in car_manager.cars:
        if car.crash_with(player.pos()):
            car_manager.reset()
            car_manager.level = 1
            player.reset_all()
    
    if player.ycor() > 280:
        car_manager.level_up()
        player.reset_all()

screen.exitonclick()

# I might save this code as a duplicate since this is as far as I got
# on my own. I guess I'm not cut out to be an expert after all
# Anyway next I'll be looking at the hints and following the course
# This comment signifies that the files in this folder are from before
# I gave up on being successful in this project, since there's not much time
# If you run this file, you will see how far I got. I think the only thing
# I had left to improve was the turtle-car-collision-detection function
# But I don't have such patience, so that's it, see you on the new files