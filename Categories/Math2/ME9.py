import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Define the ranges for knife quality and grip technique
knife_quality = np.arange(1, 6)
grip_technique = np.arange(1, 6)

# Initialize a matrix to hold the quality of chopped food
quality_matrix = np.zeros((len(knife_quality), len(grip_technique)))

# Populate the quality matrix
for i, k in enumerate(knife_quality):
    for j, g in enumerate(grip_technique):
        quality_matrix[i, j] = k * g

# Plotting the heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(quality_matrix, annot=True, fmt=".1f", cmap="YlGnBu", xticklabels=grip_technique, yticklabels=knife_quality)
plt.title('Quality of Chopped Food based on Knife Quality and Grip Technique')
plt.xlabel('Grip Technique')
plt.ylabel('Knife Quality')
plt.show()
