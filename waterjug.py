def apply_rules(state): 
    x, y = state 
    next_states = [] 
    
    if x < 4: 
        next_states.append((4, y))  # Fill jug1
    if y < 3: 
        next_states.append((x, 3))  # Fill jug2
    if x > 0: 
        next_states.append((0, y))  # Empty jug1
    if y > 0: 
        next_states.append((x, 0))  # Empty jug2
    if x + y >= 4 and y > 0: 
        next_states.append((4, y - (4 - x)))  # Pour jug2 into jug1
    if x + y >= 3 and x > 0: 
        next_states.append((x - (3 - y), 3))  # Pour jug1 into jug2
    if x + y <= 4 and y > 0: 
        next_states.append((x + y, 0))  # Pour all jug2 into jug1
    if x + y <= 3 and x > 0: 
        next_states.append((0, x + y))  # Pour all jug1 into jug2
    
    return next_states

def bfs(): 
    initial_state = (0, 0)
    goal_state = (2, 0)
    queue = [(initial_state, [])] 
    visited = set()
    
    while queue: 
        state, path = queue.pop(0) 
        if state in visited: 
            continue 
        visited.add(state) 
        if state == goal_state: 
            return path + [state] 
        next_states = apply_rules(state) 
        for next_state in next_states: 
            if next_state not in visited: 
                queue.append((next_state, path + [state]))

solution = bfs() 
if solution:
    print("Solution found:")
    for step in solution:
        print(f"jug1: {step[0]}, jug2: {step[1]}")
else:
    print("No solution found.")
