from turtle import Turtle, register_shape
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5
CREATE_CAR_CHANCES = 6

# car size: 70 x 31 pixels
CAR_RED = "assets/car_red_small.gif"
CAR_GREEN = "assets/car_green_small.gif"
CAR_BLUE = "assets/car_blue_small.gif"
car_shapes = [CAR_RED, CAR_GREEN, CAR_BLUE]


class CarManager:
    def __init__(self) -> None:
        for shape in car_shapes:
            register_shape(shape)
        self.car_speed = STARTING_MOVE_DISTANCE
        self.create_car_chances = CREATE_CAR_CHANCES
        self.should_move = True
        self.displayed_cars = []
        self.unused_cars = []
        self.initialize_all_cars()

    def initialize_all_cars(self):
        for i in range(50):
            new_car = Turtle(random.choice(car_shapes))
            new_car.penup()
            new_car.setheading(180)
            new_car.hideturtle()
            self.unused_cars.append(new_car)

    def create_car(self):
        if self.unused_cars:
            new_car = self.unused_cars.pop()
            new_car.showturtle()
            random_y = -250 + (random.randint(1, 16) * 31)
            new_car.goto(330, random_y)
            self.displayed_cars.append(new_car)

    def move_cars(self):
        if not self.should_move:
            return
        for car in self.displayed_cars:
            car.forward(self.car_speed)
            if car.xcor() <= -330:
                car.hideturtle()
                self.unused_cars.append(car)
                self.displayed_cars.remove(car)

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT
