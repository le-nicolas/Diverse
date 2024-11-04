#adjust paths by moving the drones apart if a collision is detected

# Function to check collision between drones
def check_collision(positions, min_distance):
    num_drones = len(positions)
    for i in range(num_drones):
        for j in range(i+1, num_drones):
            distance = np.linalg.norm(positions[i] - positions[j])
            if distance < min_distance:
                return True
    return False

# Simulate positions for two drones
drone1_path = np.array([interpolate_position(t, waypoints) for t in time_steps])
drone2_path = np.array([interpolate_position(t, waypoints + 5) for t in time_steps])  # Shifted second drone's path

min_distance = 2.0  # Minimum allowable distance between drones

for t in range(len(time_steps)):
    positions = [drone1_path[t], drone2_path[t]]
    if check_collision(positions, min_distance):
        print(f"Collision detected at time {time_steps[t]} between drones")
