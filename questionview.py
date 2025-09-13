from questionctrl import *
from main import App 
import tkinter as tk

class QuestionView(tk.Frame): # This is the graphical representation of the question
    def __init__(self, root: App, qC = None, **kwargs):
        # Frame initialization and configuration
        super().__init__(root, borderwidth=2, relief=tk.SOLID, height = 50, width = 100, **kwargs)
        self.qC = qC
        self.color = "sky blue" # Color chart: https://cs111.wellesley.edu/archive/cs111_fall14/public_html/labs/lab12/tkintercolor.html
        self.configure(background=self.color)
        # Frame widgets initialization
        self.qL = tk.Label() # Question Label
        #self.strVar = None # Used to get the value of the radio button selection
        self.choiceNb = 3 # the is used to create the radio buttons
        self.qChoicesRB = [] # radio buttons
        self.strVarChoice = tk.StringVar(self, value="Default") # Contains the choice of the radio buttons
        self.qB = tk.Button()
        self.counterL = tk.Label() # The label containing the number of question answered
        self.resultLabel = tk.Label()
        self.backToMenuB = tk.Button(self, text="Back to menu", command=root.displayMenuView)
    def display(self):
        self.pack(expand=1) # place it on the root, expand=1 is used to center the frame in the root
    def hide(self):
        self.pack_forget()
    def setQuestionController(self, qC):
        # We init the display after receiving the controller
        self.qC = qC
    def initDisplay(self):
        self.qL = tk.Label(self, text="Question", background="light goldenrod")
        self.qL.pack()
        for i in range(self.choiceNb):
            rb = tk.Radiobutton(self, text="capital", value="capital", variable=self.strVarChoice, command=self.printChoice, background=self.color)
            rb.pack(anchor=tk.W, padx=10) # align to left
            self.qChoicesRB.append(rb)
        self.qB = tk.Button(self, text="Submit answer", command=self.qC.checkResult, background="PaleGreen2") # type: ignore
        self.qB.pack()
        self.counterL = tk.Label(self, text="You have answered: 0/total", background=self.color)
        self.counterL.pack()
        self.backToMenuB.pack()
    def printChoice(self): # QC
        print(self.strVarChoice.get())
    def setQuestionText(self, qText: str):
        self.qL.configure(text=qText)
        # The following lines are doing the same thing as the line above
        #self.qL.config(text=qText)
        #self.qL['text']= qText
    def setQuestionChoices(self, choices : list):
        for i in range(len(self.qChoicesRB)):
            qChoiceRB = self.qChoicesRB[i]
            qChoiceRB.configure(text=choices[i], value=choices[i])
    def setProgressText(self, txt):
        self.counterL.configure(text=txt)
    def hideWidgets(self):
        self.qL.pack_forget()
        for qRB in self.qChoicesRB:
            qRB.pack_forget()
        self.qB.pack_forget()
        self.counterL.pack_forget()
    def setResult(self, goodAnswerNb, total):
        self.resultLabel = tk.Label(self, text=f"You have answered correctly to {goodAnswerNb} / {total}", background=self.color)
    def showResult(self):
        self.resultLabel.pack()

if  __name__ == "__main__":
    pass