import time
import random
from turtle import Screen, Turtle
import subprocess

from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


class App:
    def __init__(self, screen, player_img) -> None:
        self.scoreboard = Scoreboard()
        self.car_manager = CarManager()
        self.player = Player(player_img)
        self.screen = screen

        self.screen.listen()
        self.screen.onkeypress(self.player.move_forward, "w")
        self.screen.onkeypress(self.player.move_forward, "Up")
        self.screen.onkeypress(self.player.move_back, "s")
        self.screen.onkeypress(self.player.move_back, "Down")
        self.screen.onkeypress(self.player.move_left, "a")
        self.screen.onkeypress(self.player.move_left, "Left")
        self.screen.onkeypress(self.player.move_right, "d")
        self.screen.onkeypress(self.player.move_right, "Right")

        # toClose = 0
        self.screen.onkeypress(self.open_popup_window, "Escape")

        self.play_game()

    def open_popup_window(self):
        result = subprocess.run(["python", "menu.py"])
        print(result)
        if result.returncode == 1:
            self.screen.bye()

    def play_game(self):
        game_is_on = True
        while game_is_on:
            # Randomly spawn cars
            random_chance = random.randint(1, self.car_manager.create_car_chances)
            if random_chance == 1:
                self.car_manager.create_car()
            self.car_manager.move_cars()

            # Check if player finished the level
            if self.player.finish_line():
                self.scoreboard.increase_level()
                self.car_manager.increase_speed()
                if self.car_manager.create_car_chances > 2:
                    self.car_manager.create_car_chances -= 1

            # Detect player collision with car
            if self.player.detect_collision(self.car_manager.displayed_cars):
                game_is_on = False
                self.player.is_alive = False
                self.scoreboard.display_game_over()

            time.sleep(0.1)
            self.screen.update()
