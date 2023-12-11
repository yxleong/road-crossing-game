"""
Program : scoreboard.py
Author : Group 10
Analysis:
1. Manages and displays the game's scoreboard, including the level and game over message.

Design - pseudocode:
1. Define the significant constant
   FONT: Font configuration for the scoreboard display.
   SCOREBOARD_POSITION: Initial position for displaying the scoreboard.
2. The inputs are
   Level changes in the game.
3. Computations:
   Initialize the Scoreboard as a Turtle with specified attributes.
   Update and display the current level on the scoreboard.
   Increase the level and update the display when required.
   Display "GAME OVER" in the center of the screen upon game end.
4. The output is
   Display and management of the game's level and "GAME OVER" message.
"""

from turtle import Turtle

# Font configuration for the scoreboard display
FONT = ("Courier", 24, "bold")

# Initial position for displaying the scoreboard
SCOREBOARD_POSITION = (-650, 400)

# Class representing the scoreboard in the road-crossing game
class Scoreboard(Turtle):
    # Constructor for the Scoreboard class
    def __init__(self) -> None:
        # Initialize the Scoreboard as a Turtle with specified attributes
        super().__init__(visible=False)

        # Set up initial attributes for the scoreboard
        self.penup()  # Lift the pen to avoid drawing when moving
        self.color("white")  # Set the color of the scoreboard text to white
        self.level = 1  # Initial level of the player
        self.update_level()  # Display the initial level

    # Method to update and display the current level on the scoreboard
    def update_level(self):
        self.clear()  # Clear the previous display
        self.goto(SCOREBOARD_POSITION)  # Move to the scoreboard position
        self.write(
            arg=f"LEVEL: {self.level}", align="left", font=FONT
        )  # Write the current level

    # Method to increase the level and update the display
    def increase_level(self):
        self.level += 1
        self.update_level()

    # Method to display GAME OVER in the center of the screen
    def display_game_over(self):
        self.goto(0, 0)  # Move to the center of the screen
        self.write(arg="GAME OVER", align="center", font=FONT)  # Write GAME OVER

    # Method to get the current score
    def get_score(self):
        return self.level


# End of the Scoreboard class
