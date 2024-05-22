import heapq
from collections import defaultdict, deque





def dijkstra(adj_list, start):
    shortest_paths = {node: 0 for node in adj_list}
    distances = {node: float('inf') for node in adj_list}

    distances[start] = 0

    priority_queue = [(0, start)]

    while priority_queue:

        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue
        
        for neighbor, weight in adj_list[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                #print(f"Shortest path to {neighbor} is {current_node}")
                shortest_paths[neighbor] = current_node
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    #print(shortest_paths)
    return distances, shortest_paths


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
    location = input("Where are you at? ")
    destination = input("Where would ou like to go? ")
    edge_list =  {
     'A': {'B': 3, 'C': 8},
     'B': {'A': 3, 'C': 2, 'E': 5},
     'C': {'A': 8, 'B': 2, 'D': 1, 'E': 6},
     'E': {'B': 5, 'C': 6, 'D': 2, 'F': 5},
     'D': {'C': 1, 'E': 2, 'F': 3},
     'F': {'D': 3, 'E': 5}
    }
    
    distances, shortest = dijkstra(edge_list, destination)
    
    
    for nodes in edge_list:

        for roads in edge_list[nodes]:
            edge_list[nodes][roads] = 1
    print(shortest)

    

    
    
    

    single_distance, paths2 = dijkstra(edge_list, destination)
    
    direction = location
    print(single_distance)
    for i in range(int(single_distance[location])+1):
        direction = shortest[direction]
        print(f"Step {i+1}: {direction}")


