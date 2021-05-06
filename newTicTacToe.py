import random


def TicTacToe():
    playing = True
    sol = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    xplayerCard = []
    oplayerCard = []

    playerOne, playerTwo = determinePlayernames()
    order, currentPlay = pickingPlayerOrder(playerOne, playerTwo)
    piece = assigningXO(order, currentPlay)
    initalBoard(sol)

    while playing == True:
        userTurn, xplayerCard, oplayerCard = playerMove(
            playerOne, playerTwo, currentPlay, piece, xplayerCard, oplayerCard, sol)
        updatedBoard = updateBoard(userTurn, order, piece, sol)
        scoreBoard(updatedBoard)
        xdivideByTwo, odivideByTwo = divisibleByTwo(xplayerCard, oplayerCard)
        xdivideByThree, odivideByThree = divisibleByThree(
            xplayerCard, oplayerCard)
        xdivideByFour, odivideByFour = divisibleByFour(
            xplayerCard, oplayerCard)
        xRandom, xRandomX, oRandom, oRandomO = theRest(
            xplayerCard, oplayerCard)
        playing = xoWinner(xplayerCard, oplayerCard,
                           piece, xdivideByTwo, xdivideByThree,
                           xdivideByFour, odivideByTwo, odivideByThree,
                           odivideByFour, xRandom, xRandomX, oRandom, oRandomO)
        if playing == False:
            declareVictory(currentPlay)
            playAgain()
            break
        playing = gameDraw(xplayerCard, oplayerCard)
        currentPlay = switchNames(currentPlay, playerOne, playerTwo)
        piece = switchTurns(piece)


def initalBoard(sol):
    print("    |     |     ")
    print("  {} |  {}  | {}  ".format(sol[0], sol[1], sol[2]))
    print("----|-----|-----")
    print("  {} |  {}  | {}  ".format(sol[3], sol[4], sol[5]))
    print("----|-----|-----")
    print("  {} |  {}  | {}  ".format(sol[6], sol[7], sol[8]))
    print("    |     |     ")
    print()


def scoreBoard(updatedBoard):
    print("    |     |     ")
    print("  {} |  {}  | {}  ".format(
        updatedBoard[0], updatedBoard[1], updatedBoard[2]))
    print("----|-----|-----")
    print("  {} |  {}  | {}  ".format(
        updatedBoard[3], updatedBoard[4], updatedBoard[5]))
    print("----|-----|-----")
    print("  {} |  {}  | {}  ".format(
        updatedBoard[6], updatedBoard[7], updatedBoard[8]))
    print("    |     |     ")
    print()


def determinePlayernames():
    playerOne = input("Player One: What is your name?: ")
    playerOne = playerOne.title()
    print()
    playerTwo = input("Player Two: What is your name?: ")
    playerTwo = playerTwo.title()
    print()

    return playerOne, playerTwo


def pickingPlayerOrder(playerOne, playerTwo):
    order = random.randint(1, 2)

    if order == 1:
        print(f"{playerOne} gets to go first!\n")
        currentPlay = playerOne
    else:
        print(f"{playerTwo} gets to go first!\n")
        currentPlay = playerTwo

    return order, currentPlay


def assigningXO(order, firstPlay):
    assigning = int(input(
        f"{firstPlay} which would you like to play with:\n1. X's\n2. O's\n"))

    if assigning == 1:
        piece = "X"
    else:
        piece = "O"

    return piece


def playerMove(playerOne, playerTwo, currentPlay, piece, xplayerCard, oplayerCard, sol):
    getTurn = True
    print(f"\nAlright, {currentPlay}, It is your turn!")
    while getTurn == True:
        try:
            userTurn = int(input("\nWhere would you like to play?: "))
            if userTurn not in sol:
                print("\nThat number was already taken!")
                getTurn = True
            else:
                if userTurn < 1 or userTurn > 9:
                    print("\nPick a number in range 1-9!")
                    getTurn = True
                else:
                    getTurn = False
        except:
            print("\nThat is not a number! Try again!")

    card = userTurn - 1
    if piece == "X":
        xplayerCard.append(card)
    else:
        oplayerCard.append(card)

    return userTurn, xplayerCard, oplayerCard


def updateBoard(userTurn, order, piece, sol):
    for x in sol:
        if userTurn == x:
            sol[x - 1] = piece

    return sol


def switchTurns(piece):
    if piece == "X":
        piece = "O"
    else:
        piece = "X"

    return piece


def switchNames(currentPlay, playerOne, playerTwo):
    if currentPlay == playerOne:
        currentPlay = playerTwo
    else:
        currentPlay = playerOne

    return currentPlay


def xoWinner(xplayerCard, oplayerCard, piece, xdivideByTwo, xdivideByThree,
             xdivideByFour, odivideByTwo, odivideByThree, odivideByFour, xRandom, xRandomX, oRandom, oRandomO):
    solutions = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],
                 [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    print(xdivideByFour)
    playing = True
    if piece == "X":
        playerCard = xplayerCard
    else:
        playerCard = oplayerCard
    i = 0
    j = 0
    k = 3
    stopper = 3
    playerCard.sort()

    while True:
        if xdivideByTwo == solutions[i] or xdivideByThree == solutions[i] or xdivideByFour == solutions[i]:
            playing = False
            break
        if odivideByTwo == solutions[i] or odivideByThree == solutions[i] or odivideByFour == solutions[i]:
            playing = False
            break
        if playerCard[0:3] == solutions[i]:
            playing = False
            break
        if i == 7:
            i = 0
            j += 1
            k += 1

        else:
            i += 1
            if j == stopper:
                break

    return playing


def gameDraw(xplayerCard, oplayerCard):
    if len(oplayerCard) + len(xplayerCard) == 9 and playing == True:
        print("This game was a draw!  Neither player WON or LOST!")
        playing = False
    else:
        playing = True

    return playing


def declareVictory(currentPlay):
    print(f"{currentPlay}, You win!")


def playAgain():
    try:
        retry = input("Do you want to play again? (Y or N): ")
        retry = retry.upper()
        if retry == "Y":
            TicTacToe()
        else:
            if retry == "No":
                exit()
    except:
        print("You need to be more clear!")


def divisibleByTwo(xplayerCard, oplayerCard):
    xdivideByTwo = []
    odivideByTwo = []

    for x in xplayerCard:
        if x % 2 == 0:
            xdivideByTwo.append(x)
    for o in oplayerCard:
        if o % 2 == 0:
            odivideByTwo.append(o)

    xdivideByTwo.sort()
    odivideByTwo.sort()

    return xdivideByTwo, odivideByTwo


def divisibleByThree(xplayerCard, oplayerCard):
    xdivideByThree = []
    odivideByThree = []

    for x in xplayerCard:
        if x % 3 == 0:
            xdivideByThree.append(x)
    for o in oplayerCard:
        if o % 3 == 0:
            odivideByThree.append(o)

    xdivideByThree.sort()
    odivideByThree.sort()

    return xdivideByThree, odivideByThree


def divisibleByFour(xplayerCard, oplayerCard):
    xdivideByFour = []
    odivideByFour = []

    for x in xplayerCard:
        if x % 4 == 0:
            xdivideByFour.append(x)
    for o in oplayerCard:
        if o % 4 == 0:
            odivideByFour.append(o)

    xdivideByFour.sort()
    odivideByFour.sort()
    print(xdivideByFour)

    return xdivideByFour, odivideByFour


def theRest(xplayerCard, oplayerCard):
    xRandom = []
    oRandom = []
    xRandomX = []
    oRandomO = []

    for x in xplayerCard:
        if 1 or 4 or 7 in xplayerCard:
            xRandom.append(x + 1)
    for x in xplayerCard:
        if 2 or 5 or 8 in xplayerCard:
            xRandomX.append(x + 1)
    for o in oplayerCard:
        if 1 or 4 or 7 in oplayerCard:
            oRandom.append(o + 1)
    for o in oplayerCard:
        if 2 or 5 or 8 in xplayerCard:
            oRandomO.append(o + 1)

    return xRandom, xRandomX, oRandom, oRandomO


TicTacToe()

