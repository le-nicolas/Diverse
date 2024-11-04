import tkinter as tk
from tkinter import ttk
import simpy
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Simulation parameters
class IceCube:
    def __init__(self, env):
        self.env = env
        self.temp = 0  # Starting temperature
        self.melted = False

    def increase_temperature(self, increment):
        """Simulate the increase of temperature"""
        while self.temp < 100:
            yield self.env.timeout(1)  # Wait 1 time unit
            self.temp += increment  # Increase temperature
            if self.temp >= 32 and not self.melted:
                print(f'Ice begins to melt at time {self.env.now}')
                self.melted = True
            elif self.temp >= 100:
                print(f'Water begins to boil at time {self.env.now}')
            update_simulation()  # Update visualization in GUI


def update_simulation():
    """Update the Matplotlib chart with the latest temperature"""
    temperatures.append(ice_cube.temp)
    times.append(env.now)

    ax.clear()
    ax.plot(times, temperatures, label='Temperature (°C)', color='blue')
    ax.set_xlabel('Time (hours)')
    ax.set_ylabel('Temperature (°C)')
    ax.legend(loc='upper left')
    ax.set_title('Temperature vs Time')
    canvas.draw()


def start_simulation():
    """Start the SimPy simulation"""
    global ice_cube

    if env.now == 0:
        ice_cube = IceCube(env)  # Initialize ice cube

        # Start the simulation process
        env.process(ice_cube.increase_temperature(temp_increment.get()))
    
    # Run simulation step-by-step to avoid ValueError
    def run_step():
        try:
            env.step()  # Step through the simulation
            root.after(1000, run_step)  # Schedule the next step after 1 second
        except simpy.core.EmptySchedule:
            pass  # Stop stepping when there are no further events to process

    run_step()  # Start the step-by-step simulation


# Setup Tkinter GUI
root = tk.Tk()
root.title("Temperature Simulation (Ice Cube Melting)")

mainframe = ttk.Frame(root, padding="10")
mainframe.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Entry for temperature increment
ttk.Label(mainframe, text="Temperature Increment per Hour:").grid(row=0, column=0, sticky=tk.W)
temp_increment = tk.DoubleVar(value=1)
ttk.Entry(mainframe, textvariable=temp_increment).grid(row=0, column=1, sticky=(tk.W, tk.E))

# Start simulation button
ttk.Button(mainframe, text="Start Simulation", command=start_simulation).grid(row=1, column=0, columnspan=2)

# Matplotlib figure setup
fig, ax = plt.subplots(figsize=(6, 4))
canvas = FigureCanvasTkAgg(fig, master=mainframe)
canvas.get_tk_widget().grid(row=2, column=0, columnspan=2)

# Variables for tracking data
times = []
temperatures = []

# Setup SimPy environment
env = simpy.Environment()
ice_cube = None  # Will be initialized in the simulation

# Start the GUI loop
root.mainloop()
