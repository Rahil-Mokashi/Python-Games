from turtle import Turtle 

class Score(Turtle):
    
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.score = 0
        self.goto(0, 320)
        self.update_score()
        
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=('Arial', 16, 'normal'))
        
    def gameover(self):
        self.goto(0,0)
        self.write("Game Over", align="center", font=('Arial', 18, 'normal'))
        
    def increase_score(self):
        self.score = self.score + 1
        self.update_score()