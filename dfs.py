from collections import defaultdict, deque

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
print("Depth First Search Algorithim")
start = "A"

        
def dfs(visited, graph, node): 
    if node not in visited:
        if node != "A":
            print(f"Visited {node}")
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

visited = set()
print(f"Started at {start}")
que = deque([start])

dfs(visited, graph, start)



                    

            




