graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 2, 'E': 3},
    'C': {'D': 1, 'F': 4},
    'D': {},
    'E': {'F': 1},
    'F': {}
}

def dijkstra(graph, start):
    shortest_distance = {}
    predecessor = {}
    unseen_nodes = set(graph.keys())
    infinity = float('inf')
    path = []
    
    for node in unseen_nodes:
        shortest_distance[node] = infinity
    shortest_distance[start] = 0

    while unseen_nodes:
        min_node = None
        for node in unseen_nodes:
            if min_node is None:
                min_node = node
            elif shortest_distance[node] < shortest_distance[min_node]:
                min_node = node

        if min_node is None:
            break

        for child_node, weight in graph[min_node].items():
            if weight + shortest_distance[min_node] < shortest_distance[child_node]:
                shortest_distance[child_node] = weight + shortest_distance[min_node]
                predecessor[child_node] = min_node

        unseen_nodes.remove(min_node)

    current_node = 'F'
    while current_node != start:
        try:
            path.insert(0, current_node)
            current_node = predecessor[current_node]
        except KeyError:
            print('Path not reachable')
            break
    path.insert(0, start)
    if shortest_distance['F'] != infinity:
        print('Shortest distance is ' + str(shortest_distance['F']))
        print('And the path is ' + str(path))

dijkstra(graph, 'A')
