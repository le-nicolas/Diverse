import networkx as nx
import matplotlib.pyplot as plt

graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 2, 'E': 3},
    'C': {'D': 1, 'F': 4},
    'D': {},
    'E': {'F': 1},
    'F': {}
}

def draw_graph(graph, path):
    G = nx.DiGraph()
    for node, edges in graph.items():
        for adjacent_node, weight in edges.items():
            G.add_edge(node, adjacent_node, weight=weight)
            
    pos = nx.spring_layout(G)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=15)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    
    if path:
        path_edges = [(path[i], path[i+1]) for i in range(len(path) - 1)]
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='r', width=2)
    
    plt.show()

# Example path from A to F: A -> C -> D -> F
path = ['A', 'C', 'D', 'F']
draw_graph(graph, path)
