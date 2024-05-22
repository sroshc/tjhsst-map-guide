from collections import defaultdict, deque


def bfs(graph, start):
    print(f"Started at {start}")
    visited = set()
    que = deque([start])
    visited.add(start)

    while que:
        node = que.popleft()

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                print(f"Visited {neighbor}")
                que.append(neighbor)


if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    print("Breadth First Search Algorithim")
    bfs(graph, 'A')