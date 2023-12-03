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
