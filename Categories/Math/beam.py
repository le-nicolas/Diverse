import numpy as np
import matplotlib.pyplot as plt

# Beam parameters
L = 10  # Length of the beam (m)
q = 1000  # Uniform load per unit length (N/m)
E = 200e9  # Young's modulus (Pa)
I = 0.0001  # Moment of inertia (m^4)

# Define the deflection function based on the derived formula
def beam_deflection(x, L, q, E, I):
    return (-q * L / (12 * E * I)) * x**3 + (q / (24 * E * I)) * x**4

# Generate x values from 0 to L
x_values = np.linspace(0, L, 400)
# Calculate the deflection values for these x values
deflection_values = beam_deflection(x_values, L, q, E, I)

# Plotting the deflection of the beam
plt.figure(figsize=(10, 6))
plt.plot(x_values, deflection_values, label='Beam Deflection', color='blue')
plt.title('Deflection of a Simply Supported Beam Under Uniform Load')
plt.xlabel('Position along the beam (x) [m]')
plt.ylabel('Deflection (y) [m]')
plt.legend()
plt.grid(True)
plt.show()
