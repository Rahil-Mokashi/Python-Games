from turtle import Turtle, Screen 
from hen import Hen


screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Turtle Crossing")
screen.tracer(0)

hen = Hen()



screen.listen()
screen.onkey(hen.turtle_move, "Up")





game_is_on = True 
while game_is_on:
    screen.update()



















screen.exitonclick()