import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Constants
R = 8.314  # Ideal gas constant (J/(mol*K))
n = 1  # Amount of substance (mol)

# Generate temperature (T), volume (V) ranges
T = np.linspace(200, 600, 50)  # Temperature in Kelvin
V = np.linspace(0.01, 1, 50)   # Volume in m^3

# Create a 2D meshgrid
T, V = np.meshgrid(T, V)

# Calculate pressure using the Ideal Gas Law P = nRT/V
P = (n * R * T) / V

# Create 3D plot
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Plot the surface
ax.plot_surface(V, T, P, cmap='viridis')

# Labels and title
ax.set_xlabel('Volume (m^3)')
ax.set_ylabel('Temperature (K)')
ax.set_zlabel('Pressure (Pa)')
ax.set_title('3D P-V-T Surface for Ideal Gas Law')

plt.show()
