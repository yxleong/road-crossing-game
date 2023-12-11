"""
Program : main.py
Author : Group 10
Analysis:
1. This file serves as the entry point of the program.
2. It imports the Menu class from main_menu.py and initializes the main application.

Design - pseudocode:
1. Define the significant constant
   None in this file.
2. The inputs are
   None in this file.
3. Computations:
   Import Menu class from main_menu module.
   Create an instance of the Menu class.
   Start the main event loop of the Tkinter application.
4. The output is
   None in this file.
"""

# Importing the Menu class from the main_menu module
from main_menu import Menu

# Creating an instance of the Menu class, which represents the main application
main_app = Menu()

# Starting the main event loop of the Tkinter application
main_app.mainloop()
