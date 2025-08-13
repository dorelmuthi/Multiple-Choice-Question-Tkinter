import tkinter as tk
from tkinter import messagebox
#from MainMCQ import App

class MenuView(tk.Frame):
    def __init__(self, root, **kwargs):
        super().__init__(root,  borderwidth=2, relief=tk.SOLID, height = 50, width = 100, **kwargs)
        self.color = "sky blue" # Color chart: https://cs111.wellesley.edu/archive/cs111_fall14/public_html/labs/lab12/tkintercolor.html
        self.configure(background=self.color)
        self.startB = tk.Button(self, text="Start", command=root.displayQuestionView)
        self.startB.pack()
        self.historyB = tk.Button(self, text="History", command=self.displayHistory)
        self.historyB.pack()
        self.exitB = tk.Button(self, text="Exit", command=root.destroy)
        self.exitB.pack()
    def displayHistory(self):
        messagebox.showinfo(title="Information", message="In development")
    def display(self):
        self.pack(expand=1)
    def hide(self):
        self.pack_forget()

if __name__ == "__main__":
    print("Test")
