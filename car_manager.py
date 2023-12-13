"""
Program : car_manager.py
Author : Group 10
            林佩佩 B10915067
            羅翡瑩 B11015010
            盧清珍 B11015012
            梁婭瑄 B11015016
Analysis:
1. Manages the cars in the game, their creation, movement, and speed increment.

Design - pseudocode:
1. Import necessary modules
2. Define the significant constant
   COLORS: List of possible car colors.
   CREATE_CAR_CHANCES: Number of chances to create a new car.
   CAR_COUNT: Total number of cars in the game.
   STARTING_MOVE_DISTANCE: Initial distance a car moves.
   MOVE_INCREMENT: Distance increment when game level increases.  
   STARTING_POSITION_X: Initial X position for creating cars.
   BOTTOM_POSITION_Y, TOP_POSITION_Y: Y positions for creating cars.
   CAR_SHAPES: Paths to images representing different car colors.
3. Define the CarManager class
   Initialize car manager attributes
   Define method to initialize all the cars and add them to the unused car list
   Define method to create a new car and place it at a random position
   Define method to generate random offset to place a car
   Define method to move all displayed cars 
   Define method to increase the speed of cars
"""

from turtle import Turtle, register_shape
import random

# List of possible car colors
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

# Number of chances to create a new car in each iteration
CREATE_CAR_CHANCES = 6

# Total number of cars in the game
CAR_COUNT = 70

# Initial distance a car moves in each iteration
STARTING_MOVE_DISTANCE = 5

# Distance increment when the game level increases
MOVE_INCREMENT = 5

# Initial X position for creating cars
STARTING_POSITION_X = 700

# Y positions for creating cars within the game window
BOTTOM_POSITION_Y = -350
TOP_POSITION_Y = 350

# Paths to images representing different car colors
CAR_BLUE = "assets/car_blue.gif"
CAR_PURPLE = "assets/car_purple.gif"
CAR_YELLOW = "assets/car_yellow.gif"
CAR_SHAPES = [CAR_BLUE, CAR_PURPLE, CAR_YELLOW]
# car size: 60 x 35 px

# Class representing the car manager in the game
class CarManager:
    def __init__(self) -> None:
        # Register custom car shapes with Turtle graphics
        for shape in CAR_SHAPES:
            register_shape(shape)

        # Initialize car manager attributes
        self.car_speed = STARTING_MOVE_DISTANCE
        self.create_car_chances = CREATE_CAR_CHANCES
        self.displayed_cars = []  # List of currently displayed car Turtles
        self.unused_cars = []  # List of unused car Turtles
        self.initialize_all_cars()

    # Method to initialize all cars and add them to the unused cars list
    def initialize_all_cars(self):
        for _ in range(CAR_COUNT):
            # Create a new Turtle representing a car with a random shape
            new_car = Turtle(random.choice(CAR_SHAPES))
            
            # Set the car attributes
            new_car.penup()  # Lift the pen to avoid drawing while moving
            new_car.setheading(180)  # Set the initial orientation of the car to face left
            new_car.hideturtle()  # Hide the car initially
            
            # Add the new car to the list of unused cars
            self.unused_cars.append(new_car)

    # Method to create a new car and place it at a random Y position
    def create_car(self):
        # Check if there are unused cars available
        if self.unused_cars:
            # Pop a car from the list of unused cars
            new_car = self.unused_cars.pop()
            
            # Show the car on the screen
            new_car.showturtle()
            
            # Generate a random Y position for the car
            random_y = BOTTOM_POSITION_Y + self.generate_random_y_offset()
            
            # Place the car at the starting X position and the random Y position
            new_car.goto(STARTING_POSITION_X, random_y)

            # Add the new car to the list of displayed cars
            self.displayed_cars.append(new_car)

    # Method to generate a random Y offset for placing a car
    def generate_random_y_offset(self) -> int:
        offsets = [0, 40, 120, 160, 470, 510, 585, 625, 665, 705]
        offset = random.choice(offsets)
        return offset

    # Method to move all displayed cars to the left
    def move_cars(self):
        for car in self.displayed_cars:
            # Move the car forward based on its current speed
            car.forward(self.car_speed)

            # Check if the car is off the left side of the screen
            if car.xcor() <= -STARTING_POSITION_X:
                car.hideturtle()
                self.unused_cars.append(car)
                self.displayed_cars.remove(car)

    # Method to increase the speed of all cars
    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT

# End of the CarManager class
