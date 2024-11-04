import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# Initial parameters
initial_height = 0.1  # Initial height of the piston in meters (from problem)
cylinder_radius = 0.05  # Cylinder radius (arbitrary for visual purposes)

# Specific volumes for different states from problem
v1 = 0.8857  # Initial specific volume at 200 kPa and saturated vapor state (m^3/kg)
va = 1.083  # Specific volume at 200 kPa and 200 °C (m^3/kg)
vb = 0.001044  # Specific volume at 200 kPa and 100 °C (m^3/kg)

# Heights corresponding to changes in specific volumes (from problem)
ha = initial_height * (va / v1)  # Height for 200 °C
hb = initial_height * (vb / v1)  # Height for 100 °C

# Prepare figure for animation
fig, ax = plt.subplots(figsize=(6, 8))
ax.set_xlim(-cylinder_radius, cylinder_radius)
ax.set_ylim(0, 0.15)
ax.set_aspect('equal')
plt.title("Piston-Cylinder Simulation")
plt.xlabel("Cylinder (Top View)")
plt.ylabel("Height (m)")

# Cylinder visual representation (outer edge)
#cylinder = plt.Circle((0, 0), cylinder_radius, color='b', fill=False)
#ax.add_artist(cylinder)

# Piston (rectangle that moves with height)
piston = plt.Rectangle((-cylinder_radius, 0), 2*cylinder_radius, initial_height, color='g')
ax.add_artist(piston)

# Animate piston movement based on height changes
def animate(i):
    if i < 50:  # Move to height for 200 °C
        piston.set_height(initial_height + (ha - initial_height) * (i / 50))
    elif i < 100:  # Move to height for 100 °C
        piston.set_height(ha + (hb - ha) * ((i - 50) / 50))
    return piston,

# Animation function
ani = FuncAnimation(fig, animate, frames=100, interval=100, blit=True)

# Show animation
plt.show()
