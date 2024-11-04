import matplotlib.pyplot as plt
from numpy import linspace, pi, cos, sin

# Speedometer settings
current_value = 70  # Speedometer current value
max_value = 120     # Speedometer maximum value
min_value = 0       # Speedometer minimum value

# Gauge design
fig, ax = plt.subplots(figsize=(8, 6), subplot_kw={'projection': 'polar'})

# Create the background arc (speedometer)
angles = linspace(0, pi, 100)
ax.plot(angles, [1] * len(angles), color='lightgray', lw=12)

# Create colored sections on the arc
colors = ['green', 'yellow', 'red']
thresholds = [0.33, 0.66, 1.0]
for i, (color, threshold) in enumerate(zip(colors, thresholds)):
    start_angle = pi * sum(thresholds[:i])
    end_angle = pi * sum(thresholds[:i + 1])
    ax.plot(linspace(start_angle, end_angle, 100), [1] * 100, color=color, lw=10)

# Add the needle
angle = pi * (current_value - min_value) / (max_value - min_value)
ax.plot([0, angle], [0, 1], color='black', lw=3)

# Hide the default polar elements
ax.set_frame_on(False)
ax.set_yticklabels([])
ax.set_xticks([])

# Speed labels
for val in linspace(min_value, max_value, 5):
    angle = pi * (val - min_value) / (max_value - min_value)
    ax.text(angle, 1.15, f'{int(val)}', ha='center', fontsize=12, color='black')

# Add center label
ax.text(0, -0.2, f'{current_value} km/h', ha='center', fontsize=16, color='black')

# Set title
plt.title('Speedometer', size=16)

plt.show()
