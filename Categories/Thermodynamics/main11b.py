import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Initial parameters
initial_height = 0.1  # Piston height at TDC (Top Dead Center) in meters
cylinder_radius = 0.05  # Cylinder radius in meters (for visual purposes)
stroke_length = 0.08  # Total piston stroke (from TDC to BDC) in meters

# Set the total cycle to 720 degrees (full four-stroke engine cycle)
total_degrees = 720  # 720 degrees for the complete four-stroke cycle

# Prepare figure for animation
fig, ax = plt.subplots(figsize=(6, 8))
ax.set_xlim(-cylinder_radius, cylinder_radius)
ax.set_ylim(0, initial_height + stroke_length + 0.05)  # Extra space above TDC
ax.set_aspect('equal')
plt.title("Four-Stroke Engine Piston Simulation")
plt.xlabel("Cylinder (Top View)")
plt.ylabel("Piston Height (m)")

# Piston (visual representation as a rectangle)
piston = plt.Rectangle((-cylinder_radius, 0), 2 * cylinder_radius, initial_height, color='g')
ax.add_artist(piston)

# Define the animation function to simulate piston movement over four strokes
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

    # Update piston height
    piston.set_height(piston_height)
    
    return piston,

# Animation function
ani = FuncAnimation(fig, animate, frames=200, interval=50, blit=True)

# Show animation
plt.show()
