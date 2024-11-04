import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

# PID Controller for crane movement
class PIDController:
    def __init__(self, Kp, Ki, Kd, setpoint):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.setpoint = setpoint
        self.integral = 0
        self.prev_error = 0
    
    def compute(self, current_position, dt):
        # Calculate error
        error = self.setpoint - current_position
        
        # Proportional term
        P = self.Kp * error
        
        # Integral term
        self.integral += error * dt
        I = self.Ki * self.integral
        
        # Derivative term
        derivative = (error - self.prev_error) / dt
        D = self.Kd * derivative
        
        # Remember the error for the next time step
        self.prev_error = error
        
        # PID output
        return P + I + D

# Simulate crane movement (boom angle control)
def crane_movement_pid(Kp, Ki, Kd, setpoint, total_time, time_step):
    # Initialize PID controller
    pid = PIDController(Kp, Ki, Kd, setpoint)
    
    # Simulation variables
    time = np.arange(0, total_time, time_step)
    angle = np.zeros_like(time)  # Boom angle over time
    velocity = np.zeros_like(time)  # Boom angular velocity
    
    for i in range(1, len(time)):
        # Calculate the control signal (torque adjustment) using PID
        torque = pid.compute(angle[i-1], time_step)
        
        # Update the boom's angular velocity and position
        acceleration = torque
        velocity[i] = velocity[i-1] + acceleration * time_step
        angle[i] = angle[i-1] + velocity[i] * time_step
    
    return time, angle

# Function to update plot when sliders change
def update_plot():
    # Get the values from sliders
    Kp = Kp_slider.get()
    Ki = Ki_slider.get()
    Kd = Kd_slider.get()
    
    # Run simulation with new PID values
    time, angle = crane_movement_pid(Kp, Ki, Kd, setpoint, total_time, time_step)
    
    # Update the plot with new data
    ax.clear()
    ax.plot(time, angle, label="Boom Angle (degrees)")
    ax.axhline(y=setpoint, color='r', linestyle='--', label="Setpoint (Target)")
    ax.set_title("Crane Boom Angle Control using PID")
    ax.set_xlabel("Time (seconds)")
    ax.set_ylabel("Boom Angle (degrees)")
    ax.grid(True)
    ax.legend()
    
    # Redraw the plot
    canvas.draw()

# Parameters
setpoint = 30  # Desired boom angle in degrees
total_time = 20  # Total simulation time in seconds
time_step = 0.1  # Time step for simulation

# Create a Tkinter window
root = tk.Tk()
root.title("Crane PID Tuning")

# Create a figure and axis for the plot
fig, ax = plt.subplots(figsize=(8, 4))

# Add the figure to the Tkinter canvas
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# Add sliders for Kp, Ki, and Kd
Kp_slider = tk.Scale(root, from_=0, to=10, resolution=0.1, orient=tk.HORIZONTAL, label="Kp (Proportional Gain)", command=lambda x: update_plot())
Kp_slider.pack(fill=tk.X)

Ki_slider = tk.Scale(root, from_=0, to=5, resolution=0.1, orient=tk.HORIZONTAL, label="Ki (Integral Gain)", command=lambda x: update_plot())
Ki_slider.pack(fill=tk.X)

Kd_slider = tk.Scale(root, from_=0, to=2, resolution=0.01, orient=tk.HORIZONTAL, label="Kd (Derivative Gain)", command=lambda x: update_plot())
Kd_slider.pack(fill=tk.X)

# Initialize sliders with some values
Kp_slider.set(2.0)
Ki_slider.set(0.1)
Kd_slider.set(0.05)

# Initial plot
update_plot()

# Start the Tkinter main loop
root.mainloop()
