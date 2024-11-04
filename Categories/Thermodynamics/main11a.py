import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# Initial parameters
initial_height = 0.1  # Initial height of the piston in meters (TDC - Top Dead Center)
cylinder_radius = 0.05  # Cylinder radius (arbitrary for visual purposes)

# Set the total cycle degrees (720 for a four-stroke engine cycle)
total_degrees = 720

# Define the range for the piston movement (BDC to TDC)
stroke_length = 0.08  # Total piston stroke (distance from Top Dead Center to Bottom Dead Center)

# Prepare figure for animation
fig, ax = plt.subplots(figsize=(6, 8))
ax.set_xlim(-cylinder_radius, cylinder_radius)
ax.set_ylim(0, initial_height + stroke_length + 0.05)  # Adjusted to include stroke movement
ax.set_aspect('equal')
plt.title("Four-Stroke Engine Cycle Piston Simulation")
plt.xlabel("Cylinder (Top View)")
plt.ylabel("Height (m)")

# Cylinder visual representation (outer edge)
piston = plt.Rectangle((-cylinder_radius, 0), 2 * cylinder_radius, initial_height, color='g')
ax.add_artist(piston)

# Define the animation function to simulate the piston movement over four strokes
def animate(i):
    # Map the frame (i) to the angle in degrees over a full 720-degree cycle
    angle = (i / 200) * total_degrees  # Scale the frame to match the 720-degree cycle
    
    # Four-stroke cycle: Intake (0-180), Compression (180-360), Power (360-540), Exhaust (540-720)
    if 0 <= angle < 180:
        # Intake stroke: Piston moves from TDC to BDC (downward)
        piston_height = initial_height - (stroke_length * (angle / 180))
    elif 180 <= angle < 360:
        # Compression stroke: Piston moves from BDC to TDC (upward)
        piston_height = initial_height - stroke_length + (stroke_length * ((angle - 180) / 180))
    elif 360 <= angle < 540:
        # Power stroke: Piston moves from TDC to BDC (downward)
        piston_height = initial_height - (stroke_length * ((angle - 360) / 180))
    else:
        # Exhaust stroke: Piston moves from BDC to TDC (upward)
        piston_height = initial_height - stroke_length + (stroke_length * ((angle - 540) / 180))
    
    # Set the new piston height
    piston.set_height(piston_height)
    
    return piston,

# Animation function
ani = FuncAnimation(fig, animate, frames=200, interval=50, blit=True)

# Show animation
plt.show()
