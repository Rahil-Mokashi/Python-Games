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
car = CarGenerator()

screen.listen()
screen.onkey(player.player_move, "Up")

game_is_on = True 
while game_is_on:
    score.level_board()
    time.sleep(0.1)
    screen.update()
    
    car.create_car()
    car.car_move()
        
    for i in car.all_cars:
        if player.distance(i) < 30:
            score.game_over()
            game_is_on = False
            
    if player.ycor() > 290:
        player.start()
        score.level += 1
        score.level_board()
        car.carspeed += 1
        
    if score.level == 10:
        score.champion()
        game_is_on = False
        
screen.exitonclick()