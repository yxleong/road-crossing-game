"""
Program : main_menu.py
Author : GROUP 10
            林佩佩 B10915067
            羅翡瑩 B11015010
            盧清珍 B11015012
            梁婭瑄 B11015016
Analysis:
1. This file defines the main menu of the game using the Tkinter library.
2. It includes buttons to start the game, display scores, and exit the game.

Design - pseudocode:
1. Import modules from library
      tkinter
2. Define the significant constant
      PLAY_BUTTON_PATH, QUIT_BUTTON_PATH, HOME_BUTTON_PATH, RESTART_BUTTON_PATH, MAIN_MENU_BACKGROUND_PATH, SCORE_MENU_BACKGROUND_PATH: Paths to image assets.
      FONT: Font configuration for text display.
3. Define the Menu class
      Initialize the main window with specified attributes
      Create attributes for current score, images, and music
      Create a container frame and initialize frames for MainMenu, ScoreMenu, and Game
      Show the MainMenu initially
      Define method to show a specific frame and handle music and gameplay
      Define method to resize the window
      Define method to delete the Game frame
      Define method to exit the game
      Define method to play collision sound
4. Define the MainMenu class
      Initialize the MainMenu frame with background image and buttons
      Define buttons for starting the game and exiting
      Handle button placements and appearances
5. Define the ScoreMenu class
      Initialize the ScoreMenu frame with background image, buttons, and score display
      Define buttons for returning to the main menu and restarting the game
      Update the displayed score when needed
"""
from tkinter import *

# Importing other modules and constants
from game import Game, SCREEN_WIDTH, SCREEN_HEIGHT
from music import Music

# Paths to image assets for buttons and backgrounds
PLAY_BUTTON_PATH = "assets/play_button.png"
QUIT_BUTTON_PATH = "assets/quit_button.png"
HOME_BUTTON_PATH = "assets/home_button.png"
RESTART_BUTTON_PATH = "assets/restart_button.png"
MAIN_MENU_BACKGROUND_PATH = "assets/main_menu.png"
SCORE_MENU_BACKGROUND_PATH = "assets/score_menu.png"

# Font configuration for text display
FONT = ("Comic Sans MS", 72, "bold")

# Class representing the main menu of the game
class Menu(Tk):
    def __init__(self, *args, **kwargs) -> None:
        Tk.__init__(self, *args, **kwargs)

        # Setting up the main window
        self.title("Road Crossing Game 🚗")  # Set the title of the main window
        self.resize_window(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)  # Resize the window to a specified width and height

        # Initializing attributes
        self.current_score = 0  # Initialize the current score attribute to 0
        self.images = {
            "play": PhotoImage(file=PLAY_BUTTON_PATH),  # Load the play button image
            "quit": PhotoImage(file=QUIT_BUTTON_PATH),  # Load the quit button image
            "home": PhotoImage(file=HOME_BUTTON_PATH),  # Load the home button image
            "restart": PhotoImage(file=RESTART_BUTTON_PATH),  # Load the restart button image
            "bg_main_menu": PhotoImage(file=MAIN_MENU_BACKGROUND_PATH),  # Load the main menu background image
            "bg_score_menu": PhotoImage(file=SCORE_MENU_BACKGROUND_PATH),  # Load the score menu background image
        }
        self.music = Music()  # Create an instance of the Music class for handling game sounds

        # Creating a container frame to hold different pages
        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)  # Pack the container frame to the top, filling both directions

        # Dictionary to store instances of different frames
        self.frames = {}
        for F in (MainMenu, ScoreMenu, Game):  # Iterate through different frame classes
            page_name = F.__name__  # Get the name of the frame class
            frame = F(parent=container, controller=self)  # Create an instance of the frame class
            self.frames[page_name] = frame  # Store the frame instance in the dictionary
            frame.grid(row=0, column=0, sticky="nsew")  # Grid the frame to the container with sticky configuration

        # Display the main menu frame by default
        self.show_frame("MainMenu")

    # Method to switch between frames and perform specific actions based on the frame
    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()  # Bring the selected frame to the front
        self.tkraise()  # Bring the main window to the front
        if page_name == "Game":
            self.music.play_bgm()  # Play background music when entering the game frame
            frame.play_game()  # Start the game when entering the game frame

        elif page_name == "MainMenu":
            self.music.play_bgm()  # Play background music when entering the main menu frame

        elif page_name == "ScoreMenu":
            frame.update_score(self.current_score)  # Update the displayed score when entering the score menu frame
            self.music.play_gameover()  # Play game over sound when entering the score menu frame

    # Method to resize the main window
    def resize_window(self, width, height):
        ws = self.winfo_screenwidth()  # Get the screen width
        hs = self.winfo_screenheight()  # Get the screen height

        x = (ws / 2) - (width / 2)  # Calculate the x-coordinate for centering the window
        y = (hs / 2) - (height / 2)  # Calculate the y-coordinate for centering the window

        self.geometry(f"{width}x{height}+{int(x)}+{int(y)}")  # Set the window geometry

    # Method to delete the game frame and exit the game
    def delete_game_frame(self):
        self.frames["Game"].delete_game() 

    # Method to exit the game
    def exit_game(self):
        self.delete_game_frame()
        self.destroy()  # Destroy the main window to exit the game

    # Method to play collision sound
    def play_collision_music(self):
        self.music.play_collision()  # Play the collision sound effect

# Class representing the main menu of the game
class MainMenu(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        # Creating and placing a background label
        bg_label = Label(self, image=self.controller.images["bg_main_menu"])
        bg_label.image = self.controller.images["bg_main_menu"]
        bg_label.pack()  # Pack the background label into the frame

        # Creating and placing buttons for starting the game and exiting
        start_game_btn = Button(
            self,
            image=controller.images["play"],
            command=lambda: controller.show_frame("Game"),  # Show the Game frame when the button is clicked
            bd=0,  # Set border width to 0 for a clean button appearance
        )
        start_game_btn.config(width=390, height=122)  # Set the width and height of the button

        exit_game_btn = Button(

            self,
            image=controller.images["quit"],
            command=lambda: controller.exit_game(),  # Exit the game when the button is clicked
            bd=0,  # Set border width to 0 for a clean button appearance
        )
        exit_game_btn.config(width=386, height=120)  # Set the width and height of the button

        start_game_btn.place(x=460, y=222)  # Place the start game button at specified coordinates
        exit_game_btn.place(x=455, y=367)  # Place the exit game button at specified coordinates

# Class representing the score menu of the game
class ScoreMenu(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.score = self.controller.current_score

        # Creating a canvas and placing the score menu background
        self.canvas = Canvas(self)
        self.canvas.create_image(
            SCREEN_WIDTH / 2,
            SCREEN_HEIGHT / 2,
            image=controller.images["bg_score_menu"],
        )
        self.canvas.pack(expand=True, fill=BOTH)

        # Creating and placing the text displaying the current score
        self.score_text = self.canvas.create_text(670, 380, text=self.score, font=FONT)

        # Creating and placing buttons for returning to the main menu and restarting the game
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

    # Method to update the displayed score
    def update_score(self, score):
        self.score = score
        self.canvas.itemconfig(self.score_text, text=self.score)

# End of the classes
