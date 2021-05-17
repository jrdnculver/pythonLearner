import random

# List of numbers to sequence


def searching():
    findAnother = True

    numRange, randomList = sequence()
    while findAnother == True:
        search = searchFor(numRange)
        midPoint = searchAlgorithm(randomList, search)
        findAnother = finalAnswer(midPoint, randomList)

# Create sequence for algorithm


def sequence():
    while True:
        try:
            numSequence = int(
                input("How many numbers do you want in the list?: \n"))
            numRange = int(
                input("What is the high range you want of a random number?\n"))
            break
        except:
            print("That is not a valid input.  Please type a number!\n")
    maxNumber = numSequence
    randomList = random.sample(range(0, numRange), maxNumber)

    randomList.sort()

    return numRange, randomList

# Determine the number to search for


def searchFor(numRange):
    print(f"A number from 0 to {numRange} could be in the list!\n")
    search = int(input("What number do you want to search for?: \n"))

    return search


def searchAlgorithm(numbers, search):
    startIndex = 0
    endIndex = len(numbers) - 1

    while startIndex <= endIndex:
        midPoint = startIndex + (endIndex - startIndex) // 2
        midPointValue = numbers[midPoint]

        if midPointValue == search:
            return midPoint
        elif search < midPointValue:
            endIndex = midPoint - 1

        else:
            startIndex = midPoint + 1

    return None


def finalAnswer(midPoint, randomList):
    if midPoint != None:
        print(f"The midpoint was at index {midPoint}")
        print(f"The final number found was {randomList[midPoint]}")
    else:
        print("That value was not in the list")

    guessAnother = tryAnother()

    return guessAnother


def tryAnother():
    retry = input("Would you like to find another value in the same list?\n")
    retry = retry.upper()

    if retry == "Y":
        guessAnother = True
    else:
        guessAnother = False

    return guessAnother


if __name__ == "__main__":
    searching()
