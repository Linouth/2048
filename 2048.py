# Requires Python 3

import random

n = 4
board = [[0 for x in range(n)] for y in range(n)]

def printBoard(board, n):
    for x in range(n):
        for y in range(n):
            print(board[x][y], end=" ")
        print("")

def addRandomTile(board, n):
    x = random.randint(0, n-1)
    y = random.randint(0, n-1)
    randomness = random.randint(0, 5)

    if board[x][y] != 0:
        addRandomTile(board, n)

    if randomness > 0:
        board[x][y] = 2
    else:
        board[x][y] = 4

def moveTilesLeft(board, n):
    for x in range(n):
        for i in range(10):
            for y in range(n-1, 0, -1):
                if board[x][y] != 0 and board[x][y-1] == 0:
                    board[x][y-1] = board[x][y]
                    board[x][y] = 0

def addTiles(board, n):
    for x in range(n):
        for y in range(n-1):
            if board[x][y] == board[x][y+1]:
                board[x][y] = 2 * board[x][y]
                board[x][y+1] = 0

    moveTilesLeft(board, n)

# Add 6 random tiles to the board
for i in range(6):
    addRandomTile(board, n)

# Print the board
printBoard(board, n)
print("")

# Move the tiles to the left, print
moveTilesLeft(board, n)
printBoard(board, n)
print("")

# Add all equal tiles
addTiles(board, n)
printBoard(board, n)
