import numpy as np
import matplotlib.pyplot as plt

# Parameters
L = 20  # Size of the lattice (LxL)
T = 2.0  # Temperature
n_steps = 100000  # Number of Monte Carlo steps

# Initialize the lattice with random spins (+1 or -1)
lattice = np.random.choice([-1, 1], size=(L, L))

# Function to calculate the total energy of the lattice
def calculate_total_energy(lattice):
    energy = 0
    for i in range(L):
        for j in range(L):
            # Nearest neighbors with periodic boundary conditions
            S = lattice[i, j]
            neighbors = lattice[(i+1)%L, j] + lattice[i, (j+1)%L] + lattice[(i-1)%L, j] + lattice[i, (j-1)%L]
            energy += -S * neighbors
    return energy / 2  # Each pair counted twice

# Function to calculate the magnetization of the lattice
def calculate_magnetization(lattice):
    return np.sum(lattice)

# Metropolis algorithm
def metropolis(lattice, T, n_steps):
    for step in range(n_steps):
        # Pick a random spin
        i, j = np.random.randint(0, L), np.random.randint(0, L)
        S = lattice[i, j]
        # Compute the change in energy if this spin is flipped
        neighbors = lattice[(i+1)%L, j] + lattice[i, (j+1)%L] + lattice[(i-1)%L, j] + lattice[i, (j-1)%L]
        delta_E = 2 * S * neighbors
        
        # Flip the spin with probability exp(-delta_E / k_B T)
        if delta_E < 0 or np.random.rand() < np.exp(-delta_E / T):
            lattice[i, j] = -S  # Flip the spin
            
    return lattice

# Run the simulation
lattice = metropolis(lattice, T, n_steps)

# Calculate final energy and magnetization
final_energy = calculate_total_energy(lattice)
final_magnetization = calculate_magnetization(lattice)

print(f"Final Energy: {final_energy}")
print(f"Final Magnetization: {final_magnetization}")

# Plot the final lattice configuration
plt.imshow(lattice, cmap='coolwarm', interpolation='nearest')
plt.title('2D Ising Model at Thermal Equilibrium')
plt.colorbar(label='Spin')
plt.show()
