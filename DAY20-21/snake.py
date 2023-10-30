from turtle import Turtle
MOVE_DISTANCE=20
position = [(0,0),(-20,0),(-40,0)]

class Snake:
    
    def __init__(self) -> None:
        self.segments=[]
        self.create_snake()
        self.move()
        
    def create_snake(self):
        for x in position:
            self.add_segment(x)        
            
    def add_segment(self,position):
        new_segment = Turtle(shape="square")
        new_segment.penup()
        new_segment.speed("fastest")
        new_segment.goto(position)
        new_segment.color("white")
        self.segments.append(new_segment)
        
    def move(self):
        for seg_num in range(len(self.segments)-1,0,-1):
            new_x =self.segments[seg_num-1].xcor()
            new_y =self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
        self.segments[0].forward(MOVE_DISTANCE)
        
    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)
    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)
    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)
    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)
            
    def extend(self):
        self.add_segment(self.segments[-1].pos())
        
    def reset(self):
        for seg in self.segments:
            seg.hideturtle()
        self.segments.clear()
        self.create_snake()
        self.move()
                    
    
        