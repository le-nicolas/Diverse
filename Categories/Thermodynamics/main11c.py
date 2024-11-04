import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Initial parameters
initial_height = 0.1  # Piston height at TDC (Top Dead Center) in meters
cylinder_radius = 0.05  # Cylinder radius in meters (for visual purposes)
stroke_length = 0.08  # Total piston stroke (from TDC to BDC) in meters

# Set the total cycle to 720 degrees (full four-stroke engine cycle)
total_degrees = 720  # 720 degrees for the complete four-stroke cycle

# Prepare figure for animation with subplots (animation and graph)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 8))

# Subplot 1: Piston-Cylinder Animation
ax1.set_xlim(-cylinder_radius, cylinder_radius)
ax1.set_ylim(0, initial_height + stroke_length + 0.05)  # Extra space above TDC
ax1.set_aspect('equal')
ax1.set_title("Four-Stroke Engine Piston Simulation")
ax1.set_xlabel("Cylinder (Top View)")
ax1.set_ylabel("Piston Height (m)")

# Piston (visual representation as a rectangle)
piston = plt.Rectangle((-cylinder_radius, 0), 2 * cylinder_radius, initial_height, color='g')
ax1.add_artist(piston)

# Subplot 2: Crankshaft Angle vs. Piston Height Graph
ax2.set_xlim(0, 720)
ax2.set_ylim(0, initial_height + stroke_length)
ax2.set_title("Crankshaft Angle vs. Piston Height")
ax2.set_xlabel("Crankshaft Angle (degrees)")
ax2.set_ylabel("Piston Height (m)")

# Line for the graph in subplot 2
line, = ax2.plot([], [], 'r-', lw=2)

# Data lists to store the crankshaft angle and piston height
angles = []
heights = []

# Animation function to simulate piston movement and update the graph
def animate(i):
    # Map the frame (i) to the angle in degrees over a full 720-degree cycle
    angle = (i / 200) * total_degrees  # Scale the frame to match the 720-degree cycle

    # Four-stroke cycle: Intake (0-180), Compression (180-360), Power (360-540), Exhaust (540-720)
    if 0 <= angle < 180:
        # Intake stroke: Piston moves down from TDC to BDC
        piston_height = initial_height - (stroke_length * (angle / 180))
    elif 180 <= angle < 360:
        # Compression stroke: Piston moves up from BDC to TDC
        piston_height = initial_height - stroke_length + (stroke_length * ((angle - 180) / 180))
    elif 360 <= angle < 540:
        # Power stroke: Piston moves down from TDC to BDC
        piston_height = initial_height - (stroke_length * ((angle - 360) / 180))
    else:
        # Exhaust stroke: Piston moves up from BDC to TDC
        piston_height = initial_height - stroke_length + (stroke_length * ((angle - 540) / 180))

    # Update piston height in the animation
    piston.set_height(piston_height)

    # Update data for the graph
    angles.append(angle)
    heights.append(piston_height)

    # Set data for the line in the graph (Crankshaft Angle vs. Piston Height)
    line.set_data(angles, heights)

    return piston, line

# Animation function
ani = FuncAnimation(fig, animate, frames=200, interval=50, blit=True)

# Show animation and graph
plt.tight_layout()
plt.show()
