import numpy as np
import matplotlib.pyplot as plt

# Parameters
R = 0.05  # Radius of the pipe (m)
L = 1.0   # Length of the pipe (m)
mu = 0.001  # Dynamic viscosity of the fluid (Pa.s)
delta_P = 100  # Pressure difference (Pa)

# Discretize the radius
r = np.linspace(0, R, 100)

# Calculate the velocity profile
v = (delta_P / (4 * mu * L)) * (R**2 - r**2)

# Plot the velocity profile
plt.figure(figsize=(8, 6))
plt.plot(r, v)
plt.xlabel('Radius (m)')
plt.ylabel('Velocity (m/s)')
plt.title('Velocity Profile for Poiseuille Flow')
plt.grid(True)
plt.show()
