import random

# List of numbers to sequence
numbers = []


def searching():
    findAnother = True

    maxNumber = sequence()
    print(numbers)
    while findAnother == True:
        search = searchFor(maxNumber)
        midPoint = searchAlgorithm(numbers, search)
        findAnother = finalAnswer(midPoint)

# Create sequence for algorithm


def sequence():
    while True:
        try:
            numSequence = int(
                input("How many numbers do you want in the list?: "))
            break
        except:
            print("That is not a valid input.  Please type a number!")
    maxNumber = numSequence * 100
    i = 1
    while i <= numSequence:
        number = random.randint(0, maxNumber)
        if number not in numbers:
            numbers.append(number)
            i += 1

    numbers.sort()

    return maxNumber

# Determine the number to search for


def searchFor(maxNumber):
    print(f"A number from 0 to {maxNumber} could be in the list!\n")
    search = int(input("What number do you want to search for?: "))

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


def finalAnswer(midPoint):
    if midPoint != None:
        print(f"The midpoint was at index {midPoint}")
        print(f"The final number found was {numbers[midPoint]}")
    else:
        print("That value was not in the list")
        guessAnother = tryAnother()

    return guessAnother


def tryAnother():
    retry = input("Would you like to find another value in the same list?")
    retry = retry.upper()

    if retry == "Y":
        guessAnother = True
    else:
        guessAnother = False

    return guessAnother


if __name__ == "__main__":
    searching()
