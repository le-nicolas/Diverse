import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Define the piecewise linear function
def piecewise_linear_function(x, L=np.pi):
    x = np.mod(x + np.pi, 2*np.pi) - np.pi 
    if -np.pi <= x < 0:
        return (4 / np.pi) * x
    elif 0 <= x < np.pi:
        return -(4 / np.pi) * x
    else:
        return 0
    
# Define the square wave function
def square_wave(x, L=np.pi):
    x = np.remainder(x + L, 2*L) - L  # make the function periodic from -L to L
    if -np.pi < x < 0:
        return 1
    elif 0 < x < np.pi:
        return 0
    else:
        return 0

f = piecewise_linear_function
# Compute the Fourier series coefficients
def compute_fourier_coefficients(f, L, n_terms):
    a0 = (1 / (2*L)) * quad(lambda x: f(x, L), -L, L)[0]
    an = []
    bn = []
    
    for n in range(1, n_terms + 1):
        an.append((1 / L) * quad(lambda x: f(x, L) * np.cos(n * np.pi * x / L), -L, L)[0])
        bn.append((1 / L) * quad(lambda x: f(x, L) * np.sin(n * np.pi * x / L), -L, L)[0])
    
    return a0, an, bn

# Compute the Fourier series partial sum
def fourier_series_partial_sum(x, L, a0, an, bn, n_terms):
    sum = a0
    for n in range(1, n_terms + 1):
        sum += an[n-1] * np.cos(n * np.pi * x / L) + bn[n-1] * np.sin(n * np.pi * x / L)
    return sum

# Plotting the function and its Fourier series approximation
def plot_fourier_series():
    L = np.pi  # period is 2*pi
    n_terms = 5  # number of terms in the Fourier series
    x_values = np.linspace(-2*L, 2*L, 800)
    
    # Compute the true function values
    true_values = np.array([f(x, L) for x in x_values])
    
    # Compute the Fourier series coefficients
    a0, an, bn = compute_fourier_coefficients(f, L, n_terms)
    
    # Compute the Fourier series approximations
    fourier_approximations = np.array([fourier_series_partial_sum(x, L, a0, an, bn, n_terms) for x in x_values])
    
    plt.figure(figsize=(10, 6))
    
    # Plot the true function
    plt.plot(x_values, true_values, label='Function', color='blue')
    
    # Plot the Fourier series approximation
    plt.plot(x_values, fourier_approximations, label=f'Fourier Series Approximation (n={n_terms})', color='red', linestyle='--')
    
    plt.title('Fourier Series Approximation of Function')
    plt.xlabel('x')
    plt.ylabel('Function Value')
    plt.legend()
    plt.grid(True)
    plt.ylim(-1.5, 1.5)
    plt.show()

plot_fourier_series()
