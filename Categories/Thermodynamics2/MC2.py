import numpy as np
import matplotlib.pyplot as plt

# Number of random points
n_points = 10000

# Generate random x and y coordinates between -1 and 1
x = np.random.uniform(-1, 1, n_points)
y = np.random.uniform(-1, 1, n_points)

# Calculate the radius for each point
r = np.sqrt(x**2 + y**2)

# Points inside the quarter circle
inside_circle = r <= 1

# Estimate Pi using the ratio of points inside the quarter circle
pi_estimate = 4 * np.sum(inside_circle) / n_points

print(f"Estimated Pi: {pi_estimate}")

# Plot the points
plt.figure(figsize=(6,6))
plt.scatter(x[inside_circle], y[inside_circle], color='blue', s=1, label='Inside Circle')
plt.scatter(x[~inside_circle], y[~inside_circle], color='red', s=1, label='Outside Circle')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.title(f"Monte Carlo Simulation of Pi ({n_points} points)")
plt.legend()
plt.gca().set_aspect('equal', adjustable='box')
plt.show()
