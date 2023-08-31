#!/usr/bin/python3
"""Solves the N-queens puzzle.
Determines all possible solutions to placing N
N non-attacking queens on an NxN chessboard.
"""
import sys


def is_safe(board, row, col, N):
    """Check if placing a queen at position (row, col) is safe"""
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(board, col, N):
    """Recursive function to solve the N queens problem"""
    if col >= N:
        print_solution(board, N)
        return True

    res = False
    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1
            res = solve_nqueens(board, col + 1, N) or res
            board[i][col] = 0

    return res


def print_solution(board, N):
    """Print the current state of the board"""
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=' ')
        print()


def main():
    """Main function"""
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

    board = [[0 for _ in range(N)] for _ in range(N)]

    if not solve_nqueens(board, 0, N):
        print("No solutions found")


if __name__ == "__main__":
    main()
