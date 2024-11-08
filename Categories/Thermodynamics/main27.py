import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create grid data
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)

# Define a function for z values
z = np.sin(np.sqrt(x**2 + y**2))

# Create a figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create a surface plot
ax.plot_surface(x, y, z, cmap='viridis')

# Set labels
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

# Show the plot
plt.show()
