from tkinter import *

from game import Game, SCREEN_WIDTH, SCREEN_HEIGHT

PLAY_BUTTON_PATH = "images\play_button.png"
QUIT_BUTTON_PATH = "images\quit_button.png"
HOME_BUTTON_PATH = "images\home_button.png"
RESTART_BUTTON_PATH = "images\\restart_button.png"
MAIN_MENU_BACKGROUND_PATH = "images\plan_main_menu.png"
GAME_OVER_BACKGROUND_PATH = "images\game_over_menu.png"
STAR_PATH = "images\star.png"

class Menu(Tk):
    def __init__(self, *args, **kwargs) -> None:
        Tk.__init__(self, *args, **kwargs)

        self.title("Road Crossing Game 🚗")
        self.resize_window(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)

        self.current_score = 0
        self.button_images = {
            "play": PhotoImage(file=PLAY_BUTTON_PATH),
            "quit": PhotoImage(file=QUIT_BUTTON_PATH),
            "home": PhotoImage(file=HOME_BUTTON_PATH),
            "restart": PhotoImage(file=RESTART_BUTTON_PATH),
        }

        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)

        self.frames = {}
        for F in (MainMenu, ScoreMenu, Game):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # self.show_frame("MainMenu")
        self.show_frame("ScoreMenu")

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

        bg_image = PhotoImage(file=MAIN_MENU_BACKGROUND_PATH)
        bg_label = Label(self, image=bg_image)
        bg_label.image = bg_image
        # bg_label.place(x=0, y=0)
        bg_label.pack()

        start_game_btn = Button(
            self,
            image=controller.button_images["play"],
            command=lambda: controller.show_frame("Game"),
            bd=0,
        )
        # start_game_btn.pack()
        start_game_btn.config(width=378, height=120)
        # start_game_btn.place(x=458, y=222)
        # start_game_btn.lift()

        exit_game_btn = Button(
            self,
            image=controller.button_images["quit"],
            command=lambda: controller.exit_game(),
            bd=0,
        )
        exit_game_btn.config(width=386, height=120)
        # exit_game_btn.place(x=455, y=367)

        start_game_btn.place(x=458, y=222)
        exit_game_btn.place(x=455, y=367)


class ScoreMenu(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.score = self.controller.current_score

        # gg_image = PhotoImage(file=GAME_OVER_BACKGROUND_PATH)
        gg_image = PhotoImage(file='images\plan_score_menu.png')
        menu_label = Label(self, image=gg_image)
        menu_label.image = gg_image
        # menu_label.place(x=300, y=132)
        menu_label.pack()
        
        # self.label.pack(
        #     side="left", 
        #     fill="x", 
        #     pady=10
        # )

        # back_btn = Button(
        #     self,
        #     text="Go Back to Main Menu",
        #     command=lambda: controller.show_frame("MainMenu"),
        # )
        # back_btn.pack()

        # bg_image = PhotoImage(file='images\plan_game_over.gif')
        # bg_image = PhotoImage(file='assets\scene2.gif')
        # bg_label = Label(self, image=bg_image)
        # bg_label.image = bg_image
        # bg_label.pack()

        star_img = PhotoImage(file=STAR_PATH)
        self.label = Label(
            self, 
            # text=f"Score: {self.score}",
            text=self.score,
            font=("Arial", 72)
        )
        self.label.place(x=647, y=338)
        self.label.lift()

        home_btn = Button(
            self,
            image=controller.button_images["home"],
            command=lambda: controller.show_frame("MainMenu"),
            bd=0,
        )

        home_btn.config(width=139, height=139)
        home_btn.place(x=512, y=510)

        restart_btn = Button(
            self,
            image=controller.button_images["restart"],
            command=lambda: controller.show_frame("Game"),
            bd=0,
        )

        restart_btn.config(width=139, height=139)
        restart_btn.place(x=698, y=510)

    def update_score(self, score):
        self.score = score
        # self.label.config(text=f"Score: {self.score}")
        self.label.config(text=self.score)
