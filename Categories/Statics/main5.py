import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Function to create a gear shape
def create_gear(teeth, radius, width):
    angle = np.linspace(0, 2 * np.pi, 100)
    inner_radius = radius - width
    outer_radius = radius + width
    
    # Create the gear profile
    r = np.array([inner_radius if i % 2 == 0 else outer_radius for i in range(len(angle))])
    x = r * np.cos(angle)
    y = r * np.sin(angle)
    
    return x, y

# Function to update gear animation
def update(frame, gear1, gear2, ax):
    ax.clear()
    ax.set_aspect('equal')
    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)

    # Rotate the first gear
    theta1 = np.linspace(0, 2 * np.pi, len(gear1[0])) + frame * 0.05
    gear1_x_rot = gear1[0] * np.cos(theta1) - gear1[1] * np.sin(theta1)
    gear1_y_rot = gear1[0] * np.sin(theta1) + gear1[1] * np.cos(theta1)
    
    # Rotate the second gear (opposite direction)
    theta2 = np.linspace(0, 2 * np.pi, len(gear2[0])) - frame * 0.05
    gear2_x_rot = gear2[0] * np.cos(theta2) - gear2[1] * np.sin(theta2)
    gear2_y_rot = gear2[0] * np.sin(theta2) + gear2[1] * np.cos(theta2)

    # Plot the gears
    ax.fill(gear1_x_rot, gear1_y_rot, 'b')
    ax.fill(gear2_x_rot + 3.5, gear2_y_rot, 'r')

# Create the figure and axes
fig, ax = plt.subplots()

# Generate two gears
gear1 = create_gear(teeth=10, radius=1.5, width=0.2)
gear2 = create_gear(teeth=10, radius=1.5, width=0.2)

# Create animation
ani = animation.FuncAnimation(fig, update, frames=200, fargs=(gear1, gear2, ax), interval=50)

# Show the animation
plt.show()
