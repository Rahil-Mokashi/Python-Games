from turtle import Turtle
import random

COLORS = ['red', 'orange','yellow', 'green', 'blue', 'purple']
LANES = [-200, -150, -100, -50, 0, 50, 100, 150, 200]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarGenerator(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.carspeed = 5
        
    def create_car(self):
        if random.randint(1, 10) == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.choice(LANES)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)
           
    def car_move(self):
        for car in self.all_cars:
            car.backward(self.carspeed)
        
        if self.xcor() < -300:
            self.goto(300, random.choice(LANES))
            