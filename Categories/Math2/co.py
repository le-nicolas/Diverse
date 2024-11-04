import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Define symbols
t = sp.symbols('t', real=True)
z = sp.Function('z')(t)
a, b = sp.symbols('a b', complex=True)

# Define the differential equation
de = sp.Eq(sp.diff(z, t) + a*z, b)

# Solve the differential equation analytically
z_sol = sp.dsolve(de)
print(f"General Solution: {z_sol}")

# Define initial conditions (for example, z(0) = 1 + 0j)
z0 = 1 + 0j
C1 = sp.symbols('C1')
sol = z_sol.subs('C1', sp.solve(z_sol.rhs.subs(t, 0) - z0, 'C1')[0])

print(f"Solution with Initial Condition: {sol}")

# Define parameter values
a_val = 1 + 1j  # Example value for a
b_val = 0 + 1j  # Example value for b

# Substitute parameter values into the solution
sol_with_params = sol.subs({a: a_val, b: b_val})

# Convert to a numerical function
z_func = sp.lambdify(t, sol_with_params.rhs, "numpy")

# Define time array
time = np.linspace(0, 10, 400)

# Compute numerical values
z_values = z_func(time)

# Plot the real and imaginary parts of the solution
plt.figure(figsize=(12, 6))
plt.plot(time, z_values.real, label='Real part of z(t)')
plt.plot(time, z_values.imag, label='Imaginary part of z(t)')
plt.xlabel('Time')
plt.ylabel('z(t)')
plt.title('Solution of Complex Differential Equation')
plt.legend()
plt.grid(True)
plt.show()
