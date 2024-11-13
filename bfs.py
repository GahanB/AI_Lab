def bfs(graph, start):
    queue = []
    visited = []

    visited.append(start)
    queue.append(start)

    while queue:
        node = queue.pop(0)
        print(node, end=" ")

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)

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

print("Following is the Breadth First Search")
bfs(graph, 'A')
