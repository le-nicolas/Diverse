import numpy as np
import matplotlib.pyplot as plt

def markov_chain(transition_matrix, initial_state, steps):
    """
    Simulates a Markov chain and returns the state distributions over the steps.

    Parameters:
    transition_matrix (numpy array): The state transition matrix.
    initial_state (numpy array): The initial state vector.
    steps (int): The number of steps to simulate.

    Returns:
    list of numpy arrays: The state distributions at each step.
    """
    state = initial_state
    state_distributions = [state]
    for _ in range(steps):
        state = np.dot(state, transition_matrix)
        state_distributions.append(state)
    return state_distributions

def plot_markov_chain(state_distributions):
    """
    Plots the state distributions of a Markov chain over time.

    Parameters:
    state_distributions (list of numpy arrays): The state distributions at each step.
    """
    steps = len(state_distributions)
    states = len(state_distributions[0])
    
    for state in range(states):
        plt.plot(range(steps), [distribution[state] for distribution in state_distributions], label=f"State {state}")
    
    plt.xlabel("Steps")
    plt.ylabel("Probability")
    plt.title("Markov Chain State Probabilities Over Time")
    plt.legend()
    plt.grid(True)
    plt.show()

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
    state_distributions = markov_chain(transition_matrix, initial_state, steps)
    
    # Plot the state distributions
    plot_markov_chain(state_distributions)
