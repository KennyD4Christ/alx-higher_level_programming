#!/usr/bin/python3
"""
N Queens problem solution using backtracking
"""

import sys


def is_safe(board, row, col, N):
    """
    Check if it's safe to place a queen in the current position
    """
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens(board, row, N, solutions):
    """
    Solve the N Queens problem using backtracking
    """
    if row == N:
        solutions.append([[i, board[i]] for i in range(N)])
    else:
        for col in range(N):
            if is_safe(board, row, col, N):
                board[row] = col
                solve_nqueens(board, row + 1, N, solutions)


def print_solutions(N):
    """
    Print all possible solutions to the N Queens problem
    """
    board = [-1] * N
    solutions = []

    solve_nqueens(board, 0, N, solutions)

    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    print_solutions(N)
