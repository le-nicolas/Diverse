import numpy as np
import matplotlib.pyplot as plt

# Define the function and its derivatives for the Taylor series
def f(x):
    return np.exp(x)

def taylor_series_coefficients(n):
    return 1 / np.math.factorial(n)

# Compute the partial sums of the Taylor series
def taylor_series_partial_sum(x, c, n_terms):
    partial_sum = 0
    for n in range(n_terms):
        partial_sum += taylor_series_coefficients(n) * (x - c)**n
    return partial_sum

# Plotting the function and its Taylor series approximation
def plot_taylor_series():
    c = 0  # center of the series
    x_values = np.linspace(-2, 2, 400)
    n_terms = 10  # number of terms in the Taylor series
    
    # Compute the true function values
    true_values = f(x_values)
    
    # Compute the Taylor series approximations
    taylor_approximations = [taylor_series_partial_sum(x, c, n_terms) for x in x_values]
    
    plt.figure(figsize=(10, 6))
    
    # Plot the true function
    plt.plot(x_values, true_values, label='$e^x$', color='blue')
    
    # Plot the Taylor series approximation
    plt.plot(x_values, taylor_approximations, label=f'Taylor Series Approximation (n={n_terms})', color='red', linestyle='--')
    
    plt.title('Taylor Series Approximation of $e^x$')
    plt.xlabel('x')
    plt.ylabel('Function Value')
    plt.legend()
    plt.grid(True)
    plt.show()

plot_taylor_series()
