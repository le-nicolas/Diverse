# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# Parameters
motor_torque = 10  # Torque provided by the motor in Nm
friction_coefficient = 0.5  # Constant friction coefficient
load_mass = 20  # Mass of the load in kg
belt_radius = 0.1  # Radius of the pulley driving the belt in meters
belt_length = 10  # Length of the belt in meters
time_step = 0.01  # Time step in seconds
total_time = 10  # Total simulation time in seconds

# Physics constants
g = 9.81  # Gravity in m/s^2
friction_force = friction_coefficient * load_mass * g  # Friction force in Newtons

# Initialize variables
time = np.arange(0, total_time, time_step)
velocity = np.zeros_like(time)  # Belt velocity over time
acceleration = np.zeros_like(time)

# Simulation loop
for i in range(1, len(time)):
    # Calculate net force on the belt
    net_torque = motor_torque - friction_force * belt_radius
    
    # Newton's second law: F = ma, solve for acceleration
    acceleration[i] = net_torque / (load_mass * belt_radius)
    
    # Update velocity: v = v_0 + a * dt
    velocity[i] = velocity[i-1] + acceleration[i] * time_step

# Plotting results
plt.figure(figsize=(10, 6))
plt.plot(time, velocity, label="Belt Velocity (m/s)")
plt.title("Conveyor Belt Velocity Over Time")
plt.xlabel("Time (seconds)")
plt.ylabel("Belt Velocity (m/s)")
plt.grid(True)
plt.legend()
plt.show()
