from turtle import Turtle 

class Score(Turtle):
    
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        with open("data.txt", mode='r') as previous_highscore:
            the_score = int(previous_highscore.read())
            self.highscore = the_score
        self.score = 0
        self.goto(0, 320)
        self.update_score()
        
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.highscore}", align="center", font=('Arial', 16, 'normal'))
        
    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        with open("data.txt", mode='w') as new_highscore:
            new_highscore.write(str(self.highscore))
        self.score = 0
        self.update_score()
        
        
    def increase_score(self):
        self.score = self.score + 1
        self.update_score()