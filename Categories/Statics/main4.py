import numpy as np
from graphviz import Digraph

# Define a class that mimics the architecture of the system
class ForceSystem:
    def __init__(self, forces):
        # Input layer: forces are given as (magnitude, angle in degrees)
        self.forces = forces
        self.graph = Digraph(comment='Force Resolution System')

    def calculate_components(self):
        # Processing layer: decompose forces into x, y components
        self.components = []
        for i, (magnitude, angle) in enumerate(self.forces):
            angle_rad = np.radians(angle)
            fx = magnitude * np.cos(angle_rad)
            fy = magnitude * np.sin(angle_rad)
            self.components.append((fx, fy))
            # Add nodes for force decomposition
            self.graph.node(f'F{i}', f'Force {i+1}: {magnitude}N at {angle}°')
            self.graph.node(f'Fx{i}', f'Fx{i+1} = {fx:.2f}N')
            self.graph.node(f'Fy{i}', f'Fy{i+1} = {fy:.2f}N')
            # Add edges showing force decomposition
            self.graph.edge(f'F{i}', f'Fx{i}')
            self.graph.edge(f'F{i}', f'Fy{i}')
        return self.components

    def calculate_resultant(self):
        # Summing components (like aggregation)
        total_fx = sum([fx for fx, fy in self.components])
        total_fy = sum([fy for fx, fy in self.components])
        resultant_magnitude = np.sqrt(total_fx**2 + total_fy**2)
        resultant_angle = np.degrees(np.arctan2(total_fy, total_fx))
        
        # Add nodes for resultant force
        self.graph.node('Resultant_Fx', f'Total Fx = {total_fx:.2f}N')
        self.graph.node('Resultant_Fy', f'Total Fy = {total_fy:.2f}N')
        self.graph.node('Resultant', f'Resultant = {resultant_magnitude:.2f}N at {resultant_angle:.2f}°')
        
        # Add edges showing summation and resultant calculation
        self.graph.edge('Resultant_Fx', 'Resultant')
        self.graph.edge('Resultant_Fy', 'Resultant')

        return resultant_magnitude, resultant_angle

    def visualize(self):
        # Render the graph using Graphviz
        return self.graph

# Example usage
forces = [(10, 30), (15, 150), (5, 270)]  # Magnitudes and angles of forces
force_system = ForceSystem(forces)

# Step 1: Calculate components
components = force_system.calculate_components()

# Step 2: Calculate resultant force
resultant_magnitude, resultant_angle = force_system.calculate_resultant()

# Step 3: Visualize the process
graph = force_system.visualize()
graph.render('force_system', view=True, format='png')  # Saves the graph as 'force_system.png'

# Output for reference
print(f"Resultant Force: Magnitude = {resultant_magnitude:.2f}, Angle = {resultant_angle:.2f} degrees")
