import numpy as np
import matplotlib.pyplot as plt

# Parameters
load_mass = 5000  # Load mass in kg (e.g., 5 tons)
boom_length = 20  # Length of the boom in meters
gravity = 9.81  # Gravitational acceleration (m/s^2)
number_of_pulleys = 4  # Number of pulleys for mechanical advantage
counterweight_mass = 7000  # Mass of the counterweight in kg
counterweight_distance = 10  # Distance of counterweight from base in meters

# Torque calculation
def calculate_torque(load_mass, boom_length):
    load_force = load_mass * gravity  # F = m * g
    torque = load_force * boom_length  # T = F * d
    return torque

# Effective force using the pulley system
def pulley_system(load_mass, number_of_pulleys):
    load_force = load_mass * gravity  # F = m * g
    effective_force = load_force / number_of_pulleys  # Mechanical advantage
    return effective_force

# Counterweight torque calculation
def counterweight_torque(counterweight_mass, counterweight_distance):
    counterweight_force = counterweight_mass * gravity
    counterweight_torque = counterweight_force * counterweight_distance
    return counterweight_torque

# Lifting mechanism simulation
def lifting_simulation(load_mass, boom_length, number_of_pulleys, counterweight_mass, counterweight_distance):
    time_step = 0.1  # Time step for simulation
    total_time = 10  # Total simulation time in seconds
    time = np.arange(0, total_time, time_step)
    lifting_height = np.zeros_like(time)
    
    # Calculate initial torques
    load_torque = calculate_torque(load_mass, boom_length)
    counter_torque = counterweight_torque(counterweight_mass, counterweight_distance)
    
    if counter_torque < load_torque:
        print("Warning: Crane is unstable, counterweight insufficient!")
    
    # Lift the load over time
    for i in range(1, len(time)):
        # Assuming constant velocity lift for simplicity
        lifting_height[i] = lifting_height[i-1] + pulley_system(load_mass, number_of_pulleys) * time_step
    
    return time, lifting_height

# Run simulation
time, lifting_height = lifting_simulation(load_mass, boom_length, number_of_pulleys, counterweight_mass, counterweight_distance)

# Plot results
plt.figure(figsize=(10, 6))
plt.plot(time, lifting_height, label="Lifting Height (m)")
plt.title("Crane Lifting Height Over Time")
plt.xlabel("Time (seconds)")
plt.ylabel("Lifting Height (meters)")
plt.grid(True)
plt.legend()
plt.show()
