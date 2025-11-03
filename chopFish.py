# chopsticks stockfish

import random

# representation of both players' hands
oneHands = [1, 1]  # [left, right]
twoHands = [1, 1]
botHands = [1, 1]
botHands1 = [1, 1]
botHands2 = [1, 1]
firstTurn = 'Hand One'
turn = 1
botGame=[f'Game Start:', f'Hand 1', botHands1, f'Hand 2', botHands2, f'{firstTurn} goes first']
print(*botGame)
# bot instructions
def botOneTurn():
    botMove = random.choice(['1', '2', '3', '4'])
    if botMove == '1':
        if botHands1[0] >= 5:
            pass
        elif botHands2[0] >= 5:
            pass
        else:
            botHands2[0] += botHands1[0]
            if botHands2[0] >= 5:
                botHands2[0] = 5
    elif botMove == '2':
        if botHands1[0] >= 5:
            pass
        elif botHands2[1] >= 5:
            pass
        else:
            botHands2[1] += botHands1[0]
            if botHands2[1] >= 5:
                botHands2[1] = 5
    elif botMove == '3':
        if botHands1[1] >= 5:
            pass
        elif botHands2[0] >= 5:
            pass
        else:
            botHands2[0] += botHands1[1]
            if botHands2[0] >= 5:
                botHands2[0] = 5
    elif botMove == '4':
        if botHands1[1] >= 5:
            pass
        elif botHands2[1] >= 5:
            pass
        else:
            botHands2[1] += botHands1[1]
            if botHands2[1] >= 5:
                botHands2[1] = 5

def botTwoTurn():
    botMove = random.choice(['1', '2', '3', '4'])
    if botMove == '1':
        if botHands2[0] >= 5:
            pass
        elif botHands1[0] >= 5:
            pass
        else:
            botHands1[0] += botHands2[0]
            if botHands1[0] >= 5:
                botHands1[0] = 5
    elif botMove == '2':
        if botHands2[0] >= 5:
            pass
        elif botHands1[1] >= 5:
            pass
        else:
            botHands1[1] += botHands2[0]
            if botHands1[1] >= 5:
                botHands1[1] = 5
    elif botMove == '3':
        if botHands2[1] >= 5:
            pass
        elif botHands1[0] >= 5:
            pass
        else:
            botHands1[0] += botHands2[1]
            if botHands1[0] >= 5:
                botHands1[0] = 5
    elif botMove == '4':
        if botHands2[1] >= 5:
            pass
        elif botHands1[1] >= 5:
            pass
        else:
            botHands1[1] += botHands2[1]
            if botHands1[1] >= 5:
                botHands1[1] = 5

def botSim():
    firstTurn = 'Hand One'
    while sum(botHands1) < 10 and sum(botHands2) < 10:
        if firstTurn == 'Hand One':
            botOneTurn()
            botTwoTurn()
        elif firstTurn == 'Hand Two':
            botTwoTurn()
            botOneTurn()
        turn += 1
        botGame.append(f'Turn {turn}:', f'Hand 1', botHands1, f'Hand 2', botHands2)

# function for player one's turn
def oneTurn():
    move = input("Player One's move: hit left (1), hit right (2)\n")
    if move == "2":
        if twoHands[1] >= 5:
            print("nice try buddy, you already got rid of that")
            return oneTurn()
        else:
            hand = input(f"Which hand will you use? Your left hand (1): {oneHands[0]} or your right hand (2): {oneHands[1]}?\n")
            if hand == "1":
                if oneHands[0] >= 5:
                    print("you already lost that hand, go again")
                    return oneTurn()
                else:
                    twoHands[1] += oneHands[0]
            elif hand == "2":
                if oneHands[1] >= 5:
                    print("you already lost that hand, go again")
                    return oneTurn()
                else:
                    twoHands[1] += oneHands[1]
            else:
                print("try again")
                return oneTurn()
            if twoHands[1] >= 5:
                print("hand lost")
                twoHands[1] = 5
    elif move == "1":
        if twoHands[0] >= 5:
            print("nice try buddy, you already got rid of that")
            return oneTurn()
        else:
            hand = input(f"Which hand will you use? Your left hand (1): {oneHands[0]} or your right hand (2): {oneHands[1]}?\n")
            if hand == "1":
                if oneHands[0] >= 5:
                    print("you already lost that hand, go again")
                    return oneTurn()
                else:
                    twoHands[0] += oneHands[0]
            elif hand == "2":
                if oneHands[1] >= 5:
                    print("you already lost that hand, go again")
                    return oneTurn()
                else:
                    twoHands[0] += oneHands[1]
            else:
                print("try again")
                return oneTurn()
            if twoHands[0] >= 5:
                print("hand lost")
                twoHands[0] = 5
    else:
        print("try again")
        return oneTurn()

# function for player two's turn
def twoTurn():
    move = input("Player Two's move: hit left (1), hit right (2)\n")
    if move == "2":
        if oneHands[1] >= 5:
            print("nice try buddy, you already got rid of that")
            return twoTurn()
        else:
            hand = input(f"Which hand will you use? Your left hand (1): {twoHands[0]} or your right hand (2): {twoHands[1]}?\n")
            if hand == "1":
                if twoHands[0] >= 5:
                    print("you already lost that hand, go again")
                    return twoTurn()
                else:
                    oneHands[1] += twoHands[0]
            elif hand == "2":
                if twoHands[1] >= 5:
                    print("you already lost that hand, go again")
                    return twoTurn()
                else:
                    oneHands[1] += twoHands[1]
            else:
                print("try again")
                return twoTurn()
            if oneHands[1] >= 5:
                print("hand lost")
                oneHands[1] = 5
    elif move == "1":
        if oneHands[0] >= 5:
            print("nice try buddy, you already got rid of that")
            return twoTurn()
        else:
            hand = input(f"Which hand will you use? Your left hand (1): {twoHands[0]} or your right hand (2): {twoHands[1]}?\n")
            if hand == "1":
                if twoHands[0] >= 5:
                    print("you already lost that hand, go again")
                    return twoTurn()
                else:
                    oneHands[0] += twoHands[0]
            elif hand == "2":
                if twoHands[1] >= 5:
                    print("you already lost that hand, go again")
                    return twoTurn()
                else:
                    oneHands[0] += twoHands[1]
            else:
                print("try again")
                return twoTurn()
            if oneHands[0] >= 5:
                print("hand lost")
                oneHands[0] = 5
    else:
        print("try again")
        return twoTurn()

# function to check if a player won
def winConditionCheck():
    if botOpp == True:
        if sum(oneHands) >= 10:
            print("game over, bot won")
            quit()
    if sum(oneHands) >= 10:
        print("game over, player two won")
        quit()
    if sum(twoHands) >= 10:
        print("game over, player one won")
        quit()
    if sum(botHands) >= 10:
        print("game over, player one won")
        quit()

# main game loop
botOrNot = input("Would you like to play against a bot (bot) or another player (player)?\n").lower()
if botOrNot == "bot":
    botOpp = True
    #positionsFile = open("chopPositions.txt", "r")
    botSim()
    # while sum(botHands1) < 10 and sum(botHands2) < 10:
    #     print(f'Player One: {botHands1} \nBot: {botHands2}')
    #     botTurn()
    #     winConditionCheck()
    #     print(f'Player One: {botHands1} \nBot: {botHands2}')
    #     position = str(botHands1 + botHands2)
    #     botTurn()
    #     winConditionCheck()
elif botOrNot == "player":
    botOpp = False
    while sum(oneHands) < 10 and sum(twoHands) < 10:
        print(f'Player One: {oneHands} \nPlayer Two: {twoHands}')
        oneTurn()
        winConditionCheck()
        print(f'Player One: {oneHands} \nPlayer Two: {twoHands}')
        twoTurn()
        winConditionCheck()
else:
    print('invalid input, try again')
    quit()