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

# RK4 method functions
def derivatives(t, state):
    """Returns the derivatives of the state variables."""
    x, y, vx, vy = state
    dxdt = vx
    dydt = vy
    dvxdt = 0
    dvydt = -g
    return np.array([dxdt, dydt, dvxdt, dvydt])

def rk4_step(t, state, dt):
    """Performs one step of the RK4 method."""
    k1 = dt * derivatives(t, state)
    k2 = dt * derivatives(t + dt / 2, state + k1 / 2)
    k3 = dt * derivatives(t + dt / 2, state + k2 / 2)
    k4 = dt * derivatives(t + dt, state + k3)
    return state + (k1 + 2 * k2 + 2 * k3 + k4) / 6

# Simulation loop
state = np.array([x, y, vx, vy])
t = 0
while state[1] >= 0:
    state = rk4_step(t, state, dt)
    x_points.append(state[0])
    y_points.append(state[1])
    t += dt

# Plot the trajectory
plt.figure(figsize=(10, 5))
plt.plot(x_points, y_points)
plt.title('Projectile Motion Using RK4 Method')
plt.xlabel('Distance (m)')
plt.ylabel('Height (m)')
plt.grid(True)
plt.ylim(bottom=0)
plt.show()
