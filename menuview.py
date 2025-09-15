import tkinter as tk
from tkinter import messagebox
#from main import *

class MenuView(tk.Frame):
    def __init__(self, root, **kwargs):
        """Initializes MenuView object."""
        super().__init__(root,  borderwidth=2, relief=tk.SOLID, height = 50, width = 100, **kwargs)
        self.color = "sky blue" # Color chart: https://cs111.wellesley.edu/archive/cs111_fall14/public_html/labs/lab12/tkintercolor.html
        self.configure(background=self.color)
        self.start_but = tk.Button(self, text="Start", command=root.display_question_view)
        self.start_but.pack()
        self.history_but = tk.Button(self, text="History", command=self.display_history)
        self.history_but.pack()
        self.exit_but = tk.Button(self, text="Exit", command=root.destroy)
        self.exit_but.pack()

    def display_history(self):
        """Displays history."""
        messagebox.showinfo(title="Information", message="In development")
    
    def display(self):
        """Displays the MenuView frame in the center of the root application widget."""
        self.pack(expand=1)
    def hide(self):
        """Hides the MenuView frame in the root application widget without destroying it."""
        self.pack_forget()

if __name__ == "__main__":
    print("Test")
