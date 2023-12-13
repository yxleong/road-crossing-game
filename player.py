"""
Program : player.py
Author : Group 10
            林佩佩 B10915067
            羅翡瑩 B11015010
            盧清珍 B11015012
            梁婭瑄 B11015016
Analysis:
1. Represents the player character in the game, handles movement and collisions.

Design - pseudocode:
1. Import required modules
    Turtle
    register_shape
2. Define the significant constant
    STARTING_POSITION, MOVE_DISTANCE, FINISH_LINE_Y: Player starting position, movement distance, and finish line position
    POSITION_LIMIT_X, POSITION_LIMIT_Y: Player movement limits
    PLAYER_IMG: Path to the image representing the player
3. Define the Player class
    Initialize Player as a Turtle with the player image
        Register the player image
        Lift the pen to avoid drawing while moving
        Set the player's color to lime
        Set the player's orientation to face upward
        Place the player at the starting position
        Initialize the is_alive flag as True
    Define a method to move the player forward
        If the player is alive
            Move the player forward by the move distance
    Define a method to move the player backward, with boundary checking
        If the player is alive and the player's y-coordinate is above the lower limit
            Move the player backward by the move distance
    Define a method to move the player to the left, with boundary checking
        If the player is alive and the player's x-coordinate is above the left limit
            Move the player to the left by the move distance
    Define a method to move the player to the right, with boundary checking
        If the player is alive and the player's x-coordinate is below the right limit
            Move the player to the right by the move distance
    Define a method to check if the player has reached the finish line
        If the player's y-coordinate is above the finish line
            Move the player to the starting position
            Return True indicating that the player crossed the finish line
        Return False indicating that the player has not crossed the finish line
    Define a method to check for collision with cars
        For each car in the list of cars
            If the player's y-coordinate is within a range around the car's y-coordinate
                and the distance between the player and the car is within a threshold
                Set the player as not alive
                Return True indicating a collision
        Return False indicating no collision
    Define a method to check for drowning in rivers
        For each river segment in the list of rivers
            If the player's position is within the boundaries of the river segment
                Set the player as not alive
                Return True indicating drowning
        Return False indicating no drowning
"""

from turtle import Turtle, register_shape

# Initial position, movement distance, and finish line position for the player
STARTING_POSITION = (0, -410)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 410

# Position limits for the player's movement
POSITION_LIMIT_X = 640
POSITION_LIMIT_Y = 410

# Path to the image representing the player
PLAYER_IMG = "assets/Bear.gif"

# Class representing the player character in the game
class Player(Turtle):
    def __init__(self) -> None:
        # Register the player image as a custom shape
        register_shape(PLAYER_IMG)

        # Initialize the Player as a Turtle with the player image
        super().__init__(PLAYER_IMG)

        # Set up initial attributes for the player
        self.penup()  # Lift the pen to avoid drawing while moving
        self.color("lime")  # Set the player's color to lime
        self.setheading(90)  # Set the player's orientation to face upward
        self.goto(STARTING_POSITION)  # Place the player at the starting position
        self.is_alive = True  # Flag to track player's life status

    # Method to move the player forward
    def move_forward(self):
        if self.is_alive:
            self.forward(MOVE_DISTANCE)

    # Method to move the player backward, with boundary checking
    def move_back(self):
        if self.is_alive and self.ycor() > -POSITION_LIMIT_Y:
            self.back(MOVE_DISTANCE)

    # Method to move the player to the left, with boundary checking
    def move_left(self):
        if self.is_alive and self.xcor() > -POSITION_LIMIT_X:
            self.goto(self.xcor() - MOVE_DISTANCE, self.ycor())

    # Method to move the player to the right, with boundary checking
    def move_right(self):
        if self.is_alive and self.xcor() < POSITION_LIMIT_X:
            self.goto(self.xcor() + MOVE_DISTANCE, self.ycor())

    # Method to check if the player has reached the finish line
    def finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            # If the player crossed the finish line, reset to starting position
            self.goto(STARTING_POSITION)
            return True
        return False

    # Method to check for collision with cars
    def detect_collision(self, car_list):
        for car in car_list:
            if (
                # Check if the player's y-coordinate is within a range around the car's y-coordinate
                self.ycor() >= car.ycor() - 25  # Check if player is above or at the same level as the top edge of the car
                and self.ycor() <= car.ycor() + 25  # Check if player is below or at the same level as the bottom edge of the car

                # Check if the distance between the player and the car is less than or equal to a threshold
                and self.distance(car.pos()) <= 42  # Check if the Euclidean distance between the player and the car is within a specified range
            ):
                # If a collision is detected, set player as not alive
                self.is_alive = False
                return True
        return False

    # Method to check for drowning in rivers
    def detect_drowning(self, river_list):
        for river in river_list:
            if (
                self.ycor() - 20 <= river["top"]
                and self.ycor() - 10 >= river["bottom"]
                and self.xcor() + 10 >= river["left"]
                and self.xcor() - 10 <= river["right"]
            ):
                # If the player is in the river, set player as not alive
                self.is_alive = False
                return True
        return False

# End of the Player class
