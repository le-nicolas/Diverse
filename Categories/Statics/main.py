import numpy as np

# Force magnitudes
F1 = 180  # lb
F2 = 300  # lb

# Angles for F1 and F2
theta1 = np.radians(40)  # Angle with z-axis for F1
phi1 = np.radians(30)    # Angle in the x-y plane for F1
theta2 = np.radians(30)  # Angle with x-axis for F2

# F1 components
F1x = F1 * np.cos(phi1) * np.sin(theta1)
F1y = F1 * np.sin(phi1) * np.sin(theta1)
F1z = F1 * np.cos(theta1)

# F2 components
F2x = F2 * np.cos(theta2)
F2y = F2 * np.sin(theta2)
F2z = 0  # Since F2 is in the x-y plane

# Summing components
Rx = F1x + F2x
Ry = F1y + F2y
Rz = F1z + F2z

# Resultant force magnitude
R = np.sqrt(Rx**2 + Ry**2 + Rz**2)

# Direction angles for resultant force
alpha = np.degrees(np.arccos(Rx / R))  # Angle with x-axis
beta = np.degrees(np.arccos(Ry / R))   # Angle with y-axis
gamma = np.degrees(np.arccos(Rz / R))  # Angle with z-axis

print(f"Resultant Force: {R:.2f} lb")
print(f"Direction Angles: α = {alpha:.2f}°, β = {beta:.2f}°, γ = {gamma:.2f}°")
