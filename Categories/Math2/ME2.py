from fipy import CellVariable, Grid1D, DiffusionTerm, TransientTerm, Viewer

# Define mesh
nx = 100  # Number of grid points
L = 1.0   # Length of the domain
mesh = Grid1D(nx=nx, Lx=L)

# Define variables
phi = CellVariable(name="solution variable", mesh=mesh, value=0., hasOld=True)  # Set hasOld to True

# Define parameters
D = 1.0  # Diffusion coefficient
dt = 0.01  # Time step size
duration = 1.0  # Total simulation time

# Define the diffusion equation
eq = TransientTerm() == DiffusionTerm(coeff=D)

# Define initial condition
x = mesh.cellCenters[0]
phi.setValue(0.0)  # Initial condition
phi.setValue(1.0, where=(x > 0.5))  # Step function initial condition

# Create a viewer to visualize the solution
viewer = Viewer(vars=phi, datamin=0., datamax=1.)

# Time-stepping loop
time = 0.0
while time < duration:
    phi.updateOld()  # Store the current solution
    eq.solve(var=phi, dt=dt)  # Solve the diffusion equation
    viewer.plot()  # Plot the current solution
    time += dt
