import math
#each row represents a node. each column the connection(0/1).
vertices = [[0, 0, 1, 1, 0, 0, 0],
            [0, 0, 1, 0, 0, 1, 0],
            [1, 1, 0, 1, 1, 0, 0],
            [1, 0, 1, 0, 0, 0, 1],
            [0, 0, 1, 0, 0, 1, 0],
            [0, 1, 0, 0, 1, 0, 1],
            [0, 0, 0, 1, 0, 1, 0]]

#each column represents weights to the connections.
edges = [[0, 0, 1, 2, 0, 0, 0],
         [0, 0, 2, 0, 0, 3, 0],
         [1, 2, 0, 1, 3, 0, 0],
         [2, 0, 1, 0, 0, 0, 1],
         [0, 0, 3, 0, 0, 2, 0],
         [0, 3, 0, 0, 2, 0, 1],
         [0, 0, 0, 1, 0, 1, 0]]


def dijkstra_vast(vertices, edges, start):
    n = len(vertices) #rows
    distances = {v: math.inf for v in range(n)}
    distances[start] = 0

    previous = {v: None for v in range(n)}

    visited = set()

    #Looping through vertices:
    while len(visited) < n:
        #find vertex with smallest distance not yet visited
        unvisited_distances = {v: distances[v] for v in range(n) if v not in visited}
        current = min(unvisited_distances, key=unvisited_distances.get)

        visited.add(current)

        for neighbour in range(n):
            if vertices[current][neighbour] == 1:
                path = distances[current] + edges[current][neighbour]
                if path < distances[neighbour]:
                    distances[neighbour] = path
                    previous[neighbour] = current

    return distances, previous

start, end = 0, 5
distances, previous = dijkstra_vast(vertices, edges, start)

path = []
current = end
path.append(current)
while previous[current] is not None:
    current = previous[current]
    path.insert(0, current)
print(path)

"""
graph = {
    'A': {'B': 2, 'C': 1},
    'B': {'A': 2, 'D': 3},
    'C': {'A': 1, 'D': 1},
    'D': {'B': 3, 'C': 1, 'E': 5},
    'E': {'D': 5}
}

def dijkstra(graph, start): #calculates only the distances.
    distances = {node: math.inf for node in graph}
    distances[start] = 0
    visited = set()
    while len(visited) < len(graph):
        node = min((set(distances.keys()) - visited), key = distances.get())
        visited.add(node)
        #add a condition here to insert minimum distances at the start to sort effectively/
        for neighbour, distance in graph[node].items():
            path = distances[node] + distance
            if path < distances[neighbour]:
                distances[neighbour] = path
    
    return distances

start = 'A'
distances = dijkstra(graph, start)
"""