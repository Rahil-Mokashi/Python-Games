from turtle import Turtle

class Paddle(Turtle):
    
    def __init__(self, position):
        super().__init__()
        self.make_paddle(position)
        
    def make_paddle(self, position):
        self.shape("square")
        self.color("white")
        self.penup()
        self.turtlesize(stretch_len=1, stretch_wid=5)
        self.goto(position)
        
    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
        
    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    #     self.segments = []
    #     self.make_paddle_1()
    #     self.make_paddle_2()
    
    # def make_paddle_1(self):
    #     for pos in positions_1:
    #         self.add_segments(pos)
            
    # def make_paddle_2(self):
    #     for pos in positions_2:
    #         self.add_segments(pos)
            
    # def add_segments(self, position):
    #     paddle = Turtle()
    #     paddle.shape("square")
    #     paddle.speed("fastest")
    #     paddle.penup()
    #     paddle.color("white")
    #     paddle.goto(position)
    #     self.segments.append(paddle)
        