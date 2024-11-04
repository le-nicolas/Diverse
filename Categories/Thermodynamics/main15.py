import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Heat conduction through a rod

# Rod parameters
length = 10  # Length of the rod
temp_hot = 100  # Hot end temperature
temp_cold = 20  # Cold end temperature
steps = 100  # Number of steps
alpha = 0.01  # Thermal diffusivity

# Discretize the rod into small segments
dx = 0.1  # Segment length
rod = np.linspace(temp_cold, temp_hot, int(length/dx))  # Initial temperature distribution

# Time step for simulation
dt = 0.01

# Function to update the temperature distribution
def update_rod(rod, alpha, dx, dt):
    new_rod = rod.copy()
    for i in range(1, len(rod) - 1):
        new_rod[i] = rod[i] + alpha * (rod[i+1] - 2*rod[i] + rod[i-1]) * dt / dx**2
    return new_rod

# Set up the plot
fig, ax = plt.subplots()
ax.set_ylim(10, 110)
line, = ax.plot(rod)

# Animation function
def animate(frame):
    global rod
    rod = update_rod(rod, alpha, dx, dt)
    line.set_ydata(rod)
    return line,

ani = FuncAnimation(fig, animate, frames=steps, interval=50, blit=True)

plt.xlabel('Rod Length')
plt.ylabel('Temperature (°C)')
plt.title('Heat Conduction in a Rod')
plt.show()
