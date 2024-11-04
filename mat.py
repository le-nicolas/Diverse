import numpy as np

def markov_chain(transition_matrix, initial_state, steps):
    """
    Simulates a Markov chain.

    Parameters:
    transition_matrix (numpy array): The state transition matrix.
    initial_state (numpy array): The initial state vector.
    steps (int): The number of steps to simulate.

    Returns:
    numpy array: The state distribution after the specified number of steps.
    """
    state = initial_state
    for _ in range(steps):
        state = np.dot(state, transition_matrix)
    return state

# Example usage
if __name__ == "__main__":
    # Define the transition matrix
    transition_matrix = np.array([[0.9, 0.1],
                                  [0.5, 0.5]])

    # Define the initial state vector
    initial_state = np.array([1, 0])  # Starting in state 0

    # Number of steps to simulate
    steps = 10

    # Simulate the Markov chain
    final_state = markov_chain(transition_matrix, initial_state, steps)
    
    print("State distribution after {} steps:".format(steps))
    print(final_state)
