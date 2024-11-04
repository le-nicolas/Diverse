import numpy as np

# Define the transition matrix
P = np.array([
    [0.7, 0.2, 0.1],  # Transition probabilities from Sunny
    [0.3, 0.4, 0.3],  # Transition probabilities from Cloudy
    [0.2, 0.4, 0.4]   # Transition probabilities from Rainy
])

# Define the initial state vector (e.g., starting with Sunny weather)
s0 = np.array([1, 0, 0])

# Function to compute the state vector after t transitions
def markov_chain(P, s0, t):
    s = s0
    for _ in range(t):
        s = np.dot(P, s)
    return s

# Compute the state vector after 1 day
s1 = markov_chain(P, s0, 1)
print("State vector after 1 day:", s1)

# Compute the state vector after 2 days
s2 = markov_chain(P, s0, 2)
print("State vector after 2 days:", s2)

# Compute the state vector after 10 days
s10 = markov_chain(P, s0, 10)
print("State vector after 10 days:", s10)
