import matplotlib.pyplot as plt
import numpy as np

# Parameters
v0 = 50  # Initial velocity (m/s)
theta = 45  # Launch angle (degrees)
g = 9.81  # Acceleration due to gravity (m/s^2)
dt = 0.01  # Time step (s)

# Convert angle to radians
theta_rad = np.radians(theta)

# Initial conditions
vx = v0 * np.cos(theta_rad)
vy = v0 * np.sin(theta_rad)
x = 0
y = 0

# Lists to store trajectory points
x_points = [x]
y_points = [y]

# Euler method loop
while y >= 0:
    x += vx * dt
    y += vy * dt
    vy -= g * dt

    x_points.append(x)
    y_points.append(y)

# Plot the trajectory
plt.figure(figsize=(10, 5))
plt.plot(x_points, y_points)
plt.title('Projectile Motion Using Euler Method')
plt.xlabel('Distance (m)')
plt.ylabel('Height (m)')
plt.grid(True)
plt.ylim(bottom=0)
plt.show()
