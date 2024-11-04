import numpy as np
import matplotlib.pyplot as plt

# PID Controller for crane movement
class PIDController:
    def __init__(self, Kp, Ki, Kd, setpoint):
        self.Kp = Kp  # Proportional gain
        self.Ki = Ki  # Integral gain
        self.Kd = Kd  # Derivative gain
        self.setpoint = setpoint  # Desired position
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
        # Assuming mass and inertia are 1 for simplicity
        acceleration = torque  # Directly related to torque in this simplified model
        velocity[i] = velocity[i-1] + acceleration * time_step
        angle[i] = angle[i-1] + velocity[i] * time_step
    
    return time, angle

# Parameters
Kp = 2.0  # Proportional gain
Ki = 0.1  # Integral gain
Kd = 0.05  # Derivative gain
setpoint = 30  # Desired boom angle in degrees
total_time = 20  # Total simulation time in seconds
time_step = 0.1  # Time step for simulation

# Run simulation
time, angle = crane_movement_pid(Kp, Ki, Kd, setpoint, total_time, time_step)

# Plot results
plt.figure(figsize=(10, 6))
plt.plot(time, angle, label="Boom Angle (degrees)")
plt.axhline(y=setpoint, color='r', linestyle='--', label="Setpoint (Target)")
plt.title("Crane Boom Angle Control using PID")
plt.xlabel("Time (seconds)")
plt.ylabel("Boom Angle (degrees)")
plt.grid(True)
plt.legend()
plt.show()
