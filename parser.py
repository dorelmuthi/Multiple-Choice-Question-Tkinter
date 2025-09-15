from country import *

class Parser:
    """Parser class is used to parse the file containing the list of countries with their capital."""
    def __init__(self, verbose=False):
        """Initializes the ¨Parser."""
        self.countries = get_parsed_countries(verbose)

    def get_countries(self):
        """Returns the parsed countries."""
        return self.countries

def get_parsed_countries(verbose=False):
    """Parses the countries from the country-list.csv file intro a list of Countries objects."""
    countries = []
    f = open("./country-list.csv", "r", encoding='UTF-8') # open the file with the data
    line = f.readline() # read the first line and do nothing because it is the header
    while line != "": # loop through the remaining lines of the file
        line = f.readline().strip() # remove spaces at the begin and the end of the line
        line_list = line.split(",") # create a list from the line using the separator ,
        #if verbose: print(lineList)
        if len(line) >= 2:
            country = Country(name=line_list[0].strip('"'),capital=line_list[1].strip('"')) # Strip is used to remove the " at the begin and the end of the element 
            if verbose: print(country)
            countries.append(country)
    if verbose: print("Number of countries parsed: ", len(countries))
    return countries

if __name__ == "__main__":
    print("Parsing with function")
    countries = get_parsed_countries(True)
    print("Number of countries returned", len(countries))
    print()
    print("Parsing with class")
    p = Parser(True)
    countries = p.get_countries()
    print("Number of countries returned", len(countries))