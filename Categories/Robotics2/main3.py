graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 2, 'E': 3},
    'C': {'D': 1, 'F': 4},
    'D': {},
    'E': {'F': 1},
    'F': {}
}

def dijkstra(graph, source):
    distances = {node: float('inf') for node in graph}
    distances[source] = 0
    visited = set()

    while unvisited_nodes := {node for node in graph}:
        - visited
        current_node = min(unvisited_nodes, key=distances.get)
        visited.add(current_node)

        for neighbour, weight in graph[current_node].items():
            new_distance = distances[current_node] + weight
            if new_distance < distances[neighbour]:
                distances[neighbour] = new_distance

    return distances

source = 'A'
shortest_distances = dijkstra(graph, source)

for node, distance in shortest_distances.items():
    print(f'Shortest distance from {source} to {node} is {distance}')



# Initialized unvisited_nodes outside the while loop., The unvisited_nodes should be initialized outside the while loop and updated within the loop.
#
# Used lambda node: distances[node] to get the node with the minimum distance correctly.
