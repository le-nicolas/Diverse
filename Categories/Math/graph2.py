import numpy as np
import matplotlib.pyplot as plt

def plot_piecewise_function():
    # Define the function ranges
    x = np.linspace(-2*np.pi, 2*np.pi, 800)

    # Map x into the interval from -pi to pi
    x_mod = np.mod(x + np.pi, 2*np.pi) - np.pi

    # Define the function conditions
    conditions = [
        (x_mod >= -np.pi) & (x_mod < 0),
        (x_mod >= 0) & (x_mod < np.pi)
    ]

    # Define the functions
    functions = [
        lambda x: (4/np.pi)*x,
        lambda x: -(4/np.pi)*x
    ]

    # Calculate the y values
    y = np.piecewise(x_mod, conditions, functions)

    # Plot the function
    plt.plot(x, y)
    plt.title('Piecewise Function')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.show()

# Call the function
plot_piecewise_function()