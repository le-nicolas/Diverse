import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Define the piecewise function
def f_t(t):
    t = t % (2 * np.pi)  # Bring t within the range [0, 2*pi)
    if 0 < t < np.pi:
        return 1
    else:
        return 0

# Vectorize the function for numpy operations
f_t_vec = np.vectorize(f_t)

# Compute the Fourier series coefficients
def compute_fourier_coefficients(f, L, n_terms):
    a0 = (1 / (2*L)) * quad(lambda t: f(t), -L, L)[0]
    an = []
    bn = []
    
    for n in range(1, n_terms + 1):
        an.append((1 / L) * quad(lambda t: f(t) * np.cos(n * t), -L, L)[0])
        bn.append((1 / L) * quad(lambda t: f(t) * np.sin(n * t), -L, L)[0])
    
    return a0, an, bn

# Compute the Fourier series partial sum
def fourier_series_partial_sum(t, L, a0, an, bn, n_terms):
    sum = a0
    for n in range(1, n_terms + 1):
        sum += an[n-1] * np.cos(n * t) + bn[n-1] * np.sin(n * t)
    return sum

# Plotting the function and its Fourier series approximation
def plot_fourier_series():
    L = np.pi  # period is 2*pi
    n_terms = 10  # number of terms in the Fourier series
    t_values = np.linspace(-2*L, 2*L, 400)
    
    # Compute the true function values
    true_values = f_t_vec(t_values)
    
    # Compute the Fourier series coefficients
    a0, an, bn = compute_fourier_coefficients(f_t, L, n_terms)
    
    # Compute the Fourier series approximations
    fourier_approximations = np.array([fourier_series_partial_sum(t, L, a0, an, bn, n_terms) for t in t_values])
    
    plt.figure(figsize=(10, 6))
    
    # Plot the true function
    plt.plot(t_values, true_values, label='f(t)', color='blue')
    
    # Plot the Fourier series approximation
    plt.plot(t_values, fourier_approximations, label=f'Fourier Series Approximation (n={n_terms})', color='red', linestyle='--')
    
    plt.title('Fourier Series Approximation of f(t)')
    plt.xlabel('t')
    plt.ylabel('Function Value')
    plt.legend()
    plt.grid(True)
    plt.ylim(-0.5, 1.5)
    plt.show()

plot_fourier_series()
