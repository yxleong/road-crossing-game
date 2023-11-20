import time
import random
from turtle import Screen, Turtle, TurtleScreen
from tkinter import *

from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

BACKGROUND_IMG = "assets/road2_600.gif"
PLAYER_IMG = "assets/Bear.gif"


class Game(Frame):
    def __init__(self, parent, controller) -> None:
        Frame.__init__(self, parent)
        self.controller = controller

    def init_game(self):
        screen = Screen()
        screen.setup(width=600, height=600)
        screen.tracer(0)
        screen.title("Turtle Road Crossing Game 🐢")

        screen.register_shape(BACKGROUND_IMG)
        screen.register_shape(PLAYER_IMG)
        background = Turtle(BACKGROUND_IMG)

        scoreboard = Scoreboard()
        car_manager = CarManager()
        player = Player(PLAYER_IMG)

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
        tools = self.init_game()
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
            if player.detect_collision(car_manager.displayed_cars):
                game_is_on = False
                player.is_alive = False
                scoreboard.display_game_over()

            time.sleep(0.1)
            screen.update()

        # screen.bye()
        # self.controller.delete_game_frame()
        self.controller.show_frame("PauseMenu")
