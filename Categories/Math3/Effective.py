import numpy as np
from scipy.integrate import solve_ivp
import plotly.graph_objects as go
import plotly.express as px

# Define the Lorenz system of differential equations
def lorenz(t, state, sigma=10.0, beta=8.0/3.0, rho=28.0):
    x, y, z = state
    dx_dt = sigma * (y - x)
    dy_dt = x * (rho - z) - y
    dz_dt = x * y - beta * z
    return [dx_dt, dy_dt, dz_dt]

# Initial conditions
initial_state_1 = [1.0, 1.0, 1.0]
initial_state_2 = [1.0 + 1e-5, 1.0, 1.0]  # Slightly different initial condition

# Time points where solution is computed
t_span = (0, 50)
t_eval = np.linspace(t_span[0], t_span[1], 10000)

# Solve the Lorenz system
solution_1 = solve_ivp(lorenz, t_span, initial_state_1, t_eval=t_eval)
solution_2 = solve_ivp(lorenz, t_span, initial_state_2, t_eval=t_eval)

# Create 3D plot for the trajectories
fig = go.Figure()

fig.add_trace(go.Scatter3d(
    x=solution_1.y[0], y=solution_1.y[1], z=solution_1.y[2],
    mode='lines',
    name='Initial State 1'
))

fig.add_trace(go.Scatter3d(
    x=solution_2.y[0], y=solution_2.y[1], z=solution_2.y[2],
    mode='lines',
    name='Initial State 2'
))

fig.update_layout(
    title='Lorenz Attractor - Interactive 3D View',
    scene=dict(
        xaxis_title='X',
        yaxis_title='Y',
        zaxis_title='Z'
    )
)

# Plot the difference in X over time
difference_x = np.abs(solution_1.y[0] - solution_2.y[0])

fig_diff = px.line(
    x=t_eval,
    y=difference_x,
    labels={'x': 'Time', 'y': 'Difference |X1 - X2|'},
    title='Difference in X over Time (Log Scale)'
)

fig_diff.update_yaxes(type='log')

# Show the plots
fig.show()
fig_diff.show()
