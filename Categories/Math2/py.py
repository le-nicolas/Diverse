import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

def error_function(a, F_actual, m):
    F_theoretical = m * a
    error = F_actual - F_theoretical
    return np.sum(error ** 2)

def optimize_a(F_actual, m):
    initial_guess = 1.0  # Initial guess for acceleration 'a'
    result = minimize(error_function, initial_guess, args=(F_actual, m), callback=callback, options={'maxiter': 10})
    return result.x[0], result.fun

# Callback function to collect intermediate results
iteration_count = 0
history = []

def callback(xk):
    global iteration_count
    global history
    iteration_count += 1
    history.append((iteration_count, error_function(xk, F_actual, m)))

# Example usage
F_actual = 10.0  # Actual force
m = 2.0  # Mass

# Generate a range of 'a' values for visualization
a_values = np.linspace(0, 10, 100)
errors = [error_function(a, F_actual, m) for a in a_values]

# Find the optimal 'a'
optimal_a, optimal_error = optimize_a(F_actual, m)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(a_values, errors, label='Error Function')
plt.scatter(optimal_a, optimal_error, color='red', label='Optimal Solution')
plt.title('Error vs Acceleration (a)')
plt.xlabel('Acceleration (a)')
plt.ylabel('Error')
plt.legend()
plt.grid(True)

# Animate the optimization process
for i in range(len(history)):
    plt.scatter(history[i][0], history[i][1], color='green')
    plt.pause(0.5)

plt.show()

print("Optimal 'a':", optimal_a)
print("Minimum Error:", optimal_error)
