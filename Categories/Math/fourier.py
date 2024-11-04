import numpy as np
import matplotlib.pyplot as plt

# Define the function f(t)
def f(t):
    if -np.pi < t < 0:
        return 1
    elif 0 < t < np.pi:
        return 0
    else:
        return np.nan

# Create an array of t values
t_values = np.linspace(-np.pi, np.pi, 400)

# Vectorize the function to apply it over the array of t values
f_vectorized = np.vectorize(f)
f_values = f_vectorized(t_values)

# Plot the function
plt.figure(figsize=(8, 4))
plt.plot(t_values, f_values, label='f(t)')
plt.title('Graph of f(t)')
plt.xlabel('t')
plt.ylabel('f(t)')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.legend()
plt.show()
