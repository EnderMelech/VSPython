# chopsticks stockfish
oneLeftHand=1
twoLeftHand=1
oneRightHand=1
twoRightHand=1
#oneHands=f'{str(oneLeftHand)}, {str(oneRightHand)}'
#twoHands=f'{str(twoLeftHand)}, {str(twoRightHand)}'
oneHands=[oneLeftHand,oneRightHand]
twoHands=[twoLeftHand,twoRightHand]
hands=f'Player One: {str(oneHands)} \nPlayer Two: {str(twoHands)}'
def oneTurn():
    global oneLeftHand
    global twoLeftHand
    global oneRightHand
    global twoRightHand
    global oneHands
    global twoHands
    global hands
    move=input("Player One's move: hit left (hl), hit right (hr)\n")
    if move=="hr":
        if twoRightHand>=5:
            print("nice try buddy, you already got rid of that")
        else:
            move=input(f"Which hand will you use? Your left hand (lh): {oneLeftHand} or your right hand (rh): {oneRightHand}?")
            if move=="lh":
                twoRightHand=twoRightHand+oneLeftHand
            elif move=="rh":
                twoRightHand=twoRightHand+oneRightHand
            else:
                print("try again")
            if twoRightHand==5:
                print("hand lost")
    elif move=="hl":
        if twoLeftHand>=5:
            print("nice try buddy, you already got rid of that")
        else:
            move=input(f"Which hand will you use? Your left hand (lh): {oneLeftHand} or your right hand (rh): {oneRightHand}?")
            if move=="lh":
                twoLeftHand=twoLeftHand+oneLeftHand
            elif move=="rh":
                twoLeftHand=twoLeftHand+oneRightHand
            if twoLeftHand==5:
                print("hand lost")
    else:
        print("try again")
    oneHands=[oneLeftHand,oneRightHand]
    twoHands=[twoLeftHand,twoRightHand]
    hands=f'Player One: {str(oneHands)} \nPlayer Two: {str(twoHands)}'
def twoTurn():
    global oneLeftHand
    global twoLeftHand
    global oneRightHand
    global twoRightHand
    global oneHands
    global twoHands
    global hands
    move=input("Player Two's move: hit left (hl), hit right (hr)\n")
    if move=="hr":
        if oneRightHand>=5:
            print("nice try buddy, you already got rid of that")
        else:
            move=input(f"Which hand will you use? Your left hand (lh): {twoLeftHand} or your right hand (rh): {twoRightHand}?")
            if move=="lh":
                oneRightHand=oneRightHand+twoLeftHand
            elif move=="rh":
                oneRightHand=oneRightHand+twoRightHand
            else:
                print("try again")
            if oneRightHand==5:
                print("hand lost")
    elif move=="hl":
        if oneLeftHand>=5:
            print("nice try buddy, you already got rid of that")
        else:
            move=input(f"Which hand will you use? Your left hand (lh): {twoLeftHand} or your right hand (rh): {twoRightHand}?")
            if move=="lh":
                oneLeftHand=oneLeftHand+twoLeftHand
            elif move=="rh":
                oneLeftHand=oneLeftHand+twoRightHand
            if oneLeftHand==5:
                print("hand lost")
    else:
        print("try again")
    oneHands=[oneLeftHand,oneRightHand]
    twoHands=[twoLeftHand,twoRightHand]
    hands=f'Player One: {str(oneHands)} \nPlayer Two: {str(twoHands)}'
while sum(oneHands)<10 and sum(twoHands)<10:
    oneTurn()
    print(hands)
    twoTurn()
    print(hands)
if sum(oneHands)>=10:
    print("game over")
if sum(twoHands)>=10:
    print("game over")