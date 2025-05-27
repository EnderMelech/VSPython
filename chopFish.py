# chopsticks stockfish
leftHand=1
rightHand=1
hands=[leftHand,rightHand]
while sum(hands)<10:
    move=input("your move: hit left (hl), hit right (hr)\n")
    if move=="hr":
        if rightHand>=5:
            print("nice try buddy, you already got rid of that")
        elif rightHand<5:
            rightHand=rightHand+1
            if rightHand==5:
                print("hand lost")
    elif move=="hl":
        if leftHand>=5:
            print("nice try buddy, you already got rid of that")
        elif leftHand<5:
            leftHand=leftHand+1
            if leftHand==5:
                print("hand lost")
    else:
        print("try again")
    hands=[leftHand,rightHand]
    print(hands)
if sum(hands)>=10:
    print("game over")