import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Define the ODE system
def model(y, t):
    dydt = -y + np.sin(t)
    return dydt

# Initial condition
y0 = 0

# Time points where solution is computed
t = np.linspace(0, 10, 100)

# Solve ODE
y = odeint(model, y0, t)

# Plot results
plt.plot(t, y)
plt.xlabel('Time')
plt.ylabel('y(t)')
plt.title('Solution of the ODE dy/dt = -y + sin(t)')
plt.show()
