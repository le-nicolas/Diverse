import numpy as np
import matplotlib.pyplot as plt

# Constants
R = 8.314  # Universal gas constant (J/mol·K)
n = 1      # Number of moles
T_H = 500  # Temperature of hot reservoir (K)
T_C = 300  # Temperature of cold reservoir (K)
V1 = 1     # Initial volume (m^3)
V2 = 2     # Final volume (m^3)

# Define temperatures for isothermal processes
T_isothermal_expansion = T_H
T_isothermal_compression = T_C

# Define volumes for the cycle (assumed for simplicity)
V = np.array([V1, V2, V2, V1])  # Volumes during different processes
T = np.array([T_H, T_H, T_C, T_C])  # Temperatures during different processes

# Calculate pressures using the ideal gas law: P = nRT / V
P = np.array([n * R * T[i] / V[i] for i in range(4)])

# Plotting the Carnot cycle
plt.figure(figsize=(12, 6))

# Pressure-Volume (P-V) diagram
plt.subplot(1, 2, 1)
plt.plot(V, P, marker='o')
plt.title('Carnot Cycle - P-V Diagram')
plt.xlabel('Volume (m^3)')
plt.ylabel('Pressure (Pa)')
plt.grid(True)

# Temperature-Entropy (T-S) diagram
# For simplicity, use the volume to represent the entropy change
S = np.array([R * np.log(V[i] / V1) for i in range(4)])

plt.subplot(1, 2, 2)
plt.plot(S, T, marker='o')
plt.title('Carnot Cycle - T-S Diagram')
plt.xlabel('Entropy (J/K)')
plt.ylabel('Temperature (K)')
plt.grid(True)

plt.tight_layout()
plt.show()

# Calculate Carnot efficiency
def carnot_efficiency(T_H, T_C):
    return 1 - (T_C / T_H)

efficiency = carnot_efficiency(T_H, T_C)
print(f"Carnot Efficiency: {efficiency:.2%}")
