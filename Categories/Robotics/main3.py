import numpy as np
import matplotlib.pyplot as plt
import heapq
import time

# Node class for pathfinding
class Node:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent
        self.g = 0  # Distance to start node
        self.h = 0  # Heuristic (estimated distance to goal)
        self.f = 0  # Total cost (g + h)

    def __eq__(self, other):
        return self.position == other.position

    def __lt__(self, other):
        return self.f < other.f

# Heuristic function for A* (Manhattan distance)
def heuristic(current, goal):
    return abs(current[0] - goal[0]) + abs(current[1] - goal[1])

# A* pathfinding algorithm
def astar(grid, start, goal):
    open_list = []
    closed_list = set()

    start_node = Node(start)
    goal_node = Node(goal)
    heapq.heappush(open_list, start_node)

    while open_list:
        current_node = heapq.heappop(open_list)
        closed_list.add(current_node.position)

        # Goal reached
        if current_node == goal_node:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]  # Return reversed path

        # Explore neighbors
        neighbors = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
        for direction in neighbors:
            neighbor_pos = (current_node.position[0] + direction[0],
                            current_node.position[1] + direction[1])

            if (0 <= neighbor_pos[0] < grid.shape[0] and
                0 <= neighbor_pos[1] < grid.shape[1] and
                grid[neighbor_pos[0], neighbor_pos[1]] == 0 and
                neighbor_pos not in closed_list):

                neighbor_node = Node(neighbor_pos, current_node)
                neighbor_node.g = current_node.g + 1
                neighbor_node.h = heuristic(neighbor_node.position, goal_node.position)
                neighbor_node.f = neighbor_node.g + neighbor_node.h

                # If neighbor is already in the open list with a lower cost, skip it
                if any(neighbor_node == n and neighbor_node.f >= n.f for n in open_list):
                    continue

                heapq.heappush(open_list, neighbor_node)

    return None  # No path found

# Environment setup
def create_grid(width, height, obstacles):
    grid = np.zeros((width, height))
    for obs in obstacles:
        grid[obs[0], obs[1]] = 1  # Mark obstacles
    return grid

# Dynamic visualization of the mouse movement
def animate_movement(grid, path, start, goal):
    fig, ax = plt.subplots()
    ax.set_xticks(np.arange(-0.5, grid.shape[1], 1), minor=True)
    ax.set_yticks(np.arange(-0.5, grid.shape[0], 1), minor=True)
    ax.grid(which='minor', color='black', linestyle='-', linewidth=2)

    for obs in np.argwhere(grid == 1):
        ax.plot(obs[1], obs[0], 'ks')  # Black squares for obstacles

    mouse, = ax.plot(start[1], start[0], 'bo', label="Mouse")  # Blue circle for the mouse
    ax.plot(goal[1], goal[0], 'rx', label="Cheese")  # Red 'X' for the cheese
    ax.legend()

    plt.ion()
    plt.show()

    # Move the mouse step by step
    for step in path:
        mouse.set_data([step[1]], [step[0]])  # Ensure values are wrapped in lists
        plt.pause(0.5)  # Pause to animate the movement
        plt.draw()

    plt.ioff()
    plt.show()

# Main simulation
def main():
    # Grid size
    width, height = 10, 10

    # Define obstacles (x, y) positions
    obstacles = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]

    # Start and goal positions
    start = (0, 0)
    goal = (9, 9)

    # Create grid
    grid = create_grid(width, height, obstacles)

    # Find path using A*
    path = astar(grid, start, goal)

    if path:
        # Animate the mouse's movement along the path
        animate_movement(grid, path, start, goal)
    else:
        print("No path found.")

if __name__ == "__main__":
    main()
