import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np

class AdiabaticExpansionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Adiabatic Expansion - Piston Simulation")

        # Parameters for the adiabatic expansion
        self.gamma = 1.4  # Adiabatic index for air
        self.P0 = 100  # Initial pressure (kPa)
        self.V0 = 1.0  # Initial volume (m^3)

        # Tkinter canvas for the piston visualization
        self.canvas = tk.Canvas(root, width=400, height=200, bg='white')
        self.canvas.pack()

        # Draw a simple cylinder
        self.cylinder = self.canvas.create_rectangle(100, 50, 300, 150, fill="grey", outline="black")
        self.piston = self.canvas.create_rectangle(150, 50, 160, 150, fill="blue", outline="black")

        # Matplotlib figure for P-V curve
        self.fig, self.ax = plt.subplots()
        self.ax.set_xlabel("Volume (m^3)")
        self.ax.set_ylabel("Pressure (kPa)")
        self.ax.set_title("P-V Diagram")

        self.canvas_fig = FigureCanvasTkAgg(self.fig, root)
        self.canvas_fig.get_tk_widget().pack()

        # Button to start the simulation
        self.start_button = tk.Button(root, text="Start Expansion", command=self.start_expansion)
        self.start_button.pack(pady=10)

    def start_expansion(self):
        volumes = np.linspace(self.V0, 2 * self.V0, 100)
        pressures = self.P0 * (self.V0 / volumes) ** self.gamma
        self.ax.plot(volumes, pressures, label="Adiabatic Expansion")
        self.ax.legend()

        for i, volume in enumerate(volumes):
            self.update_piston(volume)
            self.root.update_idletasks()
            self.root.after(50)  # Delay to simulate real-time movement
            self.canvas_fig.draw()

    def update_piston(self, volume):
        piston_position = 100 + (volume - self.V0) * 150  # Adjust piston position with volume change
        self.canvas.coords(self.piston, piston_position, 50, piston_position + 10, 150)

root = tk.Tk()
app = AdiabaticExpansionApp(root)
root.mainloop()
