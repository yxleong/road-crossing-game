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

    # def start_game(self, container):
    #     new_game_frame = type(self.frames["Game"])(parent=container, controller=self)
    #     # self.frames["Game"] = game_frame
    #     # new_game_frame.grid(row=0, column=0, sticky="nsew")
    #     new_game_frame.tkraise()
    #     new_game_frame.play_game()

    def delete_game_frame(self):
        self.frames["Game"].delete_game()

    def resize_window(self, width, height):
        # self.geometry(f"{width}x{height}")
        ws = self.winfo_screenwidth()
        hs = self.winfo_screenheight()

        x = (ws / 2) - (width / 2)
        y = (hs / 2) - (height / 2)

        self.geometry(f"{width}x{height}+{int(x)}+{int(y)}")

    def exit_game(self):
        self.delete_game_frame()
        self.destroy()


class MainMenu(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        label = Label(self, text="This is the MainMenu page")
        label.pack(side="top", fill="x", pady=10)

        button1 = Button(
            self,
            text="Start Game",
            command=lambda: controller.show_frame("Game"),
        )
        # button2 = Button(
        #     self,
        #     text="Go to ScoreMenu",
        #     command=lambda: controller.show_frame("ScoreMenu"),
        # )
        button3 = Button(self, text="Exit Game", command=lambda: controller.exit_game())

        button1.pack()
        # button2.pack()
        button3.pack()


class ScoreMenu(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        self.score = self.controller.current_score
        self.label = Label(self, text=f"Score: {self.score}")
        self.label.pack(side="top", fill="x", pady=10)
        button = Button(
            self,
            text="Go Back to Main Menu",
            command=lambda: controller.show_frame("MainMenu"),
        )
        button.pack()

    def update_score(self, score):
        self.score = score
        self.label.config(text=f"Score: {self.score}")
