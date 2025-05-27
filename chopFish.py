# chopsticks stockfish
hand=1
# def hit(hand):
#     hand=hand+1
while hand<5:
    move=input("your move: ")
    if move=="hit":
        # hit(hand)
        hand=hand+1
        print(hand)
if hand>=5:
    print("hand lost")