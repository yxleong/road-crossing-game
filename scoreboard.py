from turtle import Turtle

FONT = ("Courier", 24, "bold")
SCOREBOARD_POSITION = (-280, 260)


class Scoreboard(Turtle):
    def __init__(
        self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = False
    ) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.penup()
        self.color("white")
        self.level = 1
        self.update_level()

    def update_level(self):
        self.clear()
        self.goto(SCOREBOARD_POSITION)
        self.write(arg=f"LEVEL: {self.level}", align="left", font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_level()

    def display_game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align="center", font=FONT)
