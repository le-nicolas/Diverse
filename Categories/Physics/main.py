import matplotlib.pyplot as plt
import numpy as np

# Define the parameters
v0 = 50  # Initial velocity (m/s)
theta = 45  # Launch angle (degrees)
g = 9.81  # Acceleration due to gravity (m/s^2)

# Convert angle to radians
theta_rad = np.radians(theta)

# Time of flight
t_flight = 2 * v0 * np.sin(theta_rad) / g

# Time intervals
t = np.linspace(0, t_flight, num=500)

# Equations of motion
x = v0 * t * np.cos(theta_rad)
y = v0 * t * np.sin(theta_rad) - 0.5 * g * t**2

# Plot the trajectory
plt.figure(figsize=(10, 5))
plt.plot(x, y)
plt.title('Projectile Motion')
plt.xlabel('Distance (m)')
plt.ylabel('Height (m)')
plt.grid(True)
plt.ylim(bottom=0)  # Ensure the y-axis starts at 0
plt.show()
