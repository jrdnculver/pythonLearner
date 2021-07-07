''' Program name: File Counts
    Author: Jordan Culver
    Date: 6/28/2021
    Summary: This program allows the input of loaded or user defined files in the directory to count upper case, lower case, 
            digits, and white space involved in a txt file. '''

import os

content = []
fracturedContent = []
LoadedFile = {1: "text.txt"}

# Program class runs program


class ProgramRun():
    def __init__(self, programName):
        self.programName = programName

    def main(self):
        self.greeting()
        selection = runFile.selectFile()
        runFile.userInputFile() if selection == 1 else runFile.loadedInputFile()
        runFile.readText()
        strAction.breakUpContent()
        strAction.isUpper()
        strAction.isLower()
        strAction.isDigits()
        strAction.isWhiteSpace()
        self.displayResults()
        self.sayGoodBye()

    # Greeting to the user

    def greeting(self):
        print(f"\n\t\t\t{self.programName.upper()}")
        print("=" * 70)
        print("This program will take a txt file, read it, and return specific counts\n")
        print("These counts consist of: ")
        print("=" * 25)
        print("Number of Upper Case Letters")
        print("Number of Lower Case Letters")
        print("Number of Total Digits")
        print("Number of Total White Spaces\n")

    # Displays final count results to the user

    def displayResults(self):
        print("\nThe results for counts is complete!")
        print("\nHere is your final REPORT:")
        print("=" * 28)
        print(f"File Name: {runFile.file}")
        print(f"Upper Case: {strAction.numUpperCase}")
        print(f"Lower Case: {strAction.numLowerCase}")
        print(f"Digits: {strAction.numDigits}")
        print(f"White Space: {strAction.numWhiteSpaces}")

    # Displays fairwell at the end of program

    def sayGoodBye(self):
        print(
            f"\nThanks for using our {self.programName} program.  Have a great day!")
        print("=" * 60)

# Class to manage loading and reading files


class FileManager():
    def __init__(self):
        self.file = " "

    def readText(self):
        self.file = self.file
        self.useFile = open(self.file, "r")
        for line in self.useFile:
            content.append(line)
        self.useFile.close()

    # User selection of loaded file... Current loaded file is text.txt

    def loadedInputFile(self):
        while True:
            i = 1
            print("\nPre-Loaded Files")
            print("=" * 20)
            for key, value in LoadedFile.items():
                print(f"{i}. {value}")
                i += 1
            selection = int(input("\nPlease select loaded file: "))
            self.file = LoadedFile.get(selection, "Error")
            if self.file != "Error":
                break
            else:
                print("\nThat is not a valid choice.  Try Again!")

    # User defined input for file loading

    def userInputFile(self):
        while True:
            try:
                self.file = input("\nEnter the file name: ")
                exist = os.path.exists(self.file)
                if exist == False:
                    raise Exception
                break
            except:
                print("\nThat file does not exist in the current Directory!")

    # User choice in selecting what type of file to load

    def selectFile(self):
        print("Please select an option for a file!")
        print("=" * 36)
        print("1. User-Defined File")
        print("2. Pre-Loaded File")

        while True:
            try:
                selection = int(input("\nWhich option do you choose?: "))
                if selection < 1 or selection > 2:
                    raise Exception
                break
            except:
                print("\nThat is not a valid choice.  Try Again!")

        return selection

# Class which represents string methods for data manipulation


class StringManagement():
    def __init__(self, stringName):
        self.stringName = stringName
        self.numUpperCase = 0
        self.numLowerCase = 0
        self.numDigits = 0
        self.numWhiteSpaces = 0

    # Atomizes data to singular letter form

    def breakUpContent(self):
        stringContent = " ".join(content)
        for letter in stringContent:
            fracturedContent.append(letter)

    # Test if character is uppercase, and adds to count if True

    def isUpper(self):
        for character in fracturedContent:
            Upped = character.isupper()
            if Upped == True:
                self.numUpperCase += 1

    # Test if character is lowercase, and adds to count if True

    def isLower(self):
        for character in fracturedContent:
            lowered = character.islower()
            if lowered == True:
                self.numLowerCase += 1

    # Test if character is a digit, and adds to count if True

    def isDigits(self):
        for digit in fracturedContent:
            digited = digit.isdigit()
            if digited == True:
                self.numDigits += 1

    # Test if whitespace character, and adds to count if True

    def isWhiteSpace(self):
        for spaceChar in fracturedContent:
            spaced = spaceChar.isspace()
            if spaced == True:
                self.numWhiteSpaces += 1


if __name__ == "__main__":
    run = ProgramRun("'File Counts'")
    runFile = FileManager()
    strAction = StringManagement("StringAlong")
    run.main()
