import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Generate random weather data for demonstration
np.random.seed(0)
days = np.arange(1, 31)
hours = np.arange(0, 24)
temperature = np.random.randint(15, 35, size=(len(days), len(hours)))

# Plot the heatmap
plt.figure(figsize=(15, 8))
sns.heatmap(temperature, cmap='YlOrRd', xticklabels=hours, yticklabels=days)
plt.title('Temperature Variations Over a Month')
plt.xlabel('Hour of the Day')
plt.ylabel('Day of the Month')
plt.show()
