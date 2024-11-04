import numpy as np
import matplotlib.pyplot as plt

# Given data
P = 500  # Pump power in W
P_in = 100e3  # Inlet pressure in Pa
P_out = 400e3  # Exit pressure in Pa
rho = 1000  # Density of water in kg/m^3
required_velocity = 20  # Required exit velocity in m/s

# Function to calculate mass flow rate
def mass_flow_rate(P, delta_P):
    return P / delta_P

# Function to calculate exit velocity based on nozzle area
def exit_velocity(area):
    return required_velocity  # Assuming we need at least 20 m/s

# Function to calculate mass flow rate for given area and velocity
def mass_flow_from_area(area, velocity):
    return rho * area * velocity

# Simulation for different nozzle exit areas
areas = np.linspace(0.001, 0.01, 100)  # Varying nozzle areas from 0.001 m^2 to 0.01 m^2
velocities = []
mass_flow_rates = []

for area in areas:
    velocity = exit_velocity(area)
    velocities.append(velocity)
    mass_flow = mass_flow_from_area(area, velocity)
    mass_flow_rates.append(mass_flow)

# Plotting results
plt.figure(figsize=(10, 6))

# Plot exit velocity
plt.subplot(2, 1, 1)
plt.plot(areas, velocities, color='blue', label='Exit Velocity')
plt.xlabel('Nozzle Exit Area (m^2)')
plt.ylabel('Exit Velocity (m/s)')
plt.title('Exit Velocity vs Nozzle Area')
plt.grid(True)

# Plot mass flow rate
plt.subplot(2, 1, 2)
plt.plot(areas, mass_flow_rates, color='red', label='Mass Flow Rate')
plt.xlabel('Nozzle Exit Area (m^2)')
plt.ylabel('Mass Flow Rate (kg/s)')
plt.title('Mass Flow Rate vs Nozzle Area')
plt.grid(True)

plt.tight_layout()
plt.show()
