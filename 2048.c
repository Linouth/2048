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

    if (inp = -1)
      break;

    moveTiles(board, inp);
  }

  return 0;
}

void moveTiles(int board[][], int inp) {
  // Write function
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
    printf("Move [w/a/s/d/q]: ");
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
            return -1;
            break;
        default:
            printf("Action is not valid. \n");
            return user_input();
    }
}
