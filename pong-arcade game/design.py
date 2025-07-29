from turtle import Turtle 

class Design(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 300)  
        self.setheading(270)  

    def draw_line(self):
        for _ in range(15): 
            self.pendown()
            self.forward(20) 
            self.penup()
            self.forward(20)
            