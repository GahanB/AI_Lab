# Function to print the chess board
def print_solution(board):
    for row in board:
        print(" ".join("Q" if col else " . " for col in row))
        print()

# Function to check if a queen can be safely placed
def is_safe(board, row, col, N):
    # Check this column on the upper side
    for i in range(row):
        if board[i][col]:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False

    # Check upper diagonal on the right side
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j]:
            return False

    return True

# Function to solve the N-Queens problem using backtracking
def solve_n_queens(board, row, N):
    # If all queens are placed successfully
    if row >= N:
        print_solution(board)
        print()
        return True

    result = False
    for col in range(N):
        if is_safe(board, row, col, N):
            # Place queen at board[row][col]
            board[row][col] = True

            # Recur to place rest of the queens
            result = solve_n_queens(board, row + 1, N) or result

            # Backtrack: remove queen from board[row][col]
            board[row][col] = False

    return result

# Main function to solve the N-Queens problem
def n_queens_problem():
    N = int(input("Enter the number of queens (board size): "))
    board = [[False] * N for _ in range(N)]

    if not solve_n_queens(board, 0, N):
        print("No solution exists.")

# Entry point of the program
if __name__ == "__main__":
    n_queens_problem()
