import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

# Beam parameters
L = 10  # Length of the beam (m)
q = 1000  # Uniform load per unit length (N/m)
E = 200e9  # Young's modulus (Pa)
I = 0.0001  # Moment of inertia (m^4)
n_terms = 10  # Number of terms in the power series

# Define the power series for the deflection
def power_series_deflection(x, coeffs):
    return sum(c * x**i for i, c in enumerate(coeffs))

# Residuals calculation based on the differential equation
def residuals(coeffs, x_values):
    res = []
    for x in x_values:
        dy4_dx4 = sum(c * (i * (i-1) * (i-2) * (i-3) * x**(i-4)) if i >= 4 else 0 for i, c in enumerate(coeffs))
        res.append(dy4_dx4 - q / (E * I))
    return np.array(res)

# Objective function to minimize the sum of squared residuals
def objective_function(coeffs, x_values):
    res = residuals(coeffs, x_values)
    return np.sum(res**2)

# Boundary condition functions
def apply_boundary_conditions(coeffs):
    coeffs[0] = 0  # y(0) = 0
    coeffs[1] = 0  # y'(0) = 0
    coeffs[2] = 0  # y''(0) = 0

    # Additional boundary conditions at x = L
    deflection_L = sum(c * L**i for i, c in enumerate(coeffs))
    moment_L = sum(c * (i * (i-1) * L**(i-2)) if i >= 2 else 0 for i, c in enumerate(coeffs))

    coeffs[3] -= deflection_L / (L**3)  # Adjust to ensure y(L) = 0
    coeffs[4] -= moment_L / (L**4)  # Adjust to ensure y''(L) = 0

    return coeffs

# Initial guess for the coefficients
initial_guess = np.zeros(n_terms)

# Generate x values for residual calculation
x_values = np.linspace(0, L, 100)

# Optimize the coefficients with boundary conditions
result = minimize(lambda coeffs: objective_function(apply_boundary_conditions(coeffs), x_values), initial_guess)
coeffs = apply_boundary_conditions(result.x)

# Generate x values for plotting
x_plot = np.linspace(0, L, 400)
# Calculate the deflection values for these x values
deflection_values = [power_series_deflection(x, coeffs) for x in x_plot]

# Plotting the deflection of the beam
plt.figure(figsize=(10, 6))
plt.plot(x_plot, deflection_values, label='Beam Deflection (Power Series)', color='blue')
plt.title('Deflection of a Simply Supported Beam Under Uniform Load (Power Series)')
plt.xlabel('Position along the beam (x) [m]')
plt.ylabel('Deflection (y) [m]')
plt.legend()
plt.grid(True)
plt.show()
