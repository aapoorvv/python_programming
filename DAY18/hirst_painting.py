import colorgram
from turtle import Turtle
from turtle import Screen
from random import *

screen =  Screen()
screen.colormode(255)

tim = Turtle()
tim.hideturtle()
tim.fillcolor("yellow")
colors = colorgram.extract('DAY18/image1.jpg', 30)
tim.speed('fastest')
rgb=[]
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r,g,b)
    rgb.append(new_color)

tim.pu() 
tim.setposition(-250,-200)
tim.width(9)      
for x in range(0,10):
    for y in range(0,10):
        tim.pencolor(choice(rgb))
        tim.dot()
        tim.forward(50)
        
    tim.backward(50)
    tim.setheading(90)
    tim.forward(50)
    if x%2==1:
        tim.setheading(360)
    else:
        tim.setheading(180)
    

screen.exitonclick()