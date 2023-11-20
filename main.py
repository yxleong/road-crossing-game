import time
import random
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import subprocess

BACKGROUND_IMG = "assets/road2_600.gif"

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtle Road Crossing Game 🐢")

screen.register_shape(BACKGROUND_IMG)
background = Turtle(BACKGROUND_IMG)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

def open_popup_window():
    result = subprocess.run(["python", "menu.py"])
    print(result)
    if result.returncode == 1:
        screen.bye()
    
screen.listen()
screen.onkeypress(player.move_forward, "w")
screen.onkeypress(player.move_back, "s")
screen.onkeypress(player.move_left, "a")
screen.onkeypress(player.move_right, "d")

#toClose = 0
screen.onkeypress(open_popup_window, "Escape")

game_is_on = True
while game_is_on:

    # Randomly spawn cars
    random_chance = random.randint(1, car_manager.create_car_chances)
    if random_chance == 1:
        car_manager.create_car()
    car_manager.move_cars()

    # Check if player finished the level
    if player.finish_line():
        scoreboard.increase_level()
        car_manager.increase_speed()
        if car_manager.create_car_chances > 2:
            car_manager.create_car_chances -= 1

    # Detect player collision with car
    if player.detect_collision(car_manager.displayed_cars):
        game_is_on = False
        player.is_alive = False
        scoreboard.display_game_over()

    time.sleep(0.1)
    screen.update()

screen.exitonclick()
