from parser import *
from questionmodel import *
from questionview import *

import tkinter as tk
import random as rand

class QuestionController: # This class makes the link between model and view
    # Create question, move to the next question when answered
    def __init__(self, question_view: QuestionView):
        """Initializes the QuestionController object."""
        self.question_view = question_view
        # Get parsed the data
        parser = Parser()
        self.countries = parser.get_countries()
        print("Countries parsed: ", len(self.countries))
        self.questions = []
        self.current_question = 0
        self.good_answer_nb = 0

    def run(self):
        """Creates the questions and displays the first question."""
        self.create_questions()
        self.question_view.init_display()
        self.load_question()
        self.question_view.display()

    def create_question(self, i = 0):
        """Creates the question using the given index i."""
        i = i if i <= len(self.countries) else len(self.countries)
        question_model = QuestionModel(self.countries[i], self.countries)
        return question_model
    
    def create_questions(self, question_nb = 10):
        """Creates the questions by taking random countries"""
        if question_nb > len(self.countries):
            question_nb = len(self.countries)
        rand_countries = rand.sample(self.countries, question_nb)
        for i in range(question_nb):
            self.questions.append(QuestionModel(rand_countries[i], self.countries))

    def get_questions(self):
        """Gets questions."""
        return self.questions
    
    def set_question_view(self, question_view):
        """Sets question_view."""
        self.question_view = question_view

    # Actions
    def print_choice(self):
        """Prints radio buttons choice."""
        print(self.question_view.get_choice_val())

    def check_result(self): # called at each submit of answer
        """Check the answer choosen and loads the next question if there is one, otherwise """
        if self.question_view.get_choice_val() == self.questions[self.current_question].get_answer():
            print("The answer is correct")
            self.good_answer_nb += 1
        else:
            print("The answer is wrong")
        # load next question
        if self.current_question + 1 < len(self.questions):
            self.current_question += 1
            self.load_question()
        else:
            self.question_view.hide_widgets()
            self.question_view.set_result(self.good_answer_nb, len(self.questions))
            self.question_view.show_result()
        self.question_view.set_progress_text(f"You have answered: {self.current_question} / {len(self.questions)}") 

    def load_question(self):
        """Loads the current question"""
        self.question_view.set_question_text(self.questions[self.current_question].get_question())
        self.question_view.set_question_choices(self.questions[self.current_question].get_multiple_choice())
        self.question_view.set_progress_text(f"You have answered: {self.current_question} / {len(self.questions)}")

if __name__ == "__main__":
    print("Test")
