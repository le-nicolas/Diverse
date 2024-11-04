import numpy as np
import matplotlib.pyplot as plt

# Define the parameters
depth = 6  # depth of water in meters
rho = 997  # density of water in kg/m^3
g = 9.807  # acceleration due to gravity in m/s^2
P0 = 101325  # atmospheric pressure in Pascals (Pa)

# Calculate the pressure at the bottom
P_bottom = P0 + rho * g * depth

# Generate depth points from 0 to 6 meters
depth_points = np.linspace(0, depth, 100)
# Calculate the pressure at each depth point
pressure_points = P0 + rho * g * depth_points

# Plotting the pressure distribution
plt.figure(figsize=(10, 6))
plt.plot(pressure_points / 1000, depth_points, label='Pressure Distribution', color='blue')
plt.fill_betweenx(depth_points, P0 / 1000, pressure_points / 1000, color='skyblue', alpha=0.5)
plt.axhline(y=depth, color='gray', linestyle='--')
plt.axvline(x=P0 / 1000, color='gray', linestyle='--')
plt.axvline(x=P_bottom / 1000, color='gray', linestyle='--')

# Labels and title
plt.title('Hydrostatic Pressure Distribution in Water')
plt.xlabel('Pressure (kPa)')
plt.ylabel('Depth (m)')
plt.gca().invert_yaxis()  # Invert y-axis to have depth increasing downwards
plt.legend()

# Show the plot
plt.grid(True)
plt.show()
