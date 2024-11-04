import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Parameters
C = 1.0  # Heat capacity
S = 1361  # Solar constant (W/m^2)
alpha = 0.3  # Albedo
epsilon = 0.612  # Emissivity
sigma = 5.67e-8  # Stefan-Boltzmann constant (W/m^2K^4)

# Differential equation
def energy_balance(T, t, C, S, alpha, epsilon, sigma):
    dTdt = (S * (1 - alpha) - epsilon * sigma * T**4) / C
    return dTdt

# Initial temperature
T0 = 288  # Initial temperature in Kelvin

# Time points
t = np.linspace(0, 1000, 1000)

# Solve the differential equation
T = odeint(energy_balance, T0, t, args=(C, S, alpha, epsilon, sigma))

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(t, T, label='Temperature')
plt.xlabel('Time (years)')
plt.ylabel('Temperature (K)')
plt.title('Simple Energy Balance Model')
plt.grid()
plt.legend()
plt.show()
