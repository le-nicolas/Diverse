import pandas as pd
import numpy as np

# Define temperature range (in °C)
temperature = np.linspace(60, 100, 5)  # Temp values from 60°C to 100°C

# Define saturated pressure values (in MPa) corresponding to the temperatures
pressure = np.array([0.0198, 0.0234, 0.0278, 0.0325, 0.0381])

# Define specific volumes (m^3/kg) for saturated liquid (vf) and saturated vapor (vg)
vf = np.array([0.001017, 0.001020, 0.001023, 0.001026, 0.001029])
vg = np.array([0.316, 0.256, 0.213, 0.182, 0.158])

# Create a Pandas DataFrame to store the table
thermo_table = pd.DataFrame({
    'Temperature (°C)': temperature,
    'Pressure (MPa)': pressure,
    'Specific Volume vf (m^3/kg)': vf,
    'Specific Volume vg (m^3/kg)': vg
})

# Print the table
print("Thermodynamic Table (Saturated Steam Properties):")
print(thermo_table)
