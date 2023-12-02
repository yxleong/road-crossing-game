import time
import random
import pygame
from turtle import Screen, Turtle
from tkinter import *

from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from background import Background, RIVERS_COOR

SCREEN_WIDTH = 1352
SCREEN_HEIGHT = 896
BGM_PATH = "assets/cute_song.mp3"
COLLISION_PATH = "assets/Collision.mp3"
GAMEOVER_PATH = "assets/Game_Over.mp3"

class Game(Frame):
    def __init__(self, parent, controller) -> None:
        Frame.__init__(self, parent)
        self.controller = controller

        self.screen = Screen()
        self.screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
        self.screen.tracer(0)
        self.screen.title("Road Crossing Game 🚗")

    def init_game_tools(self):
        background = Background()
        scoreboard = Scoreboard()
        car_manager = CarManager()
        player = Player()

        self.screen.listen()
        self.screen.onkeypress(player.move_forward, "w")
        self.screen.onkeypress(player.move_forward, "Up")
        self.screen.onkeypress(player.move_back, "s")
        self.screen.onkeypress(player.move_back, "Down")
        self.screen.onkeypress(player.move_left, "a")
        self.screen.onkeypress(player.move_left, "Left")
        self.screen.onkeypress(player.move_right, "d")
        self.screen.onkeypress(player.move_right, "Right")

        return {
            "scoreboard": scoreboard,
            "car_manager": car_manager,
            "player": player,
        }

    def play_game(self):
        self.screen.update()
        tools = self.init_game_tools()
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
                pygame.mixer.init()
                pygame.mixer.music.load(COLLISION_PATH)
                pygame.mixer.music.play()
                player.is_alive = False
                game_is_on = False
                scoreboard.display_game_over()
                self.screen.update()
                time.sleep(2)

            time.sleep(0.1)
            self.screen.update()

        pygame.mixer.init()
        pygame.mixer.music.load(GAMEOVER_PATH)
        pygame.mixer.music.play()
        player.hideturtle()
        self.controller.current_score = scoreboard.get_score()
        self.controller.show_frame("ScoreMenu")

    def delete_game(self):
        self.screen.bye()
