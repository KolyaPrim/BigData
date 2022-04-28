from typing import List
import itertools
import numpy as np

a = [['x', 'o', 'x'],
     ['x', 'o', 'x'],
     ['o', 'x', 'x']]

"""
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

"""


def tic_tac_toe_checker(board: List[List]) -> str:
    unfinished = False
    for i in enumerate(board): # (0, [x,x,x])
        if '-' in i[1]:
            unfinished = True
        if len(set(i[1])) == 1 and i[1][0] != '-':
            return f"{i[1][0]} wins"
        elif board[0][i[0]] == board[1][i[0]] == board[2][i[0]] != '-':
            return f"{i[1][i[0]]} wins"
        if board[0][0] == board[1][1] == board[2][2] \
                    or board[2][0] == board[1][1] == board[0][2]:
            return f"{i[1][1]} wins"
    if unfinished:
        return "unfinished"
    else:
        return "draw"


print(tic_tac_toe_checker(a))
