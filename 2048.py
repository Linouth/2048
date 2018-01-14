# Requires Python 3

import random
import time
import os

n = 4
board = [[0 for x in range(n)] for y in range(n)]
score = 0

def printBoard(board, n, score):
    os.system("cls" if os.name == "nt" else "clear")

    for x in range(n):
        for y in range(n):
            print(board[x][y], end=" ")
        print("")

    print("")
    print("Score:", score)
    print("")

def addRandomTile(board, n):
    x = random.randint(0, n-1)
    y = random.randint(0, n-1)
    randomness = random.randint(0, 10)

    if board[x][y] != 0:
        addRandomTile(board, n)

    if randomness > 0:
        board[x][y] = 2
    else:
        board[x][y] = 4

    return board

def moveTilesLeft(board, n):
    for x in range(n):
        for i in range(n+1):
            for y in range(n-1, 0, -1):
                if board[x][y] != 0 and board[x][y-1] == 0:
                    board[x][y-1] = board[x][y]
                    board[x][y] = 0

    return board

def addTiles(board, n, score):
    board = moveTilesLeft(board, n)

    for x in range(n):
        for y in range(n-1):
            if board[x][y] == board[x][y+1]:
                board[x][y] = 2 * board[x][y]
                board[x][y+1] = 0
                score = score + board[x][y]

    board = moveTilesLeft(board, n)
    return board, score

# Below is demo code, this is used to see if the functions behave properly until input is added
# For some reason, it sometimes overrides existing pieces

for i in range(4):
    board = addRandomTile(board, n)

printBoard(board, n, score)

print("NOTE: sometimes a number is overwritten by a new random number, I don't know why and it should be looked into")
simul_count = int(input("Enter a simulation count: "))

board, score = addTiles(board, n, score)
printBoard(board, n, score)
print("NOTE: sometimes a number is overwritten by a new random number, I don't know why and it should be looked into")
time.sleep(1)

for i in range(simul_count):

    # Add a new random tile
    board = addRandomTile(board, n)
    printBoard(board, n, score)
    print("NOTE: sometimes a number is overwritten by a new random number, I don't know why and it should be looked into")
    time.sleep(1)

    # Add all equal tiles
    board, score = addTiles(board, n, score)
    printBoard(board, n, score)
    print("NOTE: sometimes a number is overwritten by a new random number, I don't know why and it should be looked into")
    time.sleep(1)
