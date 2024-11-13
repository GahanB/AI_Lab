# Depth-First Search function
def dfs(state, visited):
    monkey, box, banana, onbox, hasBanana = state

    # Goal check: if the monkey has grabbed the banana
    if hasBanana:
        print("Monkey successfully got the banana!")
        return True

    # If this state has already been visited, skip it
    if state in visited:
        return False

    # Mark this state as visited
    visited.add(state)

    # Move monkey to the box if it's not on the box and not at the same location
    if not onbox and monkey != box:
        newState = (box, box, banana, onbox, hasBanana)
        print(f"Monkey moves from {monkey} to {box}.")
        if dfs(newState, visited):
            return True

    # Push the box to the banana if the monkey is not on the box and is at the box's location
    if not onbox and monkey == box and box != banana:
        newState = (banana, banana, banana, onbox, hasBanana)
        print(f"Monkey pushes the box from {box} to {banana}.")
        if dfs(newState, visited):
            return True

    # Climb on the box if the monkey and the box are at the banana's location
    if not onbox and monkey == box == banana:
        newState = (monkey, box, banana, True, hasBanana)
        print("Monkey climbs on the box.")
        if dfs(newState, visited):
            return True

    # Grab the banana if the monkey is on the box at the banana's location
    if onbox and box == banana:
        newState = (monkey, box, banana, onbox, True)
        print("Monkey grabs the banana!")
        if dfs(newState, visited):
            return True

    # If no solution found from this state
    return False

# Function to initiate the DFS solution
def solve_dfs():
    initial = ('door', 'corner', 'center', False, False)
    visited = set()
    if not dfs(initial, visited):
        print("The monkey failed to get the banana.")

# Execute the solution
solve_dfs()
