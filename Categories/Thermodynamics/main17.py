import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

# Heat radiation between objects

# Initial parameters
temperature_body = 500  # K, hot object temperature
ambient_temperature = 300  # K, surrounding environment temperature

# Set up the figure
fig, ax = plt.subplots()
circle = plt.Circle((0.5, 0.5), 0.1, fc="red", lw=2)
ax.add_patch(circle)
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)

# Animation function
def animate(frame):
    # Reduce the temperature of the hot body over time
    temp = temperature_body - frame * 2
    intensity = (temp - ambient_temperature) / (temperature_body - ambient_temperature)
    circle.set_facecolor((1, intensity, intensity))  # Color change indicates radiative heat loss
    return circle,

ani = FuncAnimation(fig, animate, frames=100, interval=50, blit=True)

plt.title('Heat Radiation (Temperature Change)')
plt.show()
