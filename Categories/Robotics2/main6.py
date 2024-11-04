import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 2, 'E': 3},
    'C': {'D': 1, 'F': 4},
    'D': {},
    'E': {'F': 1},
    'F': {}
}

# Initialize the graph and positions
G = nx.DiGraph()
for node, edges in graph.items():
    for neighbour, weight in edges.items():
        G.add_edge(node, neighbour, weight=weight)

pos = nx.spring_layout(G)
fig, ax = plt.subplots()

# Initialize node colors and edge labels
node_colors = ['lightblue'] * len(G.nodes())
edge_labels = nx.get_edge_attributes(G, 'weight')
distances = {node: float('inf') for node in G.nodes()}
distances['A'] = 0
visited = set()
unvisited_nodes = set(G.nodes())
steps = []

# Dijkstra's algorithm with step recording
def dijkstra(graph, source):
    while unvisited_nodes:
        current_node = min(unvisited_nodes, key=lambda node: distances[node])
        visited.add(current_node)
        unvisited_nodes.remove(current_node)
        steps.append((current_node, dict(distances)))

        for neighbour, weight in graph[current_node].items():
            new_distance = distances[current_node] + weight
            if new_distance < distances[neighbour]:
                distances[neighbour] = new_distance
                steps.append((neighbour, dict(distances)))

dijkstra(graph, 'A')

# Animation function
def update(num):
    ax.clear()
    current_node, distances = steps[num]
    node_colors = ['red' if node == current_node else 'lightblue' for node in G.nodes()]
    nx.draw(G, pos, with_labels=True, node_size=700, node_color=node_colors, ax=ax)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, ax=ax)
    distance_labels = {node: f"{dist:.0f}" for node, dist in distances.items()}
    nx.draw_networkx_labels(G, pos, labels=distance_labels, ax=ax)
    ax.set_title(f"Step {num + 1}: Processing node {current_node}")

# Create the animation
ani = FuncAnimation(fig, update, frames=len(steps), repeat=False, interval=1000)

plt.show()
