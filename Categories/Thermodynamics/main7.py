#cubic spline interpolation and polynomial interpolation
#cubic: both the first and second derivative are continuous across adjacent points ----> smoother

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline, interp1d

# Known data points (from the table)
T = np.array([65, 70])  # Temperatures in Celsius
v = np.array([0.010946, 0.009665])  # Specific volumes in m³/kg

# Target specific volume
v_target = 0.01

# Cubic Spline Interpolation
cubic_spline = CubicSpline(T, v)

# Polynomial Interpolation (degree 1 for linear interpolation as a comparison)
poly_interp = np.poly1d(np.polyfit(T, v, 1))

# Temperature range for plotting
T_range = np.linspace(64, 71, 100)

# Perform interpolation using both methods
v_spline = cubic_spline(T_range)
v_poly = poly_interp(T_range)

# Find the temperature corresponding to v_target using cubic spline
T_spline_target = np.interp(v_target, cubic_spline(T_range)[::-1], T_range[::-1])

# Find the temperature corresponding to v_target using polynomial interpolation
T_poly_target = np.interp(v_target, poly_interp(T_range)[::-1], T_range[::-1])

# Plotting the interpolation
plt.figure(figsize=(8,6))
plt.plot(T_range, v_spline, label="Cubic Spline Interpolation", color="blue", linestyle='--')
plt.plot(T_range, v_poly, label="Linear Interpolation", color="red", linestyle=':')
plt.scatter(T, v, color='black', label="Known Data Points", zorder=5)
plt.axhline(v_target, color='green', linestyle='-.', label=f"Target v = {v_target} m³/kg")

# Mark the estimated temperatures for both methods
plt.scatter(T_spline_target, v_target, color="blue", zorder=6)
plt.scatter(T_poly_target, v_target, color="red", zorder=6)

# Add annotations
plt.text(T_spline_target, v_target + 0.00002, f"Spline: {T_spline_target:.2f}°C", color="blue")
plt.text(T_poly_target, v_target - 0.00002, f"Linear: {T_poly_target:.2f}°C", color="red")

# Labels and title
plt.xlabel("Temperature (°C)")
plt.ylabel("Specific Volume (m³/kg)")
plt.title("Cubic Spline vs Linear Interpolation for Specific Volume")
plt.legend()
plt.grid(True)
plt.show()

# Display the estimated temperatures
T_spline_target, T_poly_target
