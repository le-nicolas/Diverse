import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Exponential Growth Model
def exponential_growth(N, t, r):
    dNdt = r * N
    return dNdt

# Logistic Growth Model
def logistic_growth(N, t, r, K):
    dNdt = r * N * (1 - N / K)
    return dNdt

# Initial conditions
N0 = 10
r = 0.1  # Growth rate
K = 100  # Carrying capacity

# Time points
t = np.linspace(0, 100, 1000)

# Solve ODEs
N_exp = odeint(exponential_growth, N0, t, args=(r,))
N_log = odeint(logistic_growth, N0, t, args=(r, K))

# Plot results
plt.figure(figsize=(12, 6))

plt.plot(t, N_exp, label='Exponential Growth')
plt.plot(t, N_log, label='Logistic Growth')
plt.xlabel('Time')
plt.ylabel('Population Size')
plt.legend()
plt.grid()
plt.title('Exponential vs Logistic Growth')
plt.show()
