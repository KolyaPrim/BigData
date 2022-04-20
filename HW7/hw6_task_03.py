from typing import List
import numpy as np

a = [['o', '-', 'o'],
     ['-', 'x', 'o'],
     ['x', 'x', 'x']]


def tic_tac_toe_checker(board: List[List]) -> str:
    # pass
    row, column = np.shape(board)
    unfinished = False
    rows = {}
    columns = {}
    diagonals = {0: board[0][0], 1: board[row - 1][0]}

    for i in range(0, row):
        rows[i] = True
        columns[i] = True
        for j in range(0, column - 1):
            if board[i][j] != board[i][j + 1]:  # row
                rows[i] = False
            if board[j][i] != board[j + 1][i]:  # column
                columns[i] = False

        if board[i][i] != diagonals[0]:  # straight diagonal
            diagonals[0] = False

        if board[row - 1][i] != diagonals[1]:  # reverse diagonal
            diagonals[1] = False
        row -= 1

    for line in board:
        if line.__contains__('-'):
            unfinished = True
            break
    if (str(rows.values()).__contains__('True')):
        symbol = board[rows.keys()[rows.values().index(True)], 0]
        return f"{symbol} wins"
    print(rows)
    print(columns)
    print(diagonals)
    print(unfinished)


print(tic_tac_toe_checker(a))
