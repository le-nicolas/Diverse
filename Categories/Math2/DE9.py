import sympy as sp

# Define symbols
t, s = sp.symbols('t s')
Q, V1, V2, C_in = sp.symbols('Q V1 V2 C_in', positive=True, real=True)
C1_0, C2_0 = sp.symbols('C1_0 C2_0', real=True)

# Define Laplace Transforms
C1_s = (Q * C_in / (V1 * s * (s + Q / V1))) + (C1_0 / (s + Q / V1))
C2_eq = sp.Eq(s * sp.Function('C2')(s) - C2_0, Q / V2 * (C1_s - sp.Function('C2')(s)))
C2_s = sp.solve(C2_eq, sp.Function('C2')(s))[0]

# Inverse Laplace Transform
C1_t = sp.inverse_laplace_transform(C1_s, s, t)
C2_t = sp.inverse_laplace_transform(C2_s, s, t)

C1_t, C2_t


import numpy as np
import matplotlib.pyplot as plt

# Define parameter values
Q_val = 1.0   # Flow rate
V1_val = 10.0 # Volume of tank 1
V2_val = 10.0 # Volume of tank 2
C_in_val = 1.0 # Incoming concentration of salt
C1_0_val = 0.0 # Initial concentration in tank 1
C2_0_val = 0.0 # Initial concentration in tank 2

# Define time array
time = np.linspace(0, 10, 400)

# Convert symbolic expressions to numerical functions
C1_func = sp.lambdify(t, C1_t.subs({Q: Q_val, V1: V1_val, C_in: C_in_val, C1_0: C1_0_val}), "numpy")
C2_func = sp.lambdify(t, C2_t.subs({Q: Q_val, V2: V2_val, V1: V1_val, C_in: C_in_val, C1_0: C1_0_val, C2_0: C2_0_val}), "numpy")

# Compute numerical values
C1_values = np.array([C1_func(ti) for ti in time])
C2_values = np.array([C2_func(ti) for ti in time])

# Plot the results
plt.figure(figsize=(12, 6))
plt.plot(time, C1_values, label='Concentration in Tank 1 (C1)')
plt.plot(time, C2_values, label='Concentration in Tank 2 (C2)')
plt.xlabel('Time')
plt.ylabel('Concentration')
plt.title('Concentration of Salt in Two Connected Tanks Over Time')
plt.legend()
plt.grid(True)
plt.show()
