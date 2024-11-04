import numpy as np
import matplotlib.pyplot as plt

# Beam parameters
L = 10  # Length of the beam
q = 10  # Uniform load per unit length
E = 200e9  # Young's modulus in Pascals
I = 0.0001  # Moment of inertia in m^4

# Number of terms in the power series
n_terms = 10

# Calculate the power series coefficients for the beam deflection
def compute_beam_deflection_coefficients(L, q, E, I, n_terms):
    # The solution to the differential equation with boundary conditions
    # is derived based on beam theory. For simplicity, we use the series expansion
    # for the deflection of a simply supported beam.
    coefficients = [0] * n_terms
    
    # Known solution for a simply supported beam under uniform load:
    # y(x) = (q / (24 * E * I)) * x^2 * (L^2 - x^2)
    # Expanding this into a power series, we get coefficients.
    for n in range(n_terms):
        if n % 2 == 0:  # Only even terms are non-zero
            coefficients[n] = (q / (24 * E * I)) * ((L**2) if n == 2 else (-1)**(n//2) * L**(n-2) / np.math.factorial(n))
    
    return coefficients

# Compute the deflection using the power series
def beam_deflection_power_series(x, coefficients):
    return sum(coeff * x**n for n, coeff in enumerate(coefficients))

# Visualization
def plot_beam_deflection():
    x_values = np.linspace(0, L, 400)
    coefficients = compute_beam_deflection_coefficients(L, q, E, I, n_terms)
    
    # Compute the deflection using the power series
    deflection_values = [beam_deflection_power_series(x, coefficients) for x in x_values]
    
    plt.figure(figsize=(10, 6))
    plt.plot(x_values, deflection_values, label='Beam Deflection', color='blue')
    plt.title('Deflection of a Simply Supported Beam Under Uniform Load')
    plt.xlabel('x (m)')
    plt.ylabel('Deflection y(x) (m)')
    plt.legend()
    plt.grid(True)
    plt.show()

plot_beam_deflection()
