# Requires Python 3

# What has to be done:
# - Make a full board stop the game if no other options are available
# - Write save function
# - Write load function

import random
import time
import datetime
import os

# Initialize variables
n = 4
board = [[0 for x in range(n)] for y in range(n)]
score = 0
top_score = 0

# Function to get a character without pressing enter
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

# Function to clear the screen and print the board
def printBoard(board, n, score, top_score):
    os.system("cls" if os.name == "nt" else "clear")

    for x in range(n):
        for y in range(n):
            print("%5d" % (board[x][y]), end=" ")
        print("\n")

    print("Score:\t  ", score)

    if top_score < score:
        top_score = score

    print("Top score:", top_score, "\n")

    return top_score

# Function to save the game to a text file
def saveGame(board, n, score):
    now = datetime.datetime.now()

    os.system("mkdir saves")
    filename = "saves/game-" + str(now.year) + "-" + str(now.month) + "-" + str(now.day)
    save = open(filename, "a")

    print(score, file=save)
    for x in range(n):
        for y in range(n):
            print(board[x][y], file=save)

def loadGame():
    # Write function
    return board, score

# Function to add a random tile to the board
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
        print("\n--- Game over ---")

# Function to move the tiles to the left
def moveTilesLeft(board, n):
    for x in range(n):
        for i in range(n+1):
            for y in range(n-1, 0, -1):
                if board[x][y] != 0 and board[x][y-1] == 0:
                    board[x][y-1] = board[x][y]
                    board[x][y] = 0

    return board

# Function to add all equal tiles that are next to each other in the horizontal direction
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

# Function to get the user input, close the game or start a new game, and display a help message
def getInput():
    print("Press [w/a/s/d] or [n/q/h] ")
    inp = getch()

    if inp == "w":
        return 0
    elif inp == "a":
        return 1
    elif inp == "s":
        return 2
    elif inp == "d":
        return 3
    elif inp == "n":
        return 4
    elif inp == "q":
        print("Do you want to save the board? [y/n]")
        inp = getch()
        if inp == "y":
            return 5
        else:
            return 6
    elif inp == "h":
        print("\nPress w to move up")
        print("Press a to move left")
        print("Press s to move down")
        print("Press d to move right")
        print("Press n to create a new game")
        print("Press q to quit")
        print("Press h to show help\n")
        print("Copyright (c) 2018 Jasper Vinkenvleugel, Merijn den Houting, Marten Trip\n")
        return getInput()

# Function to rotate the board 90 degrees so that only moveTilesLeft has to be implemented
def rotateBoard(board, n):
    rotated_board = [[0 for x in range(n)] for y in range(n)]

    for x in range(n):
        for y in range(n):
            rotated_board[x][y] = board[n-1-y][x]

    return rotated_board

# Function to change the board based on the value of getInput
def swipe(board, n, score, inp):
    prev_board = board

    board = rotateBoard(board, n)
    if inp == 2:
        board, score = addTiles(board, n, score)

    board = rotateBoard(board, n)
    if inp == 3:
        board, score = addTiles(board, n, score)

    board = rotateBoard(board, n)
    if inp == 0:
        board, score = addTiles(board, n, score)

    board = rotateBoard(board, n)
    if inp == 1:
        board, score = addTiles(board, n, score)

    if inp == 4:
        board = [[0 for x in range(n)] for y in range(n)]
        score = 0

    if inp == 5:
        saveGame(board, n, score)
        exit()

    if inp == 6:
        exit()

    if board != prev_board:
        board = addRandomTile(board, n)

    return board, score

# Initialize the game
board = addRandomTile(board, n)
top_score = printBoard(board, n, score, top_score)

# Run the game
while True:
    inp = getInput()
    board, score = swipe(board, n, score, inp)
    top_score = printBoard(board, n, score, top_score)
