from turtle import Turtle

class Ball(Turtle):
    
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.speed("fastest")
        self.penup()
        self.color("white")
        self.move_delay = 0.01
        self.x = 5
        self.y = 5
    
    def move(self):
        new_x = self.xcor() + self.x
        new_y = self.ycor() + self.y
        self.goto(new_x,new_y)
    
    def bounce(self):
        self.y *= -1
    
    def hit(self):
        self.x *= -1
        self.move_delay *= 0.7
        
    def reset_pos(self):
        self.goto(0,0)
        self.x *= -1
        self.move_delay = 0.01
        