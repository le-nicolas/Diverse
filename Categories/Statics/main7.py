import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create a 3D plot for the force vectors
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot F1 vector (in blue)
ax.quiver(0, 0, 0, F1_x, F1_y, F1_z, color='blue', label="F1 (50 lb)", arrow_length_ratio=0.1)

# Plot F2 vector (in red)
ax.quiver(0, 0, 0, F2_x, F2_y, F2_z, color='red', label="F2 (180 lb)", arrow_length_ratio=0.1)

# Plot Resultant vector (in green)
ax.quiver(0, 0, 0, R_x, R_y, R_z, color='green', label="Resultant", arrow_length_ratio=0.1)

# Set plot limits
ax.set_xlim([-150, 150])
ax.set_ylim([-150, 150])
ax.set_zlim([0, 150])

# Labels
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title('Force Vectors on the Spur Gear')

# Legend
ax.legend()

# Show plot
plt.show()
