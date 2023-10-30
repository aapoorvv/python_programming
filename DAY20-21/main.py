from turtle import Screen,Turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen =  Screen()
screen.setup(600,600)
screen.bgcolor("Black")
screen.title("Snake Game")

snake = Snake()
food = Food()    
score = Scoreboard()
is_game_on = True

screen.listen()
screen.onkey(snake.up,key="Up")
screen.onkey(snake.down,key="Down")
screen.onkey(snake.left,key="Left")
screen.onkey(snake.right,key="Right")

while(is_game_on):
    screen.update() 
    time.sleep(0.04)
    snake.move()
    if (snake.segments[0].distance(food)<15):
        food.refresh()
        snake.extend()
        score.add_score()
        
    if (snake.segments[0].xcor()<-280 or snake.segments[0].xcor()>280 or snake.segments[0].ycor()< -280 or snake.segments[0].ycor()>260):   
        score.reset()
        snake.reset()
        
    
    for segment in snake.segments[1::]: #slicing head of snake
        if snake.segments[0].distance(segment)<10:
            score.reset()
            snake.reset()
             
    
screen.exitonclick()