def is_valid_state(m, c):
    """
    Check if a state is valid. The number of missionaries (m) should not be
    less than the number of cannibals (c) on either side of the river unless m is 0.
    """
    return (m == 0 or m >= c) and (3 - m == 0 or (3 - m) >= (3 - c))


def apply_production_rules(state):
    """
    Generate all possible moves (next states) from the current state.
    """
    m, c, boat = state
    possible_moves = []

    if boat == 1:  # Boat is on the starting side
        if m - 2 >= 0:
            possible_moves.append((m - 2, c, 0))  # Move 2 missionaries
        if c - 2 >= 0:
            possible_moves.append((m, c - 2, 0))  # Move 2 cannibals
        if m - 1 >= 0 and c - 1 >= 0:
            possible_moves.append((m - 1, c - 1, 0))  # Move 1 missionary and 1 cannibal
        if m - 1 >= 0:
            possible_moves.append((m - 1, c, 0))  # Move 1 missionary
        if c - 1 >= 0:
            possible_moves.append((m, c - 1, 0))  # Move 1 cannibal
    else:  # Boat is on the other side
        if m + 2 <= 3:
            possible_moves.append((m + 2, c, 1))  # Bring 2 missionaries back
        if c + 2 <= 3:
            possible_moves.append((m, c + 2, 1))  # Bring 2 cannibals back
        if m + 1 <= 3 and c + 1 <= 3:
            possible_moves.append((m + 1, c + 1, 1))  # Bring 1 missionary and 1 cannibal back
        if m + 1 <= 3:
            possible_moves.append((m + 1, c, 1))  # Bring 1 missionary back
        if c + 1 <= 3:
            possible_moves.append((m, c + 1, 1))  # Bring 1 cannibal back

    return possible_moves


def bfs():
    """
    Use Breadth-First Search (BFS) to find the solution.
    """
    start_state = (3, 3, 1)  # (Missionaries, Cannibals, Boat on starting side)
    goal_state = (0, 0, 0)   # (Missionaries, Cannibals, Boat on the other side)
    
    queue = [(start_state, [])]
    visited = set()
    visited.add(start_state)

    while queue:
        current_state, path = queue.pop(0)
        
        # Check if the goal state is reached
        if current_state == goal_state:
            return path + [current_state]

        # Get next states using production rules
        next_states = apply_production_rules(current_state)
        
        for new_state in next_states:
            # Check if the new state is valid and not visited
            if new_state not in visited and is_valid_state(new_state[0], new_state[1]):
                visited.add(new_state)
                queue.append((new_state, path + [current_state]))

    return None


def print_solution(solution):
    """
    Print the solution path in a readable format.
    """
    if solution:
        print("Solution found:")
        for i, state in enumerate(solution):
            m, c, boat = state
            side = 'starting' if boat == 1 else 'other'
            m_other = 3 - m
            c_other = 3 - c
            print(f"Step {i + 1}: | Start Side: m = {m}, c = {c} | Other Side: m = {m_other}, c = {c_other} | Boat on {side} side")
    else:
        print("No solution found.")


# Run the BFS algorithm to find the solution
solution = bfs()
print_solution(solution)
