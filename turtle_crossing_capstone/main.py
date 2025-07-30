from turtle import Turtle, Screen 
from player import Player
from cars import CarGenerator
from scoreboard import Scoreboard
import random
import time


screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Turtle Crossing")
screen.tracer(0)

player = Player()
score = Scoreboard()




screen.listen()
screen.onkey(player.player_move, "Up")



cars = [] 

game_is_on = True 
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    if random.randint(1, 10) == 1:
        car = CarGenerator()
        cars.append(car)
        
    for car in cars:
        car.car_move()
        
        if player.distance(car) < 20:
            score.game_over()
            game_is_on = False
        



















screen.exitonclick()