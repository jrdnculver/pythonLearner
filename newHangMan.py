def HangmanApp():
    playing = True
    checking = True
    wrongGuess = 0
    wrongLetters = []

    while playing == True:
        secWord = gettingSecretWord()
        space()
        secWordList = copySecretLetterList(secWord)
        printBoardGame(secWordList)
        while checking == True:
            userGuess = takeGuess()
            wrongGuess, wrongGuesses = checkGuess(
                secWord, userGuess, secWordList, wrongGuess)
            checking = defineLosing(
                secWordList, wrongGuess, playing, secWord)
            guessedLetters(wrongGuesses, userGuess, wrongLetters)
            printBoardGame(secWordList)
        playing = playingAgain()


def gettingSecretWord():
    secWord = input("Please enter the word you would like to be guessed! ")
    secWord = secWord.lower()

    return secWord


def space():
    print("\n" * 10)


def copySecretLetterList(secWord):
    secWordList = []
    for letter in secWord:
        if letter != "":
            letter = "_"
            secWordList.append(letter)
        else:
            letter = " "
            secWordList.append(letter)

    return secWordList


def printBoardGame(secWordList):
    blankLetterList = secWordList
    for letter in blankLetterList:
        print(letter, end=" ")


def takeGuess():
    print("\n\n===============================")
    userGuess = input("\nWhat letter is in the word/phrase? ")
    userGuess = userGuess.lower()

    return userGuess


def checkGuess(secWord, userGuess, blankLetterList, wrongGuess):
    compareList = list(secWord)
    playing = True
    i = 0
    for x in compareList:
        if userGuess == compareList[i]:
            blankLetterList[i] = compareList[i]
            i += 1
            wrongGuesses = False
        elif userGuess not in compareList:
            i += 1
            wrongGuesses = True
        else:
            i += 1
            wrongGuesses = False

    if wrongGuesses == True and playing != False:
        wrongGuess += 1
        print(f"That is a total of {wrongGuess} wrong guesses!")
    elif wrongGuesses != True:
        print(f"You have {5 - wrongGuess} wrong guesses left!")

    return wrongGuess, wrongGuesses


def guessedLetters(wronguesses, userGuess, wrongLetters):
    userGuess = userGuess.upper()
    if wronguesses == True:
        wrongLetters.append(userGuess)

    print("Your Wrong Choices are: " f'{*wrongLetters,}')


def defineLosing(blankLetterList, wrongGuess, checking, secWord):
    if "_" not in blankLetterList:
        print("You won!  Great job guessing the letters!")
        checking = False
    elif wrongGuess == 5:
        secWord = secWord.upper()
        print(f'The word we were shooting for was: {secWord}.')
        print("Better luck next time!")
        checking = False
    else:
        checking = True

    return checking


def playingAgain():
    retry = input("\nDo you want to play another game? Y or N: ")
    retry = retry.upper()

    HangmanApp() if retry == "Y" else exit()


HangmanApp()

