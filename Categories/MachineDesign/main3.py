import matplotlib.pyplot as plt
import numpy as np

# Define the Node class representing each point in the chassis
class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Define the Beam class representing each beam in the chassis
class Beam:
    def __init__(self, node1, node2, material_strength):
        self.node1 = node1
        self.node2 = node2
        self.length = np.sqrt((node2.x - node1.x)**2 + (node2.y - node1.y)**2)
        self.material_strength = material_strength

    def draw(self, ax):
        ax.plot([self.node1.x, self.node2.x], [self.node1.y, self.node2.y], 'b-')

# Define the Chassis class representing the entire structure
class Chassis:
    def __init__(self):
        self.nodes = []
        self.beams = []

    def add_node(self, x, y):
        node = Node(x, y)
        self.nodes.append(node)
        return node

    def add_beam(self, node1, node2, material_strength=100):
        beam = Beam(node1, node2, material_strength)
        self.beams.append(beam)

    def draw(self):
        fig, ax = plt.subplots()
        for beam in self.beams:
            beam.draw(ax)
        plt.axis('equal')
        plt.grid(True)
        plt.show()

# Main code to build and simulate a simple chassis
chassis = Chassis()

# Create chassis nodes (x, y positions)
node1 = chassis.add_node(0, 0)  # Front left
node2 = chassis.add_node(4, 0)  # Front right
node3 = chassis.add_node(0, 2)  # Rear left
node4 = chassis.add_node(4, 2)  # Rear right

# Create beams to form the chassis structure
chassis.add_beam(node1, node2)  # Front beam
chassis.add_beam(node2, node4)  # Right side beam
chassis.add_beam(node4, node3)  # Rear beam
chassis.add_beam(node3, node1)  # Left side beam
chassis.add_beam(node1, node4)  # Diagonal cross beam for rigidity

# Draw the chassis design
chassis.draw()
