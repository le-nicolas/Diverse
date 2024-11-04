import numpy as np
import matplotlib.pyplot as plt

# Constants
R = 8.314  # Universal gas constant (J/mol·K)
n = 1      # Number of moles

# Define temperature and pressure ranges for visualization
T_range = np.linspace(300, 600, 100)  # Temperature range (K)
P_range = np.linspace(1, 10, 100)      # Pressure range (atm)

# Convert pressure to Pascals for consistency
P_range_pa = P_range * 101325

# Calculate specific volume for each temperature and pressure
def calculate_specific_volume(T, P):
    return R * T / (P * 101325)  # Specific volume (m^3/mol)

# Calculate enthalpy for each temperature
def calculate_enthalpy(T, Cv):
    U = n * Cv * T
    v = calculate_specific_volume(T, 1)  # Assume pressure = 1 atm for simplicity
    P = 101325  # Convert atm to Pa
    H = U + P * v
    return H

# Assume a constant heat capacity for simplicity
Cv = 12.5  # J/mol·K

# Generate data for each process
T = np.linspace(300, 600, 100)  # Temperature range
P_isentropic = np.linspace(1, 10, 100)  # Pressure for isentropic compression
H_isentropic = np.array([calculate_enthalpy(T[-1], Cv) for _ in P_isentropic])

P_isobaric = np.ones_like(T) * 5  # Constant pressure for isobaric heating (atm)
H_isobaric = np.array([calculate_enthalpy(t, Cv) for t in T])

P_isentropic_expansion = np.linspace(10, 1, 100)  # Pressure for isentropic expansion
H_isentropic_expansion = np.array([calculate_enthalpy(T[0], Cv) for _ in P_isentropic_expansion])

# Plotting
plt.figure(figsize=(12, 6))

# Isentropic Compression
plt.plot(H_isentropic, P_isentropic, label='Isentropic Compression', color='blue')

# Isobaric Heating
plt.plot(H_isobaric, P_isobaric, label='Isobaric Heating', color='green')

# Isentropic Expansion
plt.plot(H_isentropic_expansion, P_isentropic_expansion, label='Isentropic Expansion', color='red')

plt.xlabel('Enthalpy (J)')
plt.ylabel('Pressure (atm)')
plt.title('P-h Diagram')
plt.legend()
plt.grid(True)
plt.show()
