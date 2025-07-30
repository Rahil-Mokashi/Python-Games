from turtle import Turtle

FONT = ('Courier', 24, 'normal')


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.level = 1
        
    def level_board(self):
        self.write(f"LEVEL: {self.level}", )        
        
    def game_over(self):
        self.write("GAME OVER!", align="center", font=("Courier", 50, 'normal'))