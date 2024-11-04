import numpy as np

class ForceSystem:
    def __init__(self, forces, angles_theta, angles_phi):
        self.forces = forces
        self.angles_theta = np.radians(angles_theta)
        self.angles_phi = np.radians(angles_phi)

    def resolve_components(self):
        # Resolve each force into x, y, z components
        components = {'x': [], 'y': [], 'z': []}
        for i in range(len(self.forces)):
            F = self.forces[i]
            theta = self.angles_theta[i]
            phi = self.angles_phi[i]
            
            Fx = F * np.cos(phi) * np.sin(theta)
            Fy = F * np.sin(phi) * np.sin(theta)
            Fz = F * np.cos(theta)
            
            components['x'].append(Fx)
            components['y'].append(Fy)
            components['z'].append(Fz)
        
        return components
    
    def calculate_resultant(self):
        components = self.resolve_components()
        # Sum the components
        Rx = sum(components['x'])
        Ry = sum(components['y'])
        Rz = sum(components['z'])
        # Resultant force magnitude
        R = np.sqrt(Rx**2 + Ry**2 + Rz**2)
        # Direction angles
        alpha = np.degrees(np.arccos(Rx / R))
        beta = np.degrees(np.arccos(Ry / R))
        gamma = np.degrees(np.arccos(Rz / R))
        
        return R, alpha, beta, gamma

# Example usage:
forces = [180, 300]  # Force magnitudes
angles_theta = [40, 30]  # Angles with the z-axis for F1 and F2
angles_phi = [30, 0]  # Angles in x-y plane for F1 and F2

system = ForceSystem(forces, angles_theta, angles_phi)
R, alpha, beta, gamma = system.calculate_resultant()

print(f"Resultant Force: {R:.2f} lb")
print(f"Direction Angles: α = {alpha:.2f}°, β = {beta:.2f}°, γ = {gamma:.2f}°")
