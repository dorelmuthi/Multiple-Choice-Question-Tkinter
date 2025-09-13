class Country:
    def __init__(self, name, capital):
        self.name = name
        self.capital = capital
    def __repr__(self): # used when object printed
        return "Country: " + self.name + " with capital: " + self.capital
    def __str__(self): # used when object converted to string with str()
        return self.__repr__()
    def __eq__(self, other):
        if isinstance(other, Country):
            if self.name == other.name:
                return True
        return False
    def getName(self):
        return self.name
    def getCapital(self):
        return self.capital