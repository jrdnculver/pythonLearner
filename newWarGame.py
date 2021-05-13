import random

suit = "H,S,D,C".split(",")
number = [x for x in range(2, 11)] + "J,Q,K,A".split(",")


def warGame():
    warring = True
    i = 0

    simulator = input("Do you want to simulate the game? (Y or N): ")
    simulator = simulator.upper()
    if simulator == "Y":
        simulation = True
    else:
        simulation = False

    rounds = numRounds()
    deck = Deck()
    shuffleDeck(deck)
    playerOneHand, playerTwoHand = passCards(deck)
    totalRounds = 0
    while warring == True:
        playerOneCard, playerTwoCard, p1Card, p2Card, i = displayCard(
            playerOneHand, playerTwoHand, i)
        pOneValue, pTwoValue = findWinner(playerOneCard, playerTwoCard)
        oneScore = playerOneScore(pOneValue)
        twoScore = playerTwoScore(pTwoValue)
        totalRounds += 1
        evaluateScores(oneScore, twoScore, playerOneHand,
                       playerTwoHand, playerOneCard, playerTwoCard, p1Card, p2Card, pOneValue, pOneValue, i, totalRounds)
        warring, playerOneWinner, playerTwoWinner = determineWinner(
            playerOneHand, playerTwoHand,  oneScore, twoScore, i, totalRounds, rounds)
        if simulation == False:
            dealIt = input("Do you want to continue? (Y or N):  ")
            print()
            dealIt = dealIt.upper()
            if dealIt == "Y":
                continue
            else:
                warring = False
    announceWinner(playerOneWinner, playerTwoWinner,
                   totalRounds, playerOneHand, playerTwoHand)
    print()
    print(playerOneHand, "\n", playerTwoHand)
    playAgain()


def Deck():
    # Creating the deck values
    deck = []
    for suitType in suit:
        for value in number:
            card = (f"{value} of {suitType}")
            deck.append(card)

    return deck


def shuffleDeck(deck):
    # Shuffling deck
    random.shuffle(deck)

    return deck


def passCards(deck):
    # Distibuting cards to players
    playerOneHand = deck[0::2]
    playerTwoHand = deck[1::2]

    return playerOneHand, playerTwoHand

# Displaying cards, determining number of cards in hand and indexing for the ability to exchange cards per turn


def displayCard(playerOneHand, playerTwoHand, i):
    # If I reaches the end of player hand length, i will be reset to zero
    lengthOne = len(playerOneHand)
    lengthTwo = len(playerTwoHand)

    if i >= lengthOne:
        i = 0
    elif i >= lengthTwo:
        i = 0
    else:
        i = i

    playerOneCard = f"PlayerOne Card: {playerOneHand[i]}"
    print(playerOneCard)
    p1Card = playerOneHand[i]
    playerTwoCard = f"PlayerTwo Card: {playerTwoHand[i]}"
    print(playerTwoCard)
    p2Card = playerTwoHand[i]
    i += 1
    print()

    return playerOneCard, playerTwoCard, p1Card, p2Card, i


def findWinner(playerOneCard, playerTwoCard):
    # Splits and strips, then indexes to get values from each card for scoring purposes
    pOneValue = playerOneCard.split(":")
    pOneValue[1].strip()
    pTwoValue = playerTwoCard.split(":")
    pTwoValue[1].strip()
    pOneValue = pOneValue[1][1]
    pTwoValue = pTwoValue[1][1]

    return pOneValue, pTwoValue


def playerOneScore(pOneValue):
    # Set score for player One
    if pOneValue == "J":
        oneScore = 11
    elif pOneValue == "Q":
        oneScore = 12
    elif pOneValue == "K":
        oneScore = 13
    elif pOneValue == "A":
        oneScore = 14
    elif int(pOneValue) == 1:
        oneScore = 10
    elif int(pOneValue) in range(2, 10):
        oneScore = int(pOneValue)
    return oneScore


def playerTwoScore(pTwoValue):
    # Set score for player Two
    if pTwoValue == "J":
        twoScore = 11
    elif pTwoValue == "Q":
        twoScore = 12
    elif pTwoValue == "K":
        twoScore = 13
    elif pTwoValue == "A":
        twoScore = 14
    elif int(pTwoValue) == 1:
        twoScore = 10
    elif int(pTwoValue) in range(2, 10):
        twoScore = int(pTwoValue)
    return twoScore

# Comparing scores, editing hands depending on wins and losses by adding card to winners hand and removing card from losers hand.
# Also, handles tie breaker through another WAR.


def evaluateScores(oneScore, twoScore, playerOneHand, playerTwoHand, playerOneCard, playerTwoCard, p1Card, p2Card, pOneValue, pTwoValue, i, totalRounds):
    if int(oneScore) > int(twoScore):
        print("Player One wins the round!")
        playerOneHand.append(p2Card)
        playerTwoHand.remove(p2Card)
    elif int(oneScore) < int(twoScore):
        print("Player Two wins the round!")
        playerTwoHand.append(p1Card)
        playerOneHand.remove(p1Card)
    else:
        print("The cards are the same, this is WAR!")


def determineWinner(playerOneHand, playerTwoHand, oneScore, twoScore, i, totalRounds, rounds):
    # Determines the final winner of the game.
    if len(playerOneHand) == 3:
        playerOneWinner = False
        playerTwoWinner = True
        playing = False
    elif len(playerTwoHand) == 3:
        playerOneWinner = True
        playerTwoWinner = False
        playing = False
    else:
        if totalRounds == rounds:
            playing = False
            if len(playerOneHand) > len(playerTwoHand):
                playerOneWinner = True
                playerTwoWinner = False
            else:
                len(playerTwoHand) > len(playerOneHand)
                playerOneWinner = False
                playerTwoWinner = True
        else:
            playing = True
            playerOneWinner = False
            playerTwoWinner = False

    return playing, playerOneWinner, playerTwoWinner


def announceWinner(playerOneWinner, playerTwoWinner, totalRounds, playerOneHand, playerTwoHand):
    # Final output to declare victory
    if playerOneWinner == True:
        print("Player One is the winner! Great Game!")
        print(
            f"He won in {totalRounds} total rounds and having a total of {len(playerOneHand)} cards!")
    else:
        print("Player Two is the winner! Great Game!")
        print(
            f"He won in {totalRounds} total rounds and having a total of {len(playerTwoHand)} cards!")


def simulation():
    simulator = input("Do you want to simulate the game? (Y or N): ")
    simulator.upper()

    return simulator


def dealAgain(simulator):
    dealIt = input("Do you want to play another hand?")
    dealIt.upper()
    if dealIt == "Y":
        playing = True
    else:
        playing = False

    return playing


def numRounds():
    rounds = int(
        input("How many Max rounds do you want to play? "))

    return rounds


def playAgain():
    retry = input("Do you want to play again? (Y or N): ")
    retry = retry.upper()

    if retry == "Y":
        warGame()
    else:
        pass


warGame()
