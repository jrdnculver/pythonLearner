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
        if piece == "X":
            playing = xWinner(currentPlay, xplayerCard)
        else:
            playing = oWinner(currentPlay, oplayerCard)
        if playing == False:
            declareVictory(currentPlay)
            playAgain()
            break
        playing = gameDraw(oplayerCard, xplayerCard)
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
    print(xplayerCard, oplayerCard)

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


def xWinner(currentPlay, xplayerCard):
    solutions = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],
                 [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    playing = True
    xplayerCard.sort()
    i = 0
    while True:
        if xplayerCard[0:3] == solutions[i]:
            playing = False
            break
        elif xplayerCard[1:4] == solutions[i]:
            playing = False
            break
        elif xplayerCard[2:5] == solutions[i]:
            playing = False
            break
        else:

            i += 1
            if i == len(solutions):
                break
    return playing


def oWinner(currentPlay, oplayerCard):
    solutions = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],
                 [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    playing = True
    oplayerCard.sort()
    i = 0
    while True:
        if oplayerCard[0:3] == solutions[i]:
            playing = False
            break
        elif oplayerCard[1:4] == solutions[i]:
            playing = False
            break
        elif oplayerCard[2:5] == solutions[i]:
            playing = False
            break
        else:
            i += 1
            if i == len(solutions):
                break
    return playing


def gameDraw(oplayerCard, xplayerCard):
    if len(oplayerCard) + len(xplayerCard) == 9:
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


TicTacToe()
