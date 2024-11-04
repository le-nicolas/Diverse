import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import simpy
import numpy as np

# Define IceCube class to simulate state transitions
class IceCube:
    def __init__(self, env, initial_temp, melting_point=32):
        self.env = env
        self.temperature = initial_temp
        self.melting_point = melting_point
        self.state = "solid"
    
    def update_state(self):
        if self.temperature < self.melting_point:
            self.state = "solid"
        elif self.melting_point <= self.temperature < self.melting_point + 5:
            self.state = "melting"
        else:
            self.state = "melted"

# Simulation function for SimPy
def simulate_room(env, ice_cube, temp_increment, update_interval, callback):
    while True:
        yield env.timeout(update_interval)
        ice_cube.temperature += temp_increment
        ice_cube.update_state()
        callback(ice_cube)  # Update the UI and plot

# Function to update the plot and UI in real-time
def update_simulation(ice_cube):
    global times, temps
    times.append(len(times))  # Simulate time steps
    temps.append(ice_cube.temperature)

    # Update UI labels
    temperature_label.config(text=f"Current Temp: {ice_cube.temperature:.1f} °F")
    state_label.config(text=f"Ice State: {ice_cube.state}")

    # Update plot
    ax.clear()
    ax.plot(times, temps, label='Room Temperature')
    ax.axhline(y=ice_cube.melting_point, color='r', linestyle='--', label='Melting Point (32°F)')
    ax.legend(loc="upper left")
    ax.set_title("Room Temperature Over Time")
    ax.set_xlabel("Time (hours)")
    ax.set_ylabel("Temperature (°F)")
    canvas.draw()

# Tkinter UI setup
def create_ui(root, env, ice_cube, temp_increment, update_interval):
    def start_simulation():
        # Start the simulation with SimPy
        env.process(simulate_room(env, ice_cube, temp_increment.get(), update_interval, update_simulation))
        env.run(until=100)  # Run for 100 time steps
    
    # Tkinter Widgets for control
    start_button = ttk.Button(root, text="Start Simulation", command=start_simulation)
    start_button.grid(row=0, column=0)

    temp_increment_label = ttk.Label(root, text="Temperature Increment (°F per hour):")
    temp_increment_label.grid(row=1, column=0)
    temp_increment_slider = ttk.Scale(root, from_=0.5, to=5, orient='horizontal', variable=temp_increment)
    temp_increment_slider.grid(row=2, column=0)

# Initialize variables and run the application
if __name__ == "__main__":
    # Tkinter setup
    root = tk.Tk()
    root.title("Ice Cube Melting Simulation")

    # SimPy environment
    env = simpy.Environment()

    # Initial parameters
    initial_temp = 0  # Room starts at 0°F
    temp_increment = tk.DoubleVar(value=1)  # Adjustable temperature increment

    # Create an ice cube instance
    ice_cube = IceCube(env, initial_temp)

    # Create the figure for Matplotlib
    fig, ax = plt.subplots()
    times, temps = [], []

    # Matplotlib canvas
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.get_tk_widget().grid(row=3, column=0, columnspan=2)

    # Tkinter Labels
    temperature_label = ttk.Label(root, text=f"Current Temp: {initial_temp:.1f} °F")
    temperature_label.grid(row=4, column=0)
    
    state_label = ttk.Label(root, text=f"Ice State: {ice_cube.state}")
    state_label.grid(row=5, column=0)

    # Start the UI and simulation
    create_ui(root, env, ice_cube, temp_increment, update_interval=1)
    root.mainloop()
