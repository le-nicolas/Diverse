import numpy as np
import matplotlib.pyplot as plt

# Parameters
L = 1.0        # Length of the rod in meters
nx = 50        # Number of spatial points
dx = L / (nx - 1)  # Spatial step size
alpha = 1e-4   # Thermal diffusivity in m^2/s
dt = 0.01      # Time step in seconds
nt = 100       # Number of time steps

# Initial condition: temperature at all points
T = np.zeros(nx)
T[int(0.5 / dx):int(0.6 / dx)] = 100  # Initial temperature of the middle section of the rod

# Time integration using the explicit method
for n in range(nt):
    T_new = T.copy()
    for i in range(1, nx - 1):
        T_new[i] = T[i] + alpha * dt / dx**2 * (T[i + 1] - 2 * T[i] + T[i - 1])
    T = T_new.copy()

# Plot the final temperature distribution
plt.plot(np.linspace(0, L, nx), T)
plt.xlabel('Position (m)')
plt.ylabel('Temperature (C)')
plt.title('Temperature Distribution in the Rod')
plt.show()
