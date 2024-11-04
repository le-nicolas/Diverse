import numpy as np
from scipy.integrate import solve_ivp
import plotly.graph_objects as go
import plotly.express as px
import ipywidgets as widgets
from IPython.display import display, clear_output

# Define the Lorenz system of differential equations
def lorenz(t, state, sigma=10.0, beta=8.0/3.0, rho=28.0):
    x, y, z = state
    dx_dt = sigma * (y - x)
    dy_dt = x * (rho - z) - y
    dz_dt = x * y - beta * z
    return [dx_dt, dy_dt, dz_dt]

# Function to update the plots
def update_plots(initial_x1, initial_y1, initial_z1, initial_x2, initial_y2, initial_z2):
    # Initial conditions
    initial_state_1 = [initial_x1, initial_y1, initial_z1]
    initial_state_2 = [initial_x2, initial_y2, initial_z2]

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

    # Clear the output and display the new plots
    clear_output(wait=True)
    fig.show()
    fig_diff.show()

# Create sliders for the initial conditions
initial_x1_slider = widgets.FloatSlider(value=1.0, min=0.0, max=2.0, step=0.01, description='X1')
initial_y1_slider = widgets.FloatSlider(value=1.0, min=0.0, max=2.0, step=0.01, description='Y1')
initial_z1_slider = widgets.FloatSlider(value=1.0, min=0.0, max=2.0, step=0.01, description='Z1')
initial_x2_slider = widgets.FloatSlider(value=1.00001, min=0.0, max=2.0, step=0.01, description='X2')
initial_y2_slider = widgets.FloatSlider(value=1.0, min=0.0, max=2.0, step=0.01, description='Y2')
initial_z2_slider = widgets.FloatSlider(value=1.0, min=0.0, max=2.0, step=0.01, description='Z2')

# Link the sliders to the update function
widgets.interactive(update_plots,
                    initial_x1=initial_x1_slider,
                    initial_y1=initial_y1_slider,
                    initial_z1=initial_z1_slider,
                    initial_x2=initial_x2_slider,
                    initial_y2=initial_y2_slider,
                    initial_z2=initial_z2_slider)

# Display the sliders
display(initial_x1_slider, initial_y1_slider, initial_z1_slider,
        initial_x2_slider, initial_y2_slider, initial_z2_slider)
