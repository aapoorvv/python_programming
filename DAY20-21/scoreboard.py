from turtle import Turtle

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("DAY20-21/high_score.txt") as high_score:
            self.highscore = int(high_score.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.speed("fastest")
        self.goto(0,280)
        self.write(f"Score = {self.score}  High Score = {self.highscore}", align="center", font=('courier', 20, 'normal'))
    
    def update_scoreboard(self): 
        self.clear()
        self.write(f"Score = {self.score}  High Score = {self.highscore}", align="center", font=('courier', 20, 'normal'))
        
    def add_score(self):
        self.score = self.score + 1
        self.update_scoreboard()
    
    # def gameover(self):
    #     self.goto(0,0)
    #     self.write("Game Over.", align="center", font=('courier', 20, 'normal'))
    
    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        with open("DAY20-21/high_score.txt", mode='w') as high_score:
            high_score.write(f"{self.highscore}")
        self.score = 0
        self.update_scoreboard()
        
        