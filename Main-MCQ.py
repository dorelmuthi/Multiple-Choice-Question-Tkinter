"""
MCQ Multiple Choice Question
"""
import tkinter as tk
#from tkinter.ttk import * 
# # about changing the style for frame in tkinter.ttk case:
# https://stackoverflow.com/questions/54476511/setting-background-color-of-a-tkinter-ttk-frame

from QuestionController import *
from QuestionView import *

class App(tk.Tk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs) # Iinitialize the class using the constructor of Tk
        self.title("MCQ - Countries capital")
        self.geometry("600x600")
        # Create the question view
        qV = QuestionView(self)
        # Create the question controller
        qC = QuestionController(qV)
        # Set the controller to the view
        qV.setQuestionController(qC)
        qC.run() # Start the program through the controller
    def run(self):
        self.mainloop() # Starts the display of the application

if __name__ == "__main__":
    print("MCQ launched")
    app = App()
    app.run()