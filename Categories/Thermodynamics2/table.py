import numpy as np
import pandas as pd

# Constants
R = 8.314  # Universal gas constant (J/mol·K)
n = 1      # Number of moles
P = 1      # Pressure in atm
P_pa = P * 101325  # Pressure in Pascals for consistency in SI units

# Temperature range
T_range = np.array([300, 400, 500, 600, 700])  # Temperature in Kelvin

# Calculate properties
def calculate_properties(T, P):
    """
    Calculate thermodynamic properties for an ideal gas.
    
    Parameters:
    T (float): Temperature in Kelvin
    P (float): Pressure in Pascals
    
    Returns:
    dict: A dictionary with calculated properties
    """
    # Specific Volume (v)
    v = R * T / P
    
    # Internal Energy (U) - U = n * Cv * T for an ideal gas
    Cv = 12.5  # Assumed constant heat capacity at constant volume (J/mol·K)
    U = n * Cv * T
    
    # Enthalpy (H) - H = U + P * v
    H = U + P * v
    
    # Entropy (S) - S = n * R * ln(T / T0) where T0 is a reference temperature
    T0 = 300  # Reference temperature in Kelvin
    S = n * R * np.log(T / T0)
    
    return {'Temperature (K)': T, 'Pressure (Pa)': P, 'Specific Volume (m^3/mol)': v, 
            'Internal Energy (J)': U, 'Enthalpy (J)': H, 'Entropy (J/K)': S}

# Create a DataFrame to store the properties
properties_list = []
for T in T_range:
    properties_list.append(calculate_properties(T, P_pa))

df = pd.DataFrame(properties_list)

# Display the table
print("Thermodynamic Properties Table:")
print(df)
