import matplotlib.pyplot as plt
import numpy as np

# Define beam length
beam_length = 10

# Define forces (magnitude and direction)
F1 = np.array([0, -5])  # Downward force at 2 units from the fixed end
F2 = np.array([0, 7])   # Upward force at 7 units from the fixed end
F3 = np.array([3, 0])   # Horizontal force at the free end (10 units)

# Positions where the forces are applied
position_F1 = np.array([2, 0])
position_F2 = np.array([7, 0])
position_F3 = np.array([beam_length, 0])

# Set up the plot
plt.figure(figsize=(10, 5))

# Draw the beam as a line
plt.plot([0, beam_length], [0, 0], 'k-', lw=5, label='Beam')

# Draw forces as arrows
plt.quiver(position_F1[0], position_F1[1], F1[0], F1[1], angles='xy', scale_units='xy', scale=1, color='r', label='Force F1 (Downward)')
plt.quiver(position_F2[0], position_F2[1], F2[0], F2[1], angles='xy', scale_units='xy', scale=1, color='b', label='Force F2 (Upward)')
plt.quiver(position_F3[0], position_F3[1], F3[0], F3[1], angles='xy', scale_units='xy', scale=1, color='g', label='Force F3 (Horizontal)')

# Draw fixed support representation
plt.plot([0, 0], [0, -1], 'k-', lw=3)
plt.plot([-0.2, 0.2], [-1, -1], 'k-', lw=3)

# Set plot limits
plt.xlim(-1, beam_length + 1)
plt.ylim(-6, 8)

# Add labels and title
plt.xlabel('X Position')
plt.ylabel('Y Position')
plt.title('Free Body Diagram (FBD) of a Cantilever Beam')
plt.grid(True)
plt.legend()

# Display the plot
plt.show()
