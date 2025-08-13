from Parser import *
from QuestionModel import *
from QuestionView import *

import tkinter as tk
import random as rand

class QuestionController: # This class makes the link between model and view
    # Create question, move to the next question when answered
    def __init__(self, qV):
        self.qV = qV
        # Get parse the data
        p = Parser()
        self.countries = p.getCountries()
        print("Countries parsed: ", len(self.countries))
        self.questions = []
        self.strVarChoice = tk.StringVar(self.qV, value="Default")
        self.curQ = 0
        self.goodAnswerNb = 0
    def run(self):
        self.createQuestions()
        self.qV.initDisplay()
        self.loadQ()
        self.qV.display()
    def createQuestion(self, i = 0):
        i = i if i <= len(self.countries) else len(self.countries)
        qM = QuestionModel(self.countries[i], self.countries)
        return qM
    def createQuestions(self, qNb = 10):
        if qNb > len(self.countries):
            qNb = len(self.countries)
        randCountries = rand.sample(self.countries, qNb)
        for i in range(qNb):
            self.questions.append(QuestionModel(randCountries[i], self.countries))
    def getQuestions(self):
        return self.questions
    def getStrVarChoice(self):
        return self.strVarChoice
    def setQV(self, qV):
        self.qV = qV
        self.strVarChoice = tk.StringVar(self.qV, value="Default")
    # Actions
    def printChoice(self):
        print(self.strVarChoice.get())
    def checkResult(self): # called at each submit of answer
        self.strVarChoice = self.qV.strVarChoice # get the selected value from the view
        if self.strVarChoice.get() == self.questions[self.curQ].getAnswer():
            print("The answer is correct")
            self.goodAnswerNb += 1
        else:
            print("The answer is wrong")
        # load next question
        if self.curQ + 1 < len(self.questions):
            self.curQ += 1
            self.loadQ()
        else:
            self.qV.hideWidgets()
            self.qV.setResult(self.goodAnswerNb, len(self.questions))
            self.qV.showResult()
        self.qV.setProgressText(f"You have answered: {self.curQ} / {len(self.questions)}")  
    def loadQ(self):
        self.qV.setQuestionText(self.questions[self.curQ].getQuestion())
        self.qV.setQuestionChoices(self.questions[self.curQ].getMultipleChoice())
        self.qV.setProgressText(f"You have answered: {self.curQ} / {len(self.questions)}")

if __name__ == "__main__":
    print("Test")
    #qV = None
    #qc = QuestionController(qV)
