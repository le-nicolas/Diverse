import numpy as np
import matplotlib.pyplot as plt

# Set up the grid
x = np.linspace(-5, 5, 20)
y = np.linspace(-5, 5, 20)
X, Y = np.meshgrid(x, y)

# Define a hypothetical fluid velocity field (e.g., swirling flow)
U = -Y / (X**2 + Y**2 + 1)  # Velocity in X direction
V = X / (X**2 + Y**2 + 1)   # Velocity in Y direction

# Plot the velocity field using quiver
plt.quiver(X, Y, U, V, color='green')

plt.title("Fluid Flow Vector Field")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()
