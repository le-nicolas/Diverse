# Given values at the four corners of the table
P1, P2 = 100, 200  # Pressures in kPa
T1, T2 = 300, 400  # Temperatures in °C

v_P1_T1 = 0.001  # Specific volume at P1, T1
v_P2_T1 = 0.0011  # Specific volume at P2, T1
v_P1_T2 = 0.0009  # Specific volume at P1, T2
v_P2_T2 = 0.00105  # Specific volume at P2, T2

# Target pressure and temperature for interpolation
P_target = 150  # Interpolating at P = 150 kPa
T_target = 350  # Interpolating at T = 350 °C

# Perform bilinear interpolation
v_interpolated = (
    v_P1_T1 * (P2 - P_target) * (T2 - T_target) +
    v_P2_T1 * (P_target - P1) * (T2 - T_target) +
    v_P1_T2 * (P2 - P_target) * (T_target - T1) +
    v_P2_T2 * (P_target - P1) * (T_target - T1)
) / ((P2 - P1) * (T2 - T1))

# Output the interpolated specific volume
print(f"Interpolated specific volume at P = {P_target} kPa and T = {T_target} °C is v = {v_interpolated:.6f} m³/kg")
