import numpy as np
import matplotlib.pyplot as plt

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

# Plotting the results
fig, ax = plt.subplots(3, 1, figsize=(6, 10))

# Plot temperature changes
ax[0].plot(range(steps), T_hot, label='Hot Body Temp (K)', color='r')
ax[0].plot(range(steps), T_cold, label='Cold Body Temp (K)', color='b')
ax[0].set_ylabel('Temperature (K)')
ax[0].set_title('Temperature of Hot and Cold Bodies')
ax[0].legend()

# Plot entropy changes
ax[1].plot(range(steps), S_hot, label='Hot Body Entropy Change', color='r')
ax[1].plot(range(steps), S_cold, label='Cold Body Entropy Change', color='b')
ax[1].set_ylabel('Entropy Change (J/K)')
ax[1].set_title('Entropy Change in Hot and Cold Bodies')
ax[1].legend()

# Plot total entropy change
ax[2].plot(range(steps), S_total, label='Total Entropy Change', color='g')
ax[2].set_ylabel('Entropy (J/K)')
ax[2].set_xlabel('Steps')
ax[2].set_title('Total Entropy Change of the System')
ax[2].legend()

plt.tight_layout()
plt.show()
