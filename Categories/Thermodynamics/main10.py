import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def load_data(filename):
    try:
        data = pd.read_csv(filename)
        return data, 0  # Return a success code
    except FileNotFoundError:
        print("Error: File not found.")
        return None, 1
    except pd.errors.EmptyDataError:
        print("Error: No data found in the file.")
        return None, 2
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None, 3

def find_nearest_points(data, input_pressure, input_temperature):
    try:
        subset = data[data['Pressure'] == input_pressure]
        point_below = subset[subset['Temperature'] < input_temperature].tail(1)
        point_above = subset[subset['Temperature'] > input_temperature].head(1)
        
        if point_below.empty or point_above.empty:
            print("Error: Suitable data points for interpolation not found.")
            return None, None, 4
        
        return point_below, point_above, 0
    except KeyError:
        print("Error: One of the required columns is missing.")
        return None, None, 5
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None, None, 6

def interpolate(input_temperature, point_below, point_above):
    try:
        x1, y1 = point_below['Temperature'].values[0], point_below['Specific Volume'].values[0]
        x2, y2 = point_above['Temperature'].values[0], point_above['Specific Volume'].values[0]
        
        # Linear interpolation formula
        v_interpolated = y1 + (input_temperature - x1) * (y2 - y1) / (x2 - x1)
        return v_interpolated, 0
    except IndexError:
        print("Error: Not enough data points for interpolation.")
        return None, 7
    except ZeroDivisionError:
        print("Error: Division by zero error in interpolation calculation.")
        return None, 8
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None, 9

def plot_data(subset, input_temperature, v_interpolated):
    try:
        plt.scatter(subset['Temperature'], subset['Specific Volume'], label='Table Data')
        plt.scatter([input_temperature], [v_interpolated], color='red', label='Interpolated Point')
        plt.xlabel('Temperature (°C)')
        plt.ylabel('Specific Volume (m³/kg)')
        plt.legend()
        plt.show()
    except Exception as e:
        print(f"An error occurred while plotting: {e}")
        return 10

# Usage
filename = 'hypothetical_thermo_data.csv'
data, code = load_data(filename)
if code == 0:
    input_pressure = 500  # kPa
    input_temperature = 20  # Celsius
    point_below, point_above, code = find_nearest_points(data, input_pressure, input_temperature)
    if code == 0:
        v_interpolated, code = interpolate(input_temperature, point_below, point_above)
        if code == 0:
            plot_data_code = plot_data(data, input_temperature, v_interpolated)
