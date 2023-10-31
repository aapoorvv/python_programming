from turtle import Turtle

class Paddle(Turtle):
    
    def __init__(self,position) -> None:
        super().__init__()
        self.shape("square")
        self.speed("fastest")
        self.penup()
        self.goto(position)
        self.shapesize(5,1)
        self.color("white")
        
    def go_up(self):
        self.goto(self.xcor(),self.ycor() + 20)
    def go_down(self):        
        self.goto(self.xcor(),self.ycor() - 20)
        
        
        