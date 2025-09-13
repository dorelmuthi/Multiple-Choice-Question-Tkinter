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

class App(tk.Tk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs) # Iinitialize the class using the constructor of Tk
        self.title("MCQ - Countries capital")
        self.geometry("600x600")
        self.currentWindow = MenuView(self)
        self.currentWindow.display()

    def displayQuestionView(self):
        self.currentWindow.hide()
        # Create the question view
        qV = QuestionView(self)
        # Create the question controller
        qC = QuestionController(qV)
        # Set the controller to the view
        qV.setQuestionController(qC)
        qC.run() # Start the program through the controller
        self.currentWindow = qV

    def displayMenuView(self):
        reponse = messagebox.askquestion(title="Going back to the menu", message="Are you sure?")
        if reponse == messagebox.YES:
            self.currentWindow.hide()
            self.currentWindow = MenuView(self)
            self.currentWindow.display()

    def run(self):
        self.mainloop() # Starts the display of the application

if __name__ == "__main__":
    print("MCQ launched")
    app = App()
    app.run()