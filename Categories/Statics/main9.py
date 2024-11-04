import plotly.graph_objects as go

# Parameters for the gauge
current_value = 70
max_value = 120

# Create gauge figure
fig = go.Figure(go.Indicator(
    mode="gauge+number",
    value=current_value,
    gauge={
        'axis': {'range': [0, max_value]},
        'bar': {'color': "black"},
        'steps': [
            {'range': [0, max_value * 0.33], 'color': "green"},
            {'range': [max_value * 0.33, max_value * 0.66], 'color': "yellow"},
            {'range': [max_value * 0.66, max_value], 'color': "red"}],
        'threshold': {
            'line': {'color': "black", 'width': 4},
            'thickness': 0.75,
            'value': current_value}},
    title={'text': "Speedometer"}))

# Show gauge
fig.show()
