from turtle import Turtle, Screen 
positions = [(0,0), (-20,0), (-40,0)]
up = 90
down = 270
left = 180
right = 0

class Snake:
    
    def __init__(self):
        self.segments = []
        self.make_snake()
        self.head = self.segments[0]
        
    def make_snake(self):
        for pos in positions:
            self.add_segments(pos)
            
    def add_segments(self, position):
        snake = Turtle("square")
        snake.penup()
        snake.color("white")
        snake.goto(*position)
        self.segments.append(snake)
        
            
    def extend(self):
        self.add_segments(self.segments[-1].position())
        
    def move_snake(self):
        for seg in range(len(self.segments) -1, 0, -1):
            new_x = self.segments[seg-1].xcor()
            new_y = self.segments[seg-1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.segments[0].forward(20)
        
    def down(self):
        if self.head.heading() != up:
            self.head.setheading(down)
    
    def up(self):
        if self.head.heading() != down:
            self.head.setheading(up)
    
    def left(self):
        if self.head.heading() != right:
            self.head.setheading(left)
            
    def right(self):
        if self.head.heading() != left:
            self.head.setheading(right)
     
            