class Country:
    """Country is used to store the countries information from the parsed data file."""
    def __init__(self, name, capital):
        """Initializes the Country object."""
        self.name = name
        self.capital = capital

    def __repr__(self):
        """Returns the string representation for print() function."""
        return "Country: " + self.name + " with capital: " + self.capital
    
    def __str__(self):
        """Returns the string representation for str() function."""
        return self.__repr__()
    
    def __eq__(self, other):
        """Returns the result for == operator."""
        if isinstance(other, Country):
            if self.name == other.name:
                return True
        return False
    
    def get_name(self):
        """Returns name."""
        return self.name
    
    def get_capital(self):
        """Returns capital."""
        return self.capital