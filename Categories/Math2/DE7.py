import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
# Lotka-Volterra Model
def lotka_volterra(X, t, r1, a, b, d):
    N1, N2 = X
    dN1dt = r1 * N1 - a * N1 * N2
    dN2dt = b * N1 * N2 - d * N2
    return [dN1dt, dN2dt]

# Initial conditions
N1_0 = 40
N2_0 = 9
r1 = 0.1  # Prey growth rate
a = 0.02  # Predation rate coefficient
b = 0.01  # Reproduction rate of predators
d = 0.1   # Predator death rate

# Time points
t = np.linspace(0, 200, 1000)

# Solve ODEs
solution = odeint(lotka_volterra, [N1_0, N2_0], t, args=(r1, a, b, d))
N1, N2 = solution.T

# Plot results
plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(t, N1, label='Prey Population')
plt.plot(t, N2, label='Predator Population')
plt.xlabel('Time')
plt.ylabel('Population Size')
plt.legend()
plt.grid()

plt.subplot(2, 1, 2)
plt.plot(N1, N2)
plt.xlabel('Prey Population')
plt.ylabel('Predator Population')
plt.grid()
plt.title('Phase Plane')

plt.tight_layout()
plt.show()
