#waypoints: predefined key positions the drone must pass through
#linear interpolation: fpr each time t, the position is calculated by interpolating two way points
#path simul: calculating positions each timestep


import numpy as np

# Define waypoints (x, y, z) that drones will follow
waypoints = np.array([
    [0, 0, 0],     # Start point
    [5, 10, 5],    # First waypoint
    [10, 5, 10],   # Second waypoint
    [15, 15, 5],   # Third waypoint
    [20, 0, 0]     # End point
])

# Function to calculate the position of the drone at a given time t
def interpolate_position(t, waypoints):
    # Time for each segment between waypoints (assume equal time per segment)
    total_time = len(waypoints) - 1
    segment_time = total_time / (len(waypoints) - 1)

    # Find which segment we're in
    segment = int(t // segment_time)
    
    if segment >= len(waypoints) - 1:
        return waypoints[-1]  # Return last point if time exceeds the path

    # Compute the local time within the segment
    t_local = (t % segment_time) / segment_time
    
    # Linear interpolation between waypoints
    p1 = waypoints[segment]
    p2 = waypoints[segment + 1]
    
    position = (1 - t_local) * p1 + t_local * p2
    return position

# Simulate the drone's path over time
time_steps = np.linspace(0, 1, 100)
path = [interpolate_position(t, waypoints) for t in time_steps]

# Display the path
print(np.array(path))
