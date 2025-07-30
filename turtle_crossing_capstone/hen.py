from turtle import Turtle 

class Hen(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("white")
        self.penup()
        self.goto(x=0, y=-280)
        self.setheading(90)

    def turtle_move(self):
        self.forward(10)