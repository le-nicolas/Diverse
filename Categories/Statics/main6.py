import numpy as np

# Force magnitudes
F1_magnitude = 50  # lb
F2_magnitude = 180  # lb

# F1 angles
theta_xz_F1 = np.radians(24)  # angle from z-axis in xz-plane
theta_xy_F1 = np.radians(25)  # angle from xy-plane

# F2 angles
theta_z_F2 = np.radians(60)  # angle from z-axis
theta_xy_F2 = np.radians(135)  # angle in xy-plane

# Resolve F1 into Cartesian components
F1_x = F1_magnitude * np.sin(theta_xz_F1) * np.cos(theta_xy_F1)
F1_y = F1_magnitude * np.sin(theta_xz_F1) * np.sin(theta_xy_F1)
F1_z = F1_magnitude * np.cos(theta_xz_F1)

# Resolve F2 into Cartesian components
F2_x = F2_magnitude * np.sin(theta_z_F2) * np.cos(theta_xy_F2)
F2_y = F2_magnitude * np.sin(theta_z_F2) * np.sin(theta_xy_F2)
F2_z = F2_magnitude * np.cos(theta_z_F2)

# Resultant force components
R_x = F1_x + F2_x
R_y = F1_y + F2_y
R_z = F1_z + F2_z

# Resultant force magnitude
R_magnitude = np.sqrt(R_x**2 + R_y**2 + R_z**2)

# Resultant vector and magnitude
F1_components = (F1_x, F1_y, F1_z)
F2_components = (F2_x, F2_y, F2_z)
resultant_components = (R_x, R_y, R_z)
R_magnitude, F1_components, F2_components, resultant_components

# Printing the results clearly for F1, F2, and the resultant force
print("F1 Components:")
print(f"F1_x = {F1_x:.2f} lb")
print(f"F1_y = {F1_y:.2f} lb")
print(f"F1_z = {F1_z:.2f} lb")

print("\nF2 Components:")
print(f"F2_x = {F2_x:.2f} lb")
print(f"F2_y = {F2_y:.2f} lb")
print(f"F2_z = {F2_z:.2f} lb")

print("\nResultant Force Components:")
print(f"R_x = {R_x:.2f} lb")
print(f"R_y = {R_y:.2f} lb")
print(f"R_z = {R_z:.2f} lb")

print(f"\nResultant Force Magnitude: |R| = {R_magnitude:.2f} lb")

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
