from tkinter import *
import subprocess

from game import Game


class Menu(Tk):
    def __init__(self, *args, **kwargs) -> None:
        Tk.__init__(self, *args, **kwargs)

        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)

        self.frames = {}
        for F in (MainMenu, PauseMenu, Game):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("MainMenu")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

    def start_game(self, container):
        new_game_frame = type(self.frames["Game"])(parent=container, controller=self)
        # self.frames["Game"] = game_frame
        # new_game_frame.grid(row=0, column=0, sticky="nsew")
        new_game_frame.tkraise()
        new_game_frame.play_game()

    def delete_game_frame(self):
        self.frames.pop("Game")

    def resize_window(self, width, height):
        self.geometry(f"{width}x{height}")


class MainMenu(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        label = Label(self, text="This is the MainMenu page")
        label.pack(side="top", fill="x", pady=10)

        button1 = Button(
            self,
            text="Go to PauseMenu",
            command=lambda: controller.show_frame("PauseMenu"),
        )
        button2 = Button(
            self,
            text="Go to Game",
            command=lambda: controller.start_game(controller),
        )
        button1.pack()
        button2.pack()


class PauseMenu(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        label = Label(self, text="This is page 1")
        label.pack(side="top", fill="x", pady=10)
        button = Button(
            self,
            text="Go to the MainMenu page",
            command=lambda: controller.show_frame("MainMenu"),
        )
        button.pack()
