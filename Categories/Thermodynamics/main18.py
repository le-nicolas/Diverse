import numpy as np
import matplotlib.pyplot as plt

# Define state points for the Otto cycle
def otto_cycle(V1, V2, P1, T1, gamma):
    # Step 1: Isentropic Compression (1 -> 2)
    V_compress = np.linspace(V1, V2, 100)
    P_compress = P1 * (V1 / V_compress)**gamma
    
    # Step 2: Constant-volume Heat Addition (2 -> 3)
    V_add_heat = np.array([V2, V2])
    P_add_heat = np.array([P_compress[-1], P_compress[-1] * 2])  # Arbitrary heat addition
    
    # Step 3: Isentropic Expansion (3 -> 4)
    V_expand = np.linspace(V2, V1, 100)
    P_expand = P_add_heat[-1] * (V2 / V_expand)**gamma
    
    # Step 4: Constant-volume Heat Rejection (4 -> 1)
    V_reject_heat = np.array([V1, V1])
    P_reject_heat = np.array([P_expand[-1], P1])  # Returning to initial pressure
    
    return (V_compress, P_compress), (V_add_heat, P_add_heat), (V_expand, P_expand), (V_reject_heat, P_reject_heat)

# Constants for air
gamma = 1.4  # Heat capacity ratio for air
V1 = 1.0  # Initial volume in cubic meters
V2 = 0.5  # Compressed volume in cubic meters
P1 = 101325  # Initial pressure in Pascals (1 atm)
T1 = 300  # Initial temperature in Kelvin

# Get the process states
(V_compress, P_compress), (V_add_heat, P_add_heat), (V_expand, P_expand), (V_reject_heat, P_reject_heat) = otto_cycle(V1, V2, P1, T1, gamma)

# Plot the Otto cycle on a P-V diagram
plt.figure(figsize=(8, 6))
plt.plot(V_compress, P_compress, label='Isentropic Compression (1 -> 2)', color='b')
plt.plot(V_add_heat, P_add_heat, label='Constant Volume Heat Addition (2 -> 3)', color='r')
plt.plot(V_expand, P_expand, label='Isentropic Expansion (3 -> 4)', color='g')
plt.plot(V_reject_heat, P_reject_heat, label='Constant Volume Heat Rejection (4 -> 1)', color='purple')

plt.xlabel('Volume (m^3)')
plt.ylabel('Pressure (Pa)')
plt.title('Otto Cycle P-V Diagram')
plt.legend()
plt.grid(True)
plt.show()
