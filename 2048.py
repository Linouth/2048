# Requires Python 3

# What has to be done:
# - Write save function
# - Write load function

import random
import time
import os

n = 4
board = [[0 for x in range(n)] for y in range(n)]
score = 0

# Source: https://stackoverflow.com/questions/510357/python-read-a-single-character-from-the-user
def _find_getch():
    try:
        import termios
    except ImportError:
        import msvcrt
        return msvcrt.getch

    import sys, tty
    def _getch():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

    return _getch

getch = _find_getch()

def printBoard(board, n, score):
    os.system("cls" if os.name == "nt" else "clear")

    for x in range(n):
        for y in range(n):
            print("%5d" % (board[x][y]), end=" ")
        print("\n")

    print("Score:", score)
    print("")

def addRandomTile(board, n):
    if any(0 in row for row in board):
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
    else:
        print("Game over")

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

def getInput():
    print("Press [w/a/s/d] or [n/q/h] ")
    inp = getch()

    if inp == "w":
        return 3
    elif inp == "a":
        return 0
    elif inp == "s":
        return 1
    elif inp == "d":
        return 2
    elif inp == "n":
        return 4
    elif inp == "q":
        exit()
    elif inp == "h":
        print("\nPress w to move up")
        print("Press a to move left")
        print("Press s to move down")
        print("Press d to move right")
        print("Press n to create a new game")
        print("Press q to quit")
        print("Press h to show help\n")
        return getInput()

def rotateBoard(board, n):
    rotated_board = [[0 for x in range(n)] for y in range(n)]

    for x in range(n):
        for y in range(n):
            rotated_board[x][y] = board[n-1-y][x]

    return rotated_board

def swipe(board, n, score, inp):
    prev_board = board

    # Swipe tiles left (a)
    if inp == 0:
        board, score = addTiles(board, n, score)
    board = rotateBoard(board, n)

    # Swipe tiles down (s)
    if inp == 1:
        board, score = addTiles(board, n, score)
    board = rotateBoard(board, n)

    # Swipe tiles right (d)
    if inp == 2:
        board, score = addTiles(board, n, score)
    board = rotateBoard(board, n)

    # Swipe tiles up (w)
    if inp == 3:
        board, score = addTiles(board, n, score)
    board = rotateBoard(board, n)

    if inp == 4:
        board = [[0 for x in range(n)] for y in range(n)]
        score = 0

    if board != prev_board:
        board = addRandomTile(board, n)

    return board, score

board = addRandomTile(board, n)
printBoard(board, n, score)

while True:
    inp = getInput()
    board, score = swipe(board, n, score, inp)
    printBoard(board, n, score)
