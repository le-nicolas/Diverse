import numpy as np
import matplotlib.pyplot as plt

# Define the function and its derivatives for the Maclaurin series
def f(x):
    return np.sin(x)

# Define the Maclaurin series coefficients for sin(x)
def maclaurin_series_coefficients(n):
    if n % 4 == 0:
        return 0
    elif n % 4 == 1:
        return 1 / np.math.factorial(n)
    elif n % 4 == 2:
        return 0
    else:
        return -1 / np.math.factorial(n)

# Compute the partial sums of the Maclaurin series
def maclaurin_series_partial_sum(x, n_terms):
    partial_sum = 0
    for n in range(n_terms):
        partial_sum += maclaurin_series_coefficients(n) * x**n
    return partial_sum

# Plotting the function and its Maclaurin series approximation
def plot_maclaurin_series():
    x_values = np.linspace(-2*np.pi, 2*np.pi, 400)
    n_terms = 10  # number of terms in the Maclaurin series
    
    # Compute the true function values
    true_values = f(x_values)
    
    # Compute the Maclaurin series approximations
    maclaurin_approximations = [maclaurin_series_partial_sum(x, n_terms) for x in x_values]
    
    plt.figure(figsize=(10, 6))
    
    # Plot the true function
    plt.plot(x_values, true_values, label='$\sin(x)$', color='blue')
    
    # Plot the Maclaurin series approximation
    plt.plot(x_values, maclaurin_approximations, label=f'Maclaurin Series Approximation (n={n_terms})', color='red', linestyle='--')
    
    plt.title('Maclaurin Series Approximation of $\sin(x)$')
    plt.xlabel('x')
    plt.ylabel('Function Value')
    plt.legend()
    plt.grid(True)
    plt.ylim(-2, 2)
    plt.show()

plot_maclaurin_series()
