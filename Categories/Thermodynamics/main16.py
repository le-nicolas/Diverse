import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

# Set up the plot
fig, ax = plt.subplots()
x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)
line, = ax.plot(x, y, lw=2)

# Convection velocity
v = 0.05  # velocity of fluid particles

# Animation function
def animate(frame):
    line.set_ydata(np.sin(x + v * frame))  # update data to simulate motion
    return line,

ani = FuncAnimation(fig, animate, frames=100, interval=50, blit=True)

plt.xlabel('Position')
plt.ylabel('Temperature')
plt.title('Heat Convection')
plt.show()
