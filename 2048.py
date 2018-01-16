# Requires Python 3

# What has to be done:
# - Write load function

import random
import time
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
def saveGame(board, n, score, top_score):
    filename = "save"

    save = open(filename, "w")
    print(score, file=save)

    save = open(filename, "a")
    print(top_score, file=save)
    for x in range(n):
        for y in range(n):
            print(board[x][y], file=save)

def loadGame(board, n, score, top_score):
    filename = "save"
    save = open(filename, "r")

    # Read the file line by line and parse it to board, score and top_score

    return board, score, top_score

# Function to add a random tile to the board
def addRandomTile(board, n):
    count = 0

    while True:
        x = random.randint(0, n-1)
        y = random.randint(0, n-1)
        randomness = random.randint(0, 10)

        if count > n**2:
            break
        elif board[x][y] != 0:
            count = count + 1
            continue
        else:
            if randomness > 0:
                board[x][y] = 2
            else:
                board[x][y] = 4
            break

    return board

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
        return 5
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

# Function to rotate the board and then move tiles based on the input
def moveTiles(board, n, score, inp):
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

    return board, score

# Function to change the board based on the value of getInput
def swipe(board, n, score, top_score, inp):
    prev_board = board

    board, score = moveTiles(board, n, score, inp)

    if inp == 4:
        board = [[0 for x in range(n)] for y in range(n)]
        score = 0
        board = addRandomTile(board, n)

    if inp == 5:
        saveGame(board, n, score, top_score)
        exit()

    if board == prev_board:
        simul_board = board
        simul_score = 0
        simul_inp = 0

        for simul_input in range(4):
            simul_board, simul_score = moveTiles(simul_board, n, simul_score, simul_inp)
            simul_board = addRandomTile(simul_board, n)

        if simul_board == board:
            print("\n--- Game over ---\n")

            board = [[0 for x in range(n)] for y in range(n)]
            board = addRandomTile(board, n)
            saveGame(board, n, score, top_score)
            exit()

    elif board != prev_board and inp != 4:
        board = addRandomTile(board, n)

    return board, score

# Initialize the game
# board, score, top_score = loadGame(board, n, score, top_score)
board = addRandomTile(board, n)
top_score = printBoard(board, n, score, top_score)

# Run the game
while True:
    inp = getInput()
    board, score = swipe(board, n, score, top_score, inp)
    top_score = printBoard(board, n, score, top_score)
