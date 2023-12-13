"""
Program : game.py
Author : Group 10
            林佩佩 B10915067
            羅翡瑩 B11015010
            盧清珍 B11015012
            梁婭瑄 B11015016
Analysis:
1. This file manages the game logic, initializing the game environment, handling player movement, car management, collision detection, score updating, and game over scenarios.
Design - pseudocode:
1. Define the significant constant
   SCREEN_WIDTH = 1352.
   SCREEN_HEIGHT = 896.
2. The inputs are
   Key presses: 'w', 'Up', 's', 'Down', 'a', 'Left', 'd', 'Right' for player movement.
3. Computations:
   Initializing the game environment (setting up the screen, event listeners).
   Managing player and car movement.
   Spawning cars randomly on the road.
   Checking player's progress and increasing game difficulty.
   Detecting collisions between the player and cars or water.
   Handling game over scenarios.
   Updating the score.
4. The output is
   Game screen with player, cars, and obstacles.
   Increased difficulty level as player progresses.
   Score updates during gameplay.
   Game over message and transition to the score menu.
"""

import time
import random
from turtle import Screen
from tkinter import *

# Importing custom classes from other files
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from background import Background, RIVERS_COOR

# Constants defining the screen dimensions
SCREEN_WIDTH = 1352
SCREEN_HEIGHT = 896

# Class representing the game
class Game(Frame):
    def __init__(self, parent, controller) -> None:
        # Initializing the Frame
        Frame.__init__(self, parent)
        self.controller = controller

        # Creating a turtle graphics screen
        self.screen = Screen()
        self.screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
        
        # Turn off automatic screen updates
        self.screen.tracer(0)
        
        # Set the title of the game window
        self.screen.title("Road Crossing Game 🚗")

    # Method to initialize game tools and setup event listeners
    def init_game_tools(self):
        # Creating instances of custom classes
        background = Background()
        scoreboard = Scoreboard()
        car_manager = CarManager()
        player = Player()

        # Setting up event listeners for player movement
        self.screen.listen()
        self.screen.onkeypress(player.move_forward, "w")
        self.screen.onkeypress(player.move_forward, "Up")
        self.screen.onkeypress(player.move_back, "s")
        self.screen.onkeypress(player.move_back, "Down")
        self.screen.onkeypress(player.move_left, "a")
        self.screen.onkeypress(player.move_left, "Left")
        self.screen.onkeypress(player.move_right, "d")
        self.screen.onkeypress(player.move_right, "Right")

        # Returning a dictionary with the initialized tools
        return {
            "scoreboard": scoreboard,  # A reference to the initialized Scoreboard object
            "car_manager": car_manager,  # A reference to the initialized CarManager object
            "player": player,  # A reference to the initialized Player object
        }


    # Method to start and run the game
    def play_game(self):
        # Update the screen to apply initial settings
        self.screen.update()

        # Initialize game tools and retrieve instances
        tools = self.init_game_tools()
        scoreboard = tools["scoreboard"]
        car_manager = tools["car_manager"]
        player = tools["player"]

        game_is_on = True
        while game_is_on:
            # Randomly spawn cars
            random_chance = random.randint(1, car_manager.create_car_chances)
            
            # Check if the random chance allows for creating a new car
            if random_chance == 1:
                car_manager.create_car()  # Invoke the method to create a new car
            
            car_manager.move_cars()  # Move all existing cars on the road

            # Check if player finished the level
            if player.finish_line():
                scoreboard.increase_level()  # Increase the game level
                car_manager.increase_speed()  # Increase the speed of cars on the road
                if car_manager.create_car_chances > 2:
                    car_manager.create_car_chances -= 1  # Decrease the chance of creating new cars

            # Detect player collision with car or drowning
            if player.detect_collision(
                car_manager.displayed_cars
            ) or player.detect_drowning(RIVERS_COOR):
                self.controller.play_collision_music()  # Play collision sound
                player.is_alive = False  # Set player as not alive
                game_is_on = False  # End the game loop
                scoreboard.display_game_over()  # Display game over message
                self.screen.update()  # Update the screen
                time.sleep(2)  # Pause for 2 seconds

            # Pause for a short time and update the screen
            time.sleep(0.1)
            self.screen.update()

        # Hide the player turtle
        player.hideturtle()

        # Set the controller's current score and switch to the score menu
        self.controller.current_score = scoreboard.get_score()  # Get and store the current score
        self.controller.show_frame("ScoreMenu")  # Switch to the score menu

    # Method to close the game screen
    def delete_game(self):
        self.screen.bye()  # Close the game screen

# End of the Game class
