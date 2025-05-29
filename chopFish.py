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
        if oneRightHand>=5:
            print("nice try buddy, you already got rid of that")
        else:
            oneRightHand=oneRightHand+1
            if oneRightHand==5:
                print("hand lost")
    elif move=="hl":
        if oneLeftHand>=5:
            print("nice try buddy, you already got rid of that")
        else:
            oneLeftHand=oneLeftHand+1
            if oneLeftHand==5:
                print("hand lost")
    else:
        print("try again")
oneTurn()
if sum(oneHands)>=10:
    print("game over")
if sum(twoHands)>=10:
    print("game over")
print(hands)