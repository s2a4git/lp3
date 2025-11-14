# Check if placing queen at (row, col) is safe
def is_safe(board, row, col, n):
    for i in range(row):
        if board[i][col] == 1:  # column check
            return False
        if col - (row - i) >= 0 and board[i][col - (row - i)] == 1:  # left diagonal
            return False
        if col + (row - i) < n and board[i][col + (row - i)] == 1:  # right diagonal
            return False
    return True


# Backtracking
def solve(board, row, n):
    if row == n:
        return True
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            if solve(board, row + 1, n):
                return True
            board[row][col] = 0
    return False


# Driver
n = 8
board = [[0] * n for _ in range(n)]

# First queen placed manually
board[0][2] = 1

if solve(board, 1, n):  # start from next row
    for r in board:
        print(r)
else:
    print("No solution")
