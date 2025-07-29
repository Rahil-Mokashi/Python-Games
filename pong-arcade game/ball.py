from turtle import Turtle 
import time

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.dx = 10
        self.dy = 10
        self.ball_speed = 0.1
        
    def ball_move(self):
        new_x = self.xcor() + self.dx
        new_y = self.ycor() + self.dy
        self.goto(new_x, new_y)
        
    def bounce_y(self):
        self.dy *= -1
        
    def bounce_x(self):
        self.dx *= -1
        self.ball_speed *= 0.9
        
    def reset(self):
        self.goto(0, 0)
        self.ball_speed = 0.1
        time.sleep(1)
        self.bounce_x()