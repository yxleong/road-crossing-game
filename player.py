from turtle import Turtle, register_shape

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(
        self, shape: str = "turtle", undobuffersize: int = 1000, visible: bool = True
    ) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.penup()
        self.color("lime")
        self.setheading(90)
        self.goto(STARTING_POSITION)
        self.is_alive = True

    def move_forward(self):
        if self.is_alive:
            self.forward(MOVE_DISTANCE)

    def move_back(self):
        if self.is_alive and self.ycor() > -280:
            self.back(MOVE_DISTANCE)

    def move_left(self):
        if self.is_alive and self.xcor() > -280:
            self.goto(self.xcor() - MOVE_DISTANCE, self.ycor())

    def move_right(self):
        if self.is_alive and self.xcor() < 280:
            self.goto(self.xcor() + MOVE_DISTANCE, self.ycor())

    def finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            self.goto(STARTING_POSITION)
            return True
        return False

    def detect_collision(self, car_list):
        for car in car_list:
            if (
                self.ycor() >= car.ycor() - 25
                and self.ycor() <= car.ycor() + 25
                and self.distance(car.pos()) <= 45
            ):
                self.is_alive = False
                return True
        return False
