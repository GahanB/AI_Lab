initial_state = [2, 8, 3, 1, 6, 4, 7, 0, 5]
goal_state = [1, 2, 3, 8, 0, 4, 7, 6, 5]

def swap(board, i, j):
    board[i], board[j] = board[j], board[i]

def get_successors(board):
    empty = board.index(0)
    successors = []
    x, y = empty % 3, empty // 3
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)] 
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_board = list(board)
            swap(new_board, empty, ny * 3 + nx)
            successors.append(new_board)
    return successors

def bfs_solve(initial, goal):
    queue = [[initial, 0, []]]  
    visited = {tuple(initial)}   

    while queue:
        current, moves, path = queue.pop(0)
        path = path + [current]
        if current == goal:
            return moves, path

        for successor in get_successors(current):
            if tuple(successor) not in visited:
                visited.add(tuple(successor))
                queue.append([successor, moves + 1, path])
    return -1, []

move_count, path = bfs_solve(initial_state, goal_state)
print(f"Number of moves to solve the puzzle: {move_count}")
for step, state in enumerate(path):
    print(f"Step {step}: {state}")
