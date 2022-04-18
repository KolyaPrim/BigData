from typing import List
import numpy as np

a = [['-', '-', 'o'],
     ['-', 'x', 'o'],
     ['x', 'o', 'x']]


def tic_tac_toe_checker(board: List[List]) -> str:
    # pass
    row, column = np.shape(board)
    for i in range(0, row):
        for j in range(0, column):
            pass
            board[i][j]  # row

            board[i][j]  # column

        board[i][i]  # straight diagonal

        board[row-1][i] # reverse diagonal
        row -= 1


tic_tac_toe_checker(a)
