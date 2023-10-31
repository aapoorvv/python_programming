from turtle import Screen,Turtle
import time
from paddles import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen =  Screen()
screen.setup(800,600)
screen.bgcolor("Black")
screen.title("Ping Pong")

r_paddle = Paddle((370,0))
l_paddle = Paddle((-380,0))
ball = Ball()
score = Scoreboard()
is_game_on = True

screen.listen()
screen.onkeypress(r_paddle.go_up,key="Up")
screen.onkeypress(l_paddle.go_up,key="w")
screen.onkeypress(r_paddle.go_down,key="Down")
screen.onkeypress(l_paddle.go_down,key="s")

while(is_game_on):
    time.sleep(ball.move_delay)
    screen.update() 
    ball.move()
    if (ball.ycor()< -280 or ball.ycor()>280):
        ball.bounce()
    if ((ball.xcor()== 360 or ball.xcor()== -370) and (ball.distance(r_paddle)<=60 or ball.distance(l_paddle)<=60)):
        ball.hit()
    if (ball.xcor()== 380):
        score.add_lscore()
    if(ball.xcor()== -390):
        score.add_rscore()   
    if ((ball.xcor()== 360 or ball.xcor()== -370)):
        screen.listen()
        screen.onkeypress(ball.reset_pos,key="space")
    if(score.lscore==5 or score.rscore==5):
        score.gameover()
        is_game_on = False
                   
screen.exitonclick()