import numpy as np
import matplotlib.pyplot as plt

# Define the function ranges
x = np.linspace(-2*np.pi, 2*np.pi, 1000)

# Map x into the interval from -pi to pi
x_mod = np.mod(x + np.pi, 2*np.pi) - np.pi

# Define the piecewise function
def piecewise_func(x):
    return np.where((x > -np.pi) & (x < 0), 1, 0)

# Calculate the y values
y = piecewise_func(x_mod)

# Define a function to calculate the Fourier series approximation
def fourier_series(x, n_terms):
    a0 = 1 / 2  # This is the average value of the function over one period
    result = a0
    for n in range(1, n_terms + 1):
        bn = 2 * (1 - np.cos(n * np.pi)) / (n * np.pi)
        result += bn * np.sin(n * x)
    return result

# Plot the original piecewise function
plt.plot(x, y, label='Original Piecewise Function')

# Plot the Fourier series approximation
n_terms = 10  # Number of terms in the Fourier series
y_fourier = fourier_series(x, n_terms)
plt.plot(x, y_fourier, label=f'Fourier Series Approximation ({n_terms} terms)', linestyle='--')

# Plot settings
plt.title('Piecewise Function and its Fourier Series Approximation')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()