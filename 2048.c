#include <stdio.h>
#include <time.h>
#include <math.h>

#define BOARD_SIZE 4

int main(void) {
  int n = BOARD_SIZE;
  int inp;
  int board[n][n] = {0};

  srand(time(NULL));

  while(1) {
    addRandomTile(board);
    printBoard(board);
    inp = userInput();

    if (inp = 5)
      break;

    if (inp = 6)
      saveBoard(board);
      continue;

    moveTiles(board, inp);
  }

  return 0;
}

void moveTiles(int *board, int inp) {
  if (inp == 1) swipeUp(board);
  rotateBoard(board);
  if (inp == 2) swipeUp(board);
  rotateBoard(board);
  if (inp == 3) swipeUp(board);
  rotateBoard(board);
  if (inp == 4) swipeUp(board);
  rotateBoard(board);
}

int swipeUp(board) {
  int n = BOARD_SIZE;
  int x, y, i, j;

  // Do something for each row
  for (x = 0; x < n; x++) {

    // Swipe all tiles to the top, and do this 10 times (how many times can this happen, max?)
    for (j = 0; j < 10; j++) {
      for (i = n-1; i = 0; i--) {
        if (board[x][i] == 0 || board[x][i+1] != 0)
          board[x][i] = board[x][i+1];
      }
    }

    // Add up all equal tiles
    for (y = 0; y < n; y++) {
      if (board[x][y] == board[x][y+1]) {
        board[x][y] = 2 * board[x][y];
        board[x][y+1] = 0;
      }
    }

    // Again, swipe all tiles to the top (try it 10 times??)
    for (j = 0; j < 10; j++) {
      for (i = n-1; i = 0; i--) {
        if (board[x][i] == 0 || board[x][i+1] != 0)
          board[x][i] = board[x][i+1];
      }
    }

  }

  return board;
}

void rotateBoard(int *board) {
  int n = BOARD_SIZE;
  int tempBoard[n][n] = {0}

  // copy the current board into tempBoard[][]
  for(int i=0; i<cols; i++) {
    for(int j=0; j<rows; j++) {
        tempBoard[i][j] = board[i][j];
    }
  }

  // rotate board[][] 90 degrees clockwise
  for(int i=0; i<cols; i++) {
    for(int j=0; j<rows; j++) {
        board[i][j] = tempBoard[rows-1-j][i];
    }
  }
}

void printBoard(int board[][]) {
  int x, y;

  system("clear");

  for (x = 0; x < BOARD_SIZE; x++) {
    for (y = 0; y < BOARD_SIZE; y++) {
      printf("%5d", board[x][y]);
    }
    printf("\n");
  }
}

void addRandomTile(int board[][]) {
  int x = rand(BOARD_SIZE);
  int y = rand(BOARD_SIZE);
  if (board[x][y] != 0) {
    addRandomTile()
    return;
  }
  int random = rand(10);
  if (random > 0) {
    board[x][y] = 2;
  } else {
    board[x][y] = 4;
  }
}

int userInput() {
    char inp[8];
    printf("Move [w/a/s/d/q/s]: ");
    scanf("%8s", &inp);
    inp[sizeof inp-1] = 0;-

    switch (inp[0]) {
        case 'w':
            return 1;
            break;
        case 'a':
            return 2;
            break;
        case 's':
            return 3;
            break;
        case 'd':
            return 4;
            break;
        case 'q':
            return 5;
            break;
        case 's':
            return 6;
            break;
        default:
            printf("Action is not valid. \n");
            return user_input();
    }
}

void saveBoard(int board[][]) {
  int x, y;
  FILE *save;

  save = fopen("save.txt", "w");

  for (x = 0; x < BOARD_SIZE; x++) {
    for (y = 0; y < BOARD_SIZE; y++) {
      fprintf(save, "%5d", board[x][y]);
    }
    fprintf(save, "\n");
  }

  fclose(save);
}
