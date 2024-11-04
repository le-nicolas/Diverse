import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

# Constants
R = 8.314  # Universal gas constant in J/(mol*K)

# Function to calculate pressure based on Ideal Gas Law and plot PV diagram
def calculate_and_plot():
    try:
        volume = float(volume_entry.get())
        moles = float(moles_entry.get())
        temperature = float(temperature_entry.get())

        if volume <= 0 or moles <= 0 or temperature <= 0:
            raise ValueError("All inputs must be positive numbers.")

        # Ideal Gas Law: P = (nRT) / V
        pressure = (moles * R * temperature) / volume
        result_label.config(text=f"Pressure: {pressure:.2f} Pa")

        # Generate PV curve for visualization
        volumes = np.linspace(0.1, volume, 100)
        pressures = (moles * R * temperature) / volumes

        # Clear the previous plot
        ax.clear()

        # Plot the new PV curve
        ax.plot(volumes, pressures, label=f'T = {temperature} K', color='blue')
        ax.set_xlabel("Volume (m³)")
        ax.set_ylabel("Pressure (Pa)")
        ax.set_title("Pressure vs Volume (PV Diagram)")
        ax.legend()

        # Redraw the canvas
        canvas.draw()

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numerical values.")

# Function to clear the inputs and result
def clear_inputs():
    volume_entry.delete(0, tk.END)
    moles_entry.delete(0, tk.END)
    temperature_entry.delete(0, tk.END)
    result_label.config(text="")
    ax.clear()  # Clear the plot
    canvas.draw()  # Redraw the blank canvas

# Tkinter window setup
root = tk.Tk()
root.title("Ideal Gas Law Calculator with PV Diagram")

# Labels and Entries for Inputs
volume_label = tk.Label(root, text="Volume (m³):")
volume_label.grid(row=0, column=0, padx=10, pady=10)

volume_entry = tk.Entry(root)
volume_entry.grid(row=0, column=1, padx=10, pady=10)

moles_label = tk.Label(root, text="Moles of Gas (mol):")
moles_label.grid(row=1, column=0, padx=10, pady=10)

moles_entry = tk.Entry(root)
moles_entry.grid(row=1, column=1, padx=10, pady=10)

temperature_label = tk.Label(root, text="Temperature (K):")
temperature_label.grid(row=2, column=0, padx=10, pady=10)

temperature_entry = tk.Entry(root)
temperature_entry.grid(row=2, column=1, padx=10, pady=10)

# Buttons for Calculate and Clear
calculate_button = tk.Button(root, text="Calculate & Plot", command=calculate_and_plot)
calculate_button.grid(row=3, column=0, columnspan=2, pady=20)

clear_button = tk.Button(root, text="Clear", command=clear_inputs)
clear_button.grid(row=4, column=0, columnspan=2, pady=10)

# Result label
result_label = tk.Label(root, text="")
result_label.grid(row=5, column=0, columnspan=2, pady=10)

# Matplotlib Figure setup
fig, ax = plt.subplots(figsize=(5, 4))
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().grid(row=6, column=0, columnspan=2, pady=20)

# Start the GUI event loop
root.mainloop()
