#differential equations can be very helpful for understanding their behavior
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def f(x, y):
    return x - y

def direction_field(f, x_range, y_range, density=20):
    x = np.linspace(x_range[0], x_range[1], density)
    y = np.linspace(y_range[0], y_range[1], density)
    X, Y = np.meshgrid(x, y)
    U = 1
    V = f(X, Y)
    N = np.sqrt(U**2 + V**2)
    U, V = U/N, V/N
    
    plt.quiver(X, Y, U, V, color='blue', headlength=0, headaxislength=0)

def plot_solution(f, x_range, y0, t_max=10):
    t = np.linspace(x_range[0], t_max, 200)
    sol = odeint(lambda y, t: f(t, y), y0, t)
    plt.plot(t, sol, label=f'Initial: y(0)={y0}')

# Define the ranges for x and y
x_range = [0, 10]
y_range = [-5, 5]

plt.figure(figsize=(10, 8))

# Plot the direction field
direction_field(f, x_range, y_range, density=20)

# Plot solution curves for different initial conditions
initial_conditions = [0, 1, -1, 2, -2]
for y0 in initial_conditions:
    plot_solution(f, x_range, y0)

plt.xlim(x_range)
plt.ylim(y_range)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Direction Field and Solution Curves for dy/dx = x - y')
plt.legend()
plt.grid()
plt.show()
