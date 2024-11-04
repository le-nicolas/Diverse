import numpy as np
import matplotlib.pyplot as plt

# Constants
gamma = 1.4  # Adiabatic index for air
R = 287.05  # Gas constant for air (J/kg·K)
V1 = 0.001  # Initial volume in cubic meters (m^3)
V2 = 0.0005  # Compressed volume in cubic meters
P1 = 101325  # Initial pressure in Pascals (Pa)
T1 = 300  # Initial temperature in Kelvin (K)

# Functions for state transitions
def isentropic_compression(V1, V2, P1, T1, gamma):
    """Returns pressure and temperature after isentropic compression."""
    P2 = P1 * (V1 / V2)**gamma
    T2 = T1 * (V1 / V2)**(gamma - 1)
    return P2, T2

def constant_volume_heat_addition(P2, T2, Q_in, R):
    """Returns pressure and temperature after heat addition."""
    T3 = T2 + Q_in / R  # Using ideal gas law, Q_in in Joules
    P3 = P2 * (T3 / T2)
    return P3, T3

def isentropic_expansion(V2, V1, P3, T3, gamma):
    """Returns pressure and temperature after isentropic expansion."""
    P4 = P3 * (V2 / V1)**gamma
    T4 = T3 * (V2 / V1)**(gamma - 1)
    return P4, T4

def constant_volume_heat_rejection(P4, T4, Q_out, R):
    """Returns pressure and temperature after heat rejection."""
    T1_new = T4 - Q_out / R
    P1_new = P4 * (T1_new / T4)
    return P1_new, T1_new

# Simulating the Otto cycle
Q_in = 1500  # Heat added during combustion (Joules)
Q_out = 800  # Heat rejected during exhaust (Joules)

# Step 1: Isentropic compression (1 -> 2)
P2, T2 = isentropic_compression(V1, V2, P1, T1, gamma)

# Step 2: Constant volume heat addition (2 -> 3)
P3, T3 = constant_volume_heat_addition(P2, T2, Q_in, R)

# Step 3: Isentropic expansion (3 -> 4)
P4, T4 = isentropic_expansion(V2, V1, P3, T3, gamma)

# Step 4: Constant volume heat rejection (4 -> 1)
P1_new, T1_new = constant_volume_heat_rejection(P4, T4, Q_out, R)

# Displaying the results
print(f"Pressure after compression (P2): {P2} Pa")
print(f"Temperature after compression (T2): {T2} K")
print(f"Pressure after heat addition (P3): {P3} Pa")
print(f"Temperature after heat addition (T3): {T3} K")
print(f"Pressure after expansion (P4): {P4} Pa")
print(f"Temperature after expansion (T4): {T4} K")
print(f"Final pressure after heat rejection (P1_new): {P1_new} Pa")
print(f"Final temperature after heat rejection (T1_new): {T1_new} K")

# Plotting the simulation results (P-V diagram)
V_compress = np.linspace(V1, V2, 100)
P_compress = P1 * (V1 / V_compress)**gamma
V_expand = np.linspace(V2, V1, 100)
P_expand = P3 * (V2 / V_expand)**gamma

# Plot
plt.plot(V_compress, P_compress, label="Isentropic Compression")
plt.plot([V2, V2], [P2, P3], label="Heat Addition (Constant Volume)", color='r')
plt.plot(V_expand, P_expand, label="Isentropic Expansion", color='g')
plt.plot([V1, V1], [P4, P1_new], label="Heat Rejection (Constant Volume)", color='purple')

plt.xlabel('Volume (m^3)')
plt.ylabel('Pressure (Pa)')
plt.title('Otto Cycle - P-V Diagram')
plt.grid(True)
plt.legend()
plt.show()
