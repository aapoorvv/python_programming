from turtle import Turtle
from turtle import Screen
from random import *

tim = Turtle()
tim.shape("arrow")
tim.fillcolor("green")
colors = ["blue", "green", "yellow", "red", "pink", "brown", "cyan", "black", "purple", "maroon"]
direction = [0,90,180,270]
# tim.forward(100)
# tim.left(90)
# tim.forward(100)
# tim.left(90)
# tim.forward(100)
# tim.left(90)
# tim.forward(100) 

tim.speed("fastest")
tim.pensize(2)
# for x in range(30):
#     tim.forward(5)
#     tim.penup()
#     tim.forward(5)
#     tim.pendown()

#polygon
# def draw(n):
#     tim.pencolor(colors[n-3])
#     for x in range(0,n):
#         tim.forward(50)
#         tim.left(360/n)
# for b in range(3,10):
#     draw(b)
screen =  Screen()
screen.colormode(255)


def random_color():
    r=randint(0,255)
    g=randint(0,255)
    b=randint(0,255)
    randx = (r,g,b)
    return randx
# tim.pensize(10)
# n=200
# for x in range(0,n):
#     tim.pencolor(random_color())
#     tim.forward(10)
#     tim.setheading(choice(direction))
p=10
tim.pensize(2)    
for x in range(0,360//p):
    tim.pencolor(random_color())
    tim.circle(100)
    current_heading = tim.heading()
    tim.setheading(current_heading + p)
    
screen.exitonclick()    
