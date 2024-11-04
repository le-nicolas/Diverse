import numpy as np
import matplotlib.pyplot as plt

# Set up the grid for temperature values
x = np.linspace(-5, 5, 20)
y = np.linspace(-5, 5, 20)
X, Y = np.meshgrid(x, y)

# Define a temperature field (hypothetically)
T = np.exp(-(X**2 + Y**2))  # Gaussian distribution (higher in the center)

# Compute the temperature gradient (representing heat flow)
dT_dx, dT_dy = np.gradient(T)

# Plot the temperature field as a contour
plt.contourf(X, Y, T, cmap='hot')
plt.colorbar(label='Temperature')

# Plot the heat flux (vector field)
plt.quiver(X, Y, -dT_dx, -dT_dy, color='blue')  # Negative gradient represents heat flow direction

plt.title("Heat Flow Vector Field")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()
