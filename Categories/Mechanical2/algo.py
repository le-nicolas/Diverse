import matplotlib.pyplot as plt
import numpy as np

def draw_fbd(beam_length, forces, support_types):
    """
    Draw the Free-Body Diagram (FBD) of the beam with applied forces and supports.

    Args:
    beam_length (float): Length of the beam.
    forces (list of tuples): List containing forces in the format (position, Fx, Fy).
    support_types (list of tuples): List containing support types and their positions (e.g., 'fixed' or 'roller').
    """
    plt.figure(figsize=(10, 5))

    # Draw the beam
    plt.plot([0, beam_length], [0, 0], 'k-', lw=5, label='Beam')

    # Draw forces as arrows
    for force in forces:
        pos, Fx, Fy = force
        plt.quiver(pos, 0, Fx, Fy, angles='xy', scale_units='xy', scale=1, color='r', label=f'Force at {pos}')

    # Draw supports
    for support in support_types:
        support_type, pos = support
        if support_type == 'fixed':
            plt.plot([pos, pos], [0, -1], 'k-', lw=3)
            plt.plot([pos - 0.2, pos + 0.2], [-1, -1], 'k-', lw=3)
        elif support_type == 'roller':
            plt.plot([pos - 0.2, pos + 0.2], [-0.5, -0.5], 'k-', lw=3)
            plt.plot(pos, -0.5, 'o', color='k')

    plt.xlim(-1, beam_length + 1)
    plt.ylim(-6, 8)
    plt.xlabel('X Position')
    plt.ylabel('Y Position')
    plt.title('Free Body Diagram (FBD) of the Beam')
    plt.grid(True)
    plt.legend()
    plt.show()

def is_statically_determinate(equilibrium_equations, unknowns):
    """
    Check if a system is statically determinate or indeterminate.

    Args:
    equilibrium_equations (int): Number of equilibrium equations.
    unknowns (int): Number of unknown forces/moments.

    Returns:
    str: 'Determinate' if the system is statically determinate,
         'Indeterminate' if statically indeterminate.
    """
    if equilibrium_equations == unknowns:
        return "Statically Determinate"
    elif equilibrium_equations < unknowns:
        return "Statically Indeterminate"
    else:
        return "Over-constrained or Redundant"

def solve_statics(equations, unknowns):
    """
    Solve for unknown forces and moments using equilibrium equations.

    Args:
    equations (list of list): List of equations representing equilibrium conditions.
    unknowns (list): List of unknown forces/moments.

    Returns:
    numpy array: Solution for the unknowns.
    """
    try:
        A = np.array(equations)
        b = np.zeros(len(unknowns))
        solution = np.linalg.solve(A, b)
        return solution
    except np.linalg.LinAlgError:
        return "Cannot solve: The system may be indeterminate or inconsistent."

# Example usage
beam_length = 10

# Define forces (position, Fx, Fy)
forces = [
    (2, 0, -5),  # Downward force at 2 units from the fixed end
    (7, 0, 7),   # Upward force at 7 units from the fixed end
    (10, 3, 0)   # Horizontal force at the free end (10 units)
]

# Define support types (type, position)
support_types = [
    ('fixed', 0)  # Fixed support at the left end
]

# Draw initial FBD
draw_fbd(beam_length, forces, support_types)

equilibrium_equations = 3  # For 2D statics (sum of forces in x, y and sum of moments)
unknowns = 3  # Assume 3 unknown forces/moments for simplicity

# Check if the problem is statically determinate
determinate_status = is_statically_determinate(equilibrium_equations, unknowns)
print(f"The system is {determinate_status}.")

# Define a set of linear equations representing equilibrium conditions
equations = [
    [1, 1, 1],  # Sum of forces in x-direction
    [0, 1, 1],  # Sum of forces in y-direction
    [2, -1, 0]  # Sum of moments around a point
]

# Solve for unknowns
solution = solve_statics(equations, ['F1', 'F2', 'F3'])
print(f"Solution for the unknowns: {solution}")

# Update the FBD to reflect solved forces
# For simplicity, we assume the solution is [R1, R2, R3] where R1, R2, R3 are reaction forces
solved_forces = [
    (0, solution[0], 0),  # Reaction force at the fixed end in x-direction
    (0, 0, solution[1]),  # Reaction force at the fixed end in y-direction
    (10, 0, solution[2])  # Force at the free end
]

# Draw updated FBD
draw_fbd(beam_length, solved_forces, support_types)
