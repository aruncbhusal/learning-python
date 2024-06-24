from turtle import Turtle,clearscreen
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

# I tried to think of a different solution for long but I think I will
# have to just trust my guts and make two classes for this one.

class CarManager:
    def __init__(self):
        self.level = 1
        self.cars = []
        
    def new_car(self):
        if random.randint(1,random.randint(5,10)) == 1:
            car = Car()
            self.cars.append(car)
        
    def delete_car(self,car):
        car.reset()
        car.hideturtle()
        self.cars.remove(car)
        
    def move(self):
        self.move_speed = STARTING_MOVE_DISTANCE + MOVE_INCREMENT*(self.level-1)
        for car in self.cars:
            car.forward(self.move_speed)
            if car.xcor() < -300:
                self.delete_car(car)
    
    def reset(self):
        for car in self.cars:
            car.hideturtle()
            self.cars.clear

    def level_up(self):
        self.reset()
        self.level += 1
    

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.up()
        self.shape("square")
        self.shapesize(stretch_len= 2, stretch_wid= 1)
        self.setheading(180)
        self.color(random.choice(COLORS))
        self.goto(300, random.randint(-260, 260))
        
    def crash_with(self,position):
        if (self.ycor() - position[1]) >= -10 and (self.ycor() - position[1]) <= 10:
            if (position[0] - self.xcor()) >= 0 and (position[0] - self.xcor()) < 40:
                return True
            else:
                return False
        elif (self.xcor() - position[0]) >= -10 and (self.xcor() - position[0]) <= 10:
            if (self.ycor() - position[1]) >= 0 and (self.ycor() - position[1]) < 30:
                return True
            else:
                return False

