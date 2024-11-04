import numpy as np

def gauss_jordan_elimination(A, b):
    try:
        A = np.array(A, dtype=float)
        b = np.array(b, dtype=float).reshape(-1, 1)
        augmented_matrix = np.hstack((A, b))
        n = len(b)

        print("Initial augmented matrix:")
        print(augmented_matrix)
        print()

        for i in range(n):
            # Pivoting
            max_row = np.argmax(np.abs(augmented_matrix[i:, i])) + i
            augmented_matrix[[i, max_row]] = augmented_matrix[[max_row, i]]
            print(f"After pivoting (swapping rows {i} and {max_row}):")
            print(augmented_matrix)
            print()

            # Check for zero pivot element
            if augmented_matrix[i, i] == 0:
                continue

            # Normalize pivot row
            augmented_matrix[i] = augmented_matrix[i] / augmented_matrix[i, i]
            print(f"After normalizing row {i}:")
            print(augmented_matrix)
            print()

            # Eliminate other rows
            for j in range(n):
                if j != i:
                    augmented_matrix[j] -= augmented_matrix[j, i] * augmented_matrix[i]
                    print(f"After eliminating row {j} using row {i}:")
                    print(augmented_matrix)
                    print()

        x = augmented_matrix[:, -1]
        return x
    except Exception as e:
        print(f"Exception occurred: {e}")
        return None

def backtracking_solver(A, b, depth=0):
    if depth > len(A):
        return None

    print(f"Backtracking depth {depth}:")
    print("Matrix A:")
    print(A)
    print("Vector b:")
    print(b)
    print()

    solution = gauss_jordan_elimination(A, b)
    if solution is not None:
        return solution

    for i in range(depth, len(A)):
        A_copy = A.copy()
        b_copy = b.copy()
        A_copy[[depth, i]] = A_copy[[i, depth]]
        b_copy[[depth, i]] = b_copy[[i, depth]]

        print(f"Trying permutation at depth {depth}, swapping rows {depth} and {i}")
        result = backtracking_solver(A_copy, b_copy, depth + 1)
        if result is not None:
            return result

    return None

# Example usage with a difficult system
A = [
    [0.0001, 1, 10],
    [3, -1, 0],
    [1, 2, -1]
]
b = [1, 20, 0]

solution = backtracking_solver(np.array(A), np.array(b))
print("Solution:", solution)
