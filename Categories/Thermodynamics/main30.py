import numpy as np
import matplotlib.pyplot as plt

# Create a grid of points
Y, X = np.mgrid[-3:3:100j, -3:3:100j]

# Define vector field (example: a simple radial field)
U = -1 - X**2 + Y
V = 1 + X - Y**2

# Create a quiver plot
plt.figure()
plt.quiver(X, Y, U, V, color='blue')
plt.xlim(-3, 3)
plt.ylim(-3, 3)
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('2D Quiver Plot Example')
plt.grid()
plt.show()
