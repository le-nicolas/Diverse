import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Define the piecewise linear function
def piecewise_linear_function(x, L=np.pi):
    x_mod = np.mod(x + L, 2*L) - L
    return np.piecewise(x_mod, [x_mod < 0, x_mod >= 0], 
                        [lambda x: (4/np.pi)*x, lambda x: -(4/np.pi)*x])

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
    sum = a0 / 2  # a0/2 term
    for n in range(1, n_terms + 1):
        sum += an[n-1] * np.cos(n * np.pi * x / L) + bn[n-1] * np.sin(n * np.pi * x / L)
    return sum

# Function to plot the Fourier series approximation
def plot_fourier_series(f, L=np.pi, n_terms=5, num_points=800):
    x_values = np.linspace(-2*L, 2*L, num_points)
    
    # Compute the true function values (piecewise function)
    true_values = np.array([f(x, L) for x in x_values])
    
    # Compute the Fourier series coefficients
    a0, an, bn = compute_fourier_coefficients(f, L, n_terms)
    
    # Compute the Fourier series approximations
    fourier_approximations = np.array([fourier_series_partial_sum(x, L, a0, an, bn, n_terms) for x in x_values])
    
    # Plotting
    plt.figure(figsize=(10, 6))
    
    # Plot the piecewise function
    plt.plot(x_values, true_values, label='Piecewise Function', color='blue')
    
    # Plot the Fourier series approximation
    plt.plot(x_values, fourier_approximations, label=f'Fourier Series Approximation (n={n_terms})', color='red', linestyle='--')
    
    plt.title('Fourier Series Approximation of Piecewise Function')
    plt.xlabel('x')
    plt.ylabel('Function Value')
    plt.legend()
    plt.grid(True)
    plt.ylim(-1.5, 1.5)
    plt.show()

# Example usage:
plot_fourier_series(piecewise_linear_function)
