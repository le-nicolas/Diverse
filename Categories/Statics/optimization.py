import numpy as np
from scipy.optimize import minimize

# Cost function to minimize: distance traveled by drone
def cost_function(waypoints_flat):
    # Reshape the flat array back into (n_waypoints, 3) shape
    waypoints = waypoints_flat.reshape(-1, 3)
    
    total_distance = 0
    for i in range(len(waypoints) - 1):
        total_distance += np.linalg.norm(waypoints[i] - waypoints[i+1])
    return total_distance

# Initial guess for waypoints (5 waypoints in 3D space)
initial_waypoints = np.random.rand(5, 3) * 20  # Random waypoints in 3D

# Flatten the initial guess for the optimizer
initial_waypoints_flat = initial_waypoints.flatten()

# Optimize waypoints to minimize distance
optimized_result = minimize(cost_function, initial_waypoints_flat)

# Reshape the optimized waypoints back into (n_waypoints, 3) shape
optimized_waypoints = optimized_result.x.reshape(-1, 3)

# Print the optimized waypoints
print("Optimized waypoints:")
print(optimized_waypoints)
