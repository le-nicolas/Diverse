import numpy as np
import matplotlib.pyplot as plt

# Parameters
K = 10  # Hydraulic conductivity
L = 100  # Length of the aquifer
n = 100  # Number of grid points
h0 = 10  # Hydraulic head at the left boundary
hL = 5   # Hydraulic head at the right boundary

# Discretization
dx = L / (n - 1)
x = np.linspace(0, L, n)

# Initialize hydraulic head array
h = np.zeros(n)
h[0] = h0
h[-1] = hL

# Finite difference method to solve the steady-state equation
for i in range(1, n-1):
    h[i] = (h[i-1] + h[i+1]) / 2

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(x, h, label='Hydraulic Head')
plt.xlabel('Distance (x)')
plt.ylabel('Hydraulic Head (h)')
plt.title('1D Steady-State Groundwater Flow')
plt.grid()
plt.legend()
plt.show()
