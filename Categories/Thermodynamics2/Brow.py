
#Brownian motion is a random motion of particles suspended in a fluid (liquid or gas) resulting from their collision with the fast atoms or molecules in the gas or liquid. 
#It is a great example of a random walk and is commonly modeled using stochastic processes.
import numpy as np
import matplotlib.pyplot as plt

def simulate_brownian_motion(steps, delta_t, delta_r):
    """
    Simulate Brownian motion in 2D.

    Parameters:
    steps (int): Number of steps to simulate.
    delta_t (float): Time step size.
    delta_r (float): Scale of random displacements.

    Returns:
    np.ndarray: Array of (x, y) positions of the particle over time.
    """
    # Initialize arrays to hold x and y positions
    x_positions = np.zeros(steps)
    y_positions = np.zeros(steps)

    # Simulate Brownian motion
    for i in range(1, steps):
        # Generate random displacements for x and y
        dx = delta_r * np.sqrt(delta_t) * np.random.randn()
        dy = delta_r * np.sqrt(delta_t) * np.random.randn()

        # Update positions
        x_positions[i] = x_positions[i - 1] + dx
        y_positions[i] = y_positions[i - 1] + dy

    return x_positions, y_positions

# Parameters for the simulation
steps = 1000       # Number of steps
delta_t = 1        # Time step size
delta_r = 1        # Scale of random displacements

# Simulate Brownian motion
x_positions, y_positions = simulate_brownian_motion(steps, delta_t, delta_r)

# Plot the trajectory of the particle
plt.figure(figsize=(8, 8))
plt.plot(x_positions, y_positions, linestyle='-', color='b', marker='o', markersize=2, label='Particle Trajectory')
plt.title('Brownian Motion of a Particle in 2D')
plt.xlabel('X Position')
plt.ylabel('Y Position')
plt.grid(True)
plt.legend()
plt.show()
