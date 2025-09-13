from country import *
import random as rand

class QuestionModel: # This is the logical representation of the question for the model
    def __init__(self, country: Country, countries: list, choiceNb: int = 2):
        """
        Creates a question, its answer and its multiple choice.
        choiceNb is the number of wrong choices
        """
        self.question = f"What is the capital of {country.getName()} ?"
        self.answer = country.getCapital()
        self.multipleChoice = [] # this will contain the capitals from which the user must choose
        choiceNb = choiceNb if choiceNb <= len(countries) else len(countries)
        self.multipleChoice = rand.sample(countries, choiceNb) # choose randomly without repetition a given number of countries
        self.multipleChoice = [ country.capital for country in self.multipleChoice]
        self.multipleChoice.append(self.answer)
        rand.shuffle(self.multipleChoice)
    def getQuestion(self):
        return self.question
    def getAnswer(self):
        return self.answer
    def getMultipleChoice(self):
        return self.multipleChoice
    def __repr__(self):
        repr = self.question
        for capital in self.multipleChoice:
            repr += "\n" + capital
        repr += f"\nAnswer: {self.answer}"
        return repr
    def __str__(self):
        return self.__repr__()