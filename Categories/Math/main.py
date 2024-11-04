import numpy as np
import matplotlib.pyplot as plt

# Define the coefficients for the power series
# For example, consider the series sum of (x^n)/n!
def power_series_coefficients(n):
    return 1 / np.math.factorial(n)

# Calculate the radius of convergence
def radius_of_convergence():
    n = np.arange(1, 100)
    coefficients = np.array([power_series_coefficients(i) for i in n])
    R = 1 / np.max(np.abs(coefficients)**(1/n))
    return R

# Plotting the power series terms and interval of convergence
def plot_power_series():
    R = radius_of_convergence()
    c = 0  # center of the series

    # Define the interval of convergence
    x_interval = np.linspace(c - R*1.5, c + R*1.5, 400)
    
    # Compute a few terms of the power series for visualization
    terms = [power_series_coefficients(n) * (x_interval - c)**n for n in range(10)]
    series_sum = np.sum(terms, axis=0)
    
    plt.figure(figsize=(10, 6))
    
    # Plot the power series approximation
    plt.plot(x_interval, series_sum, label='Power Series Approximation')
    
    # Plot vertical lines indicating the radius of convergence
    plt.axvline(c - R, color='r', linestyle='--', label='Radius of Convergence')
    plt.axvline(c + R, color='r', linestyle='--')
    
    # Highlight the interval of convergence
    plt.fill_between(x_interval, -1, 1, where=(x_interval > c - R) & (x_interval < c + R), color='green', alpha=0.2, label='Interval of Convergence')
    
    plt.title('Power Series and Interval of Convergence')
    plt.xlabel('x')
    plt.ylabel('Series Value')
    plt.legend()
    plt.grid(True)
    plt.ylim(-1, 1)
    plt.show()

plot_power_series()
