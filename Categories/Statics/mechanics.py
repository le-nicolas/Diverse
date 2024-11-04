# architecture that can handle dynamic inputs for force and vector resolution
# OOP

# yeah

import math

class Vector:
    def __init__(self, magnitude, angle_deg):
        self.magnitude = magnitude
        self.angle_deg = angle_deg
        self.angle_rad = math.radians(angle_deg)
        self.x_component = self.magnitude * math.cos(self.angle_rad)
        self.y_component = self.magnitude * math.sin(self.angle_rad)

    def resolve_components(self):
        return self.x_component, self.y_component

class ForceSystem:
    def __init__(self):
        self.forces = []

    def add_force(self, magnitude, angle_deg):
        vector = Vector(magnitude, angle_deg)
        self.forces.append(vector)

    def find_resultant(self):
        total_x = sum(force.x_component for force in self.forces)
        total_y = sum(force.y_component for force in self.forces)

        resultant_magnitude = math.sqrt(total_x**2 + total_y**2)
        resultant_angle_rad = math.atan2(total_y, total_x)
        resultant_angle_deg = math.degrees(resultant_angle_rad)
        
        return resultant_magnitude, resultant_angle_deg

# Example Usage
def main():
    system = ForceSystem()

    # Taking inputs (dynamic)
    num_forces = int(input("Enter number of forces: "))
    for i in range(num_forces):
        magnitude = float(input(f"Enter magnitude of force {i+1} (kN): "))
        angle_deg = float(input(f"Enter angle of force {i+1} (degrees): "))
        system.add_force(magnitude, angle_deg)

    # Finding the resultant
    magnitude, direction = system.find_resultant()
    print(f"\nResultant Force: {magnitude:.2f} kN")
    print(f"Direction: {direction:.2f} degrees counterclockwise from the x-axis")

if __name__ == "__main__":
    main()
