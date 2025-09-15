from country import *
import random as rand

class QuestionModel:
    """QuestionModel is the logical representation of the question."""
    def __init__(self, country: Country, countries: list, choice_nb: int = 2):
        """Creates a question, its answer and its multiple choice.
        choiceNb is the number of wrong choices."""
        self.question = f"What is the capital of {country.get_name()} ?"
        self.answer = country.get_capital()
        self.multiple_choice = [] # this will contain the capitals from which the user must choose
        choice_nb = choice_nb if choice_nb <= len(countries) else len(countries)
        self.multiple_choice = rand.sample(countries, choice_nb) # choose randomly without repetition a given number of countries
        self.multiple_choice = [ country.capital for country in self.multiple_choice]
        self.multiple_choice.append(self.answer)
        rand.shuffle(self.multiple_choice)

    def get_question(self):
        """Gets question."""
        return self.question
    
    def get_answer(self):
        """Gets answers."""
        return self.answer
    
    def get_multiple_choice(self):
        """Gets multiple_choice."""
        return self.multiple_choice
    
    def __repr__(self):
        """Gets the string representation of QuestionModel for the print() function."""
        repr = self.question
        for capital in self.multiple_choice:
            repr += "\n" + capital
        repr += f"\nAnswer: {self.answer}"
        return repr
    
    def __str__(self):
        """Gets the string representation of QuestionModel."""
        return self.__repr__()