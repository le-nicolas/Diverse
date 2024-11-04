import numpy as np
import matplotlib.pyplot as plt

# Generate a range of small volume increments (delta V)
delta_V = np.linspace(0.01, 1, 500)

# Simulate specific volume fluctuations approaching a limit
# This is an illustrative example; the actual fluctuation pattern may differ
specific_volume_fluctuations = np.sin(1 / delta_V) / delta_V + 0.1 * np.random.randn(len(delta_V))

# Apply damping to simulate convergence to a specific volume v
specific_volume_convergence = 1 / (1 + np.exp(-10 * (delta_V - 0.5)))

# Combine fluctuations and convergence to get the final plot data
final_specific_volume = specific_volume_fluctuations * specific_volume_convergence

# Plotting the graph similar to the given image
plt.figure(figsize=(8, 6))
plt.plot(delta_V, final_specific_volume, color='b')
plt.axhline(y=0, color='k', linestyle='--')  # Representing the specific volume v
plt.axvline(x=0.5, color='k', linestyle='--')  # Highlighting the point where convergence occurs
plt.xlabel(r'$\delta V$')
plt.ylabel(r'$\frac{\delta V}{\delta m}$')
plt.title('Continuum Limit for Specific Volume')
plt.grid(True)
plt.show()
