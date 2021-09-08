from turtle import Turtle
import random

COLOUR = ["red", "orange", "blue", "yellow", "pink", "purple"]


class Car_Manager():
    def __init__(self):
        self.all_cars =[]
        self.car_speed = 10

    def create_car(self):
        choice = random.randint(1, 6)
        if choice == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.penup()
            new_car.color(random.choice(COLOUR))
            new_car.goto(300, random.randint(-220, 220))
            self.all_cars.append(new_car)

    def move_car(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += 5
