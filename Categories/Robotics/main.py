#


import numpy as np
import matplotlib.pyplot as plt
import heapq

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

# Visualization
def visualize_grid(grid, path, start, goal):
    plt.imshow(grid, cmap='gray')
    plt.scatter(start[1], start[0], marker="o", color="blue", label="Mouse")
    plt.scatter(goal[1], goal[0], marker="x", color="red", label="Cheese")
    if path:
        path = np.array(path)
        plt.plot(path[:, 1], path[:, 0], color="green", label="Path")
    plt.legend()
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

    # Visualize the result
    visualize_grid(grid, path, start, goal)

if __name__ == "__main__":
    main()
