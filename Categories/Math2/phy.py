import numpy as np
import matplotlib.pyplot as plt

class RRT:
    def __init__(self, start, goal, obstacle_list, expand_dis=0.5, goal_sample_rate=5, max_iter=500):
        self.start = Node(start[0], start[1])
        self.goal = Node(goal[0], goal[1])
        self.obstacle_list = obstacle_list
        self.expand_dis = expand_dis
        self.goal_sample_rate = goal_sample_rate
        self.max_iter = max_iter

    def planning(self):
        self.node_list = [self.start]
        for i in range(self.max_iter):
            rnd_node = self.get_random_node()
            nearest_ind = self.get_nearest_node_index(self.node_list, rnd_node)
            nearest_node = self.node_list[nearest_ind]
            new_node = self.steer(nearest_node, rnd_node, self.expand_dis)
            if self.check_collision(new_node, self.obstacle_list):
                near_inds = self.find_near_nodes(new_node)
                self.node_list.append(new_node)
                if self.reach_to_goal(new_node):
                    return self.generate_final_course(len(self.node_list) - 1)
                self.rewire(new_node, near_inds)

        return None  # cannot find path

    def steer(self, from_node, to_node, extend_length=float("inf")):
        new_node = Node(from_node.x, from_node.y)
        d, theta = self.calc_distance_and_angle(new_node, to_node)
        new_node.cost += min(extend_length, d)
        new_node.parent = from_node

        return new_node

    def generate_final_course(self, goal_ind):
        path = [[self.goal.x, self.goal.y]]
        while self.node_list[goal_ind].parent is not None:
            node = self.node_list[goal_ind]
            path.append([node.x, node.y])
            goal_ind = self.node_list.index(node.parent)
        path.append([self.start.x, self.start.y])
        return path

    def rewire(self, new_node, near_inds):
        for i in near_inds:
            near_node = self.node_list[i]
            d, _ = self.calc_distance_and_angle(near_node, new_node)
            scost = new_node.cost + d
            if near_node.cost > scost:
                if not self.check_collision_extend(near_node, new_node, self.obstacle_list):
                    continue
                near_node.parent = new_node
                near_node.cost = scost
                for i in range(len(self.node_list)):
                    if self.node_list[i] == near_node:
                        continue
                    d, _ = self.calc_distance_and_angle(near_node, self.node_list[i])
                    if self.node_list[i].cost > near_node.cost + d:
                        self.node_list[i].parent = near_node
                        self.node_list[i].cost = near_node.cost + d

    def find_near_nodes(self, new_node):
        nnode = len(self.node_list) + 1
        r = 50.0 * np.sqrt((np.log(nnode) / nnode))
        dist_list = [(node.x - new_node.x) ** 2 + (node.y - new_node.y)
                     ** 2 for node in self.node_list]
        near_inds = [dist_list.index(i) for i in dist_list if i <= r ** 2]
        return near_inds

    def get_random_node(self):
        if np.random.randint(0, 100) > self.goal_sample_rate:
            return Node(np.random.uniform(-10, 10), np.random.uniform(-10, 10))
        return Node(self.goal.x, self.goal.y)

    @staticmethod
    def check_collision(node, obstacle_list):
        for (ox, oy, size) in obstacle_list:
            dx = ox - node.x
            dy = oy - node.y
            d = dx * dx + dy * dy
            if d <= size ** 2:
                return False  # collision
        return True  # safe

    @staticmethod
    def check_collision_extend(from_node, to_node, obstacle_list):
        for (ox, oy, size) in obstacle_list:
            if Line(from_node.x, from_node.y, to_node.x, to_node.y).distance(ox, oy) <= size:
                return False
        return True  # safe

    @staticmethod
    def get_nearest_node_index(node_list, rnd_node):
        dlist = [(node.x - rnd_node.x) ** 2 + (node.y - rnd_node.y)
                 ** 2 for node in node_list]
        minind = dlist.index(min(dlist))
        return minind

    @staticmethod
    def calc_distance_and_angle(from_node, to_node):
        dx = to_node.x - from_node.x
        dy = to_node.y - from_node.y
        d = np.sqrt(dx ** 2 + dy ** 2)
        theta = np.arctan2(dy, dx)
        return d, theta

    def reach_to_goal(self, node):
        d, _ = self.calc_distance_and_angle(node, self.goal)
        if d <= self.expand_dis:
            return True
        return False


class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.parent = None
        self.cost = 0.0


class Line:
    def __init__(self, x0, y0, x1, y1):
        self.x0, self.y0, self.x1, self.y1 = x0, y0, x1, y1

    def distance(self, x, y):
        return np.abs((self.y1 - self.y0) * x - (self.x1 - self.x0) * y + self.x1 * self.y0 - self.y1 * self.x0) / \
               np.sqrt((self.y1 - self.y0) ** 2 + (self.x1 - self.x0) ** 2)


def plot_path(obstacle_list, path):
    plt.figure()
    ax = plt.gca()
    for (ox, oy, size) in obstacle_list:
        circle = plt.Circle((ox, oy), size, color='k')
        ax.add_artist(circle)
    for i in range(len(path) - 1):
        plt.plot([path[i][0], path[i + 1][0]], [
                 path[i][1], path[i + 1][1]], '-b')
    plt.plot([x[0] for x in path], [x[1] for x in path], '-r')
    plt.grid(True)
    plt.axis("equal")
    plt.show()


if __name__ == '__main__':
    start = (-5, -5)
    goal = (5, 5)
    obstacle_list = [(0, 0, 2)]
    rrt = RRT(start, goal, obstacle_list)
    path = rrt.planning()
    if path is not None:
        print("Path found!")
        plot_path(obstacle_list, path)
    else:
        print("Failed to find a path.")
