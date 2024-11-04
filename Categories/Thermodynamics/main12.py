import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parameters
rod_length = 1.0  # length of the rod (meters)
nx = 100  # number of spatial points
dx = rod_length / (nx - 1)  # distance between points
alpha = 0.01  # thermal diffusivity (m^2/s)
dt = 0.0005  # time step
total_time = 5  # total time for the simulation (seconds)
nt = int(total_time / dt)  # number of time steps

# Initial temperature distribution (cold rod with a hot spot in the middle)
T = np.zeros(nx)
T[int(nx / 4):int(3 * nx / 4)] = 100  # hot region in the middle
T_new = T.copy()

# Set up the plot
fig, ax = plt.subplots()
x = np.linspace(0, rod_length, nx)
line, = ax.plot(x, T)
ax.set_ylim(0, 120)
ax.set_xlabel('Position along the rod (m)')
ax.set_ylabel('Temperature (°C)')
ax.set_title('1D Heat Conduction (Fourier’s Law)')

# Update function for the animation
def update(frame):
    global T, T_new
    for i in range(1, nx - 1):
        T_new[i] = T[i] + alpha * (T[i - 1] - 2 * T[i] + T[i + 1]) * dt / dx**2
    T[:] = T_new[:]
    line.set_ydata(T)
    return line,
#mura ra siyag katong sa machine learning nga training process? :DDD
# i love this :D

# Animate the temperature distribution over time
ani = FuncAnimation(fig, update, frames=nt, interval=20, blit=True)

# Show the plot
plt.show()
