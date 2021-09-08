from turtle import Turtle, Screen
import time
from player import Player
from car_manager import Car_Manager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


is_game_on = True
gamer = Player()
cars = Car_Manager()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(gamer.upward, "Up")

while is_game_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.move_car()

    for car in cars.all_cars:
        if car.distance(gamer) < 20:
            is_game_on = False
            scoreboard.game_over()

    if gamer.is_on_finish_line():
        gamer.goto_start()
        cars.level_up()
        scoreboard.update_score()

screen.exitonclick()