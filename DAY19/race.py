from turtle import *
from random import *

screen =  Screen()
screen.colormode(255)

is_race_on = False
screen.setup(width=1000, height=400)
user_bet = screen.textinput(title="Place your Bets",prompt="Enter the color")
print(user_bet)
all_turtles = []
colors = ["red", "dark orange", "gold", "green", "blue", "purple"]
for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.up()
    new_turtle.speed("fastest")
    new_turtle.fillcolor(colors[turtle_index])
    new_turtle.pencolor(colors[turtle_index])
    new_turtle.goto(-450,-125 + 50*turtle_index)
    all_turtles.append(new_turtle)

if (user_bet):
    is_race_on = True

while(is_race_on):
    for turtle in all_turtles:
        rand_distance = randint(0,11)
        turtle.forward(rand_distance)
        if (turtle.xcor()>=500):
            is_race_on = False
            winning_color = turtle.pencolor()
            if(user_bet==winning_color):
                print("You were right,",user_bet,"turtle won ;)")
            else:
                print("You were wrong,",user_bet,"turtle lost :(")

print(all_turtles)
screen.exitonclick()