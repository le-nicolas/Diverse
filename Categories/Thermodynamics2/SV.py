import numpy as np
import matplotlib.pyplot as plt

# Define the function to compute specific volume from density
def specific_volume(density):
    """
    Compute the specific volume from density.
    
    Parameters:
    density (float or np.ndarray): Density of the substance (kg/m^3).
    
    Returns:
    float or np.ndarray: Specific volume (m^3/kg).
    """
    return 1 / density

# Parameters
densities = np.linspace(1, 1000, 100)  # Densities ranging from 1 to 1000 kg/m^3

# Compute specific volumes
specific_volumes = specific_volume(densities)

# Plotting specific volume vs. density
plt.figure(figsize=(8, 6))
plt.plot(densities, specific_volumes, label='Specific Volume vs. Density')
plt.xlabel('Density (kg/m^3)')
plt.ylabel('Specific Volume (m^3/kg)')
plt.title('Specific Volume in Continuum Limit')
plt.grid(True)
plt.legend()
plt.show()
