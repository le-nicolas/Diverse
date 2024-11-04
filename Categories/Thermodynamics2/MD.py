import numpy as np
import matplotlib.pyplot as plt

# Constants
epsilon = 1.0  # Depth of the potential well
sigma = 1.0    # Finite distance at which the inter-particle potential is zero
mass = 1.0     # Mass of particles
dt = 0.01      # Time step
num_steps = 1000  # Number of simulation steps
num_particles = 10  # Number of particles

# Initialize positions and velocities
positions = np.random.rand(num_particles, 2) * 10.0  # Random initial positions in 2D
velocities = np.random.randn(num_particles, 2) * 0.1  # Random initial velocities

def lennard_jones_force(positions):
    """
    Calculate the Lennard-Jones force for each pair of particles.

    Parameters:
    positions (np.ndarray): Array of particle positions.

    Returns:
    np.ndarray: Array of forces on each particle.
    """
    forces = np.zeros_like(positions)
    num_particles = len(positions)
    
    for i in range(num_particles):
        for j in range(i + 1, num_particles):
            # Compute displacement vector between particles
            r_ij = positions[i] - positions[j]
            r2 = np.dot(r_ij, r_ij)
            r6 = r2**3
            r12 = r6**2
            force_magnitude = 24 * epsilon * (2 * (sigma**12 / r12) - (sigma**6 / r6)) / r2
            force_vector = force_magnitude * r_ij
            
            # Update forces
            forces[i] += force_vector
            forces[j] -= force_vector
            
    return forces

# Time integration (Verlet algorithm)
for step in range(num_steps):
    # Calculate forces
    forces = lennard_jones_force(positions)
    
    # Update positions
    positions += velocities * dt + 0.5 * forces / mass * dt**2
    
    # Update velocities
    new_forces = lennard_jones_force(positions)
    velocities += 0.5 * (forces + new_forces) / mass * dt

# Plot final positions of particles
plt.scatter(positions[:, 0], positions[:, 1], color='b')
plt.title('Final Positions of Particles in 2D')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()
