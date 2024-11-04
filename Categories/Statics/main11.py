import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Function to plot vectors in 3D
def plot_vector(ax, vector, color='b', label=None):
    origin = np.array([0, 0, 0])
    ax.quiver(*origin, *vector, color=color, label=label, arrow_length_ratio=0.1)

# Function to plot the "before" visualization (original vectors and force)
def visualize_before(vector1, vector2, force):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    # Set labels for axes
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    # Plot original vectors
    plot_vector(ax, vector1, color='b', label='Vector 1')
    plot_vector(ax, vector2, color='r', label='Vector 2')
    
    # Plot force vector
    plot_vector(ax, force, color='g', label='Force')
    
    # Set limits to make sure all vectors are visible
    max_range = np.array([vector1, vector2, force]).max()
    ax.set_xlim([-max_range, max_range])
    ax.set_ylim([-max_range, max_range])
    ax.set_zlim([-max_range, max_range])

    # Show the legend
    ax.legend()

    plt.title("Before: Original Vectors and Force")
    plt.show()

# Function to plot the "after" visualization (force decomposed into parallel and perpendicular)
def visualize_after(vector1, vector2, force, force_parallel, force_perpendicular):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Set labels for axes
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    # Plot original vectors
    plot_vector(ax, vector1, color='b', label='Vector 1')
    plot_vector(ax, vector2, color='r', label='Vector 2')

    # Plot force vector and its components
    plot_vector(ax, force, color='g', label='Force')
    plot_vector(ax, force_parallel, color='orange', label='Parallel Component')
    plot_vector(ax, force_perpendicular, color='purple', label='Perpendicular Component')

    # Set limits to make sure all vectors are visible
    max_range = np.array([vector1, vector2, force, force_parallel, force_perpendicular]).max()
    ax.set_xlim([-max_range, max_range])
    ax.set_ylim([-max_range, max_range])
    ax.set_zlim([-max_range, max_range])

    # Show the legend
    ax.legend()

    plt.title("After: Force Decomposition (Parallel and Perpendicular)")
    plt.show()

# Example vectors
vector1 = np.array([2, 3, 5])
vector2 = np.array([1, 0, 4])
force = np.array([4, 2, 1])

# Normalize vector2 for parallel component calculation
vector2_unit = vector2 / np.linalg.norm(vector2)

# Parallel and perpendicular components
force_parallel = np.dot(force, vector2_unit) * vector2_unit
force_perpendicular = force - force_parallel

# Visualize the "before" scenario (original vectors and force)
visualize_before(vector1, vector2, force)

# Visualize the "after" scenario (force decomposed into parallel and perpendicular components)
visualize_after(vector1, vector2, force, force_parallel, force_perpendicular)
