from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10



class CarManager:
    
    def __init__(self) -> None:
        super().__init__()
        self.cars = []
        self.move()
        self.car_speed = 1
    
    def create_car(self):
        new_car = Turtle(shape="square")
        new_car.shapesize(1,2)
        new_car.penup()
        new_car.speed(self.car_speed)
        new_car.goto(300,random.randrange(-10,12)*20)
        new_car.color(random.choice(COLORS))
        new_car.setheading(180)
        self.cars.append(new_car)
    
    def move(self):
        for car in self.cars:
            car.forward(STARTING_MOVE_DISTANCE)
    
    def levelup(self):
        self.car_speed += MOVE_INCREMENT