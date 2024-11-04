import numpy as np

def gauss_jordan_elimination(A, b):
    """
    Solves the system of linear equations Ax = b using Gauss-Jordan elimination.
    
    Parameters:
    A (2D list or numpy array): Coefficient matrix
    b (1D list or numpy array): Constant terms
    
    Returns:
    x (numpy array): Solution to the system
    """
    # Form the augmented matrix
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float).reshape(-1, 1)
    augmented_matrix = np.hstack((A, b))
    
    n = len(b)
    print("Initial augmented matrix:")
    print(augmented_matrix)
    print()

    for i in range(n):
        # Find the pivot
        max_row = np.argmax(np.abs(augmented_matrix[i:, i])) + i
        augmented_matrix[[i, max_row]] = augmented_matrix[[max_row, i]]
        print(f"After pivoting (swapping rows {i} and {max_row}):")
        print(augmented_matrix)
        print()

        # Check if the pivot is zero
        if augmented_matrix[i, i] == 0:
            print(f"Zero pivot found at row {i}, column {i}. Skipping row.")
            continue

        # Normalize the pivot row
        augmented_matrix[i] = augmented_matrix[i] / augmented_matrix[i, i]
        print(f"After normalizing row {i}:")
        print(augmented_matrix)
        print()

        # Eliminate the column entries
        for j in range(n):
            if j != i:
                augmented_matrix[j] -= augmented_matrix[j, i] * augmented_matrix[i]
                print(f"After eliminating row {j} using row {i}:")
                print(augmented_matrix)
                print()

    # Extract the solution
    x = augmented_matrix[:, -1]
    return x

# Example usage
A = [
    [0.0001, 1, 1],
    [1, -1, 0],
    [1, 1, -1]
]
b = [1, 0, 0]

solution = gauss_jordan_elimination(A, b)
print("Solution:", solution)
