# chopsticks stockfish

import random
import json

# representation of both players' hands
oneHands = [1, 1]  # [left, right]
twoHands = [1, 1]
botHands = [1, 1]
botHands1 = [1, 1]
botHands2 = [1, 1]
firstTurn = 'Hand One'
turn = 0.5
botGame=[f'Game Start:', f'Hand 1', f'{botHands1}', f'Hand 2', f'{botHands2}', f'{firstTurn} goes first']

# bot instructions
def botSimTurn(attacker, defender):
    botMove = random.choice(['1', '2', '3', '4'])
    attackerHand = 0 if botMove in ['1', '2'] else 1
    defenderHand = 0 if botMove in ['1', '3'] else 1
    if attacker[attackerHand] < 5 and defender[defenderHand] < 5:
        defender[defenderHand] += attacker[attackerHand]
        if defender[defenderHand] >= 5:
            defender[defenderHand] = 5
    else:
        botSimTurn(attacker, defender)

# bot sim main function
def botSim(firstTurn='Hand One'):
    global turn
    current_player = firstTurn
    while sum(botHands1) < 10 and sum(botHands2) < 10:
        if current_player == 'Hand One':
            botSimTurn(botHands1, botHands2)
            current_player = 'Hand Two'
        else:
            botSimTurn(botHands2, botHands1)
            current_player = 'Hand One'
        turn += 0.5
        botGame.extend([f'Turn {turn}: Hand 1 {botHands1}, Hand 2 {botHands2}'])
    print(*botGame)

# function for player one's turn
def playerTurn(attacker, defender, playerName):
    move = input(f"{playerName}'s move: hit left (1), hit right (2)\n")
    if move not in ['1', '2']:
        print('try again')
        return playerTurn(attacker, defender, playerName)
    targetHand = 0 if move == '1' else 1
    if defender[targetHand] >= 5:
        print('nice try buddy, you already got rid of that')
        return playerTurn(attacker, defender, playerName)
    hand = input(f'Which hand will you use? Your left hand (1): {attacker[0]} or your right hand (2): {attacker[1]}?\n')
    if hand not in ['1', '2']:
        print('try again')
        return playerTurn(attacker, defender, playerName)
    attackingHand = 0 if hand == '1' else 1
    if attacker[attackingHand] >= 5:
        print('you already lost that hand, go again')
        return playerTurn(attacker, defender, playerName)
    defender[targetHand] += attacker[attackingHand]
    if defender[targetHand] >= 5:
        print('hand lost')
        defender[targetHand] = 5

# function to check if a player won
def winConditionCheck():
    if botOpp == True:
        if sum(oneHands) >= 10:
            print('game over, bot won')
            quit()
    if sum(oneHands) >= 10:
        print('game over, player two won')
        quit()
    if sum(twoHands) >= 10:
        print('game over, player one won')
        quit()
    if sum(botHands) >= 10:
        print('game over, player one won')
        quit()

# main game loop
while True:
    botOrNot = input('Would you like to play against a bot (bot) or another player (player)?\n').lower()
    if botOrNot in ['bot', 'player']:
        break
    print('invalid input, try again')
if botOrNot == 'bot':
    botOpp = True
    #positionsFile = open('chopPositions.txt', 'r')
    botSim()
    # while sum(botHands1) < 10 and sum(botHands2) < 10:
    #     print(f'Player One: {botHands1} \nBot: {botHands2}')
    #     botTurn()
    #     winConditionCheck()
    #     print(f'Player One: {botHands1} \nBot: {botHands2}')
    #     position = str(botHands1 + botHands2)
    #     botTurn()
    #     winConditionCheck()
elif botOrNot == 'player':
    botOpp = False
    while sum(oneHands) < 10 and sum(twoHands) < 10:
        print(f'Player One: {oneHands} \nPlayer Two: {twoHands}')
        playerTurn(oneHands, twoHands, 'Player One')
        winConditionCheck()
        print(f'Player One: {oneHands} \nPlayer Two: {twoHands}')
        playerTurn(twoHands, oneHands, 'Player Two')
        winConditionCheck()