import tkinter as tk
from tkinter import ttk
import simpy
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

# Simulation parameters
class HeatElement:
    """Each element represents a part of the rod."""
    def __init__(self, env, index, initial_temp, k, rod):
        self.env = env
        self.index = index  # Element index in the rod
        self.temp = initial_temp  # Initial temperature
        self.k = k  # Thermal conductivity
        self.rod = rod  # Reference to the full rod

    def heat_transfer(self):
        """Simulate the heat transfer between this element and its neighbors."""
        while True:
            yield self.env.timeout(1)  # Wait for 1 time unit (e.g., 1 second)

            # Update temperature based on neighbors
            if 0 < self.index < len(self.rod) - 1:
                left_temp = self.rod[self.index - 1].temp
                right_temp = self.rod[self.index + 1].temp
            elif self.index == 0:  # Leftmost element
                left_temp = self.temp  # Boundary condition
                right_temp = self.rod[self.index + 1].temp
            elif self.index == len(self.rod) - 1:  # Rightmost element
                left_temp = self.rod[self.index - 1].temp
                right_temp = self.temp  # Boundary condition
            
            # Heat transfer calculation based on difference in temperatures
            delta_temp = self.k * (left_temp + right_temp - 2 * self.temp)
            self.temp += delta_temp
            
            # Update the plot in the GUI
            update_simulation()


def update_simulation():
    """Update the Matplotlib chart with the latest temperatures."""
    temperatures = [element.temp for element in rod]

    ax.clear()
    ax.plot(range(len(rod)), temperatures, label='Temperature (°C)', color='red')
    ax.set_xlabel('Rod Element Index')
    ax.set_ylabel('Temperature (°C)')
    ax.legend(loc='upper left')
    ax.set_title('Temperature Distribution in the Rod')
    canvas.draw()


def start_simulation():
    """Start the SimPy simulation."""
    global rod

    if env.now == 0:
        # Initialize rod elements
        rod = [HeatElement(env, i, initial_temp.get(), thermal_conductivity.get(), rod) for i in range(num_elements.get())]

        # Start the heat transfer process for each element
        for element in rod:
            env.process(element.heat_transfer())
    
    # Run the simulation step by step
    def run_step():
        try:
            env.step()  # Step through the simulation
            root.after(1000, run_step)  # Schedule the next step after 1 second
        except simpy.core.EmptySchedule:
            pass  # Stop when no further events are processed

    run_step()  # Start stepping through the simulation


# Setup Tkinter GUI
root = tk.Tk()
root.title("Finite Element Heat Transfer Simulation")

mainframe = ttk.Frame(root, padding="10")
mainframe.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Entries for parameters
ttk.Label(mainframe, text="Number of Elements:").grid(row=0, column=0, sticky=tk.W)
num_elements = tk.IntVar(value=10)
ttk.Entry(mainframe, textvariable=num_elements).grid(row=0, column=1, sticky=(tk.W, tk.E))

ttk.Label(mainframe, text="Initial Temperature (°C):").grid(row=1, column=0, sticky=tk.W)
initial_temp = tk.DoubleVar(value=25)
ttk.Entry(mainframe, textvariable=initial_temp).grid(row=1, column=1, sticky=(tk.W, tk.E))

ttk.Label(mainframe, text="Thermal Conductivity (k):").grid(row=2, column=0, sticky=tk.W)
thermal_conductivity = tk.DoubleVar(value=0.1)
ttk.Entry(mainframe, textvariable=thermal_conductivity).grid(row=2, column=1, sticky=(tk.W, tk.E))

# Start simulation button
ttk.Button(mainframe, text="Start Simulation", command=start_simulation).grid(row=3, column=0, columnspan=2)

# Matplotlib figure setup
fig, ax = plt.subplots(figsize=(6, 4))
canvas = FigureCanvasTkAgg(fig, master=mainframe)
canvas.get_tk_widget().grid(row=4, column=0, columnspan=2)

# Variables for tracking data
rod = []

# Setup SimPy environment
env = simpy.Environment()

# Start the GUI loop
root.mainloop()
