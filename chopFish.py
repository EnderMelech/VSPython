# chopsticks stockfish
oneHands = [1, 1]  # [left, right]
twoHands = [1, 1]  # [left, right]

def oneTurn():
    global oneHands, twoHands
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

def twoTurn():
    global oneHands, twoHands
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

def winConditionCheck():
    if sum(oneHands) >= 10:
        print("game over, player two won")
        quit()
    if sum(twoHands) >= 10:
        print("game over, player one won")
        quit()

while sum(oneHands) < 10 and sum(twoHands) < 10:
    print(f'Player One: {oneHands} \nPlayer Two: {twoHands}')
    oneTurn()
    winConditionCheck()
    print(f'Player One: {oneHands} \nPlayer Two: {twoHands}')
    twoTurn()
    winConditionCheck()