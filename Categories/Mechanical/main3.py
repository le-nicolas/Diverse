import numpy as np
import matplotlib.pyplot as plt

# Define the mass and position of each component in the system
components = {
    'component1': {'mass': 2.0, 'position': np.array([1.0, 2.0, 0.0])},
    'component2': {'mass': 1.5, 'position': np.array([-1.0, -2.0, 0.0])},
    'component3': {'mass': 2.5, 'position': np.array([2.0, 1.0, 0.0])},
    # Add more components as needed
}

# Calculate the center of mass
total_mass = sum(comp['mass'] for comp in components.values())
center_of_mass = sum(comp['mass'] * comp['position'] for comp in components.values()) / total_mass

# Check if the center of mass is on the z-axis (axis of rotation)
if np.linalg.norm(center_of_mass[:2]) == 0:
    print("Center of mass is on the axis of rotation. The system is balanced.")
else:
    print("Center of mass is not on the axis of rotation. The system is unbalanced.")
    print("Center of Mass:", center_of_mass)
    
    # Calculate the centrifugal force and vibrations
    omega = 2 * np.pi * 10  # rotational speed in rad/s (example value, can be changed)
    radius = np.linalg.norm(center_of_mass[:2])
    centrifugal_force = total_mass * omega**2 * radius
    print(f"Centrifugal Force: {centrifugal_force:.2f} N")

    # Simulate vibrations (simple harmonic motion)
    time = np.linspace(0, 2, 1000)
    vibrations = radius * np.sin(omega * time)
    
    plt.plot(time, vibrations)
    plt.title('Vibrations Due to Off-Center Mass')
    plt.xlabel('Time (s)')
    plt.ylabel('Displacement (m)')
    plt.grid(True)
    plt.show()
