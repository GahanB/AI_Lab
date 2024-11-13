def dfs(graph, start):
    stack = [start]
    visited = set()

    while stack:
        node = stack.pop()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            stack.extend(reversed(graph[node]))  # Add neighbors in reverse order

graph = {
    'A': ['B', 'D'],
    'B': ['C', 'F'],
    'C': ['E', 'G'],
    'D': ['F'],
    'E': ['F'],
    'F': ['B', 'F'],
    'G': ['E', 'K'],
    'K': []
}

print("Following is the Depth First Search")
dfs(graph, 'A')
