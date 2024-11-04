import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_aspect('equal')
ax.set_xlabel("Volume")
ax.set_ylabel("Pressure")

# Parameters for the isothermal process
V_initial = 1
P_initial = 10
n = 1   # Number of moles
R = 8.314  # Gas constant
T = 300   # Temperature (Kelvin)
V_range = np.linspace(1, 9, 300)  # Volume range for the process

# Ideal gas law to calculate pressure at different volumes (isothermal)
P = (n * R * T) / V_range

# Initialize the piston as a rectangle
piston, = ax.plot([], [], 'ro-', lw=2)
piston_rect = plt.Rectangle((0.5, 0), 1, 1, fill=True, color='blue')

# Adding the piston graphic to the plot
ax.add_patch(piston_rect)

def init():
    piston.set_data([], [])
    return piston,

# Animation function
def animate(i):
    # Update piston height
    piston_rect.set_width(V_range[i])  # The piston moves as volume increases

    # Update plot data for the PV diagram
    piston.set_data(V_range[:i], P[:i])

    return piston, piston_rect

# Create animation
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=len(V_range), interval=20, blit=True)

# Show plot and animation
plt.show()
