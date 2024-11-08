import numpy as np
import matplotlib.pyplot as plt

# Define material properties
elastic_modulus = 200  # Elastic modulus in GPa (Gigapascals) for steel
yield_strength = 0.4  # Yield strength in GPa
plastic_modulus = 10  # Plastic modulus in GPa (lower than elastic modulus)

# Define the maximum force to apply
max_force = 1.0  # in GPa
force_steps = 100

# Initialize force and deformation arrays
forces = np.linspace(0, max_force, force_steps)
deformations = np.zeros(force_steps)

for i, force in enumerate(forces):
    if force <= yield_strength:
        # Elastic deformation (Hooke's Law: F = k*x -> x = F/k)
        deformations[i] = force / elastic_modulus
    else:
        # Plastic deformation
        elastic_deformation = yield_strength / elastic_modulus
        plastic_force = force - yield_strength
        plastic_deformation = plastic_force / plastic_modulus
        deformations[i] = elastic_deformation + plastic_deformation

# Plotting the force vs. deformation curve
plt.figure(figsize=(10, 6))
plt.plot(deformations, forces, label='Force vs Deformation Curve', color='b')
plt.axvline(x=yield_strength / elastic_modulus, color='r', linestyle='--', label='Yield Point')
plt.xlabel('Deformation (strain)')
plt.ylabel('Force (GPa)')
plt.title('Force vs Deformation Curve')
plt.legend()
plt.grid(True)
plt.show()
