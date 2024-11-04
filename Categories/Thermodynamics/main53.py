import simpy
import matplotlib.pyplot as plt
import numpy as np

class PumpSimulation:
    def __init__(self, env, power, inlet_pressure, outlet_pressure, efficiency):
        self.env = env
        self.power = power  # Pump power in kW
        self.inlet_pressure = inlet_pressure  # In kPa
        self.outlet_pressure = outlet_pressure  # In kPa
        self.efficiency = efficiency  # Efficiency as a fraction (0-1)
        self.energy_consumed = 0  # kWh consumed
        self.flow_rate = 0  # Initial flow rate in kg/s
        self.run_time = 0

    def run(self):
        while True:
            flow_rate = self.calculate_flow_rate()
            self.energy_consumed += self.power * self.env.now  # Track energy usage over time
            print(f"At time {self.env.now} hrs: Flow rate = {flow_rate} kg/s, Energy = {self.energy_consumed:.2f} kWh")
            self.flow_rate = flow_rate
            yield self.env.timeout(1)  # Simulate each hour

    def calculate_flow_rate(self):
        # Use the pump's power and efficiency to calculate flow rate based on pressure difference
        delta_p = self.outlet_pressure - self.inlet_pressure  # Pressure difference in kPa
        flow_rate = (self.power * 1000 * self.efficiency) / (delta_p * 100)  # Simplified flow equation
        return flow_rate

# Define plotting functions
def plot_flow_rate_vs_time(flow_rates, times):
    plt.plot(times, flow_rates, label="Flow Rate (kg/s)")
    plt.xlabel("Time (hours)")
    plt.ylabel("Flow Rate (kg/s)")
    plt.title("Flow Rate Over Time")
    plt.legend()
    plt.show()

def plot_energy_vs_time(energies, times):
    plt.plot(times, energies, label="Energy Consumed (kWh)", color="orange")
    plt.xlabel("Time (hours)")
    plt.ylabel("Energy Consumed (kWh)")
    plt.title("Energy Consumption Over Time")
    plt.legend()
    plt.show()

# Simulation Setup
def run_simulation():
    env = simpy.Environment()
    pump = PumpSimulation(env, power=0.5, inlet_pressure=100, outlet_pressure=400, efficiency=0.8)
    env.process(pump.run())

    # Data collection for plotting
    flow_rates = []
    energies = []
    times = []
    
    for time in range(10):  # Simulate 10 hours
        env.run(until=time + 1)
        flow_rates.append(pump.flow_rate)
        energies.append(pump.energy_consumed)
        times.append(time)

    # Plotting results
    plot_flow_rate_vs_time(flow_rates, times)
    plot_energy_vs_time(energies, times)

# Run the simulation
run_simulation()
