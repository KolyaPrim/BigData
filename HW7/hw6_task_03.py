from typing import List
import itertools
import numpy as np

a = [['o', 'x', 'x'],
     ['x', 'o', 'o'],
     ['o', 'x', 'x']]


def tic_tac_toe_checker(board: List[List]) -> str:
    # pass
    row, column = np.shape(board)
    unfinished = False
    rows = []
    columns = []
    diagonals = [(0, board[0][0]), (1, board[row - 1][0])]
    for i in range(0, row):
        rows.append((i, board[i][0]))
        columns.append((i, board[0][i]))
        for j in range(0, column - 1):
            if board[i][j] != board[i][j + 1]:  # row
                rows[i] = [None, None]
            if board[j][i] != board[j + 1][i]:  # column
                columns[i] = [None, None]

        if board[i][i] != diagonals[0][1]:  # straight diagonal
            diagonals[0] = [None, None]

        if board[row - 1][i] != diagonals[1][1]:  # reverse diagonal
            diagonals[1] = [None, None]
        row -= 1

    for line in board:
        if line.__contains__('-'):
            unfinished = True
            break

    for r, c, d in itertools.zip_longest(rows, columns, diagonals):
        if type(r) == tuple:
            return f"{r[1]} wins!"
        elif type(c) == tuple:
            return f"{c[1]} wins!"
        elif type(d) == tuple:
            return f"{d[1]} wins!"

    if unfinished:
        return "unfinished"
    else:
        return "draw!"


print(tic_tac_toe_checker(a))
