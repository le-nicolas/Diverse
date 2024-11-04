import numpy as np

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
equilibrium_equations = 3  # For 2D statics (sum of forces in x, y and sum of moments)
unknowns = 3  # Assume 3 unknown forces/moments for simplicity

# Check if the problem is statically determinate
determinate_status = is_statically_determinate(equilibrium_equations, unknowns)
print(f"The system is {determinate_status}.")

# Define a set of linear equations representing equilibrium conditions
# Example equations: F1 + F2 + F3 = 0 (force balance in x and y), M1 = 0 (moment balance)
equations = [
    [1, 1, 1],  # Sum of forces in x-direction
    [0, 1, 1],  # Sum of forces in y-direction
    [2, -1, 0]  # Sum of moments around a point
]

# Solve for unknowns
solution = solve_statics(equations, ['F1', 'F2', 'F3'])
print(f"Solution for the unknowns: {solution}")
