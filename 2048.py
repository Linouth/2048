# Requires Python 3

# What has to be done:
# - Write input function
# - Write rotate function
# - Rewrite addRandomTile() to return game over in case no tiles can be added
# - Write save function
# - Write load function

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
            print("%5d" % (board[x][y]), end=" ")
        print("\n")

    print("Score:", score)
    print("")

def addRandomTile(board, n):
    x = random.randint(0, n-1)
    y = random.randint(0, n-1)
    randomness = random.randint(0, 10)

    if board[x][y] != 0:
        addRandomTile(board, n)
    else:
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

def inp():
    # Write input function
    return inp

def rotateBoard(board, n):
    # Write rotate function
    return board

def swipe(board, n, score, inp):
    prev_board = board

    if inp == 0:
        board, score = addTiles(board, n, score)
    board = rotateBoard(board, n)

    if inp == 1:
        board, score = addTiles(board, n, score)
    board = rotateBoard(board, n)

    if inp == 2:
        board, score = addTiles(board, n, score)
    board = rotateBoard(board, n)

    if inp == 3:
        board, score = addTiles(board, n, score)
    board = rotateBoard(board, n)

    if board != prev_board:
        board = addRandomTile(board, n)

    return board, score

# Below is demo code, this is used to see if the functions behave properly until input is added
# This demo code has to be removed to implement the other functions

# Create 4 random tiles
for i in range(4):
    board = addRandomTile(board, n)

# Print the board
printBoard(board, n, score)

# Get simulation count
simul_count = int(input("Enter a simulation count: "))

# Add the tiles of the board
board, score = addTiles(board, n, score)
# time.sleep(1)

for i in range(simul_count):

    # Add a new random tile
    board = addRandomTile(board, n)
    printBoard(board, n, score)
    # time.sleep(1)

    # Add all equal tiles
    board, score = addTiles(board, n, score)
    printBoard(board, n, score)
    # time.sleep(1)

# End of the demo code
