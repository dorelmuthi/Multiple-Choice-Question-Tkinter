"""
This file contains the class that will parse the file containing the list of countries with their capital.
"""

from country import *

class Parser:
    def __init__(self, verbose=False):
        self.countries = getParsedCountries(verbose)
    def getCountries(self):
        return self.countries

def getParsedCountries(verbose=False):
    countries = []
    f = open("./country-list.csv", "r", encoding='UTF-8') # open the file with the data
    line = f.readline() # read the first line and do nothing because it is the header
    while line != "": # loop through the remaining lines of the file
        line = f.readline().strip() # remove spaces at the begin and the end of the line
        lineList = line.split(",") # create a list from the line using the separator ,
        #if verbose: print(lineList)
        if len(line) >= 2:
            country = Country(name=lineList[0].strip('"'),capital=lineList[1].strip('"')) # Strip is used to remove the " at the begin and the end of the element 
            if verbose: print(country)
            countries.append(country)
    if verbose: print("Number of countries parsed: ", len(countries))
    return countries

if __name__ == "__main__":
    print("Parsing with function")
    countries = getParsedCountries(True)
    print("Number of countries returned", len(countries))
    print()
    print("Parsing with class")
    p = Parser(True)
    countries = p.getCountries()
    print("Number of countries returned", len(countries))