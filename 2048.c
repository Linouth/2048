#include <stdio.h>
#include <time.h>
#include <math.h>

#define BOARD_SIZE 4

int main(void) {
  int n = BOARD_SIZE;
  int inp;
  int board[n][n] = {0};
  int points = 0;

  srand(time(NULL));

  while(1) {
    addRandomTile(board);
    printBoard(board, points);
    inp = userInput();

    if (inp = 5)
      break;

    if (inp = 6) {
      saveBoard(board);
      continue;
    }

    swipe(board, inp, points);
  }

  return 0;
}

void swipe(int *board, int inp, int *points) {
  if (inp == 1) swipeUp(board, points);
  rotateBoard(board);
  if (inp == 2) swipeUp(board, points);
  rotateBoard(board);
  if (inp == 3) swipeUp(board, points);
  rotateBoard(board);
  if (inp == 4) swipeUp(board, points);
  rotateBoard(board);
}

void swipeUp(int *board, int *points) {
  int n = BOARD_SIZE;
  int x, y, i, j;

  // Do something for each row
  for (x = 0; x < n; x++) {

    // Remove empty space between tiles in a row
    moveTilesUp(board, x);

    // Add up all equal tiles in a row
    for (y = 0; y < n; y++) {
      if (board[x][y] == board[x][y+1]) {
        board[x][y] = 2 * board[x][y];
        board[x][y+1] = 0;

        points = points + board[x][y];
      }
    }

    // Again, remove empty space between tiles in a row
    moveTilesUp(board, x);

  }
}

void moveTilesUp(int *board, int x) {
  int n = BOARD_SIZE;
  int i, j;

  for (i = 0; i < 10; i++) {
    for (j = n-1; j = 1; j--) {
      if (board[x][j] != 0 && board[x][j-1] == 0)
        board[x][j-1] = board[x][j];
        board[x][j] = 0;
    }
  }
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

void printBoard(int board[][], points) {
  int x, y;

  system("clear");

  for (x = 0; x < BOARD_SIZE; x++) {
    for (y = 0; y < BOARD_SIZE; y++) {
      printf("%5d", board[x][y]);
    }
    printf("\n");
  }
  printf("\n%d\n\n", points);
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

  printf("The board is saved.\n", );
  // Add tile delay
}
