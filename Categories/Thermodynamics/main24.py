import tkinter as tk

class HeatConductionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Fourier's Law - Heat Conduction Simulation")

        self.label = tk.Label(root, text="Heat Conduction Through a Rod", font=('Helvetica', 14))
        self.label.pack()

        self.canvas = tk.Canvas(root, width=400, height=100, bg='white')
        self.canvas.pack()

        self.temp_left = 100  # Temperature on the left side of the rod
        self.temp_right = 50  # Temperature on the right side of the rod
        self.length = 100     # Length of the rod

        # Drawing the rod
        self.rod = self.canvas.create_rectangle(50, 40, 350, 60, fill='blue')

        # Label to show temperatures
        self.temp_label_left = tk.Label(root, text=f"Temp Left: {self.temp_left}°C")
        self.temp_label_left.pack(side=tk.LEFT, padx=10)

        self.temp_label_right = tk.Label(root, text=f"Temp Right: {self.temp_right}°C")
        self.temp_label_right.pack(side=tk.RIGHT, padx=10)

        # Button to start the heat conduction simulation
        self.start_button = tk.Button(root, text="Start Simulation", command=self.start_simulation)
        self.start_button.pack(pady=10)

    def start_simulation(self):
        for step in range(1, 101):
            # Simulate heat conduction by interpolating temperatures
            temp_avg = self.temp_left + (self.temp_right - self.temp_left) * step / 100
            color_value = int(255 * (1 - (temp_avg - self.temp_right) / (self.temp_left - self.temp_right)))
            color = f'#{color_value:02x}{color_value:02x}ff'  # Interpolating color (blue to white)
            
            self.canvas.itemconfig(self.rod, fill=color)
            self.root.update()
            self.root.after(50)

root = tk.Tk()
app = HeatConductionApp(root)
root.mainloop()
