''' Program name: Good Sentence!
    Author: Jordan Culver
    Date: 6/29/2021
    Summary: This program will take input from the user, having the option to take a full sentence or entering word by word, and returning
                that sentence in a corrected format for the user with the number of words displayed, as well.'''

'''
run.programName; program name; string
run.sentence; list to hold initial words; list(string)
words; user input for words; string
numWords; number of words to input; int
i; keep count for interations; int
sen.fracturedSentence; corrected sentence placed in this list; list(string)
sen.punctuation; dictionary for correct ? input with key words; string/char
capitalize; holds and capitalizes for word in list; string
middle; list which hold all but the first and last word; list(string)
lastLetter; last letter, digit, or special character in the last word; string
lasWord; last word in the list; string
correctPunc; holds either . or ? depending on key word argument; string
puncuate; final word with concatenated appropriate punctuation mark; string
sen.joined; holds the final sentence with modifications; string

'''

# Program Class




from io import RawIOBase
class Program():
    def __init__(self, programName):
        self.programName = programName
        self.sentence = []

    # Main Running Function

    def main(self):
        self.greeting()
        self.menuWordGet()
        sen.moveMiddleSentence()
        sen.capitalizeFirst()
        sen.correctPuncuation()
        sen.joining()
    # Greet the user

    def greeting(self):
        print(f"\n\t\t{self.programName}")
        print("=" * 50)

    # Get full sentence from user for modification (currently turned off)

    def gettingSentence(self):
        words = input(
            "\nPlease input a sentence (No worries on Grammar!): \n\n")
        self.sentence = words.split()

    def menuWordGet(self):
        print("How would you like to input the information?")
        print("=" * 50)
        print("1. Full Sentence")
        print("2. Number Indicated")
        print("3. During Process Indicated")
        while True:
            try:
                selection = int(input("\nPlease make a numbered selection: "))
                if selection < 1 or selection > 3:
                    raise Exception
                break
            except Exception:
                print("\nThat value is not valid.  Select a different value.")

        if selection == 1:
            run.gettingSentence()
        elif selection == 2:
            run.gettingWords()
        else:
            run.gettingWordsCurrent()

    def gettingWordsCurrent(self):
        while True:
            words = input("\nEnter a single word for your sentence: ")
            words = words.strip(" ")
            self.sentence.append(words)

            confirm = input(
                "\nDo you have another word for your sentence: (Y or N): ").capitalize()

            if confirm != "Y":
                break

    # Get a single word at a time from user

    def gettingWords(self):
        while True:
            try:
                numWords = int(
                    input("\nHow many words are in your sentence?: "))
                break
            except:
                print("\nThat is not a number.  Please type a number!")
        print("=" * 40)
        i = 0
        while i < numWords:
            word = input("Enter your sentence one word at a time: ")
            word = word.strip(" ")
            self.sentence.append(word)
            i += 1

    # Good bye message after completion of program

    def sayingGoobye(self):
        print(
            f"\nThanks for using our {self.programName} program.  Have a great day!")

# Sentence changing class


class Sentence():
    def __init__(self):
        self.fracturedSentence = []
        self.punctuation = {"Who": "?", "What": "?",
                            "When": "?", "Where": "?", "Why": "?", "Is": "?", "Can": "?", "Will": "?", "Am": "?",
                            "Which": "?", "Whose": "?", "Whom": "?"}
    # Will capitlaize the first word in the sentence

    def capitalizeFirst(self):
        capitalize = run.sentence[0].capitalize()
        self.fracturedSentence.insert(0, capitalize)
    # Will take second to second-to-last values from self.sentence list and append to new list

    def moveMiddleSentence(self):
        middle = run.sentence[1:-1]
        for word in middle:
            self.fracturedSentence.append(word)
    # Corrects punctuation based on user input

    def correctPuncuation(self):
        lastLetter = run.sentence[-1][-1]
        lastWord = run.sentence[-1]
        correctPunc = self.punctuation.get(self.fracturedSentence[0], ".")
        if lastLetter != correctPunc and lastLetter.isdigit() or lastLetter.isalpha():
            punctuate = lastWord + correctPunc
        elif lastLetter != correctPunc and not lastLetter.isdigit() or not lastLetter.isalpha():
            punctuate = lastWord.rstrip(".?") + correctPunc
        else:
            punctuate = lastWord

        self.fracturedSentence.append(punctuate)
    # Joins the final list to make a string sentence with all the modifications

    def joining(self):
        self.joined = " ".join(self.fracturedSentence)
        print("=" * 60)
        print(f"\nCorrected Sentence: {self.joined}")
        print(
            f"Word Count: {len(self.fracturedSentence)} ")
        print("=" * 60)


if __name__ == "__main__":
    sen = Sentence()
    run = Program("Good Sentence!")
    run.main()
