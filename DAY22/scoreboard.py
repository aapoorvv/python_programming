from turtle import Turtle

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.lscore = 0 
        self.rscore =0        
        self.color("white")
        self.penup()
        self.hideturtle()
        self.speed("fastest")
        self.goto(0,280)
        self.write(f"Score: {self.lscore}-{self.rscore}", align="center", font=('courier', 20, 'normal'))
        
    def add_lscore(self):
        self.lscore = self.lscore + 1
        self.clear()
        self.update_scoreboard()
    
    def add_rscore(self):
        self.rscore = self.rscore + 1
        self.clear()
        self.update_scoreboard()
    
    def update_scoreboard(self): 
        self.write(f"Score: {self.lscore}-{self.rscore}", align="center", font=('courier', 20, 'normal'))
    
    def gameover(self):
        self.goto(0,0)
        self.write("Game Over.", align="center", font=('courier', 20, 'normal'))