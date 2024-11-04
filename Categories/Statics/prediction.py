#Forecast where the leader will be in the future, enabling smoother and more anticipatory following behavior.

def predict_trajectory(x_current, y_current, v_x, v_y, a_x, a_y, time_step):
    # Predict future position using kinematic equations
    x_future = x_current + v_x * time_step + 0.5 * a_x * (time_step**2)
    y_future = y_current + v_y * time_step + 0.5 * a_y * (time_step**2)
    return x_future, y_future

# Example leader's current state
x_current, y_current = 0, 0  # Leader's current position
v_x, v_y = 1, 1  # Leader's velocity (1 m/s in x and y)
a_x, a_y = 0.1, 0.1  # Leader's acceleration (0.1 m/s² in x and y)
time_step = 1  # Predict 1 second into the future

x_future, y_future = predict_trajectory(x_current, y_current, v_x, v_y, a_x, a_y, time_step)
print(f"Predicted future position: ({x_future}, {y_future})")
