import random


def TicTacToe():
    playing = True
    gameOver = False
    sol = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    playerOne, playerTwo = determinePlayernames()
    currentPlay = pickingPlayerOrder(playerOne, playerTwo)
    piece = assigningXO(currentPlay)
    initalBoard(sol)

    while playing == True:
        userTurn = playerMove(currentPlay, sol)
        updatedBoard = updateBoard(userTurn, piece, sol)
        scoreBoard(updatedBoard)
        gameOver = gameDraw(sol)
        if gameOver == True:
            break
        playing = xoWinner(sol)
        if playing == False:
            declareVictory(currentPlay)
            break
        currentPlay = switchNames(currentPlay, playerOne, playerTwo)
        piece = switchTurns(piece)
    playAgain()


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
    playerOne = input("Player One: What is your name?: \n")
    playerOne = playerOne.title()
    print()
    playerTwo = input("Player Two: What is your name?: \n")
    playerTwo = playerTwo.title()
    print()

    return playerOne, playerTwo


def pickingPlayerOrder(playerOne, playerTwo):
    order = random.randint(1, 2)

    currentPlay = playerOne if order == 1 else playerTwo
    print(f"{currentPlay} gets to go first!\n")

    return currentPlay


def assigningXO(firstPlay):
    assigning = int(input(
        f"{firstPlay} which would you like to play with:\n\n1. X's\n2. O's\n"))

    piece = "X" if assigning == 1 else "O"

    return piece


def playerMove(currentPlay, sol):
    print(f"\nAlright, {currentPlay}, It is your turn!")
    while True:
        try:
            userTurn = int(input("\nWhere would you like to play?: \n"))
            if userTurn not in sol:
                print("\nThat number was already taken!\n")
            else:
                if userTurn < 1 or userTurn > 9:
                    print("\nPick a number in range 1-9!\n")
                else:
                    break
        except:
            print("\nThat is not a number! Try again!\n")

    return userTurn


def updateBoard(userTurn, piece, sol):
    for x in sol:
        if userTurn == x:
            sol[x - 1] = piece

    return sol


def switchTurns(piece):
    piece = piece
    piece = "O" if piece == "X" else "X"

    return piece


def switchNames(currentPlay, playerOne, playerTwo):
    currentPlay = playerTwo if currentPlay != playerTwo else playerOne

    return currentPlay


def xoWinner(sol):
    solutions = [[sol[0], sol[1], sol[2]], [sol[3], sol[4], sol[5]], [sol[6], sol[7], sol[8]], [sol[0], sol[3], sol[6]], [
        sol[1], sol[4], sol[7]], [sol[2], sol[5], sol[8]], [sol[0], sol[4], sol[8]], [sol[2], sol[4], sol[6]]]

    oWinner = [["O", "O", "O"]]
    xWinner = [["X", "X", "X"]]

    winnerY = [x for x in solutions if any(
        x == y for y in oWinner)]

    winnerX = [x for x in solutions if any(
        x == y for y in xWinner)]

    playing = False if winnerY != [] else False if winnerX != [] else True

    return playing


def gameDraw(sol):
    gameOver = False
    playing = True
    draw = [x for x in range(1, 10)]

    newDraw = [x for x in draw if any(x == y for y in sol)]

    gameOver = True if newDraw == [] else False
    print("This game was a draw!  Neither player WON or LOST!\n") if gameOver == True else print()

    return gameOver


def declareVictory(currentPlay):
    print(f"{currentPlay}, You win!\n")


def playAgain():
    try:
        retry = input("Do you want to play again? (Y or N): \n")
        retry = retry.upper()
    except:
        print("You need to be more clear!\n")

    TicTacToe() if retry == "Y" else (
        exit() if retry == "N" else print("That didn't work.\n"))


if __name__ == "__main__":
    TicTacToe()

