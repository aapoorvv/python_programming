import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
score = Scoreboard()
screen.listen()
screen.onkey(player.move,key="Up")
loop = 1
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    loop+=1
    if loop%6==0:
        car.create_car()
    if (player.ycor() >= 280):
        score.add_score()
        player.gotostart()
        car.levelup()
    car.move()
    for c in car.cars:
        if (player.distance(c)<20):
            score.gameover()
            game_is_on = False
            



screen.exitonclick()