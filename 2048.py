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

addRandomTile(board, n)
printBoard(board, n)
