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
        self.move_speed = STARTING_MOVE_DISTANCE

        
    def new_car(self):
        if random.randint(1,7) == 1:
        # That proud feeling when you use your logic and it matches the solution
        # I had a nester randomizer but for the sake of performance, I'll just
        # make it single, less computation, more monotonocity
            car = Car()
            self.cars.append(car)
        # As expected, the video just used a Turtle object rather than making
        # a whole new class, but at this this way it looks cooler
        
    def delete_car(self,car):
        car.reset()
        car.hideturtle()
        self.cars.remove(car)
        
    def move(self):
        for car in self.cars:
            car.backward(self.move_speed)
            if car.xcor() < -300:
                self.delete_car(car)
    
    def reset(self):
        for car in self.cars:
            car.hideturtle()
            self.cars.clear

    def level_up(self):
        self.reset()
        self.level += 1
        self.move_speed += MOVE_INCREMENT

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.up()
        self.shape("square")
        self.shapesize(stretch_len= 2, stretch_wid= 1)
        # I had set the heading to 180, but figured moving backwards was cleaner
        self.color(random.choice(COLORS))
        self.goto(300, random.randint(-260, 260))
        
    # I had a collision detection method but it was overly complicated and still
    # did not get the job done so I used the method given in the course