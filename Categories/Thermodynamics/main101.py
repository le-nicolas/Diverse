from fenics import *
import numpy as np
import matplotlib.pyplot as plt

# Define constants
L = 1.0  # Length of the rod
Nx = 50  # Number of spatial divisions
alpha = 0.01  # Thermal diffusivity
dt = 0.01  # Time step size
time_steps = 100  # Number of time steps

# Define the mesh and function space
mesh = IntervalMesh(Nx, 0, L)
V = FunctionSpace(mesh, 'P', 1)  # Linear elements

# Define boundary conditions (T=0 at both ends)
T_left = Constant(0.0)
T_right = Constant(0.0)
bc_left = DirichletBC(V, T_left, 'near(x[0], 0)')
bc_right = DirichletBC(V, T_right, 'near(x[0], L)')
bcs = [bc_left, bc_right]

# Define initial condition (temperature distribution)
T_0 = Expression('100*exp(-100*(x[0] - 0.5)*(x[0] - 0.5))', degree=2)
T_n = interpolate(T_0, V)

# Define the variational problem
T = TrialFunction(V)
v = TestFunction(V)
f = Constant(0.0)  # Source term (can be used for heat generation)
a = T * v * dx + alpha * dt * dot(grad(T), grad(v)) * dx
L = (T_n + dt * f) * v * dx

# Time-stepping
T = Function(V)
for n in range(time_steps):
    solve(a == L, T, bcs)  # Solve the linear system
    T_n.assign(T)  # Update the previous solution

# Plot the final temperature distribution
x = np.linspace(0, L, Nx+1)
T_vals = [T(xi) for xi in x]
plt.plot(x, T_vals)
plt.xlabel('Position (m)')
plt.ylabel('Temperature (C)')
plt.title('Final Temperature Distribution')
plt.show()
