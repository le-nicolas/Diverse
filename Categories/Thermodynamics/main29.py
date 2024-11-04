import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create a grid of points
X, Y, Z = np.meshgrid(np.arange(-5, 5, 1),
                      np.arange(-5, 5, 1),
                      np.arange(-5, 5, 1))

# Define vector field
U = Y
V = -X
W = Z

# Create a 3D quiver plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.quiver(X, Y, Z, U, V, W, length=0.5, normalize=True)

# Set labels
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis')
ax.set_title('3D Quiver Plot Example')

plt.show()
