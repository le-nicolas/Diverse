import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define state points for the Otto cycle
def otto_cycle(V1, V2, P1, gamma):
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

# Get the process states
(V_compress, P_compress), (V_add_heat, P_add_heat), (V_expand, P_expand), (V_reject_heat, P_reject_heat) = otto_cycle(V1, V2, P1, gamma)

# Create a figure and axis for the plot
fig, ax = plt.subplots(figsize=(8, 6))
ax.set_xlim(V1 * 0.9, V2 * 1.1)
ax.set_ylim(P1 * 0.9, P_add_heat[-1] * 1.1)
ax.set_xlabel('Volume (m^3)')
ax.set_ylabel('Pressure (Pa)')
ax.set_title('Otto Cycle P-V Diagram')
ax.grid(True)

# Initialize line objects for each process
line, = ax.plot([], [], lw=2)

# Animation function: updates the lines during the animation
def animate(i):
    # Clear current plot
    ax.clear()
    
    # Plot segments based on the frame index i
    if i < len(V_compress):  # Isentropic Compression
        ax.plot(V_compress[:i], P_compress[:i], color='b', lw=2)
    elif i < len(V_compress) + len(V_add_heat):  # Constant-Volume Heat Addition
        ax.plot(V_compress, P_compress, color='b', lw=2)
        ax.plot(V_add_heat[:i-len(V_compress)+1], P_add_heat[:i-len(V_compress)+1], color='r', lw=2)
    elif i < len(V_compress) + len(V_add_heat) + len(V_expand):  # Isentropic Expansion
        ax.plot(V_compress, P_compress, color='b', lw=2)
        ax.plot(V_add_heat, P_add_heat, color='r', lw=2)
        ax.plot(V_expand[:i-len(V_compress)-len(V_add_heat)+1], P_expand[:i-len(V_compress)-len(V_add_heat)+1], color='g', lw=2)
    else:  # Constant-Volume Heat Rejection
        ax.plot(V_compress, P_compress, color='b', lw=2)
        ax.plot(V_add_heat, P_add_heat, color='r', lw=2)
        ax.plot(V_expand, P_expand, color='g', lw=2)
        ax.plot(V_reject_heat[:i-len(V_compress)-len(V_add_heat)-len(V_expand)+1], P_reject_heat[:i-len(V_compress)-len(V_add_heat)-len(V_expand)+1], color='purple', lw=2)
    
    ax.set_xlim(V1 * 0.9, V2 * 1.1)
    ax.set_ylim(P1 * 0.9, P_add_heat[-1] * 1.1)
    ax.set_xlabel('Volume (m^3)')
    ax.set_ylabel('Pressure (Pa)')
    ax.set_title('Otto Cycle P-V Diagram')
    ax.grid(True)

# Create the animation
anim = FuncAnimation(fig, animate, frames=400, interval=10)

# Show the animation
plt.show()
