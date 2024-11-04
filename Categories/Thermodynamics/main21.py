import tkinter as tk
from tkinter import messagebox

# Constants
R = 8.314  # Universal gas constant in J/(mol*K)

# Function to calculate pressure based on Ideal Gas Law
def calculate_pressure():
    try:
        volume = float(volume_entry.get())
        moles = float(moles_entry.get())
        temperature = float(temperature_entry.get())

        if volume <= 0 or moles <= 0 or temperature <= 0:
            raise ValueError("All inputs must be positive numbers.")

        # Ideal Gas Law: P = (nRT) / V
        pressure = (moles * R * temperature) / volume
        result_label.config(text=f"Pressure: {pressure:.2f} Pa")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numerical values.")

# Function to clear the inputs and result
def clear_inputs():
    volume_entry.delete(0, tk.END)
    moles_entry.delete(0, tk.END)
    temperature_entry.delete(0, tk.END)
    result_label.config(text="")

# Tkinter window setup
root = tk.Tk()
root.title("Ideal Gas Law Calculator")

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
calculate_button = tk.Button(root, text="Calculate Pressure", command=calculate_pressure)
calculate_button.grid(row=3, column=0, columnspan=2, pady=20)

clear_button = tk.Button(root, text="Clear", command=clear_inputs)
clear_button.grid(row=4, column=0, columnspan=2, pady=10)

# Result label
result_label = tk.Label(root, text="")
result_label.grid(row=5, column=0, columnspan=2, pady=10)

# Start the GUI event loop
root.mainloop()
