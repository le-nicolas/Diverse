import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# System parameters
m = 1.0  # Mass
c = 0.5  # Damping coefficient
k = 2.0  # Spring constant

# PID controller parameters
Kp = 300.0  # Proportional gain
Ki = 200.0  # Integral gain
Kd = 50.0   # Derivative gain

# Desired position
setpoint = 1.0

# Initial conditions: [position, velocity, integral of error]
initial_conditions = [0.0, 0.0, 0.0]

# Time points
t = np.linspace(0, 10, 1000)

# Define the system of differential equations
def pid_mass_spring_damper(state, t, m, c, k, setpoint, Kp, Ki, Kd):
    x, v, integral_error = state  # unpack the state vector
    error = setpoint - x
    derivative_error = -v
    
    # PID control law
    u = Kp * error + Ki * integral_error + Kd * derivative_error
    
    # System dynamics
    dxdt = v
    dvdt = (u - c*v - k*x) / m
    dintegral_error_dt = error
    
    return [dxdt, dvdt, dintegral_error_dt]

# Solve the differential equation
solution = odeint(pid_mass_spring_damper, initial_conditions, t, args=(m, c, k, setpoint, Kp, Ki, Kd))

# Extract the position and velocity
x = solution[:, 0]
v = solution[:, 1]

# Plot the results
plt.figure(figsize=(12, 6))

# Position plot
plt.subplot(2, 1, 1)
plt.plot(t, x, label='Position (x)')
plt.plot(t, setpoint * np.ones_like(t), 'r--', label='Setpoint')
plt.xlabel('Time (s)')
plt.ylabel('Position (m)')
plt.legend()
plt.grid()

# Control input plot
control_input = Kp * (setpoint - x) + Ki * solution[:, 2] + Kd * (-v)
plt.subplot(2, 1, 2)
plt.plot(t, control_input, label='Control Input (u)')
plt.xlabel('Time (s)')
plt.ylabel('Control Input')
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()
