from turtle import Turtle, register_shape
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
CREATE_CAR_CHANCES = 6
CAR_COUNT = 70
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5
STARTING_POSITION_X = 700
BOTTOM_POSITION_Y = -350
TOP_POSITION_Y = 350

# car size: 70 x 31 pixels
CAR_RED = "assets/car_red_small.gif"
CAR_GREEN = "assets/car_green_small.gif"
CAR_BLUE = "assets/car_blue_small.gif"
CAR_SHAPES = [CAR_RED, CAR_GREEN, CAR_BLUE]


class CarManager:
    def __init__(self) -> None:
        for shape in CAR_SHAPES:
            register_shape(shape)
        self.car_speed = STARTING_MOVE_DISTANCE
        self.create_car_chances = CREATE_CAR_CHANCES
        self.displayed_cars = []
        self.unused_cars = []
        self.initialize_all_cars()

    def initialize_all_cars(self):
        for _ in range(CAR_COUNT):
            new_car = Turtle(random.choice(CAR_SHAPES))
            new_car.penup()
            new_car.setheading(180)
            new_car.hideturtle()
            self.unused_cars.append(new_car)

    def create_car(self):
        if self.unused_cars:
            new_car = self.unused_cars.pop()
            new_car.showturtle()
            random_y = BOTTOM_POSITION_Y + (random.randint(1, 18) * 40)
            new_car.goto(STARTING_POSITION_X, random_y)
            self.displayed_cars.append(new_car)

    def move_cars(self):
        for car in self.displayed_cars:
            car.forward(self.car_speed)
            if car.xcor() <= -STARTING_POSITION_X:
                car.hideturtle()
                self.unused_cars.append(car)
                self.displayed_cars.remove(car)

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT
