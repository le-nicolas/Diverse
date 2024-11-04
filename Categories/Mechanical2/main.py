import matplotlib.pyplot as plt
import numpy as np

# Define the vectors
A = np.array([3, 2])
B = np.array([1, 4])

# Calculate the sum of vectors
C = A + B

# Set up the plot
plt.figure()
plt.quiver(0, 0, A[0], A[1], angles='xy', scale_units='xy', scale=1, color='r', label='Vector A')
plt.quiver(0, 0, B[0], B[1], angles='xy', scale_units='xy', scale=1, color='b', label='Vector B')
plt.quiver(0, 0, C[0], C[1], angles='xy', scale_units='xy', scale=1, color='g', label='Vector C = A + B')

# Set plot limits
plt.xlim(0, 5)
plt.ylim(0, 5)

# Set labels and title
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Vector Addition in 2D')
plt.grid()
plt.legend()

# Show the plot
plt.show()
