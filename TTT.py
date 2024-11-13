import random

box = [" "] * 9
game = True

def printBoard():
    print(f" {box[0]} | {box[1]} | {box[2]} ")
    print("---|---|---")
    print(f" {box[3]} | {box[4]} | {box[5]} ")
    print("---|---|---")
    print(f" {box[6]} | {box[7]} | {box[8]} ")
    print("-----------------------------------------------")

def Game():
    return " " in box

def possibilities():
    return [i for i, ele in enumerate(box) if ele == " "]

def userGame(user):
    pos = possibilities()
    print("Possible moves:", pos)
    while True:
        move = input("Enter the choice (0-8) where you want to enter your move: ")
        if move.isdigit() and int(move) in pos:
            box[int(move)] = user
            break
        else:
            print("Invalid position!")

def randomMove(user):
    pos = possibilities()
    if pos:
        move = random.choice(pos)
        box[move] = user

def win():
    win_pos = [(0, 1, 2), (3, 4, 5), (6, 7, 8), 
               (0, 3, 6), (1, 4, 7), (2, 5, 8), 
               (0, 4, 8), (2, 4, 6)]
    for x, y, z in win_pos:
        if box[x] == box[y] == box[z] and box[x] != " ":
            return box[x]
    return False

printBoard()
player = ['X', 'O']
user = input("Enter the player 'X' or 'O': ").upper()

while game:
    printBoard()
    if user == 'X':
        userGame(user)
        winner = win()
        if not winner:
            randomMove('O')
            winner = win()
    else:
        randomMove('X')
        winner = win()
        if not winner:
            printBoard()
            userGame(user)
            winner = win()
    
    if winner:
        printBoard()
        print(f"{winner} won the game!")
        break
    if not possibilities():
        game = False

if not win():
    print("Game is a draw")
