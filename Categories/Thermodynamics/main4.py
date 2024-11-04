# interpolation between two known points, the weighted average is essentially
# way of bleding the two values based on how close the desired point is to each of them

# Given data points from the image
P1 = 150.9  # Pressure at point 1 (lower bound)
P2 = 182.6  # Pressure at point 2 (upper bound)

v1 = 0.09101  # Volume at point 1
v2 = 0.10885  # Volume at point 2

v = 0.1  # The volume we want to interpolate at

# Linear interpolation formula
P = P1 + ((v - v1) / (v2 - v1)) * (P2 - P1)

# Output the interpolated pressure
print(f"Interpolated pressure at v = {v} is P = {P:.2f} kPa")

# Additional example for temperature interpolation
T1 = -20  # Temperature at point 1
T2 = -15  # Temperature at point 2

# Linear interpolation for temperature
T = T1 + ((v - v1) / (v2 - v1)) * (T2 - T1)

# Output the interpolated temperature
print(f"Interpolated temperature at v = {v} is T = {T:.2f} °C")
