import numpy as np
import matplotlib.pyplot as plt

# Constants
R = 8.314  # Universal gas constant (J/mol·K)
n = 1      # Number of moles

# Temperature and Entropy ranges
T_range = np.linspace(300, 600, 100)  # Temperature range from 300 K to 600 K

# Isothermal process
T_isothermal = 450  # Constant temperature for isothermal process
S_isothermal = R * n * np.log(T_range / T_isothermal)  # Entropy change for isothermal process

# Isochoric process
# Assume initial entropy S_initial for isochoric
S_initial = 500  # Initial entropy value (J/K)
S_isochoric = S_initial + R * n * np.log(T_range / 300)  # Entropy change for isochoric process

# Isobaric process
T_isobaric_initial = 300
T_isobaric_final = 600
S_isobaric_initial = R * n * np.log(T_isobaric_initial / T_isobaric_initial)
S_isobaric = R * n * np.log(T_range / T_isobaric_initial)  # Entropy change for isobaric process

# Plotting
plt.figure(figsize=(10, 6))

# Isothermal process
plt.plot(T_isothermal * np.ones_like(T_range), S_isothermal, label='Isothermal Process', color='blue')

# Isochoric process
plt.plot(T_range, S_isochoric, label='Isochoric Process', color='green')

# Isobaric process
plt.plot(T_range, S_isobaric, label='Isobaric Process', color='red')

plt.xlabel('Temperature (K)')
plt.ylabel('Entropy (J/K)')
plt.title('T-S Diagram')
plt.legend()
plt.grid(True)
plt.show()
