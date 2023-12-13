"""
Program : main.py
Author : GROUP 10
            林佩佩 B10915067
            羅翡瑩 B11015010
            盧清珍 B11015012
            梁婭瑄 B11015016
Analysis:
1. This file serves as the entry point of the program
2. It imports the Menu class from main_menu.py and initializes the main application

Design - pseudocode:
1. Import required module
      main_menu
2. Create an instance of the Menu class
      main_app
3. Start the main event loop
"""

# Importing the Menu class from the main_menu module
from main_menu import Menu

# Creating an instance of the Menu class, which represents the main application
main_app = Menu()

# Starting the main event loop of the Tkinter application
main_app.mainloop()
