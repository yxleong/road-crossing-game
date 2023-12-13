"""
Program : background.py
Author : GROUP 10
            林佩佩 B10915067
            羅翡瑩 B11015010
            盧清珍 B11015012
            梁婭瑄 B11015016
Analysis:
1. Manages the game's background visuals, including allowed and not allowed areas

Design - pseudocode:
1. Import required modules
      Turtle
      register_shape
2. Define the significant constant
   BACKGROUND_SHAPE, RIVERS_SHAPE: File paths for background shapes
   RIVERS_COOR: Coordinates for each river segment
3. Define the Background class
      Initialize Background
            Register the allowed combination shape
            Register the not allowed combination shape
      Create a Turtle for the background using the allowed combination shape
      Create a Turtle for the rivers using the not allowed combination shape
      Set up the rivers Turtle
            Lift the pen to avoid drawing when moving
            Move the rivers Turtle to a specified location
"""

from turtle import Turtle, register_shape

# Define file paths for custom shape images
BACKGROUND_SHAPE = "assets/allowedCombination.gif"
RIVERS_SHAPE = "assets/notAllowedCombination.gif"

# Define coordinates for each river segment
RIVER_1_COOR = {"left": -676, "right": -583, "top": 17, "bottom": -133}
RIVER_2_COOR = {"left": -480, "right": -262, "top": 17, "bottom": -133}
RIVER_3_COOR = {"left": -159, "right": 108, "top": 17, "bottom": -133}
RIVER_4_COOR = {"left": 211, "right": 435, "top": 17, "bottom": -133}
RIVER_5_COOR = {"left": 538, "right": 676, "top": 17, "bottom": -133}
RIVERS_COOR = [RIVER_1_COOR, RIVER_2_COOR, RIVER_3_COOR, RIVER_4_COOR, RIVER_5_COOR]

# Class representing the background of the game
class Background:
    def __init__(self) -> None:
        # Register custom shapes with Turtle graphics
        register_shape(BACKGROUND_SHAPE)
        register_shape(RIVERS_SHAPE)

        # Create a Turtle for the background using the allowed combination shape
        self.background = Turtle(BACKGROUND_SHAPE)

        # Create a Turtle for the rivers using the not allowed combination shape
        self.rivers = Turtle(RIVERS_SHAPE)

        # Set up the rivers Turtle
        self.rivers.penup()
        self.rivers.goto(-2, -58)

# End of the Background class
