from tkinter import *
import pygame
from game import Game, SCREEN_WIDTH, SCREEN_HEIGHT

PLAY_BUTTON_PATH = "assets/play_button.png"
QUIT_BUTTON_PATH = "assets/quit_button.png"
HOME_BUTTON_PATH = "assets/home_button.png"
RESTART_BUTTON_PATH = "assets/restart_button.png"
MAIN_MENU_BACKGROUND_PATH = "assets/main_menu.png"
SCORE_MENU_BACKGROUND_PATH = "assets/score_menu.png"
FONT = ("Comic Sans MS", 72, "bold")
BGM_PATH = "assets/cute_song.mp3"
GAMEOVER_PATH = "assets/Game_Over.mp3"


class Menu(Tk):
    def __init__(self, *args, **kwargs) -> None:
        Tk.__init__(self, *args, **kwargs)

        self.title("Road Crossing Game 🚗")
        self.resize_window(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)

        self.current_score = 0
        self.images = {
            "play": PhotoImage(file=PLAY_BUTTON_PATH),
            "quit": PhotoImage(file=QUIT_BUTTON_PATH),
            "home": PhotoImage(file=HOME_BUTTON_PATH),
            "restart": PhotoImage(file=RESTART_BUTTON_PATH),
            "bg_main_menu": PhotoImage(file=MAIN_MENU_BACKGROUND_PATH),
            "bg_score_menu": PhotoImage(file=SCORE_MENU_BACKGROUND_PATH),
        }

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
            pygame.mixer.init()
            pygame.mixer.music.load(BGM_PATH)
            pygame.mixer.music.play(-1)
            frame.play_game()
            
        elif page_name == "MainMenu":
            pygame.mixer.init()
            pygame.mixer.music.load(BGM_PATH)
            pygame.mixer.music.play(-1)
            
        elif page_name == "ScoreMenu":
            frame.update_score(self.current_score)
            pygame.mixer.music.stop()
            pygame.mixer.init()
            pygame.mixer.music.load(GAMEOVER_PATH)
            pygame.mixer.music.play()

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

        bg_label = Label(self, image=self.controller.images["bg_main_menu"])
        bg_label.image = self.controller.images["bg_main_menu"]
        # bg_label.place(x=0, y=0)
        bg_label.pack()

        start_game_btn = Button(
            self,
            image=controller.images["play"],
            command=lambda: controller.show_frame("Game"),
            bd=0,
        )
        # start_game_btn.pack()

        # start_game_btn.config(width=378, height=120)
        start_game_btn.config(width=390, height=122)

        # start_game_btn.place(x=458, y=222)
        # start_game_btn.lift()

        exit_game_btn = Button(
            self,
            image=controller.images["quit"],
            command=lambda: controller.exit_game(),
            bd=0,
        )
        exit_game_btn.config(width=386, height=120)
        # exit_game_btn.place(x=455, y=367)

        start_game_btn.place(x=460, y=222)
        exit_game_btn.place(x=455, y=367)


class ScoreMenu(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.score = self.controller.current_score

        self.canvas = Canvas(self)
        self.canvas.create_image(
            SCREEN_WIDTH / 2,
            SCREEN_HEIGHT / 2,
            image=controller.images["bg_score_menu"],
        )
        self.canvas.pack(expand=True, fill=BOTH)
        self.score_text = self.canvas.create_text(670, 380, text=self.score, font=FONT)

        home_btn = Button(
            self,
            image=controller.images["home"],
            command=lambda: controller.show_frame("MainMenu"),
            bd=0,
        )
        home_btn.config(width=139, height=139)
        home_btn.place(x=512, y=510)

        restart_btn = Button(
            self,
            image=controller.images["restart"],
            command=lambda: controller.show_frame("Game"),
            bd=0,
        )
        restart_btn.config(width=139, height=139)
        restart_btn.place(x=698, y=510)

    def update_score(self, score):
        self.score = score
        self.canvas.itemconfig(self.score_text, text=self.score)
