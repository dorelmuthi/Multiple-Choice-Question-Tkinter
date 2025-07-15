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
        # Create the question controller
        qC = QuestionController()
        # Display the question
        qV = QuestionView(self, qC)
        qV.pack(expand=1) # expand=1 is used to center the frame in the root
    def run(self):
        self.mainloop() # Starts the display of the application

if __name__ == "__main__":
    print("MCQ launched")
    app = App()
    app.run()