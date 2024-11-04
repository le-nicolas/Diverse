import numpy as np
import matplotlib.pyplot as plt

# Sample data (RPM vs Power vs Torque)
data = {
    "Run 1": {
        "RPM": [2000, 2500, 3000, 3500, 4000, 4500, 5000],
        "Power": [100, 150, 200, 240, 250, 245, 240],  # HP
        "Torque": [300, 320, 340, 360, 370, 365, 350],  # lb-ft
    },
    "Run 2": {
        "RPM": [2000, 2500, 3000, 3500, 4000, 4500, 5000],
        "Power": [105, 155, 210, 250, 260, 255, 250],
        "Torque": [310, 330, 350, 370, 380, 375, 360],
    },
    "Run 3": {
        "RPM": [2000, 2500, 3000, 3500, 4000, 4500, 5000],
        "Power": [110, 160, 215, 255, 265, 260, 255],
        "Torque": [320, 340, 360, 380, 390, 385, 370],
    }
}

# Plotting the data
def plot_dyno(data):
    plt.figure(figsize=(10, 6))
    
    for run, values in data.items():
        # Plot Power
        plt.plot(values['RPM'], values['Power'], label=f'{run} Power', linestyle='-', marker='o')
        # Plot Torque
        plt.plot(values['RPM'], values['Torque'], label=f'{run} Torque', linestyle='--', marker='x')

    plt.title("Engine Power and Torque vs RPM")
    plt.xlabel("RPM (x1000)")
    plt.ylabel("Power (HP) / Torque (lb-ft)")
    plt.legend()
    plt.grid(True)
    
    # Show the plot
    plt.show()

# Call the function to plot data
plot_dyno(data)
