import matplotlib.pyplot as plt
import numpy as np

# Given values
horizontal_distance = 2.19  # meters
n_air = 1  # refractive index of air
n_water = 1.33  # refractive index of water

# Assume an angle of incidence (θ1)
theta1 = 45  # in degrees
theta1_rad = np.radians(theta1)

# Calculate the angle of refraction (θ2) using Snell's Law
theta2_rad = np.arcsin(n_air * np.sin(theta1_rad) / n_water)
theta2 = np.degrees(theta2_rad)

# Calculate the actual depth (d) using trigonometry
actual_depth = horizontal_distance * np.tan(theta2_rad)

# Calculate the apparent depth (d')
apparent_depth = actual_depth / n_water

# Improved visualization
fig, ax = plt.subplots(figsize=(10, 6))

# Plot light paths
ax.plot([0, horizontal_distance], [0, -actual_depth], 'r--', label='Light Path in Water')
ax.plot([0, horizontal_distance], [0, -apparent_depth], 'b-', label='Apparent Depth')
ax.plot([horizontal_distance, horizontal_distance], [0, -actual_depth], 'k:', label='Actual Depth')
ax.plot([0, horizontal_distance], [0, 0], 'k-', label='Water Surface')

# Adding angles
ax.annotate(r'$\theta_1$', xy=(horizontal_distance/2, 0), xytext=(horizontal_distance/2 + 0.1, -0.2),
            arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=0.3"),
            fontsize=12, ha='center')
ax.annotate(r'$\theta_2$', xy=(horizontal_distance, -actual_depth/2), xytext=(horizontal_distance - 0.3, -actual_depth/2 - 0.3),
            arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=-0.3"),
            fontsize=12, ha='center')

# Annotate apparent and actual depths
ax.text(horizontal_distance + 0.3, -actual_depth / 2, 'Actual Depth', fontsize=12, ha='center')
ax.text(horizontal_distance + 0.3, -apparent_depth / 2, 'Apparent Depth', fontsize=12, ha='center')

# Indicate horizontal distance
ax.annotate('Horizontal Distance = 2.19 m', xy=(horizontal_distance / 2, 0.05), xytext=(horizontal_distance / 2, 0.2),
            arrowprops=dict(arrowstyle="<->", lw=1.5),
            fontsize=12, ha='center')

# Axes and labels
ax.set_xlim(-0.5, horizontal_distance + 0.5)
ax.set_ylim(-actual_depth - 0.5, 1)
ax.set_xlabel('Horizontal Distance (m)', fontsize=14)
ax.set_ylabel('Depth (m)', fontsize=14)
ax.set_title('Refraction of Light in Water', fontsize=16)

# Adding legend
ax.legend(loc='upper right')

# Improving the aspect ratio
plt.gca().set_aspect('equal', adjustable='box')
plt.grid(True, linestyle='--', alpha=0.7)

plt.show()

# Output actual and apparent depths
actual_depth, apparent_depth
