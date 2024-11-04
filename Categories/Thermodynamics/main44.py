import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants
gamma = 1.4  # Ratio of specific heats (Cp/Cv) for air
P_initial = 500000  # Initial pressure in Pascals
V_initial = 0.001   # Initial volume in cubic meters
V_final = 0.003     # Final volume in cubic meters
n = 1  # Number of moles of gas
R = 8.314  # Gas constant

# Calculate initial temperature using the ideal gas law: PV = nRT
T_initial = (P_initial * V_initial) / (n * R)

# Function for calculating pressure during adiabatic expansion: P*V^gamma = constant
def adiabatic_pressure(V):
    return P_initial * (V_initial / V) ** gamma

# Create volume and pressure data for the PV diagram
V_values = np.linspace(V_initial, V_final, 300)
P_values = adiabatic_pressure(V_values)

# Setup the figure for animation
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

# Piston axis
ax1.set_xlim(0, V_final * 1.1)
ax1.set_ylim(0, 0.5)
ax1.set_xlabel('Piston Position')
ax1.set_ylabel('Piston Height')

# PV diagram axis
ax2.set_xlim(V_initial, V_final)
ax2.set_ylim(0, P_initial)
ax2.set_xlabel('Volume (m^3)')
ax2.set_ylabel('Pressure (Pa)')
ax2.set_title('Adiabatic Expansion (PV Diagram)')

# Initialize plots for piston and PV diagram
piston, = ax1.plot([], [], 'o-', lw=2)
pv_line, = ax2.plot([], [], lw=2)

# Function to update the piston and PV plot during animation
def update(frame):
    # Update piston position
    V_current = V_values[frame]
    piston_x = [0, V_current]  # Horizontal piston motion
    piston_y = [0.1, 0.1]      # Vertical piston height
    piston.set_data(piston_x, piston_y)

    # Update the PV diagram with the current state
    pv_line.set_data(V_values[:frame], P_values[:frame])

    return piston, pv_line

# Create animation
ani = FuncAnimation(fig, update, frames=len(V_values), interval=50, blit=True)

# Display the animation
plt.tight_layout()
plt.show()
