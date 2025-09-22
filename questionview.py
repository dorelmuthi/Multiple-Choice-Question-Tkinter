from main import App
from constants import * 
import tkinter as tk

class QuestionView(tk.Frame):
    def __init__(self, root: App, **kwargs):
        """Initializes the QuestionView class which is the graphical representation of the question."""
        # Frame initialization and configuration
        super().__init__(root, borderwidth=2, relief=tk.SOLID, height = 50, width = root.app_width, **kwargs)
        # Styling the frame
        self.background_color = BACKGROUND_COLOR # Color chart: https://cs111.wellesley.edu/archive/cs111_fall14/public_html/labs/lab12/tkintercolor.html
        self.configure(background=self.background_color)
        # Frame widgets initialization with empty constructors
        self.question_lab = tk.Label() # Displays the question.
        self.question_choices_radbut = [] # Radio buttons to display the choices and to choose the anwser to the quesiton.
        self.submit_but = tk.Button() # Submits the answer of the question.
        self.counter_lab = tk.Label() # Contains the number of question answered.
        self.result_lab = tk.Label() # Contains the number of question anwsered correctly per total.
        self.back_to_menu_but = tk.Button(self, text="Back to menu", command=root.display_menu_view) # Returns to main menu.
        # Properties related to the widgets
        self.choice_nb = 3 # Used to create the radio buttons.
        self.choice_strvar = tk.StringVar(self, value="Default") # Contains the choice value of the radio buttons.

    def display(self):
        """Places the QuestionView frame in the center of the root widget of the application."""
        self.pack(expand=1) # expand=1 is used to center the frame in the root

    def hide(self):
        """Hides the QuestionView frame without destroying the object."""
        self.pack_forget()

    def init_display(self):
        """Initializes the widgets with default values."""
        self.question_lab = tk.Label(self, text="Question", background="light goldenrod")
        self.question_lab.pack()
        for i in range(self.choice_nb):
            choice_radbut = tk.Radiobutton(self, text="capital", value="capital", variable=self.choice_strvar, background=self.background_color) # type: ignore
            choice_radbut.pack(anchor=tk.W, padx=10) # align to left
            self.question_choices_radbut.append(choice_radbut)
        self.submit_but = tk.Button(self, text="Submit answer", background="PaleGreen2") # type: ignore
        self.submit_but.pack()
        self.counter_lab = tk.Label(self, text="You have answered: 0/total", background=self.background_color)
        self.counter_lab.pack()
        self.back_to_menu_but.pack()

    # Command / Action Setters
    def set_submit_command(self, func):
        """Sets the submit button command."""
        self.submit_but.configure(command=func)

    def set_choice_command(self, func):
        """Sets the choice radio buttons command."""
        for choice_radbut in self.question_choices_radbut:
            choice_radbut.configure(command=func)

    def get_choice_val(self):
        """Gets the choice value."""
        return self.choice_strvar.get()
    
    def set_question_text(self, question_text: str):
        """Sets the question text in the question label."""
        self.question_lab.configure(text=question_text)
        # The following lines are doing the same thing as the line above
        #self.qL.config(text=qText)
        #self.qL['text']= qText

    def set_question_choices(self, choices : list):
        """Sets the question choices in the radio buttons."""
        for i in range(len(self.question_choices_radbut)):
            qChoiceRB = self.question_choices_radbut[i]
            qChoiceRB.configure(text=choices[i], value=choices[i])

    def set_progress_text(self, txt):
        """Sets the progress text in the counter label."""
        self.counter_lab.configure(text=txt)

    def hide_widgets(self):
        """Hide all the widgets of the QuestionView frame."""
        self.question_lab.pack_forget()
        for question_radbut in self.question_choices_radbut:
            question_radbut.pack_forget()
        self.submit_but.pack_forget()
        self.counter_lab.pack_forget()

    def set_result(self, goodAnswerNb, total):
        """Sets the result text (the number of correctly anwsered question on the total) in result label."""
        self.result_lab = tk.Label(self, text=f"You have answered correctly to {goodAnswerNb} / {total}", background=self.background_color)
    
    def show_result(self):
        """Place and display the result label in the QuestionView frame."""
        self.result_lab.pack()

if  __name__ == "__main__":
    pass