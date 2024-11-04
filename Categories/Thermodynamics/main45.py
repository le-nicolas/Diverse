import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants for the Carnot cycle
V1, V2 = 1, 2  # Volume limits
P1, P2 = 1, 2  # Pressure limits

# Set up the figure
fig, ax = plt.subplots()
ax.set_xlim(0.5, 2.5)
ax.set_ylim(0.5, 2.5)
ax.set_xlabel("Volume")
ax.set_ylabel("Pressure")
ax.set_title("Carnot Cycle")

line, = ax.plot([], [], lw=2)

# Define stages of the Carnot cycle (4 stages)
volumes = [np.linspace(V1, V2, 100), np.full(100, V2), np.linspace(V2, V1, 100), np.full(100, V1)]
pressures = [np.full(100, P1), np.linspace(P1, P2, 100), np.full(100, P2), np.linspace(P2, P1, 100)]

# Combine stages into one complete cycle
V_cycle = np.concatenate(volumes)
P_cycle = np.concatenate(pressures)

# Update function for animation
def update(frame):
    line.set_data(V_cycle[:frame], P_cycle[:frame])
    return line,

ani = animation.FuncAnimation(fig, update, frames=len(V_cycle), interval=100, blit=True)
plt.show()
