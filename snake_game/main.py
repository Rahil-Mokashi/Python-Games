from turtle import Turtle, Screen 
from snake import Snake
from food import Food
from score import Score
import time 

screen = Screen()
screen.bgcolor("black")
screen.title("My Snake Game")
screen.setup(width=700, height=700)
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()



screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True 
while game_is_on:
    screen.update()
    time.sleep(0.1)
    
    snake.move_snake()
     
    # Detect collision with the food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()
        
    
    # Detect collision with wall  
    if snake.head.xcor() > 345 or snake.head.xcor() < -345 or snake.head.ycor() > 345 or snake.head.ycor() < -345:
        score.reset()
        snake.reset()
    
    # Detect collision with tail
    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 10:
            score.reset()
            snake.reset()
    

screen.exitonclick()