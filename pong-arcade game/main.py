from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Scoreboard
from design import Design
import time

screen = Screen()

screen.bgcolor("black")
screen.setup(width=1200, height=600)
screen.title("Pong - The Arcade Game")
screen.tracer(0)

design = Design()
score = Scoreboard()

paddle_1 = Paddle((560, 0))
paddle_2 = Paddle((-560, 0))
ball = Ball()

screen.listen()
screen.onkeypress(paddle_1.up, "Up")
screen.onkeypress(paddle_1.down, "Down")
screen.onkeypress(paddle_2.up, "w")
screen.onkeypress(paddle_2.down, "s")


game_is_on = True 
while game_is_on:
    design.draw_line()
    screen.update()
    
    time.sleep(ball.ball_speed)
    ball.ball_move()
    
     # Detect collision with wall
     
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
        
    # Detect collision with paddle
    if ball.distance(paddle_1) < 40 and ball.xcor() > 540 or ball.distance(paddle_2) < 40 and ball.xcor() < -540:
        ball.bounce_x() 
        
    # Detect if the ball exceeds the screen
    if ball.xcor() > 610:
        ball.reset()
        score.l_scoreboard()
        

    if ball.xcor() < -610:
        ball.reset()
        score.r_scoreboard()
          

screen.exitonclick()