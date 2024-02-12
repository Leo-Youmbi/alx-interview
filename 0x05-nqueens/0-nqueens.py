#!/usr/bin/python3
"""
    N-queen problem
    The next algo solve any N queen in any NxN
    Being N > 3
"""

import sys

NUMBER_OF_ARGS_REQUIRED = 1


def get_real_position(colPlacements, index, size):
    return colPlacements[index][0] * size + colPlacements[index][1]


def isSafe(colPlacements: list) -> bool:
    rowId = len(colPlacements) - 1
    for i in range(rowId):
        diff = abs(colPlacements[i][1] - colPlacements[rowId][1])
        if diff == 0 or diff == rowId - i:
            return False
    return True


def solveNQueens(
        size_of_board: int,
        row: int,
        placements: list,
        result: list
        ) -> None:

    if row == size_of_board:
        print(placements)
        result.append(placements)
    else:
        for col in range(size_of_board):
            placements.append([row, col])
            if isSafe(placements):
                solveNQueens(size_of_board, row+1, placements, result)
            placements.pop()


def is_integer(value: str) -> bool:
    """
    Evaluates if a string value is an integer
    """
    try:
        value = int(value)
        return True
    except ValueError:
        return False


if __name__ == '__main__':
    arguments = sys.argv

    if len(arguments) != NUMBER_OF_ARGS_REQUIRED + 1:
        print("Usage: nqueens{}".format(' N' * NUMBER_OF_ARGS_REQUIRED))
    elif not is_integer(arguments[1]):
        print("N must be a number")
    elif eval(arguments[1]) < 4:
        print("N must be at least 4")
    else:
        n = int(arguments[1])
        result = []
        solveNQueens(n, 0, [], result)
