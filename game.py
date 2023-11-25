import time
import random
from turtle import Screen, Turtle
from tkinter import *

from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from background import Background, RIVERS_COOR

SCREEN_WIDTH = 1352
SCREEN_HEIGHT = 896


class Game(Frame):
    def __init__(self, parent, controller) -> None:
        Frame.__init__(self, parent)
        self.controller = controller

    def init_game_tools(self):
        screen = Screen()
        screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
        screen.tracer(0)
        screen.title("Turtle Road Crossing Game 🐢")

        background = Background()
        scoreboard = Scoreboard()
        car_manager = CarManager()
        player = Player()

        screen.listen()
        screen.onkeypress(player.move_forward, "w")
        screen.onkeypress(player.move_forward, "Up")
        screen.onkeypress(player.move_back, "s")
        screen.onkeypress(player.move_back, "Down")
        screen.onkeypress(player.move_left, "a")
        screen.onkeypress(player.move_left, "Left")
        screen.onkeypress(player.move_right, "d")
        screen.onkeypress(player.move_right, "Right")

        # self.play_game()
        return {
            "screen": screen,
            "scoreboard": scoreboard,
            "car_manager": car_manager,
            "player": player,
        }

    def play_game(self):
        tools = self.init_game_tools()
        screen = tools["screen"]
        scoreboard = tools["scoreboard"]
        car_manager = tools["car_manager"]
        player = tools["player"]

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
            if player.detect_collision(
                car_manager.displayed_cars
            ) or player.detect_drowning(RIVERS_COOR):
                game_is_on = False
                player.is_alive = False
                scoreboard.display_game_over()
                time.sleep(2)

            time.sleep(0.1)
            screen.update()

        # screen.bye()
        # self.controller.delete_game_frame()
        self.controller.show_frame("PauseMenu")
