from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0 
        self.color("black")
        self.penup()
        self.hideturtle()
        self.speed("fastest")
        self.goto(0,270)
        self.write(f"Level - {self.score}", align="center", font=('courier', 20, 'normal'))
        
    def update_scoreboard(self): 
        self.write(f"Level - {self.score}", align="center", font=('courier', 20, 'normal'))
        
    def add_score(self):
        self.score = self.score + 1
        self.clear()
        self.update_scoreboard()
    
    def gameover(self):
        self.goto(0,0)
        self.write("Game Over.", align="center", font=('courier', 20, 'normal'))
        