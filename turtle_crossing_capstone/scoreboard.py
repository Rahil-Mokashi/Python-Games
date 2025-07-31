from turtle import Turtle

FONT = ('Courier', 20, 'normal')

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.level = 1
             
    def game_over(self):
        gameover = Turtle()
        gameover.penup()
        gameover.hideturtle()
        gameover.color("white")
        gameover.write("GAME OVER!", align = "center", font = ("Courier", 50, "normal")) 
           
    def level_board(self):
        self.clear()
        self.goto((-260, 240))
        self.write(f"LEVEL: {self.level}", font = FONT)     
        
    def champion(self):
        champ = Turtle()
        champ.penup()
        champ.color("white")
        champ.hideturtle()
        champ.write("REACHED LEVEL 10: YOU ARE CHAMPION", align="center", font=("Courier", 20, "normal"))   
        
    