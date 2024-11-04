import matplotlib.pyplot as plt

def f(t, y):
    """
    Define the ordinary differential equation (ODE) y' = f(t, y) here.
    This is the function you want to integrate numerically.
    """
    return t * y  # Example ODE, change as needed

def runge_kutta4(t0, y0, h, n):
    """
    Implements the fourth-order Runge-Kutta method for numerical integration.
    
    Parameters:
    t0: Initial time
    y0: Initial value of y(t0)
    h: Step size
    n: Number of steps
    
    Returns:
    t_values: Array of time values
    y_values: Array of corresponding y values
    """
    t_values = [t0]
    y_values = [y0]
    for i in range(n):
        t = t_values[-1]
        y = y_values[-1]
        k1 = h * f(t, y)
        k2 = h * f(t + 0.5*h, y + 0.5*k1)
        k3 = h * f(t + 0.5*h, y + 0.5*k2)
        k4 = h * f(t + h, y + k3)
        
        y_next = y + (k1 + 2*k2 + 2*k3 + k4) / 6.0
        t_next = t + h
        
        t_values.append(t_next)
        y_values.append(y_next)
    return t_values, y_values

# Example usage
t0 = 0  # Initial time
y0 = 1  # Initial value of y(t0)
h = 0.1  # Step size
n = 100  # Number of steps

t_values, y_values = runge_kutta4(t0, y0, h, n)

# Plotting the results
plt.plot(t_values, y_values)
plt.xlabel('t')
plt.ylabel('y(t)')
plt.title('Numerical Integration using Runge-Kutta 4th Order')
plt.grid(True)
plt.show()
