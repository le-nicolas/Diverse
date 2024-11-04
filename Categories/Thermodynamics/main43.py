import numpy as np
import matplotlib.pyplot as plt

# Example: Simulating a PV diagram for a thermodynamic cycle
P = np.linspace(100, 400, 50)  # Pressure
V = 1 / P                      # Ideal gas law relation for simplicity

plt.plot(V, P)
plt.xlabel('Volume')
plt.ylabel('Pressure')
plt.title('PV Diagram')
plt.show()
