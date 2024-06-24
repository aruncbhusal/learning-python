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

# (This comment indicates that I've given up on doing it solo and have
# resorted to taking help from the course. To see how far I got before it,
# you can visit the solo_attempt folder.)

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
screen.title("Cross The Road Carefully Turtle-chan")
screen.tracer(0)

screen.listen()

player = Player()
screen.onkeypress(player.move,"w")
# onkey() didn't work when holding, it registered when released only

car_manager = CarManager()

scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    car_manager.new_car()
    car_manager.move()
    screen.update()
    for car in car_manager.cars:
        if car.distance(player) < 20:
            # I had a separate method to check this but
            # didn't know how simple this was
            # I used to reset my game when this happened
            # But maybe it's better to just quit
            scoreboard.game_over()
            game_is_on = False
    if player.at_finish_line():
        car_manager.level_up()
        scoreboard.level_up()
        player.go_to_start()

screen.exitonclick()