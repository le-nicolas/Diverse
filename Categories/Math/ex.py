import numpy as np
import matplotlib.pyplot as plt

# Define the function f(x) = 1 / (1 - x)
def f(x):
    return 1 / (1 - x)

# Define the series expansion up to N terms
def series_expansion(x, N):
    return sum(x**n for n in range(N+1))

# Generate x values
x_values = np.linspace(-2, 2, 400)

# Calculate the function values
f_values = f(x_values)

# Calculate the series expansion values for different N
N_values = [1, 2, 3, 5, 10]
series_values = [series_expansion(x_values, N) for N in N_values]

# Plot the function and the series expansions
plt.figure(figsize=(10, 6))

# Plot the original function
plt.plot(x_values, f_values, label=r'$f(x) = \frac{1}{1-x}$', color='blue')

# Plot the series expansions
colors = ['red', 'green', 'orange', 'purple', 'brown']
for series, N, color in zip(series_values, N_values, colors):
    plt.plot(x_values, series, label=f'Series Expansion (N={N})', linestyle='--', color=color)

# Highlight the region of convergence
plt.axvspan(-1, 1, color='yellow', alpha=0.3, label='Convergence Region')

# Add plot details
plt.title(r'Function $f(x) = \frac{1}{1-x}$ and its Series Expansions')
plt.xlabel('x')
plt.ylabel('f(x) and Series Expansions')
plt.ylim(-5, 5)
plt.legend()
plt.grid(True)
plt.show()
