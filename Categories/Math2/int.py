import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Define the velocity function v(t)
def velocity(t):
    return 3 * t**2 + 2 * t + 1  # Example velocity function

# Define the time interval
a = 0  # Start time
b = 5  # End time

# Compute the definite integral to find the total distance traveled
distance, _ = quad(velocity, a, b)
print(f"Total distance traveled from t={a} to t={b} is {distance} units.")

# Visualization
time = np.linspace(a, b, 400)
velocity_values = velocity(time)

plt.figure(figsize=(12, 6))
plt.plot(time, velocity_values, label='Velocity v(t)')
plt.fill_between(time, velocity_values, alpha=0.3)
plt.xlabel('Time')
plt.ylabel('Velocity')
plt.title('Velocity Function and Distance Traveled')
plt.legend()
plt.grid(True)
plt.show()
