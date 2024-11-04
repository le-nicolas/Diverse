import numpy as np

# Define a class that mimics the architecture of the system
class ForceSystem:
    def __init__(self, forces):
        # Input layer: forces are given as (magnitude, angle in degrees)
        self.forces = forces
    
    def calculate_components(self):
        # Processing layer: decompose forces into x, y components
        self.components = []
        for magnitude, angle in self.forces:
            angle_rad = np.radians(angle)  # Convert angle to radians
            fx = magnitude * np.cos(angle_rad)
            fy = magnitude * np.sin(angle_rad)
            self.components.append((fx, fy))
        return self.components

    def calculate_resultant(self):
        # Summing components (like aggregation)
        total_fx = sum([fx for fx, fy in self.components])
        total_fy = sum([fy for fx, fy in self.components])
        resultant_magnitude = np.sqrt(total_fx**2 + total_fy**2)
        resultant_angle = np.degrees(np.arctan2(total_fy, total_fx))
        return resultant_magnitude, resultant_angle

# Example usage
forces = [(10, 30), (15, 150), (5, 270)]  # Magnitudes and angles of forces
force_system = ForceSystem(forces)

# Step 1: Calculate components
components = force_system.calculate_components()
print("Force Components:", components)

# Step 2: Calculate resultant force
resultant_magnitude, resultant_angle = force_system.calculate_resultant()
print(f"Resultant Force: Magnitude = {resultant_magnitude:.2f}, Angle = {resultant_angle:.2f} degrees")
