import numpy as np
import matplotlib.pyplot as plt

# Parameters
L = 20  # Lattice size
T = 2.0  # Temperature
num_steps = 10000  # Number of Monte Carlo steps

# Initialize spins randomly (-1 or +1)
spins = np.random.choice([-1, 1], size=(L, L))

def compute_energy(spins):
    """
    Compute the total energy of the spin configuration.

    Parameters:
    spins (np.ndarray): Lattice of spins.

    Returns:
    float: Total energy of the configuration.
    """
    energy = 0
    for i in range(L):
        for j in range(L):
            # Calculate interaction with nearest neighbors (periodic boundary conditions)
            S = spins[i, j]
            neighbors = spins[(i + 1) % L, j] + spins[(i - 1) % L, j] + spins[i, (j + 1) % L] + spins[i, (j - 1) % L]
            energy += -S * neighbors
    return energy / 2  # Each interaction counted twice

def compute_magnetization(spins):
    """
    Compute the total magnetization of the spin configuration.

    Parameters:
    spins (np.ndarray): Lattice of spins.

    Returns:
    float: Total magnetization of the configuration.
    """
    return np.sum(spins)

def monte_carlo_step(spins, T):
    """
    Perform one step of the Monte Carlo simulation using the Metropolis algorithm.

    Parameters:
    spins (np.ndarray): Lattice of spins.
    T (float): Temperature.

    Returns:
    None
    """
    for _ in range(L * L):
        # Pick a random spin
        i, j = np.random.randint(0, L, size=2)
        
        # Calculate energy change if this spin is flipped
        S = spins[i, j]
        neighbors = spins[(i + 1) % L, j] + spins[(i - 1) % L, j] + spins[i, (j + 1) % L] + spins[i, (j - 1) % L]
        delta_E = 2 * S * neighbors
        
        # Metropolis criterion: accept or reject the move
        if delta_E < 0 or np.random.rand() < np.exp(-delta_E / T):
            spins[i, j] *= -1

# Run the Monte Carlo simulation
energies = []
magnetizations = []

for step in range(num_steps):
    monte_carlo_step(spins, T)
    
    # Record energy and magnetization
    if step % 100 == 0:
        energies.append(compute_energy(spins))
        magnetizations.append(compute_magnetization(spins))

# Plot final spin configuration
plt.imshow(spins, cmap='coolwarm')
plt.title('Final Spin Configuration')
plt.show()

# Plot energy and magnetization over time
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.plot(energies)
plt.title('Energy over Time')
plt.xlabel('Monte Carlo Step')
plt.ylabel('Energy')

plt.subplot(1, 2, 2)
plt.plot(magnetizations)
plt.title('Magnetization over Time')
plt.xlabel('Monte Carlo Step')
plt.ylabel('Magnetization')

plt.tight_layout()
plt.show()
