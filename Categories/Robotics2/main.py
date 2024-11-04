# i guess my very first try to theory...
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
    unseenNodes = graph
    infinity = float('inf')
    path = []
    for node in unseenNodes:
        shortest_distance[node] = infinity
    shortest_distance[start] = 0

    while unseenNodes:
        minNode = None
        for node in unseenNodes:
            if minNode is None:
                minNode = node
            elif shortest_distance[node] < shortest_distance[minNode]:
                minNode = node

        for childNode, weight in graph[minNode].items():
            if weight + shortest_distance[minNode] < shortest_distance[childNode]:
                shortest_distance[childNode] = weight + shortest_distance[minNode]
                predecessor[childNode] = minNode
        unseenNodes.pop(minNode)

    currentNode = 'F'
    while currentNode != start:
        try:
            path.insert(0, currentNode)
            currentNode = predecessor[currentNode]
        except KeyError:
            print('Path not reachable')
            break
    path.insert(0, start)
    if shortest_distance['F'] != infinity:
        print('Shortest distance is ' + str(shortest_distance['F']))
        print('And the path is ' + str(path))

#The issue with your code is the way you're handling the unseenNodes dictionary. 
# #You're modifying the dictionary while iterating over it, which is causing problems. 
# #Instead, you should maintain a separate set of nodes to keep track of which nodes have not been visited yet.

