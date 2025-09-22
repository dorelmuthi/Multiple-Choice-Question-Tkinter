"""
MCQ Multiple Choice Question
"""
import tkinter as tk
from tkinter import messagebox
#from tkinter.ttk import * 
# # about changing the style for frame in tkinter.ttk case:
# https://stackoverflow.com/questions/54476511/setting-background-color-of-a-tkinter-ttk-frame

from questionctrl import *
from questionview import *
from menuview import *
from constants import *

class App(tk.Tk):
    def __init__(self, **kwargs):
        """Initializes the root window of the application and display it in the middle of the screen."""
        super().__init__(**kwargs) # Iinitialize the class using the constructor of Tk
        self.title("MCQ - Countries capital")
        self.app_width = 600
        self.app_height = 600
        self.app_start_x, self.app_start_y = self.get_centered_starting_pos()
        self.geometry("{width}x{height}+{start_x}+{start_y}".format(
            width = self.app_width, height = self.app_height, 
            start_x=self.app_start_x, start_y=self.app_start_y))
        self.configure(background=BACKGROUND_COLOR)
        self.current_window = MenuView(self)
        self.current_window.display()

    def get_centered_starting_pos(self):
        """Returns the centerd starting position on the basis of the screen size 
        and the application size in pixels, in order to display the application centered
        on the screen of the computer."""
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        app_start_x = screen_width // 2 - self.app_width // 2
        app_start_y = screen_height // 2 - self.app_height // 2
        return app_start_x, app_start_y

    def display_question_view(self):
        """Displays the view allowing to display the questions to answer."""
        self.current_window.hide()
        # 1 Create the question view
        question_view = QuestionView(self)
        # 2 Create the question controller and give the view to the controller
        question_ctrl = QuestionController(question_view)
        # 3 Start the program through the controller
        question_ctrl.run()
        self.current_window = question_view

    def display_menu_view(self):
        """Displays the starting main menu of the application."""
        reponse = messagebox.askquestion(title="Going back to the menu", message="Are you sure?")
        if reponse == messagebox.YES:
            self.current_window.hide()
            self.current_window = MenuView(self)
            self.current_window.display()

    def run(self):
        """Sarts the display of the application"""
        self.mainloop()

if __name__ == "__main__":
    print("MCQ launched")
    app = App()
    app.run()