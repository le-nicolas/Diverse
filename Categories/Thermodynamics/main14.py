import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants and initial conditions
T_hot_initial = 500  # Temperature of the hot body (K)
T_cold_initial = 300  # Temperature of the cold body (K)
C_hot = 1000  # Heat capacity of the hot body (J/K)
C_cold = 1000  # Heat capacity of the cold body (J/K)
Q_total = 5000  # Total heat transfer (J)

# Number of steps to simulate the heat transfer process
steps = 100
dQ = Q_total / steps  # Heat transferred per step

# Arrays to store temperature and entropy changes
T_hot = np.zeros(steps)
T_cold = np.zeros(steps)
S_hot = np.zeros(steps)
S_cold = np.zeros(steps)
S_total = np.zeros(steps)

# Initial values
T_hot[0] = T_hot_initial
T_cold[0] = T_cold_initial

# Calculate temperature and entropy changes
for i in range(1, steps):
    # Temperature changes (heat transfer is small so we assume linear)
    T_hot[i] = T_hot[i-1] - dQ / C_hot
    T_cold[i] = T_cold[i-1] + dQ / C_cold
    
    # Entropy changes for hot and cold bodies
    S_hot[i] = S_hot[i-1] - dQ / T_hot[i]
    S_cold[i] = S_cold[i-1] + dQ / T_cold[i]
    
    # Total entropy change
    S_total[i] = S_hot[i] + S_cold[i]

# Set up the figure and subplots
fig, ax = plt.subplots(3, 1, figsize=(6, 10))

ax[0].set_xlim(0, steps)
ax[0].set_ylim(200, 550)
ax[1].set_xlim(0, steps)
ax[1].set_ylim(-10, 60)
ax[2].set_xlim(0, steps)
ax[2].set_ylim(-10, 60)

# Initialize lines for the plots
line_hot_temp, = ax[0].plot([], [], lw=2, label='Hot Body Temp (K)', color='r')
line_cold_temp, = ax[0].plot([], [], lw=2, label='Cold Body Temp (K)', color='b')

line_hot_entropy, = ax[1].plot([], [], lw=2, label='Hot Body Entropy Change', color='r')
line_cold_entropy, = ax[1].plot([], [], lw=2, label='Cold Body Entropy Change', color='b')

line_total_entropy, = ax[2].plot([], [], lw=2, label='Total Entropy Change', color='g')

ax[0].legend()
ax[1].legend()
ax[2].legend()

# Initialize plot limits and labels
def init():
    line_hot_temp.set_data([], [])
    line_cold_temp.set_data([], [])
    line_hot_entropy.set_data([], [])
    line_cold_entropy.set_data([], [])
    line_total_entropy.set_data([], [])
    return line_hot_temp, line_cold_temp, line_hot_entropy, line_cold_entropy, line_total_entropy

# Update function for animation
def update(frame):
    x = np.arange(frame)
    
    # Update temperature lines
    line_hot_temp.set_data(x, T_hot[:frame])
    line_cold_temp.set_data(x, T_cold[:frame])
    
    # Update entropy lines
    line_hot_entropy.set_data(x, S_hot[:frame])
    line_cold_entropy.set_data(x, S_cold[:frame])
    
    # Update total entropy line
    line_total_entropy.set_data(x, S_total[:frame])
    
    return line_hot_temp, line_cold_temp, line_hot_entropy, line_cold_entropy, line_total_entropy

# Create animation
ani = FuncAnimation(fig, update, frames=steps, init_func=init, blit=True, repeat=False)

# Show animation
plt.tight_layout()
plt.show()
