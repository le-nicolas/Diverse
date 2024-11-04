import numpy as np
import matplotlib.pyplot as plt

# Define the exponential function and its Maclaurin series
def exp_function(x):
    return np.exp(x)

def maclaurin_series_e_x(x, n_terms):
    return np.sum([x**n / np.math.factorial(n) for n in range(n_terms)], axis=0)

# Simulation of the series convergence
def simulate_convergence():
    x_values = np.linspace(-2, 2, 400)
    true_values = exp_function(x_values)
    
    plt.figure(figsize=(10, 6))
    
    # Plot the true function
    plt.plot(x_values, true_values, label='$e^x$', color='blue')
    
    colors = plt.cm.viridis(np.linspace(0, 1, 10))
    for n_terms, color in zip(range(1, 11), colors):
        approx_values = maclaurin_series_e_x(x_values, n_terms)
        plt.plot(x_values, approx_values, linestyle='--', color=color, label=f'{n_terms} terms')
    
    plt.title('Convergence of Maclaurin Series for $e^x$')
    plt.xlabel('x')
    plt.ylabel('Function Value')
    plt.legend()
    plt.grid(True)
    plt.ylim(-1, 8)
    plt.show()

simulate_convergence()
