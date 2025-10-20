# chopsticks stockfish

# representation of both players' hands
oneHands = [1, 1]  # [left, right]
twoHands = [1, 1]
botHands = [1, 1]
position = str(oneHands+twoHands+botHands) # position is the current game position in one variable

# bot instructions
def botTurn(position):
    # Open positions file
    # Find line that contains the sum of the position
    # Read a few characters further to get the line that is the beginning of the section of possible positions with that sum
    # Find the current position in that section
    # Read a few characters further to get the number that represents best move for the bot to make
    #sum(position)

# function for player one's turn
def oneTurn():
    move = input("Player One's move: hit left (hl), hit right (hr)\n")
    if move == "hr":
        if twoHands[1] >= 5:
            print("nice try buddy, you already got rid of that")
            return oneTurn()
        else:
            hand = input(f"Which hand will you use? Your left hand (lh): {oneHands[0]} or your right hand (rh): {oneHands[1]}?\n")
            if hand == "lh":
                if oneHands[0] >= 5:
                    print("you already lost that hand, go again")
                    return oneTurn()
                else:
                    twoHands[1] += oneHands[0]
            elif hand == "rh":
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
    elif move == "hl":
        if twoHands[0] >= 5:
            print("nice try buddy, you already got rid of that")
            return oneTurn()
        else:
            hand = input(f"Which hand will you use? Your left hand (lh): {oneHands[0]} or your right hand (rh): {oneHands[1]}?\n")
            if hand == "lh":
                if oneHands[0] >= 5:
                    print("you already lost that hand, go again")
                    return oneTurn()
                else:
                    twoHands[0] += oneHands[0]
            elif hand == "rh":
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
    move = input("Player Two's move: hit left (hl), hit right (hr)\n")
    if move == "hr":
        if oneHands[1] >= 5:
            print("nice try buddy, you already got rid of that")
            return twoTurn()
        else:
            hand = input(f"Which hand will you use? Your left hand (lh): {twoHands[0]} or your right hand (rh): {twoHands[1]}?\n")
            if hand == "lh":
                if twoHands[0] >= 5:
                    print("you already lost that hand, go again")
                    return twoTurn()
                else:
                    oneHands[1] += twoHands[0]
            elif hand == "rh":
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
    elif move == "hl":
        if oneHands[0] >= 5:
            print("nice try buddy, you already got rid of that")
            return twoTurn()
        else:
            hand = input(f"Which hand will you use? Your left hand (lh): {twoHands[0]} or your right hand (rh): {twoHands[1]}?\n")
            if hand == "lh":
                if twoHands[0] >= 5:
                    print("you already lost that hand, go again")
                    return twoTurn()
                else:
                    oneHands[0] += twoHands[0]
            elif hand == "rh":
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
    twoHands = [1, 1]
    #positionsFile = open("chopPositions.txt", "r")
elif botOrNot == "player":
    botOpp = False
    botHands = [1, 1]
else:
    print('invalid input, try again')
    quit()

if botOpp == True:
    while sum(oneHands) < 10 and sum(botHands) < 10:
        print(f'Player One: {oneHands} \nBot: {botHands}')
        oneTurn()
        winConditionCheck()
        print(f'Player One: {oneHands} \nBot: {botHands}')
        position = str(oneHands+botHands)
        botTurn()
        winConditionCheck()

if botOpp == False:
    while sum(oneHands) < 10 and sum(twoHands) < 10:
        print(f'Player One: {oneHands} \nPlayer Two: {twoHands}')
        oneTurn()
        winConditionCheck()
        print(f'Player One: {oneHands} \nPlayer Two: {twoHands}')
        twoTurn()
        winConditionCheck()