from turtle import *

screen =  Screen()
screen.colormode(255)

tim = Turtle()

def move_forward():
    tim.forward(20)
def move_backward():
    tim.forward(-20)
def move_left():
    tim.left(10)
def move_right():
    tim.right(10)
    
def cclear():
    tim.clear()
    tim.up()
    tim.home()
    tim.down()
    

screen.listen()
screen.onkeypress(move_forward,key="w")
screen.onkeypress(move_backward,key="s")
screen.onkeypress(move_left,key="a")
screen.onkeypress(move_right,key="d")
screen.onkeypress(cclear,key=" ")

screen.exitonclick()