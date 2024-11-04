import tkinter as tk
import math

# Constants
INITIAL_TEMPERATURE = 300  # K
INITIAL_ENTROPY = 0        # reference point for entropy
HEAT_CAPACITY = 1.0        # specific heat (constant value for simplicity)
MASS = 1.0                 # kg of gas
TEMP_STEP = 10             # temperature increment per step

# Function to calculate entropy change (ΔS = m * C * ln(T2 / T1))
def entropy_change(T1, T2, mass, C):
    return mass * C * math.log(T2 / T1)

# Tkinter GUI setup
class EntropyVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Entropy Change Visualization")
        
        # Initial temperature and entropy
        self.temperature = INITIAL_TEMPERATURE
        self.entropy = INITIAL_ENTROPY
        
        # Label to display current temperature and entropy
        self.temp_label = tk.Label(root, text=f"Temperature: {self.temperature} K")
        self.temp_label.pack()
        
        self.entropy_label = tk.Label(root, text=f"Entropy: {self.entropy:.2f} J/K")
        self.entropy_label.pack()
        
        # Canvas for the graph
        self.canvas = tk.Canvas(root, width=400, height=200, bg='white')
        self.canvas.pack()
        
        # Button to increase temperature
        self.button = tk.Button(root, text="Increase Temperature", command=self.increase_temperature)
        self.button.pack()
        
        # Initialize graph coordinates
        self.prev_x = 0
        self.prev_y = 100
    
    def increase_temperature(self):
        # Calculate new temperature and entropy change
        new_temperature = self.temperature + TEMP_STEP
        delta_S = entropy_change(self.temperature, new_temperature, MASS, HEAT_CAPACITY)
        self.entropy += delta_S
        
        # Update temperature and entropy
        self.temperature = new_temperature
        self.temp_label.config(text=f"Temperature: {self.temperature} K")
        self.entropy_label.config(text=f"Entropy: {self.entropy:.2f} J/K")
        
        # Draw the entropy change on the canvas
        self.draw_entropy_graph()

    def draw_entropy_graph(self):
        # Normalize temperature and entropy to fit in the canvas
        x = self.temperature - INITIAL_TEMPERATURE
        y = 200 - (self.entropy * 10)  # scaling factor
        
        # Draw line showing the entropy change as temperature increases
        self.canvas.create_line(self.prev_x, self.prev_y, x, y, fill="blue", width=2)
        
        # Update previous coordinates
        self.prev_x = x
        self.prev_y = y

# Main application loop
if __name__ == "__main__":
    root = tk.Tk()
    app = EntropyVisualizer(root)
    root.mainloop()
