import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Constants
C_m = 1.0  # Membrane capacitance, in uF/cm^2
g_Na = 120.0  # Maximum conductances, in mS/cm^2
g_K = 36.0
g_L = 0.3
V_Na = 50.0  # Nernst reversal potentials, in mV
V_K = -77.0
V_L = -54.387

# External current
I_ext = 10.0  # in uA/cm^2

# Alpha and beta functions for gating variables
def alpha_m(V): return 0.1 * (V + 40.0) / (1 - np.exp(-(V + 40.0) / 10.0))
def beta_m(V): return 4.0 * np.exp(-(V + 65.0) / 18.0)
def alpha_h(V): return 0.07 * np.exp(-(V + 65.0) / 20.0)
def beta_h(V): return 1.0 / (1 + np.exp(-(V + 35.0) / 10.0))
def alpha_n(V): return 0.01 * (V + 55.0) / (1 - np.exp(-(V + 55.0) / 10.0))
def beta_n(V): return 0.125 * np.exp(-(V + 65.0) / 80.0)

# The Hodgkin-Huxley model differential equations
def hodgkin_huxley(y, t, I_ext):
    V, m, h, n = y

    # Gating variable derivatives
    dmdt = alpha_m(V) * (1 - m) - beta_m(V) * m
    dhdt = alpha_h(V) * (1 - h) - beta_h(V) * h
    dndt = alpha_n(V) * (1 - n) - beta_n(V) * n

    # Ionic currents
    I_Na = g_Na * m**3 * h * (V - V_Na)
    I_K = g_K * n**4 * (V - V_K)
    I_L = g_L * (V - V_L)

    # Membrane potential derivative
    dVdt = (I_ext - I_Na - I_K - I_L) / C_m

    return [dVdt, dmdt, dhdt, dndt]

# Initial conditions
V0 = -65.0
m0 = 0.05
h0 = 0.6
n0 = 0.32
y0 = [V0, m0, h0, n0]

# Time vector
t = np.linspace(0, 50, 10000)  # 50 ms, 10000 points

# Solve ODE
solution = odeint(hodgkin_huxley, y0, t, args=(I_ext,))

# Extract results
V = solution[:, 0]
m = solution[:, 1]
h = solution[:, 2]
n = solution[:, 3]

# Plot results
plt.figure(figsize=(12, 8))

plt.subplot(2, 1, 1)
plt.plot(t, V, label='Membrane Potential (V)')
plt.xlabel('Time (ms)')
plt.ylabel('Membrane Potential (mV)')
plt.legend()
plt.grid()

plt.subplot(2, 1, 2)
plt.plot(t, m, label='m-gate')
plt.plot(t, h, label='h-gate')
plt.plot(t, n, label='n-gate')
plt.xlabel('Time (ms)')
plt.ylabel('Gating Variables')
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()

