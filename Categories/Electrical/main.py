import matplotlib.pyplot as plt

# Create a figure for the PCB layout
fig, ax = plt.subplots()

# Define component positions on a simple 2D grid
components = {
    'Resistor': (2, 2),
    'Capacitor': (4, 2),
    'IC': (3, 4),
    'Ground': (1, 1),
    'Power': (5, 1)
}

# Plot components as points
for component, position in components.items():
    ax.scatter(position[0], position[1], s=300, label=component)
    ax.text(position[0] + 0.1, position[1] + 0.1, component, fontsize=9)

# Connect components with lines (representing traces)
connections = [
    ('Resistor', 'IC'),
    ('Capacitor', 'IC'),
    ('IC', 'Ground'),
    ('IC', 'Power')
]

for start, end in connections:
    start_pos = components[start]
    end_pos = components[end]
    ax.plot([start_pos[0], end_pos[0]], [start_pos[1], end_pos[1]], 'k-', lw=2)

# Set up the layout for the plot
ax.set_xlim(0, 6)
ax.set_ylim(0, 5)
ax.set_title("Basic PCB Layout Simulation")
ax.grid(True)

# Show component placement and traces
plt.legend()
plt.show()
