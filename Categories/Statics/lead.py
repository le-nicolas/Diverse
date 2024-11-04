import numpy as np

class Drone:
    def __init__(self, drone_id, initial_position):
        self.drone_id = drone_id
        self.position = np.array(initial_position)  # [x, y, z] position
        self.velocity = np.array([0, 0, 0])        # [vx, vy, vz] velocity

    def update_position(self, new_position):
        self.position = np.array(new_position)

    def follow(self, leader_position, distance_offset):
        # Calculate the direction vector from the follower to the leader
        direction = leader_position - self.position
        # Normalize the direction
        norm = np.linalg.norm(direction)
        if norm != 0:
            direction = direction / norm
        # Move the follower to maintain a fixed distance from the leader
        target_position = leader_position - direction * distance_offset
        self.update_position(target_position)

    def lead(self, new_position):
        # The leader moves based on a predefined trajectory
        self.update_position(new_position)

# Initialize leader and followers
leader = Drone(drone_id=0, initial_position=[0, 0, 10])  # Leader starts at [0, 0, 10]
followers = [
    Drone(drone_id=1, initial_position=[-5, 0, 10]),  # Follower 1 starts at a distance
    Drone(drone_id=2, initial_position=[-5, -5, 10])  # Follower 2 starts at a distance
]

# Example trajectory for the leader (straight line along x-axis)
leader_trajectory = [
    [i, 0, 10] for i in range(0, 100)  # Leader moves along x-axis
]

# Set fixed distance for followers
follower_distance = 5  # Maintain 5 units distance from the leader

# Simulation loop
for step in leader_trajectory:
    # Move the leader
    leader.lead(step)

    # Update followers' positions based on the leader's new position
    for follower in followers:
        follower.follow(leader.position, follower_distance)

    # Print positions for visualization
    print(f"Leader Position: {leader.position}")
    for i, follower in enumerate(followers):
        print(f"Follower {i+1} Position: {follower.position}")
