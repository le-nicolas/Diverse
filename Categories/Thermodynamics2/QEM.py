import numpy as np
import matplotlib.pyplot as plt

# Parameters
mass = 2.0  # Mass of the substance (kg)
specific_heat_capacity = 900  # Specific heat capacity (J/kg·K) for example, Aluminum
temperature_initial = 20.0  # Initial temperature (°C)
temperature_final = 100.0  # Final temperature (°C)

# Calculate the energy required
def calculate_energy(mass, specific_heat_capacity, T_initial, T_final):
    delta_T = T_final - T_initial
    Q = mass * specific_heat_capacity * delta_T
    return Q

# Calculate energy
energy_required = calculate_energy(mass, specific_heat_capacity, temperature_initial, temperature_final)
print(f"Energy required to heat {mass} kg of substance from {temperature_initial}°C to {temperature_final}°C: {energy_required:.2f} J")

# Plotting temperature vs. energy
temperatures = np.linspace(temperature_initial, temperature_final, 100)
energies = [calculate_energy(mass, specific_heat_capacity, temperature_initial, T) for T in temperatures]

plt.figure(figsize=(8, 6))
plt.plot(temperatures, energies, label='Energy vs. Temperature')
plt.xlabel('Temperature (°C)')
plt.ylabel('Energy Required (J)')
plt.title('Energy Required to Change Temperature of a Substance')
plt.legend()
plt.grid(True)
plt.show()
