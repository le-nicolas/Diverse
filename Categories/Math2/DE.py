import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Define the differential equations
def lotka_volterra(z, t, alpha, beta, delta, gamma):
    x, y = z
    dxdt = alpha * x - beta * x * y
    dydt = delta * x * y - gamma * y
    return [dxdt, dydt]

# Parameters
alpha = 1.1
beta = 0.4
delta = 0.1
gamma = 0.4

# Initial conditions: 40 prey and 9 predators
z0 = [40, 9]

# Time points where the solution is computed
t = np.linspace(0, 50, 500)

# Solve the differential equations
solution = odeint(lotka_volterra, z0, t, args=(alpha, beta, delta, gamma))

# Plot the results
prey, predators = solution.T
plt.figure(figsize=(10, 6))
plt.plot(t, prey, label='Prey')
plt.plot(t, predators, label='Predators')
plt.xlabel('Time')
plt.ylabel('Population')
plt.title('Lotka-Volterra Predator-Prey Model')
plt.legend()
plt.grid()
plt.show()
