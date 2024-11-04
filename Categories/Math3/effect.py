import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the Lorenz system of differential equations
def lorenz(t, state, sigma=10.0, beta=8.0/3.0, rho=28.0):
    x, y, z = state
    dx_dt = sigma * (y - x)
    dy_dt = x * (rho - z) - y
    dz_dt = x * y - beta * z
    return [dx_dt, dy_dt, dz_dt]

# Initial conditions
initial_state_1 = [1.0, 1.0, 1.0]
initial_state_2 = [1.0 + 1e-5, 1.0, 1.0]  # Slightly different initial condition

# Time points where solution is computed
t_span = (0, 50)
t_eval = np.linspace(t_span[0], t_span[1], 10000)

# Solve the Lorenz system
solution_1 = solve_ivp(lorenz, t_span, initial_state_1, t_eval=t_eval)
solution_2 = solve_ivp(lorenz, t_span, initial_state_2, t_eval=t_eval)

# Plot the results
fig = plt.figure(figsize=(12, 6))

# 3D plot of the two trajectories
ax = fig.add_subplot(121, projection='3d')
ax.plot(solution_1.y[0], solution_1.y[1], solution_1.y[2], label='Initial State 1')
ax.plot(solution_2.y[0], solution_2.y[1], solution_2.y[2], label='Initial State 2', alpha=0.7)
ax.set_title('Lorenz Attractor - 3D View')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()

# 2D plot of the differences in X over time
ax2 = fig.add_subplot(122)
ax2.plot(t_eval, np.abs(solution_1.y[0] - solution_2.y[0]), color='red')
ax2.set_title('Difference in X over Time')
ax2.set_xlabel('Time')
ax2.set_ylabel('Difference |X1 - X2|')
ax2.set_yscale('log')

plt.tight_layout()
plt.show()
