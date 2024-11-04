import numpy as np
import matplotlib.pyplot as plt

# Define phase boundaries based on approximations for water
# These are not precise values but used for illustration purposes
def sublimation_curve(T):
    # Approximate sublimation curve (Pa) up to triple point
    return 611 * np.exp(25.0 * (1 - T/273.16))

def vaporization_curve(T):
    # Clausius–Clapeyron equation approximation for vaporization
    return 611 * np.exp(17.27 * (T - 273.16) / (T - 35.86))

def melting_curve(T):
    # Approximate melting curve for water (slightly decreasing with pressure)
    return 101325 * (1 - 0.0001 * (273.15 - T))

# Temperature range (K)
T_sublimation = np.linspace(180, 273.16, 100)  # Below triple point, sublimation line
T_vaporization = np.linspace(273.16, 647.096, 100)  # Between triple point and critical point
T_melting = np.linspace(180, 273.15, 100)  # Below triple point, melting curve

# Get phase boundary data
P_sublimation = sublimation_curve(T_sublimation)
P_vaporization = vaporization_curve(T_vaporization)
P_melting = melting_curve(T_melting)

# Plot P-T Diagram
plt.figure(figsize=(8, 6))
plt.plot(T_sublimation, P_sublimation, label="Sublimation Curve (Solid ⇌ Vapor)", color='blue')
plt.plot(T_vaporization, P_vaporization, label="Vaporization Curve (Liquid ⇌ Vapor)", color='green')
plt.plot(T_melting, P_melting, label="Melting Curve (Solid ⇌ Liquid)", color='orange')

# Highlight critical point and triple point
plt.scatter(647.096, 22064e3, color='red', zorder=5, label="Critical Point (374°C, 22.064 MPa)")
plt.scatter(273.16, 611, color='purple', zorder=5, label="Triple Point (0.01°C, 611 Pa)")

# Labels and title
plt.yscale('log')  # Logarithmic scale for pressure
plt.xlabel('Temperature (K)')
plt.ylabel('Pressure (Pa)')
plt.title('Pressure-Temperature (P-T) Diagram for Water')
plt.grid(True, which="both", ls="--")
plt.legend()
plt.tight_layout()

# Show plot
plt.show()
