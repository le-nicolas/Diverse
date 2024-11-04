import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Define the square wave function
def square_wave(x):
    return 1 if (x % (2 * np.pi)) < np.pi else -1

# Compute the Fourier series coefficients
def compute_fourier_coefficients(f, L, n_terms):
    a0 = (1 / (2*L)) * quad(lambda x: f(x), -L, L)[0]
    an = []
    bn = []
    
    for n in range(1, n_terms + 1):
        an.append((1 / L) * quad(lambda x: f(x) * np.cos(n * np.pi * x / L), -L, L)[0])
        bn.append((1 / L) * quad(lambda x: f(x) * np.sin(n * np.pi * x / L), -L, L)[0])
    
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
    n_terms = 10  # number of terms in the Fourier series
    x_values = np.linspace(-2*L, 2*L, 400)
    
    # Compute the true function values
    true_values = np.array([square_wave(x) for x in x_values])
    
    # Compute the Fourier series coefficients
    a0, an, bn = compute_fourier_coefficients(square_wave, L, n_terms)
    
    plt.figure(figsize=(10, 6))
    
    # Plot the true function
    plt.plot(x_values, true_values, label='Square Wave', color='blue')
    
    # Plot the Fourier series approximation for different numbers of terms
    colors = plt.cm.viridis(np.linspace(0, 1, n_terms))
    for k in range(1, n_terms + 1):
        fourier_approximations = np.array([fourier_series_partial_sum(x, L, a0, an, bn, k) for x in x_values])
        plt.plot(x_values, fourier_approximations, linestyle='--', color=colors[k-1], label=f'{k} terms')
    
    plt.title('Convergence of Fourier Series for Square Wave')
    plt.xlabel('x')
    plt.ylabel('Function Value')
    plt.legend()
    plt.grid(True)
    plt.ylim(-2, 2)
    plt.show()

plot_fourier_series()
