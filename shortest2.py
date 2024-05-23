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
    '''edge_list =  {
     'A': {'B': 3, 'C': 8},
     'B': {'A': 3, 'C': 2, 'E': 5},
     'C': {'A': 8, 'B': 2, 'D': 1, 'E': 6},
     'E': {'B': 5, 'C': 6, 'D': 2, 'F': 5},
     'D': {'C': 1, 'E': 2, 'F': 3},
     'F': {'D': 3, 'E': 5}
    }'''
    edge_list = {
    'A': {'B': 5},
    'B': {'A': 5, 'D': 5, 'C': 10},
    'C': {'T': 5, 'X': 5, 'B': 10},
    'D': {'E': 5, 'F': 5, 'T': 11, 'B': 5},
    'E': {'D': 5},
    'F': {'D': 5, 'G': 5},
    'G': {'F': 5, 'H': 5, 'Y': 10},
    'H': {'G': 5, 'Z': 10, 'K': 8},
    'I': {'U': 8, 'J': 5, 'Y': 6},
    'J': {'I': 5, 'S': 12, 'Z': 6},
    'K': {'L': 1, 'P': 4, 'H': 8},
    'L': {'K': 1, 'M': 10},
    'M': {'L': 10, 'N': 8, 'S': 6},
    'N': {'O': 3, 'M': 8},
    'O': {'N': 3},
    'P': {'Q': 8, 'K': 4},
    'Q': {'P': 8, 'R': 4},
    'R': {'Q': 4},
    'S': {'M': 6, 'J': 8},
    'T': {'D': 10, 'U': 6, 'C': 5},
    'U': {'T': 6, 'W': 6, 'I': 8, 'V': 6},
    'V': {'U': 6},
    'W': {'X': 5, 'U': 8},
    'Y': {'G': 10, 'I':6},
    'X': {'C': 5, 'W': 5},
    'Z': {'H': 10, 'J': 6}
    }


    distances, shortest = dijkstra(edge_list, destination)
    
    
    for nodes in edge_list:

        for roads in edge_list[nodes]:
            edge_list[nodes][roads] = 1


    

    
    
    

    single_distance, paths2 = dijkstra(edge_list, destination)
    
    direction = location

    for i in range(int(single_distance[location])+1):
        direction = shortest[direction]
        if direction == 0: break
        print(f"Step {i+1}: {direction}")


