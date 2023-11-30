from tkinter import *

from game import Game, SCREEN_WIDTH, SCREEN_HEIGHT


class Menu(Tk):
    def __init__(self, *args, **kwargs) -> None:
        Tk.__init__(self, *args, **kwargs)

        self.title("Road Crossing Game 🚗")
        self.resize_window(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)

        self.current_score = 0

        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)

        self.frames = {}
        for F in (MainMenu, ScoreMenu, Game):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("MainMenu")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()
        self.tkraise()
        if page_name == "Game":
            frame.play_game()
        elif page_name == "ScoreMenu":
            frame.update_score(self.current_score)

    def resize_window(self, width, height):
        ws = self.winfo_screenwidth()
        hs = self.winfo_screenheight()

        x = (ws / 2) - (width / 2)
        y = (hs / 2) - (height / 2)

        self.geometry(f"{width}x{height}+{int(x)}+{int(y)}")

    def delete_game_frame(self):
        self.frames["Game"].delete_game()

    def exit_game(self):
        self.delete_game_frame()
        self.destroy()


class MainMenu(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        label = Label(self, text="This is the MainMenu page")
        label.pack(side="top", fill="x", pady=10)

        start_game_btn = Button(
            self,
            text="Start Game",
            command=lambda: controller.show_frame("Game"),
        )
        # button2 = Button(
        #     self,
        #     text="Go to ScoreMenu",
        #     command=lambda: controller.show_frame("ScoreMenu"),
        # )
        exit_game_btn = Button(
            self, text="Exit Game", command=lambda: controller.exit_game()
        )

        start_game_btn.pack()
        # button2.pack()
        exit_game_btn.pack()


class ScoreMenu(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        self.score = self.controller.current_score
        self.label = Label(self, text=f"Score: {self.score}")
        self.label.pack(side="top", fill="x", pady=10)
        back_btn = Button(
            self,
            text="Go Back to Main Menu",
            command=lambda: controller.show_frame("MainMenu"),
        )
        back_btn.pack()

    def update_score(self, score):
        self.score = score
        self.label.config(text=f"Score: {self.score}")
