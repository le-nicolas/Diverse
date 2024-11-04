import matplotlib.pyplot as plt

# Data from the table (Pressure in kPa, Specific Volume in m^3/kg)
pressure = [2.34, 500, 2000, 5000, 15000, 50000]
specific_volume = [0.001002, 0.001002, 0.001001, 0.001000, 0.000995, 0.000980]

# Calculate changes in specific volume (delta_v) between each point
delta_v = [specific_volume[i] - specific_volume[i+1] for i in range(len(specific_volume)-1)]

# Print the changes
for i, dv in enumerate(delta_v):
    print(f"Change in specific volume from state {chr(97+i)} to {chr(98+i)}: {dv:.8f} m^3/kg")

# Plot the specific volume vs pressure
plt.figure(figsize=(8,6))
plt.plot(pressure, specific_volume, marker='o')
plt.xlabel('Pressure (kPa)')
plt.ylabel('Specific Volume (m^3/kg)')
plt.title('Specific Volume vs Pressure for Water at 20°C')
plt.grid(True)
plt.xscale('log')  # Logarithmic scale for better visualization
plt.show()
