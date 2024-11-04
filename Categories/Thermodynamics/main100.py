import numpy as np
import matplotlib.pyplot as plt

# Constants
L = 1.0  # length of the rod (m)
Nx = 10  # number of spatial points
dx = L / (Nx - 1)  # spatial step
alpha = 0.01  # thermal diffusivity (m^2/s)
dt = 0.01  # time step (s)
T0 = 100.0  # initial temperature (deg C)
T_left = 0.0  # boundary condition at x=0
T_right = 0.0  # boundary condition at x=L
time_steps = 500  # total time steps

# Initial temperature distribution
T = np.ones(Nx) * T0
T[0] = T_left
T[-1] = T_right

# Function to solve the 1D heat equation
def solve_heat_eq(T, alpha, dt, dx, time_steps):
    for _ in range(time_steps):
        T_new = T.copy()
        for i in range(1, Nx - 1):
            T_new[i] = T[i] + alpha * dt / dx**2 * (T[i+1] - 2*T[i] + T[i-1])
        T = T_new.copy()
        T[0], T[-1] = T_left, T_right  # Maintain boundary conditions
    return T

# Solve the equation
final_temp = solve_heat_eq(T, alpha, dt, dx, time_steps)

# Plotting the results
x = np.linspace(0, L, Nx)
plt.plot(x, final_temp, label='Temperature Distribution')
plt.xlabel('Position (m)')
plt.ylabel('Temperature (deg C)')
plt.title('1D Heat Conduction - Final Temperature Distribution')
plt.legend()
plt.show()
