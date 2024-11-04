import numpy as np
from scipy.optimize import minimize

# Efficiency function of Carnot engine
def carnot_efficiency(temps):
    T_hot, T_cold = temps
    if T_cold >= T_hot:  # Invalid if cold temp is higher than or equal to hot
        return 0
    return -(1 - T_cold / T_hot)  # Negative because we're maximizing

# Initial guesses for temperatures
initial_guess = [500, 300]  # Example: Hot = 500K, Cold = 300K
bounds = [(300, 800), (200, 500)]  # Constraints for temperature ranges

result = minimize(carnot_efficiency, initial_guess, bounds=bounds)

print(f"Optimal temperatures for maximum efficiency: Hot = {result.x[0]:.2f}K, Cold = {result.x[1]:.2f}K")
print(f"Maximum efficiency: {-(result.fun):.4f}")
