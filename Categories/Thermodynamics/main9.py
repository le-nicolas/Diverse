import pandas as pd

# Load the data from a CSV file
thermo_table = pd.read_csv('hypothetical_thermo_data.csv')

# Preview the data
print(thermo_table.head())

import numpy as np

# Simple linear interpolation function
def interpolate(x, x1, y1, x2, y2):
    return y1 + (x - x1) * (y2 - y1) / (x2 - x1)

# User inputs: pressure and temperature
input_pressure = 500  # kPa
input_temperature = 20  # Celsius

# Find the nearest points in the table (for simplicity, filtering on pressure)
subset = thermo_table[thermo_table['Pressure'] == input_pressure]

# Sort by temperature and get the two closest values for interpolation
subset = subset.sort_values('Temperature')
point_below = subset[subset['Temperature'] < input_temperature].tail(1)
point_above = subset[subset['Temperature'] > input_temperature].head(1)

# Perform interpolation for specific volume, for example
v_interpolated = interpolate(
    input_temperature, 
    point_below['Temperature'].values[0], point_below['Specific Volume'].values[0],
    point_above['Temperature'].values[0], point_above['Specific Volume'].values[0]
)

print(f"Interpolated specific volume: {v_interpolated}")

import matplotlib.pyplot as plt

# Plot the table data for pressure 500 kPa
plt.scatter(subset['Temperature'], subset['Specific Volume'], label='Table Data')

# Plot the user’s interpolated point
plt.scatter([input_temperature], [v_interpolated], color='red', label='Interpolated Point')

plt.xlabel('Temperature (°C)')
plt.ylabel('Specific Volume (m³/kg)')
plt.legend()
plt.show()
